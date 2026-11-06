# -*- coding: utf-8 -*-
"""Monta as fontes do DocX (docx.json, content/, media/) a partir dos Markdown de docs/ (horus-v2-docs).

Os fragmentos de content/ e os diagramas de media/ saem DAQUI: editar um deles à mão se perde
na próxima montagem. Mude o Markdown e monte de novo.

Pré-requisitos: markdown-it-py e playwright (Python), o Chromium do Playwright e o bundle do
Mermaid 11 (`npm pack mermaid@11.17.2`, e depois `tar -xzf` do `package/dist/mermaid.min.js`).

Uso, da raiz do horus-v2-docs (a pasta que tem docs/, fontes/ e ferramentas/):
  python ferramentas/montar_fontes.py . fontes <caminho do mermaid.min.js>
  python <plugin docx>/scripts/docx.py gerar --config fontes/docx.json --saida docs
  python <plugin docx>/scripts/docx.py validar --site docs
Os Markdown (docs/leitura e docs/raw), as fontes (fontes/) e o portal pronto (docs/, que o GitHub Pages serve) moram no
mesmo repositório. O caminho de um .md entre crases ("docs/raw/produto/04-….md") vira link: para a página dele no portal
ou, se ele só existe no repositório, para o arquivo no GitHub.

O índice de cada página (o modelo 01, "Cartões", aprovado pelo dono; a galeria dos modelos está em
fontes/modelos-mf/) sai do próprio DocX desde 03/11/2026.

A documentação de leitura (docs/leitura/, D-144) entra no portal assim: a visão geral é a primeira seção; a página
de leitura de cada mf é a página dela (mf-1nn), aberta pelo título do cartão; e a agregação do inventário de cada mf
vira uma página fora dos índices (mf-1nn-inventario), aberta pelos links "Produto" e "Arquitetura" do cartão.
"""
from __future__ import annotations
import copy, json, re, sys, unicodedata
from collections import defaultdict
from html import escape
from pathlib import Path, PurePosixPath
from urllib.parse import unquote
from markdown_it import MarkdownIt
from markdown_it.token import Token

DOCS = [
    # (caminho na pasta v2, id da seção, título, resumo, categoria, destaque)
    ("README.md", "pasta-v2", "A pasta da v2", "Os documentos de visão e as decisões de produto do Horus v2, e como a pasta se organiza.", "Comece aqui", False),
    ("docs/raw/produto/01-temas-da-visao-do-produto.md", "produto-temas", "Temas da visão de produto", "O propósito a validar e os temas que a visão do Horus precisa responder.", "Produto", False),
    ("docs/raw/produto/02-norte-do-produto.md", "produto-norte", "Norte do produto", "Por que o Horus existe, para quem, o que promete e como saberemos que deu certo.", "Produto", False),
    ("docs/raw/produto/03-inventario-de-lacunas.md", "produto-lacunas", "Inventário de lacunas", "O que o norte afirma, comparado com o que o Horus faz hoje.", "Produto", False),
    ("docs/raw/produto/04-macro-funcionalidades-de-hoje.md", "produto-mfs-hoje", "Macro funcionalidades de hoje", "O que o Horus já entrega hoje, em linguagem de valor.", "Produto", False),
    ("docs/raw/produto/05-v2.0-consolidada.md", "produto-v20", "A v2.0 consolidada", "O que a v2.0 é: o que entra, o que fica fora, as regras já decididas e os riscos.", "Produto", True),
    ("docs/raw/produto/06-versoes.md", "produto-versoes", "As versões, mf a mf", "Uma tabela por versão, com as macro funcionalidades da v2.0 e da v2.1.", "Produto", False),
    ("docs/raw/produto/07-mapa-de-objetivos-e-funcionalidades.md", "produto-mapa", "Mapa de objetivos e funcionalidades", "Para cada objetivo do produto, as funcionalidades que o cumprem e a entrega de cada uma.", "Produto", False),
    ("docs/raw/produto/backlog-estrategico.md", "produto-backlog", "Backlog estratégico", "O registro das decisões de produto: o que o Horus entrega, para quem e em que ordem.", "Produto", False),
    ("docs/raw/backlog/README.md", "backlog-atividades", "Backlog de atividades", "Reservado aos épicos, às histórias e às tasks, que vêm depois da arquitetura.", "Produto", False),
    ("docs/raw/arquitetura/README.md", "arquitetura", "A pasta da arquitetura", "Os documentos do arquiteto de soluções, a situação de cada um e os números do registro.", "Arquitetura · visão e decisões", False),
    ("docs/raw/arquitetura/01-estrategia-da-solucao.md", "arquitetura-01", "01 · Estratégia da solução", "Como o Horus v2 atinge os objetivos do produto: as entregas, os marcos e a fila do dono.", "Arquitetura · visão e decisões", True),
    ("docs/raw/arquitetura/02-registro-de-decisoes.md", "arquitetura-02", "02 · Registro de decisões", "As decisões de tecnologia, cada uma com quem decide, as opções e o porquê.", "Arquitetura · visão e decisões", True),
    ("docs/raw/arquitetura/03-metas-de-qualidade.md", "arquitetura-03", "03 · Metas de qualidade", "Disponibilidade, recuperação, volume, rapidez e custo por organização, e como se mede cada um.", "Arquitetura · visão e decisões", False),
    ("docs/raw/arquitetura/04-software.md", "arquitetura-04", "04 · Software", "Os módulos, os componentes e os contratos do servidor e do front.", "Arquitetura · construção", False),
    ("docs/raw/arquitetura/05-motor-de-analise-e-ia.md", "arquitetura-05", "05 · Motor de análise e IA", "Como a pergunta vira resposta: o motor, o modelo semântico, a web, o agente e os provedores de IA.", "Arquitetura · construção", False),
    ("docs/raw/arquitetura/06-dados.md", "arquitetura-06", "06 · Dados", "O que o Horus guarda, de quem é cada dado, como as organizações ficam separadas e por quanto tempo.", "Arquitetura · construção", False),
    ("docs/raw/arquitetura/07-seguranca.md", "arquitetura-07", "07 · Segurança", "Quem entra, o que cada pessoa pode fazer e o que cada uma vê.", "Arquitetura · construção", False),
    ("docs/raw/arquitetura/08-integracoes.md", "arquitetura-08", "08 · Integrações", "O e-mail, a Meta e o WhatsApp, os provedores de IA, os bancos dos clientes e a web.", "Arquitetura · construção", False),
    ("docs/raw/arquitetura/09-infraestrutura-e-ambientes.md", "arquitetura-09", "09 · Infraestrutura e ambientes", "Onde o Horus roda: a VPS da construção com o minikube, a produção real na nuvem e o on-premises.", "Arquitetura · operação", False),
    ("docs/raw/arquitetura/10-publicacao-e-operacao.md", "arquitetura-10", "10 · Publicação e operação", "Como uma versão chega a uma instância, a cópia de segurança, o acesso e os incidentes.", "Arquitetura · operação", False),
    ("docs/raw/arquitetura/11-observabilidade.md", "arquitetura-11", "11 · Observabilidade", "O que se mede, quem é avisado e quando, e o que a telemetria nunca carrega.", "Arquitetura · operação", False),
    ("docs/raw/arquitetura/12-qualidade-e-testes.md", "arquitetura-12", "12 · Qualidade e testes", "Como cada publicação se prova antes de subir, sem chamar modelo de IA pago.", "Arquitetura · operação", False),
    ("docs/raw/arquitetura/13-custo-de-operacao.md", "arquitetura-13", "13 · Custo de operação", "Quanto custa operar, por organização e por componente, e o orçamento da produção real.", "Arquitetura · operação", False),
    ("docs/raw/arquitetura/14-conferencia-do-produto.md", "arquitetura-14", "14 · Conferência do produto", "As respostas do arquiteto às pendências do PO, os itens a devolver e as verificações pendentes.", "Arquitetura · conferência", False),
]
DIRS = {"docs/raw/arquitetura": "arquitetura", "docs/raw/backlog": "backlog-atividades", "docs/raw/produto": "produto-temas", "": "pasta-v2"}

LEITURA = "docs/leitura"
REPO_BLOB = "https://github.com/fabioabr/horus-v2-docs/blob/main/"  # o arquivo .md, quando ele não é página do portal
VISAO_GERAL = (f"{LEITURA}/visao-geral.md", "visao-geral", "O Horus v2", "O que o Horus v2 é, para quem, que problemas resolve, como funciona e as 19 macro funcionalidades.", "Comece aqui", False)
# O emoji do título de uma página de leitura vira o ícone do assunto no índice da página (Font Awesome 5).
# Os emojis dos cartões da entrada (e das linhas do modo Lista): um por documento e um por macro funcionalidade.
EMOJI_DOC = {
    "visao-geral": "🔭", "pasta-v2": "🗂️",
    "produto-temas": "🧠", "produto-norte": "🧭", "produto-lacunas": "🕳️", "produto-mfs-hoje": "📍", "produto-v20": "🚀",
    "produto-versoes": "🔀", "produto-mapa": "🗺️", "produto-backlog": "📌", "backlog-atividades": "📝",
    "arquitetura": "🏛️", "arquitetura-01": "🎯", "arquitetura-02": "📜", "arquitetura-03": "📏",
    "arquitetura-04": "💻", "arquitetura-05": "✨", "arquitetura-06": "🗄️", "arquitetura-07": "🛡️", "arquitetura-08": "🔌",
    "arquitetura-09": "🏗️", "arquitetura-10": "🚢", "arquitetura-11": "📡", "arquitetura-12": "🧪", "arquitetura-13": "💰",
    "arquitetura-14": "✅",
}
EMOJI_MF = {
    "MF-101": "🏷️", "MF-102": "🏢", "MF-103": "🎫", "MF-104": "🔗", "MF-105": "🤖", "MF-106": "🔐", "MF-107": "💬",
    "MF-108": "📊", "MF-109": "🌐", "MF-110": "⚡", "MF-111": "📱", "MF-112": "📋", "MF-113": "📤", "MF-114": "⏰",
    "MF-115": "🦾", "MF-116": "🧾", "MF-117": "🏠", "MF-118": "🗃️", "MF-119": "🔍",
}
ICONES_LEITURA = {"🧭": "compass", "✨": "star", "📈": "chart-line", "🚶": "walking", "🧩": "puzzle-piece", "🔗": "link",
                  "🚧": "ban", "⏳": "hourglass-half", "📚": "book", "👥": "users", "🎯": "bullseye", "⚙": "cogs", "🧱": "cubes",
                  "🗓": "calendar-alt", "🏢": "building"}

def frente(texto: str) -> tuple[dict, str]:
    """Separa o front-matter de uma página de leitura (chave: valor, listas entre colchetes) do corpo."""
    if not texto.startswith("---\n"):
        return {}, texto
    bloco, _, corpo = texto[4:].partition("\n---\n")
    dados: dict = {}
    for linha in bloco.splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", linha)
        if not m:
            continue
        valor = m.group(2).split(" #", 1)[0].strip()
        if valor.startswith("[") and valor.endswith("]"):
            valor = [a or b.strip() for a, b in re.findall(r'"([^"]*)"|([^,]+)', valor[1:-1]) if a or b.strip()]
        dados[m.group(1)] = valor
    return dados, corpo

def ascii_slug(texto: str) -> str:
    """O slug do GitHub (minúsculas, sem pontuação, espaço vira hífen), sem acentos."""
    t = unicodedata.normalize("NFKD", texto.strip().lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9_\- ]", "", t)
    return t.replace(" ", "-")

def texto_inline(tok: Token) -> str:
    return "".join(c.content for c in (tok.children or []) if c.type in ("text", "code_inline"))

# As 19 mfs da v2 (MF-101 a MF-119). Os códigos antigos (MF-01, MF-001) não casam.
PADRAO_MF = re.compile(r"MF-(1(?:0[1-9]|1[0-9]))(?!\d)")

def mfs_em(texto: str) -> set[str]:
    return {"MF-" + m.group(1) for m in PADRAO_MF.finditer(texto)}

def sem_ids(tokens: list[Token]) -> list[Token]:
    """Cópia dos tokens sem os ids, para o trecho citado na página da MF não repetir a âncora do documento."""
    copia = copy.deepcopy(tokens)
    for t in copia:
        if t.attrs:
            t.attrs.pop("id", None)
    return copia

def fim_da_secao(tokens: list[Token], i: int) -> int:
    """O índice do próximo título do mesmo nível ou acima do título em i."""
    nivel, j = int(tokens[i].tag[1]), i + 3
    while j < len(tokens) and not (tokens[j].type == "heading_open" and int(tokens[j].tag[1]) <= nivel):
        j += 1
    return j

# Os assuntos da página de cada MF, na ordem da página, e os documentos de onde cada um vem.
# O ícone de cada assunto no índice da página (Font Awesome 5), os do modelo 01 aprovado pelo dono.
ICONES = {"o-que-e": "book-open", "entregas": "box-open", "objetivos": "bullseye", "decisoes-produto": "tasks",
          "arquitetura": "layer-group", "decisoes-arquitetura": "project-diagram", "v1": "history", "citada": "link"}
# Os textos do índice da página de MF: os tópicos de cada assunto são as fontes de onde ele vem.
TOPICOS_MF = {"title": "De onde vem", "text": "Referências que fundamentam esta funcionalidade",
              "unit": ["referência", "referências"], "none": "Outras citações", "empty": "Nenhuma referência listada no índice."}

ASSUNTOS = [
    ("o-que-e", "O que é", ["produto-mfs-hoje", "produto-lacunas"]),
    ("entregas", "Nas entregas", ["produto-v20", "produto-versoes"]),
    ("objetivos", "Objetivos", ["produto-mapa"]),
    ("decisoes-produto", "Decisões de produto", ["produto-backlog"]),
    ("arquitetura", "Arquitetura", ["arquitetura-01", "arquitetura-03", "arquitetura-04", "arquitetura-05", "arquitetura-06", "arquitetura-07",
                                    "arquitetura-08", "arquitetura-09", "arquitetura-10", "arquitetura-11", "arquitetura-12", "arquitetura-13"]),
    ("decisoes-arquitetura", "Decisões de arquitetura", ["arquitetura-02"]),
    ("v1", "O que se reaproveita da v1", ["arquitetura-14"]),
]

def main() -> int:
    raiz, destino, mermaid_js = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    md = MarkdownIt("commonmark", {"html": False}).enable("table").enable("strikethrough")
    # As fontes do portal: a visão geral de leitura, o inventário (DOCS) e a página de leitura de cada mf.
    paginas_leitura = []
    for caminho_mf in sorted((raiz / LEITURA / "mfs").glob("mf-1*.md")):
        fm, _ = frente(caminho_mf.read_text(encoding="utf-8"))
        paginas_leitura.append((caminho_mf.relative_to(raiz).as_posix(), fm["codigo"].lower(), fm["nome"], "", "", False))
    fontes = [VISAO_GERAL, *DOCS, *paginas_leitura]
    leitura = {f[1] for f in fontes if f[0].startswith(LEITURA + "/")}
    por_caminho = {d[0]: d[1] for d in fontes}
    ids: set[str] = set()
    for d in fontes:
        ids.update({d[1], "title-" + d[1]})
    # As 19 mfs e a entrega de cada uma vêm da seção 4 do 01 (que já tem a ARQ-090). Cada uma ganha uma página, mf-1nn.
    estrategia = (raiz / "docs/raw/arquitetura/01-estrategia-da-solucao.md").read_text(encoding="utf-8")
    entrega = {m.group(1): (m.group(2).strip(), m.group(3).strip()) for m in re.finditer(r"^\| `(MF-\d{3}):([^`]+)` \| ([^|]+) \|", estrategia, re.M)}
    if len(entrega) != 19:
        raise SystemExit(f"esperadas 19 MFs na seção 4 do 01, achadas {len(entrega)}")
    ids.update(codigo.lower() for codigo in entrega)
    docs = []
    curtos: dict[str, list[str]] = {}
    linhas_mf: dict[tuple[str, str], list[str]] = {}
    # ---------------------------------------------------------------- passo 1: títulos e IDs
    for caminho, sid, titulo, resumo, categoria, destaque in fontes:
        fm, texto = frente((raiz / caminho).read_text(encoding="utf-8"))
        texto = texto.lstrip("\n")
        linhas = texto.split("\n")
        if linhas and linhas[0].startswith("# "):
            texto = "\n".join(linhas[1:])
        tokens = md.parse(texto)
        for i, tok in enumerate(tokens):
            if tok.type == "heading_open":
                nivel = min(6, max(3, int(tok.tag[1]) + 1))
                tok.tag = f"h{nivel}"
                tokens[i + 2].tag = f"h{nivel}"
                if sid in leitura and nivel == 3:
                    filhos = tokens[i + 1].children or []
                    primeiro = next((c for c in filhos if c.type == "text" and c.content.strip()), None)
                    em = primeiro and re.match(r"^\s*([←-⯿\U0001f000-\U0001faff]️?)\s+", primeiro.content)
                    if em:
                        primeiro.content = primeiro.content[em.end():]
                        icone = ICONES_LEITURA.get(em.group(1).replace("️", ""))
                        if icone:
                            tok.attrSet("data-dx-icone", icone)
                nome = texto_inline(tokens[i + 1])
                m = re.match(r"(ARQ|D)-(\d{3}) ·", nome)
                base = (m.group(1).lower() + "-" + m.group(2)) if m else (sid + "-" + (ascii_slug(nome) or "secao"))
                ident, k = base, 2
                while ident in ids:
                    ident, k = f"{base}-{k}", k + 1
                ids.add(ident)
                tok.attrSet("id", ident)
                if m:
                    curtos.setdefault(base, []).append(ident)
            # A linha de cada MF nas tabelas do 06-versoes e da seção 4 do 01 ganha âncora, para os cartões da entrada.
            if tok.type == "tr_open" and sid in ("produto-versoes", "arquitetura-01"):
                celula = next((x for x in tokens[i:i + 4] if x.type == "inline"), None)
                mm = celula and re.match(r"`?(MF-\d{3})", celula.content)
                if mm:
                    base, k = f"{sid}-{mm.group(1).lower()}", 2
                    ident = base
                    while ident in ids:
                        ident, k = f"{base}-{k}", k + 1
                    ids.add(ident)
                    tok.attrSet("id", ident)
                    linhas_mf.setdefault((sid, mm.group(1)), []).append(ident)
        docs.append(dict(caminho=caminho, sid=sid, titulo=titulo, resumo=resumo, categoria=categoria, destaque=destaque, tokens=tokens,
                         leitura=sid in leitura, fm=fm))
    ambiguos = {k for k, v in curtos.items() if len(v) > 1} | {"d-000"}
    avisos: list[str] = []

    def ancora(alvo: str, frag: str, origem: str) -> str:
        a = ascii_slug(unquote(frag))
        m = re.match(r"(arq|d)-(\d{3})(-|$)", a)
        if m:
            curto = f"{m.group(1)}-{m.group(2)}"
            if curto in ids and curto not in ambiguos:
                return curto
        if alvo + "-" + a in ids:
            return alvo + "-" + a
        avisos.append(f"{origem}: âncora #{frag} não achada em {alvo}; o link vai ao início da seção")
        return alvo

    por_nome: dict[str, list[str]] = defaultdict(list)
    for caminho_doc in por_caminho:
        por_nome[PurePosixPath(caminho_doc).name].append(caminho_doc)

    def normalizar(caminho: str) -> str:
        partes: list[str] = []
        for p in PurePosixPath(caminho).parts:
            if p == "..":
                partes = partes[:-1]
            elif p != ".":
                partes.append(p)
        return "/".join(partes)

    def resolver_md(ref: str, base_dir: PurePosixPath) -> str | None:
        """O caminho de um .md citado entre crases: a página dele no portal (#id), o arquivo no GitHub ou nada.
        Com barra, vale primeiro o caminho a partir da raiz do repositório; sem barra, o da pasta do documento."""
        a_partir_da_raiz, ao_lado = normalizar(ref), normalizar(str(base_dir / ref))
        candidatos = [a_partir_da_raiz, ao_lado] if "/" in ref else [ao_lado, a_partir_da_raiz]
        for cand in candidatos:
            if cand in por_caminho:
                return "#" + por_caminho[cand]
        if "/" not in ref and len(por_nome.get(ref, [])) == 1:
            return "#" + por_caminho[por_nome[ref][0]]  # o nome solto de um documento que só existe uma vez
        for cand in candidatos:
            if (raiz / cand).is_file():
                return REPO_BLOB + cand
        return None

    # ---------------------------------------------------------------- passo 2: links, códigos e diagramas
    diagramas = []
    for d in docs:
        sid, base_dir = d["sid"], PurePosixPath(d["caminho"]).parent
        tokens = d["tokens"]
        titulo_atual = d["titulo"]
        for i, tok in enumerate(tokens):
            if tok.type == "heading_open":
                titulo_atual = texto_inline(tokens[i + 1])
            if tok.type == "fence" and tok.info.strip() == "mermaid":
                n = sum(1 for x in diagramas if x["sid"] == sid) + 1
                nome = f"media/{sid}-diagrama-{n}.svg"
                diagramas.append(dict(sid=sid, arquivo=nome, fonte=tok.content, titulo=titulo_atual))
                tok.meta = {"diagrama": nome, "titulo": titulo_atual}
            if tok.type != "inline" or not tok.children:
                continue
            dentro_titulo = i > 0 and tokens[i - 1].type == "heading_open"
            filhos, novos, em_link = tok.children, [], 0
            for c in filhos:
                if c.type == "link_open":
                    href = c.attrGet("href") or ""
                    if re.match(r"^(https?:|mailto:)", href):
                        pass
                    elif href.startswith("#"):
                        c.attrSet("href", "#" + ancora(sid, href[1:], d["caminho"]))
                    else:
                        caminho, _, frag = href.partition("#")
                        alvo_caminho = str(PurePosixPath(*[p for p in (base_dir / unquote(caminho)).parts])) if caminho else d["caminho"]
                        partes = []
                        for p in PurePosixPath(alvo_caminho).parts:
                            if p == "..":
                                partes = partes[:-1]
                            elif p != ".":
                                partes.append(p)
                        normal = "/".join(partes).rstrip("/")
                        alvo = por_caminho.get(normal) or DIRS.get(normal)
                        if alvo:
                            c.attrSet("href", "#" + (ancora(alvo, frag, d["caminho"]) if frag else alvo))
                        elif normal.endswith(".md") and (raiz / normal).is_file():
                            c.attrSet("href", REPO_BLOB + normal)
                        else:
                            c.meta = {"remover": True}
                            avisos.append(f"{d['caminho']}: link para fora do portal virou texto: {href}")
                    em_link += 1
                    novos.append(c)
                    continue
                if c.type == "link_close":
                    em_link -= 1
                    novos.append(c)
                    continue
                if c.type == "code_inline" and not em_link and not dentro_titulo:
                    destino_md = resolver_md(c.content, base_dir) if re.fullmatch(r"[\w./-]+\.md", c.content) else None
                    if destino_md:
                        a = Token("link_open", "a", 1); a.attrSet("href", destino_md)
                        novos.extend([a, c, Token("link_close", "a", -1)])
                        continue
                    m = re.fullmatch(r"(ARQ|D)-(\d{3})", c.content)
                    curto = m and (m.group(1).lower() + "-" + m.group(2))
                    # "MF-110" e "MF-110:Pergunta rápida" levam à página da MF.
                    mf = re.fullmatch(r"(MF-\d{3})(?::.*)?", c.content)
                    if mf and mf.group(1) in entrega:
                        curto = mf.group(1).lower()
                    if curto and curto in ids and curto not in ambiguos:
                        a = Token("link_open", "a", 1); a.attrSet("href", "#" + curto)
                        novos.extend([a, c, Token("link_close", "a", -1)])
                        continue
                novos.append(c)
            # os links removidos: fecha o par também
            pilha, saida = [], []
            for c in novos:
                if c.type == "link_open":
                    pilha.append(bool(c.meta and c.meta.get("remover")))
                    if pilha[-1]:
                        continue
                elif c.type == "link_close":
                    if pilha and pilha.pop():
                        continue
                saida.append(c)
            # Cada campo em negrito numa linha própria ("**Quem decide:**", "**Decisão:**"…) continua numa linha própria.
            # Só no inventário: na leitura, uma linha quebrada que começa em negrito é só o texto que continua.
            for j in range(len(saida) - 1 if not d["leitura"] else 0):
                k = j + 1
                while k < len(saida) and saida[k].type == "text" and not saida[k].content:
                    k += 1  # o markdown-it-py põe um texto vazio entre a quebra e o negrito
                if saida[j].type == "softbreak" and k < len(saida) and saida[k].type == "strong_open":
                    saida[j] = Token("hardbreak", "br", 0)
            tok.children = saida

    # ---------------------------------------------------------------- render
    estado = {"thead": False, "tabela": 0, "titulo": ""}
    def r_table_open(self, tokens, idx, options, env):
        estado["tabela"] += 1
        rotulo = escape(f"Tabela {estado['tabela']} de {env['titulo']}", quote=True)
        return f'<div class="table-responsive" tabindex="0" role="region" aria-label="{rotulo}"><table class="table table_shortcode">'
    def r_table_close(self, tokens, idx, options, env):
        return "</table></div>"
    def r_thead_open(self, tokens, idx, options, env):
        estado["thead"] = True; return "<thead>"
    def r_thead_close(self, tokens, idx, options, env):
        estado["thead"] = False; return "</thead>"
    def r_th_open(self, tokens, idx, options, env):
        return '<th scope="col">' if estado["thead"] else "<th>"
    def r_fence(self, tokens, idx, options, env):
        tok = tokens[idx]
        if tok.meta and tok.meta.get("diagrama"):
            arq, tit = tok.meta["diagrama"], tok.meta["titulo"]
            w, h = env["dimensoes"][arq]
            alt = escape(f"Diagrama: {tit}", quote=True)
            return (f'<figure><div class="lightbox_shortcode"><img src="{arq}" width="{w}" height="{h}" alt="{alt}">'
                    f'<a href="{arq}" class="img_popup" aria-label="Ampliar o diagrama"><i class="icon_plus" aria-hidden="true"></i></a></div>'
                    f'<figcaption>Diagrama de “{escape(tit)}”. Selecione o “+” para ampliar.</figcaption></figure>')
        lang = re.sub(r"[^a-z0-9-]", "", (tok.info.strip().split() or ["none"])[0].lower()) or "none"
        return f'<pre class="snippets"><code class="language-{lang}" data-lang="{lang}">{escape(tok.content)}</code></pre>'
    for nome, f in [("table_open", r_table_open), ("table_close", r_table_close), ("thead_open", r_thead_open), ("thead_close", r_thead_close), ("th_open", r_th_open), ("fence", r_fence), ("code_block", r_fence)]:
        md.add_render_rule(nome, f)

    # ---------------------------------------------------------------- diagramas em SVG
    (destino / "media").mkdir(parents=True, exist_ok=True)
    (destino / "content").mkdir(parents=True, exist_ok=True)
    dimensoes = {}
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page()
        pag.set_content("<!doctype html><html><body></body></html>")
        pag.add_script_tag(path=str(mermaid_js))
        pag.evaluate("""() => mermaid.initialize({startOnLoad: false, securityLevel: 'strict', theme: 'base',
            fontFamily: 'Segoe UI, system-ui, sans-serif',
            themeVariables: {primaryColor: '#E7F0FA', primaryBorderColor: '#1668BE', primaryTextColor: '#1d2746',
              lineColor: '#58647a', secondaryColor: '#F6F8FB', tertiaryColor: '#FFFFFF', fontFamily: 'Segoe UI, system-ui, sans-serif'},
            htmlLabels: false, flowchart: {htmlLabels: false, curve: 'basis'}, sequence: {useMaxWidth: false}})""")
        # O SVG vai dentro de <img>: precisa ser XML bem formado, com tamanho e fundo próprios.
        js = """async ([id, src]) => {
            const {svg} = await mermaid.render(id, src);
            const caixa = document.createElement('div'); caixa.innerHTML = svg;
            const el = caixa.querySelector('svg'); const vb = el.viewBox.baseVal;
            el.removeAttribute('style'); el.removeAttribute('width'); el.removeAttribute('height');
            el.setAttribute('width', Math.round(vb.width)); el.setAttribute('height', Math.round(vb.height));
            const fundo = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            for (const [k, v] of [['x', vb.x], ['y', vb.y], ['width', vb.width], ['height', vb.height], ['fill', '#ffffff']]) fundo.setAttribute(k, v);
            el.insertBefore(fundo, el.firstChild);
            return [new XMLSerializer().serializeToString(el), Math.round(vb.width), Math.round(vb.height)];
        }"""
        import xml.etree.ElementTree as ET
        for i, dg in enumerate(diagramas):
            svg, w, h = pag.evaluate(js, [f"dg{i}", dg["fonte"]])
            ET.fromstring(svg)  # aborta se o XML não for bem formado
            (destino / dg["arquivo"]).write_text(svg, encoding="utf-8")
            dimensoes[dg["arquivo"]] = (w, h)
        nav.close()

    # ---------------------------------------------------------------- fragmentos e configuração
    def identificacao(sid: str, fm: dict) -> str:
        """A identificação da mf, do front-matter da página de leitura, como a primeira seção da página."""
        lista = lambda v: ", ".join(v) if isinstance(v, list) else str(v)
        relacionadas = ", ".join(f'<a href="#{escape(c.lower(), quote=True)}">{escape(entrega[c][0])}</a> ({escape(c)})' for c in fm.get("relacionadas", []) if c in entrega)
        data = fm.get("atualizado", "")
        linhas_id = [("Código", escape(fm.get("codigo", ""))), ("Entrega", escape(fm.get("entrega", ""))), ("Situação", escape(fm.get("situacao", ""))),
                     ("Camada", escape(fm.get("camada", ""))), ("Objetivos", escape(lista(fm.get("objetivos", [])))),
                     ("Quem usa", escape(lista(fm.get("quem_usa", [])))), ("Complexidade", escape(fm.get("complexidade", ""))),
                     ("Relacionadas", relacionadas), ("Atualizado", escape("/".join(reversed(data.split("-"))) if data else ""))]
        corpo = "".join(f'<tr><th scope="row">{rotulo}</th><td>{valor}</td></tr>' for rotulo, valor in linhas_id if valor)
        rotulo_tabela = escape(f"Identificação de {fm.get('codigo', '')} · {fm.get('nome', '')}", quote=True)
        return (f'<h3 id="{sid}-identificacao" data-dx-icone="id-card">Identificação</h3>'
                f'<div class="table-responsive" tabindex="0" role="region" aria-label="{rotulo_tabela}"><table class="table table_shortcode"><tbody>{corpo}</tbody></table></div>\n')

    secoes = []
    for d in docs:
        estado["tabela"] = 0
        html = md.renderer.render(d["tokens"], md.options, {"titulo": d["titulo"], "dimensoes": dimensoes})
        if d["leitura"] and d["fm"].get("codigo"):
            # A página de leitura da mf: a identificação logo depois da frase-resumo, e o caminho até o inventário no fim.
            corte = html.find("<h3")
            corte = corte if corte >= 0 else len(html)
            inventario = f'{d["sid"]}-inventario'
            html = (html[:corte] + identificacao(d["sid"], d["fm"]) + html[corte:]
                    + f'<p>📚 <a href="#{inventario}">Tudo o que o inventário diz desta mf, assunto por assunto</a>.</p>\n')
            (destino / "content" / f"{d['sid']}.html").write_text(html, encoding="utf-8")
            continue
        (destino / "content" / f"{d['sid']}.html").write_text(html, encoding="utf-8")
        s = {"id": d["sid"], "title": d["titulo"], "summary": d["resumo"], "category": d["categoria"], "source": f"content/{d['sid']}.html"}
        if d["destaque"]:
            s["featured"] = True
        if d["sid"] in EMOJI_DOC:
            s["emoji"] = EMOJI_DOC[d["sid"]]
        secoes.append(s)
    # Os logos horizontais do Horus: o de texto escuro para o fundo claro, o de texto claro para o topo do portal.
    marca_dir = raiz.resolve() / "docs" / "marca"
    for nome in ("horus-claro.svg", "horus-escuro.svg"):
        (destino / "media" / nome).write_bytes((marca_dir / nome).read_bytes())
    (destino / "media" / "horus-marca.svg").unlink(missing_ok=True)
    # ---------------------------------------------------------------- as páginas das mfs
    # Cada página junta o que os documentos já dizem da MF, sem texto novo: as linhas de tabela que a citam, as seções
    # com ela no título, as decisões de produto (D-) e de arquitetura (ARQ-) e, por fim, onde mais ela é citada.
    por_sid = {d["sid"]: d for d in docs}
    assunto_de = {sid: chave for chave, _, sids in ASSUNTOS for sid in sids}
    tabelas = defaultdict(list)       # (mf, sid) -> [(id do título, título, tokens da tabela)]
    secoes_mf = defaultdict(list)     # (mf, sid) -> [(id do título, título, tokens do corpo)]
    citada = defaultdict(dict)        # mf -> {(sid, id do título): (documento, título)}
    for d in docs:
        if d["leitura"]:
            continue                  # a agregação é do inventário; a leitura não entra nela
        sid, tokens = d["sid"], d["tokens"]
        trechos = defaultdict(list)   # mf -> [(início, fim)] das seções já copiadas, para não citar duas vezes
        if sid not in ("produto-backlog", "arquitetura-02"):
            for i, tok in enumerate(tokens):
                if tok.type == "heading_open":
                    for mf in mfs_em(tokens[i + 1].content) & set(entrega):
                        j = fim_da_secao(tokens, i)
                        secoes_mf[(mf, sid)].append((tok.attrGet("id"), texto_inline(tokens[i + 1]), tokens[i + 3:j]))
                        trechos[mf].append((i, j))
        dentro = lambda mf, k: any(a <= k < b for a, b in trechos[mf])
        cabeca, n_tabela, k, depois_das_decisoes = (sid, d["titulo"]), 0, 0, False
        while k < len(tokens):
            tok = tokens[k]
            if tok.type == "heading_open":
                cabeca = (tok.attrGet("id"), texto_inline(tokens[k + 1]))
                depois_das_decisoes = depois_das_decisoes or (sid == "produto-backlog" and cabeca[1] == "Decisões")
            elif tok.type == "table_open":
                fim = next(x for x in range(k, len(tokens)) if tokens[x].type == "table_close")
                n_tabela += 1
                # No 02, só o índice; no backlog, só as pendências (as tabelas das decisões são de conversão de números).
                vale = not ((sid == "arquitetura-02" and n_tabela > 1) or (sid == "produto-backlog" and depois_das_decisoes))
                cab_ini = next(x for x in range(k, fim) if tokens[x].type == "thead_open")
                cab_fim = next(x for x in range(k, fim) if tokens[x].type == "thead_close")
                linhas_por_mf = defaultdict(list)
                x = cab_fim
                while x < fim:
                    if tokens[x].type == "tr_open":
                        y = next(z for z in range(x, fim) if tokens[z].type == "tr_close")
                        achadas = set().union(*[mfs_em(t.content) for t in tokens[x:y] if t.type == "inline"]) & set(entrega)
                        for mf in achadas:
                            if vale and not dentro(mf, x):
                                linhas_por_mf[mf].append(tokens[x:y + 1])
                        x = y
                    x += 1
                for mf, linhas in linhas_por_mf.items():
                    corpo = [tokens[k]] + tokens[cab_ini:cab_fim + 1] + [Token("tbody_open", "tbody", 1)] + [t for l in linhas for t in l] + [Token("tbody_close", "tbody", -1), tokens[fim]]
                    tabelas[(mf, sid)].append((cabeca[0], cabeca[1], corpo))
                k = fim
            elif tok.type == "inline" and tokens[k - 1].type != "heading_open" and sid not in ("produto-backlog", "arquitetura-02"):
                for mf in mfs_em(tok.content) & set(entrega):
                    if not dentro(mf, k):
                        citada[mf][(sid, cabeca[0])] = (d["titulo"], cabeca[1])
            k += 1
    # As decisões de produto: cada D- que cita a MF fora das tabelas; a "Definição macro" dela entra inteira no "O que é".
    decisoes_d, definicoes = defaultdict(list), defaultdict(list)
    tokens = por_sid["produto-backlog"]["tokens"]
    for i, tok in enumerate(tokens):
        if tok.type != "heading_open":
            continue
        m = re.match(r"D-(\d{3}) · (.*)", texto_inline(tokens[i + 1]))
        if not m or m.group(1) == "000":
            continue
        j = fim_da_secao(tokens, i)
        corpo = tokens[i + 3:j]
        em_tabela, mencoes, situacao, versao = 0, mfs_em(m.group(2)), "", ""
        for t in corpo:
            em_tabela += 1 if t.type == "table_open" else -1 if t.type == "table_close" else 0
            if t.type == "inline" and not em_tabela:
                mencoes |= mfs_em(t.content)
                s = re.match(r"Situação: (.+?)(?: \(|$| ·)", t.content)
                if s and not situacao:
                    situacao = s.group(1).strip()
                    v = re.search(r"Versão: ([^·\n]+)", t.content)
                    versao = v.group(1).strip() if v else ""
        for mf in mencoes & set(entrega):
            decisoes_d[mf].append((tok.attrGet("id"), "D-" + m.group(1), m.group(2), situacao, versao))
            if m.group(2).startswith("Definição macro") and mf in mfs_em(m.group(2)):
                definicoes[mf].append((tok.attrGet("id"), "D-" + m.group(1), corpo))

    def fonte(texto_antes: str, ident: str, titulo: str) -> str:
        return f'<p class="dx-fonte">{texto_antes} <a href="#{escape(ident, quote=True)}">{escape(titulo)}</a>:</p>'

    paginas_mf, assuntos_mf = {}, {}
    for codigo, (nome, quando) in entrega.items():
        pid = codigo.lower() + "-inventario"
        env = {"titulo": f"{codigo} · {nome}", "dimensoes": dimensoes}
        estado["tabela"] = 0
        partes, assuntos = [], []
        for chave, titulo_assunto, sids in ASSUNTOS:
            blocos = []
            if chave == "o-que-e":
                for ident, numero, corpo in definicoes[codigo]:
                    blocos.append(f'<h4 id="{pid}-{ident}">Definição macro · {numero}</h4>' + fonte("No", ident, f"Backlog estratégico, {numero}")
                                  + md.renderer.render(sem_ids(corpo), md.options, env))
            if chave == "decisoes-produto" and decisoes_d[codigo]:
                linhas_d = "".join(f'<tr><td><a href="#{escape(ident, quote=True)}"><code>{numero}</code></a></td><td>{escape(titulo)}</td><td>{escape(situacao)}</td><td>{escape(versao)}</td></tr>'
                                   for ident, numero, titulo, situacao, versao in decisoes_d[codigo])
                estado["tabela"] += 1
                blocos.append(f'<h4 id="{pid}-produto-backlog-d">Backlog estratégico · {len(decisoes_d[codigo])} decisões</h4>'
                              f'<div class="table-responsive" tabindex="0" role="region" aria-label="{escape("Decisões de produto de " + env["titulo"], quote=True)}">'
                              '<table class="table table_shortcode"><thead><tr><th scope="col">Nº</th><th scope="col">Decisão</th><th scope="col">Situação</th><th scope="col">Versão</th></tr></thead>'
                              f'<tbody>{linhas_d}</tbody></table></div>')
            for sid in sids:
                pedacos = []
                for ident, titulo, corpo in secoes_mf[(codigo, sid)]:
                    pedacos.append(fonte("A seção", ident, titulo) + md.renderer.render(sem_ids(corpo), md.options, env))
                for ident, titulo, corpo in tabelas[(codigo, sid)]:
                    pedacos.append(fonte("Em", ident, titulo) + md.renderer.render(sem_ids(corpo), md.options, env))
                if pedacos:
                    nome_doc = por_sid[sid]["titulo"] if sid != "produto-backlog" else "Backlog estratégico · pendências"
                    blocos.append(f'<h4 id="{pid}-{sid}">{escape(nome_doc)}</h4>' + "".join(pedacos))
            if blocos:
                assuntos.append(chave)
                partes.append(f'<h3 id="{pid}-{chave}" data-dx-icone="{ICONES[chave]}">{escape(titulo_assunto)}</h3>' + "".join(blocos))
        outros = [(sid, ident, doc, titulo) for (sid, ident), (doc, titulo) in citada[codigo].items()]
        if outros:
            assuntos.append("citada")
            itens = "".join(f'<li><a href="#{escape(ident, quote=True)}">{escape(doc)}{"" if ident == sid else " · " + escape(titulo)}</a></li>' for sid, ident, doc, titulo in outros)
            partes.append(f'<h3 id="{pid}-citada" data-dx-icone="{ICONES["citada"]}">Também citada em</h3><ul>{itens}</ul>')
        (destino / "content" / f"{pid}.html").write_text("\n".join(partes) + "\n", encoding="utf-8")
        paginas_mf[codigo], assuntos_mf[codigo] = pid, assuntos
        # A agregação é uma página fora dos índices: chega-se a ela pelo cartão e pela página de leitura da mf.
        secoes.append({"id": pid, "title": f"{nome}: o inventário", "category": "Inventário das mfs", "source": f"content/{pid}.html",
                       "summary": f"Tudo o que os documentos do inventário dizem da {codigo}, assunto por assunto.",
                       "listed": False, "topics": TOPICOS_MF})

    # ---------------------------------------------------------------- a entrada: os cartões das mfs
    # O que entra em cada versão vem do 06-versoes. O cartão leva à página da MF: o título, ao começo; "Produto" e
    # "Arquitetura", aos assuntos. A primeira aparição da MF declara a página; a extensão na v2.1 só aponta para ela.
    versoes = (raiz / "docs/raw/produto/06-versoes.md").read_text(encoding="utf-8")
    i21 = versoes.index("## 🟢 v2.1")
    linhas = lambda texto: {m.group(1): m.group(3).strip() for m in re.finditer(r"^\| `(MF-\d{3})` \| ([^|]+) \| ([^|]+) \|", texto, re.M)}
    entra20, entra21 = linhas(versoes[:i21]), linhas(versoes[i21:versoes.index("## ➖ Fora do produto")])
    com_pagina: set[str] = set()
    def cartao(codigo, nome, resumo, selo, extensao=False):
        pid, assuntos = paginas_mf[codigo], assuntos_mf[codigo]
        leitura_mf = codigo.lower()
        if leitura_mf not in leitura:
            raise SystemExit(f"falta a página de leitura da {codigo} em {LEITURA}/mfs/")
        produto = next((a for a in (["entregas"] if extensao else ["o-que-e", "entregas", "objetivos", "decisoes-produto"]) if a in assuntos), None)
        arquitetura = next((a for a in ("arquitetura", "decisoes-arquitetura", "v1") if a in assuntos), None)
        c = {"code": codigo, "title": nome, "summary": resumo, "badge": selo, "links": []}
        if codigo in EMOJI_MF:
            c["emoji"] = EMOJI_MF[codigo]
        if produto:
            c["links"].append({"label": "Produto", "href": f"#{pid}-{produto}"})
        if arquitetura:
            c["links"].append({"label": "Arquitetura", "href": f"#{pid}-{arquitetura}"})
        if codigo in com_pagina:
            c["href"] = f"#{leitura_mf}"
        else:
            com_pagina.add(codigo)
            c.update(id=leitura_mf, source=f"content/{leitura_mf}.html")
        return c
    v20, v21 = [], []
    for codigo, (nome, quando) in entrega.items():
        so_21 = quando.startswith(("v2.1", "As duas etapas na v2.1"))
        if not so_21:
            v20.append(cartao(codigo, nome, entra20[codigo], "v2.0 + v2.1" if "v2.1" in quando else "v2.0"))
    for codigo, (nome, quando) in entrega.items():
        so_21 = quando.startswith(("v2.1", "As duas etapas na v2.1"))
        if so_21 and codigo in entra20 and codigo in entra21:
            v21.append(cartao(codigo, nome, entra20[codigo].rstrip(".") + ". " + entra21[codigo], "v2.1"))
        elif so_21:
            v21.append(cartao(codigo, nome, entra21[codigo], "v2.1"))
        elif codigo in entra21:
            v21.append(cartao(codigo, nome, entra21[codigo], "extensão", extensao=True))
    novas = sum(1 for c in v21 if c["badge"] == "v2.1")
    # A região "Visão" da entrada: um cartão por tópico da página "O Horus v2" (o Comece aqui). O resumo é escrito à mão: o
    # primeiro parágrafo de cada tópico ("Três problemas, nesta ordem:") não serve de resumo. O id é o do tópico, sem o prefixo.
    visao_topicos = [
        ("o-que-e-o-horus", "💡", "O que é o Horus", "Um chat de análise: pergunte do jeito que fala e receba gráfico, tabela, indicador ou texto, com a fonte de cada número."),
        ("para-quem", "👥", "Para quem", "O gestor de área, o executivo e o comprador."),
        ("que-problemas-resolve", "🎯", "Que problemas resolve", "A pergunta de análise na hora, a investigação do porquê e o aviso quando algo muda."),
        ("como-funciona-em-grandes-linhas", "⚙️", "Como funciona, em grandes linhas", "Do dado ligado ao aviso que chega sozinho, em seis passos."),
        ("as-macro-funcionalidades", "🧩", "As macro funcionalidades", f"As {len(paginas_mf)} mf: cada uma entrega um valor inteiro a alguém, e elas se agrupam em camadas."),
        ("as-entregas-v20-e-v21", "🚀", "As entregas: v2.0 e v2.1", "A v2.0 sai inteira, de uma vez, em SaaS; a v2.1 reúne o que ficou fora dela."),
        ("como-o-horus-e-entregue", "📦", "Como o Horus é entregue", "Marca branca, uma versão só em SaaS ou on-premises e várias organizações por instância."),
        ("o-que-o-horus-nao-e", "🚫", "O que o Horus não é", "Só lê: não altera nada, não arruma os dados, não inventa número e não decide por você."),
        ("para-saber-mais", "📚", "Para saber mais", "Os documentos que aprofundam a visão: o norte do produto, os temas, a v2.0 consolidada e mais."),
    ]
    visao = [{"code": f"{n:02d}", "emoji": emoji, "title": titulo, "summary": resumo, "href": f"visao-geral.html#visao-geral-{ident}",
              "links": [{"label": "Ler", "href": f"#visao-geral-{ident}"}]}
             for n, (ident, emoji, titulo, resumo) in enumerate(visao_topicos, 1)]
    config = {
        "schema_version": 1, "language": "pt-BR", "layout": "portal",
        "project": {
            "name": "Horus v2",
            "description": "A documentação de produto e de arquitetura do Horus v2: a visão, as decisões, a estratégia e como ele vai ser construído.",
            "version": "v2.0 em desenho, sem versão publicada",
            "owner": "Maind Tech",
            "updated": "2026-11-03",
            "eyebrow": "Maind Horus / Horus v2",
            "hero_title": "O Horus v2, do produto à arquitetura.",
            "footer": "Maind Horus · Horus v2 · documento interno",
            "header_links": False,
            "logo": "media/horus-claro.svg",
            "logo_light": "media/horus-escuro.svg",
            "nav_button": "Comece aqui",
        },
        "portal": {"macros": {"title": "Visão e macro funcionalidades", "groups": [
            {"label": "Visão", "text": f"O que é o Horus, em {len(visao)} passos: o conteúdo do Comece aqui.", "items": visao},
            {"label": "v2.0", "text": f"A primeira entrega: {len(v20)} macro funcionalidades.", "items": v20},
            {"label": "v2.1", "text": f"A segunda entrega: {novas} macro funcionalidades novas e {len(v21) - novas} extensões.", "items": v21},
        ]}},
        "assets": [{"source": "media/horus-claro.svg", "target": "media/horus-claro.svg"}, {"source": "media/horus-escuro.svg", "target": "media/horus-escuro.svg"}]
                  + [{"source": dg["arquivo"], "target": dg["arquivo"]} for dg in diagramas],
        "sections": secoes,
    }
    (destino / "docx.json").write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(secoes)} documentos, {len(paginas_mf)} páginas de mf, {len(diagramas)} diagramas, {len(ids)} IDs; ambíguos sem link: {sorted(ambiguos)}")
    for a in avisos:
        print("aviso:", a)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
