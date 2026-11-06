# Manual de geração do documento ARQ-xxx: o roteiro e a forma padrão

Situação: 🟡 proposta ao dono · Data: 06/11/2026 · Vale para: as 23 mfs (18 da v2.0 e 5 da v2.1)

Um **documento ARQ-xxx** é a arquitetura de uma macro funcionalidade (mf): `ARQ-101` é a arquitetura da `MF-101`, e o
número é sempre o da mf. Ele existe em duas formas, sempre juntas: o `.md` que o arquiteto escreve com o
[esqueleto](../docs/raw/arquitetura/mfs/_modelo.md) e a página HTML gerada a partir dele.

**O objetivo deste manual** é ser duas coisas:
- o **roteiro** (roadmap): a ordem em que a documentação de arquitetura das 23 mfs é criada, fase a fase e etapa a
  etapa, com o que sai de cada uma;
- a **forma padrão**: como cada documento é, igual nas 23 mfs, para que dois autores que nunca se falaram entreguem
  documentos que parecem do mesmo autor.

| Parte | Seções | O que responde |
| --- | --- | --- |
| **1 · A forma padrão** | 1 a 5 | Como o documento é: o que entra, a anatomia, os diagramas, as ADRs, a entrada |
| **2 · O roteiro** | 6 a 8 | Em que ordem se cria, quem faz cada etapa e o que sai dela |
| **3 · A régua** | 9 a 15 | As regras, as conferências e as armadilhas que o roteiro consulta |

Quem for gerar um documento (uma pessoa ou um agente) lê este manual, o esqueleto e o `.md` da mf, e mais nada.

**Na leitura:** "**assunto** N" é um dos 17 assuntos do documento (a seção N do `.md`); "**seção** N" é uma seção deste
manual.

**Caminhos.** Os que começam por `docs/` ou `manuais/` são relativos à raiz do repositório `v2-docs`; os demais
(`content/`, `diagramas/`, `docx.json`) são relativos a `documentacao-arquitetura/`.

⚠️ **Nome a confirmar.** `ARQ-nnn` já é o número das **decisões do registro geral** (documento 02, hoje até `ARQ-097`).
Um documento `ARQ-101` e uma decisão `ARQ-101` seriam homônimos assim que o registro chegasse lá. Enquanto o dono não
escolhe, o documento se cita sempre como "o documento ARQ-101" ou "a arquitetura da MF-101", e a decisão, como "a
decisão `ARQ-nnn`".

---

# Parte 1 · A forma padrão

## 1. A regra que manda: componentes e conexões, não código

O documento diz **do que o sistema é feito e como as peças se ligam**. Ele não diz como se programa.

| Entra | Não entra |
| --- | --- |
| O componente: nome, responsabilidade, módulo dono e a tecnologia que a stack já dá | Tabela, coluna, índice, comando de banco |
| A conexão: de quem para quem, por qual contrato, **imediata ou em segundo plano**, e o que trafega **em categoria** ("a contagem de assentos", "o nome de quem ocupa") | Rota, verbo de HTTP, JSON de exemplo, nome de campo |
| O contrato, pelo **nome e pela responsabilidade** ("pedido de turno", "evento assentos cortados") | Assinatura, classe, método, trecho de código |
| O limite que o documento de tema já fixou ("atende em até N segundos") | Passo de implementação, tarefa, estimativa de esforço |
| A decisão (ADR) em termos de componentes e conexões | Nome de arquivo do código novo |

**Exceção única:** o assunto 14 (o que vem da v1.xx) cita o que já existe no repositório do jeito de sempre,
`horus@318db52b:<caminho>`, porque ali o caminho é referência, e não decisão.

**Dois testes de bolso.** (1) Se o trecho pode ser copiado para um editor e compilado, está baixo demais: suba para o
componente. (2) Se alguém de fora do time técnico perceberia a diferença (um gesto, um dado na tela, uma regra, o que se
paga), a decisão não é só do arquiteto: vira ADR 🟡 e vai para a fila do dono.

**O que isso muda no HTML.** A página **não tem** bloco de código (`code-block`) nem abas de código (`codetabs`);
`<code>` fica só para nomes (de componente, de contrato, de decisão). O modelo de dados (MER), o contrato da API e os
diagramas de sequência detalhados são **anexos** (assunto 17): só se linka o que estiver publicado.

## 2. A anatomia: o `.md` e a página

O `.md` (`docs/raw/arquitetura/mfs/mf-nnn-nome.md`) é a **fonte**; a página é **derivada** dele, um para um. O `.md`
segue o [esqueleto](../docs/raw/arquitetura/mfs/_modelo.md): uma parte 0 de **pontos de ataque** e os **17 assuntos**,
sempre na mesma ordem. A página tem **19 `h3`, nesta ordem**, com o número do assunto no título (assim a página e o
`.md` se acham pelo número). O arquivo é `content/arq-nnn.html`; a página do DocX tem `id` `arq-nnn`, e o `id` de cada
`h3` é `arq-nnn-<sufixo>`.

| `h3` | Título na página | Sufixo | O que é |
| --- | --- | --- | --- |
| — | Resumo | `resumo` | A frase, a ficha (módulo, entrega, objetivos, complexidade, situação, data) e o aviso de rascunho |
| 0 | Pontos de ataque | `pontos-de-ataque` | Tabela: assunto, por que pede decisão, quem decide |
| 1 | O que a mf precisa garantir | `garantias` | As exigências E1… e as `D-nnn` |
| 2 | Fronteira e dependências | `fronteira` | Dentro, fora, de quem depende |
| 3 | Componentes, contratos e fluxos | `componentes` | **O diagrama de componentes e conexões** + a tabela dos componentes |
| 4 | Dados e história | `dados` | Categorias, onde moram, retenção |
| 5 | Segurança, acesso e privacidade | `seguranca` | Permissões, em nome de quem, LGPD, abuso |
| 6 | Integrações de fora | `integracoes` | Serviço, contrato, falha, custo |
| 7 | O motor e a IA | `motor` | Só nas mfs que usam o motor |
| 8 | Concorrência, falha e recuperação | `falhas` | Ordem, repetição segura, degradação |
| 9 | Desempenho, volume e custo | `desempenho` | Volume, meta, custo por organização |
| 10 | Observabilidade e avisos | `observabilidade` | O que mede, quem é avisado |
| 11 | Ambientes, publicação e versões | `publicacao` | Migração, SaaS e on-premises |
| 12 | Testes e provas | `testes` | A prova de cada exigência |
| 13 | A tela | `tela` | Só nas mfs com tela |
| 14 | O que vem da v1.xx | `v1` | ♻️ fica · 🔧 reescreve · ❌ sai |
| 15 | Registro de decisão de arquitetura (ADR-xxx) | `adrs` | O índice e **uma ADR por `h4`** (seção 4) |
| 16 | Riscos, o que falta decidir e o que volta ao PO | `riscos` | Riscos, fila do dono, devoluções |
| 17 | Marcos e anexos | `marcos` | O que fica de pé em cada marco; os anexos |

- **Assunto que não vale:** mantenha o `h3` e ponha um aviso `callout--neutral` com o título "Não se aplica" e o motivo.
  Nenhum assunto some da página.
- **Assunto que segue o padrão:** uma frase e a citação (`ARQ-nnn`), sem repetir o documento de tema.
- **Cada `h4`** dentro de um assunto tem `id` `arq-nnn-<sufixo>-<tópico>`; as ADRs são a exceção (`adr-nnn`).
- **O tamanho:** a página é de consulta, mas não é um dossiê. Um assunto que passa de uma tela e meia merece tabela ou
  diagrama, não mais prosa.

## 3. Os diagramas padrão

O DocX **não desenha**: ele embute a página que a skill `archify-maind` entrega. Confira que as duas skills (`archify` e
`archify-maind`) existem e que há Node 18 ou mais; se faltar uma, diga ao dono e siga com tabela. **Nunca** improvise um
desenho nem um visualizador de SVG no lugar do Archify.

**O que desenhar** (e só o que o `.md` confirma):

| Diagrama | Quando | Tipo do Archify | O que mostra |
| --- | --- | --- | --- |
| **Componentes e conexões** | **Sempre, um por documento**, no assunto 3 | `architecture` | Os componentes da mf, os vizinhos de outras mfs e as conexões entre eles |
| **Um fluxo que manda** | Um por fluxo do assunto 3 em que a **ordem das chamadas** importa (de dois a quatro) | `sequence` (ou `workflow`, se for processo) | Quem chama quem, em que ordem, e o que volta |
| **Estados** | Só se a mf tem um ciclo de vida que a arquitetura precisa mostrar | `lifecycle` | Os estados e as passagens |

**Não** se desenha o MER na página de arquitetura (é anexo) e não se desenha o que uma tabela já explica.

**Convenções, iguais nos 23 documentos** (para os diagramas se parecerem):
- Um grupo por **módulo do documento 04** (Fundação, Plataforma, Dados e IA, Motor, Canais, Acompanhar e avisar, Prova e
  controle, Fora do executável). O módulo da mf fica em destaque, e os vizinhos aparecem só com a conexão que importa,
  nomeados como "MF-103 · Assentos".
- O **rótulo da conexão** é o nome do contrato e diz **"imediata"** ou **"em segundo plano"** (fila, caixa de saída).
- O **mesmo tipo de componente** usa o mesmo tipo semântico e o mesmo ícone em todos os documentos.
- **Até uns 12 nós** por diagrama, um diagrama por ideia. Passou disso, divida.
- A linha de apoio do nó vai **inteira no `sublabel`** (o visualizador esconde o `tag` no zoom de leitura).
- A aba **Explicações** leva três cartões (o que o desenho mostra; o que é imediato e o que vai para segundo plano; o
  que ficou de fora). O formato de cartão só aceita itens: cada frase vira um tópico.

**Como fazer cada um** (de `documentacao-arquitetura/`):

```bash
node ~/.claude/skills/archify/bin/archify.mjs finalize architecture diagramas/fontes/arq-101-componentes.json diagramas/fontes/arq-101-componentes.archify.html --quality showcase --json
node ~/.claude/skills/archify-maind/scripts/skin.mjs --html diagramas/fontes/arq-101-componentes.archify.html --spec diagramas/fontes/arq-101-componentes.json --out diagramas/arq-101-componentes.html
```

- Nomes: `arq-nnn-componentes` e `arq-nnn-fluxo-<assunto>`. O `.archify.html` é o artefato dos gates e **não** entra no
  site.
- Declare em `docx.json`, em `diagrams` (`id`, `title`, `description`, `source`) e ponha o marcador **vazio** no
  fragmento.
- O texto continua sendo do fragmento: o diagrama não o substitui, e a busca só lê o título e a descrição dele.
- **Mudou a fonte** (o JSON): refaça o `finalize` e a casca. Editar a página de `diagramas/` se perde.
- 🪤 O Archify trava a pasta `fontes/` durante cada entrega. Em paralelo, cada autor usa `--out-dir
  diagramas/fontes/arq-nnn-review-N`.
- Limites a declarar na entrega: só o MER tem as abas Dados, Links e Descrição completas; os painéis do diagrama abrem
  perto do canto inferior direito.

## 4. A ADR padrão

Cada ADR é um `h4` com `id="adr-nnn"` dentro do assunto 15. A numeração é **uma sequência só para todas as mfs**, e o
índice geral fica em `mfs/README.md` e na página `indice-de-adrs`. Estrutura (copie e troque o texto):

1. O `h4` com o número e o título: `ADR-012 · Título curto`.
2. Uma linha de selos: a **situação**, a data e o alcance.
3. Uma tabela de duas colunas (`table.t`) com **Quem decide · Contexto · Decisão · Aplica · Alternativas · Por que esta
   · Consequências · Reabrir quando**. A linha "Decisão" em `<strong>`.
4. Se for 🟡, um `callout--warning` "Aguarda o dono". Se for ⚪, um `callout--neutral` "Substituída por" com o link
   `#adr-nnn`.

| Situação | Selo |
| --- | --- |
| ✅ Confirmada pelo dono | `badge badge--success` |
| 🟢 Decidida pelo arquiteto | `badge badge--info` |
| 🟡 Proposta ao dono | `badge badge--warning` |
| ⚪ Substituída | `badge` (o padrão) |

Antes das ADRs vai o **índice** da mf (`table.t`: número, decisão, situação, quem decide), com o número como link para o
`h4`. A ADR **não se reescreve**: a nova substitui a antiga, que passa a ⚪ e ganha o aviso. Uma ADR que vale para mais
de uma mf sobe para o registro geral como decisão `ARQ-nnn`, e as páginas a citam em "Aplica".

## 5. A entrada e as páginas de apoio

- **Entrada (`index`)**: o portal do DocX, com `portal.macros` em dois grupos, **v2.0** (18) e **v2.1** (5). Cada cartão
  tem `code` (`ARQ-101`), `badge` (a versão), `title` (o nome da mf), `summary` (a "Em uma frase" do `.md`) e três
  `links`: **Componentes** (`#arq-nnn-componentes`), **Decisões** (`#arq-nnn-adrs`) e **Riscos** (`#arq-nnn-riscos`). Só
  entra no site a mf que já tem `.md`: não se criam páginas vazias.
- **`como-ler`** (categoria "Para começar"): o que a página mostra e o que não mostra (a seção 1 deste manual, em
  linguagem do leitor), os 17 assuntos, as marcas, a legenda dos diagramas e o glossário.
- **`indice-de-adrs`** (categoria "Referência"): uma tabela com todas as ADRs de todas as mfs, em ordem de número, com
  situação, mf e link. É a única página escrita com os dados de todas as mfs.

---

# Parte 2 · O roteiro

## 6. O roteiro em fases

Cinco fases, uma depois da outra. Cada uma só começa quando a anterior está **pronta**.

| Fase | O que se faz | O que sai | Pronto quando |
| --- | --- | --- | --- |
| **0 · Terreno** (uma vez) | O dono confirma o esqueleto, estes manuais, o nome do código do documento (o aviso ⚠️ do começo), a numeração das ADR e o site separado. Conferem-se as skills (`documentar`, `archify`, `archify-maind`, Node 18+) e a marca | A decisão da família registrada; a pasta `documentacao-arquitetura/` com `docx.json` mínimo e `.gitignore`; o `mfs/README.md` com o índice de ADR e o próximo número | O dono confirmou, e o terreno está de pé |
| **1 · Piloto** (MF-101) | Faz-se **um** documento inteiro, do `.md` à página aberta no navegador. Provam-se 🔎 duas coisas: que gerar este site não mexe nos outros de `docs/`, e que o `validar` aceita o link para a página de produto | O `.md` e a página do ARQ da MF-101; os ajustes que o piloto pedir voltam ao esqueleto e a estes manuais | O dono revisou o piloto, e os manuais refletem o que se aprendeu |
| **2 · v2.0** | Os outros 17 documentos, em levas de quatro a cinco, **pelos marcos do documento 01 (§6)** | 18 documentos; o `indice-de-adrs` completo; a fila do dono consolidada | Os 18 estão gerados, conferidos e abertos no navegador |
| **3 · v2.1** | Os 5 restantes, com o aviso "Versão 2.1, em construção" no resumo | 23 documentos | Idem |
| **4 · Publicação** | **Só com ordem do dono** (seção 13) | O site em `docs/arquitetura/`, no Pages | O Pages servindo e conferido ao vivo |

**Depois da fase 4, o roteiro vira rotina:** quando uma decisão muda o que a mf pede, o arquiteto muda o `.md` (a ADR
antiga passa a ⚪ e nasce a nova), regera-se a página e roda-se a seção 12 de novo.

**Onde cada fase trava.** O gargalo é o `.md`: ele precisa do arquiteto, e as ADR 🟡 precisam do dono. A página sai
depressa quando o `.md` está pronto. Por isso a fila do dono (assunto 16) se atende a cada leva, e não só no fim.

## 7. O roteiro de um documento, etapa por etapa

É o que se repete em cada mf das fases 1 a 3. As etapas 1 a 3 são do arquiteto; as 4 a 8 podem ir para um agente.

| # | Etapa | Quem | O que se faz | O que sai |
| --- | --- | --- | --- | --- |
| 1 | **Preparar** | Arquiteto | Lê a leitura da mf (`docs/leitura/mfs/`), as `D-nnn` dela, a linha da mf na tabela 3.6 do documento 04 e os documentos de tema (03 a 13) que ela toca | A lista de exigências E1… |
| 2 | **Escrever o `.md`** | Arquiteto | Copia o esqueleto para `mfs/mf-nnn-nome.md` e preenche os assuntos **1, 2, 3…** na ordem. A parte 0 (pontos de ataque) vai **por último**, porque resume o que pediu decisão | O `.md` em `rascunho` |
| 3 | **Decidir** | Arquiteto, dono, PO | Cada decisão vira uma ADR; o teste de bolso (seção 1) diz de quem é. As 🟡 vão para a fila do dono; o que é do produto volta ao PO como `P-nnn` ou `I-nnn` | As ADRs e a fila |
| 4 | **Escrever a página** | Autor ou agente | Escreve `content/arq-nnn.html` copiando os componentes (seção 10) e seguindo a anatomia (seção 2) | O fragmento HTML |
| 5 | **Desenhar** | Autor ou agente | O diagrama de componentes e conexões e os de fluxo (seção 3) | O JSON do Archify e a casca de cada um |
| 6 | **Integrar** | Quem integra | Atualiza `docx.json`, o `README.md`, o `como-ler`, o `indice-de-adrs` e o índice de ADR de `mfs/README.md` | Os arquivos compartilhados em dia |
| 7 | **Gerar e validar** | Quem integra | `gerar` e `validar` (seção 9) | O site de teste em `site/` |
| 8 | **Conferir e olhar** | Quem integra | As conferências automáticas, visuais e de conteúdo (seção 12) | A lista do que passou e do que falta |
| 9 | **Entregar** | Quem integra | Entrega os links e as lacunas. O dono revisa as ADR 🟡; a `situacao` do `.md` passa a `em revisão` e, no fim, a `fechada` | O documento entregue |

## 8. A produção em paralelo

Um agente por documento, sempre com `model:` explícito, e **nenhum agente edita arquivo compartilhado**.

- **Cada agente escreve só** o próprio `content/arq-nnn.html` e os próprios diagramas, e **devolve**: (1) os caminhos
  criados e o resultado do `finalize`, da casca e do `gerar`/`validar` numa cópia; (2) o item de `portal.macros`; (3) as
  entradas de `diagrams`; (4) as linhas da tabela de fontes; (5) os termos novos do glossário; (6) as ADRs com o número,
  o título e a situação; (7) tudo que não saiu como pedido.
- **Quem integra** (a sessão principal) faz a etapa 6 **uma vez** por leva. Sem isso, dois agentes brigam pelo mesmo
  `docx.json`.
- O briefing é **um arquivo só**, com o que vale para todos; cada agente recebe só os dados da própria mf.
- **A numeração das ADR** é reservada por quem integra **antes** da leva (um bloco de números por documento), para dois
  agentes não pegarem o mesmo.

---

# Parte 3 · A régua

## 9. Onde moram os arquivos e como se gera (🟡 proposta ao dono)

```
v2-docs/
└── documentacao-arquitetura/      ← o site dos documentos ARQ-xxx (novo)
    ├── docx.json                  ← a configuração: a entrada, as páginas de apoio, as 23 mfs e os diagramas
    ├── content/                   ← como-ler.html · indice-de-adrs.html · arq-101.html … arq-123.html
    ├── diagramas/                 ← a casca de cada diagrama; fontes/ guarda o JSON do Archify e o .archify.html dos gates
    ├── README.md                  ← a tabela de fontes de cada página
    └── .gitignore                 ← site/, *.archify.html e os recibos dos gates
```

A saída vai para `docs/arquitetura/`, que o GitHub Pages serve (`…/horus-v2-docs/arquitetura/`). É um site **próprio**,
com a sua configuração, a sua entrada e o seu manifesto; não divide arquivo com nenhum outro site.

```bash
python "${CLAUDE_PLUGIN_ROOT}/scripts/docx.py" gerar --config documentacao-arquitetura/docx.json --saida docs/arquitetura
python "${CLAUDE_PLUGIN_ROOT}/scripts/docx.py" validar --site docs/arquitetura
```

Para teste, gere na pasta local `site/` (que o git ignora) e só depois em `docs/arquitetura`. Para isolar a marca de
qualquer configuração do usuário, aponte `CLAUDE_USER_HOME` para uma pasta vazia. O gerador valida os links e os ids
antes de gravar; saída com edição manual é recusada (não apague o manifesto para contornar).

## 10. A marca e os componentes

- **Design:** `kbr` (o padrão). A marca é a do projeto (`docs-brand.yml`): o **logo é o do Horus**; se o `gerar` avisar
  que usou o placeholder, repasse o aviso. Sem fontes externas (`fontes_externas: false`). Não se edita o CSS da Kinto.
- **Componente se copia, não se escreve de cabeça.** Abra `examples/content/componentes.html` do plugin `docx` (ou a
  `referencia/componentes.html` do `kbr-docs`), copie a marcação e troque só o texto. O CSS depende da estrutura exata.
- **Os que a página usa:** aviso (`callout`, com `ico` e um bloco de conteúdo), selo (`badge`), tabela (`table.t` dentro
  de `.table-wrap`), passos (`ol.steps`), cartões (`rel-grid` com `rel-card`) e perguntas (`faq`, só se ajudar).
- **Ícones do aviso:** `i` informação · `!` atenção · `✓` sucesso · `×` crítico · `•` nota.
- **Selos que existem:** `badge`, `--info`, `--success`, `--warning`, `--danger`, `--solid`, `--dot`. Não existe
  `--neutral`.
- 🪤 Negrito dentro de `<li>` é `<strong>`, nunca `<b>` (o `<b>` vira título de aviso).
- Fragmento: sem `html`, `head`, `body`, `h1`, `h2`, `script`, `style`, `link`, `form`, `iframe`, `object` nem `embed`.
  Começa em `h3`; todo `h3` e todo `h4` que vira tópico tem `id` **único no site inteiro**; link interno é `href="#id"`.

## 11. As regras de escrita do texto

- **Português do Brasil com acentuação.** UTF-8, LF, sem BOM. Escreva com `Write` e `Edit`; o PowerShell 5.1
  (`Get-Content`, `Set-Content`) corrompe acentos.
- **Os códigos entram:** `D-nnn`, as decisões `ARQ-nnn`, `ADR-nnn`, `P-nnn` e `I-nnn`, sempre em `<code>`. Confira cada
  um contra o backlog e o registro (seção 12).
- **Termo técnico vem traduzido na primeira vez**, com uma analogia curta quando ajudar ("caixa de saída: um recado
  gravado junto com a mudança, para nenhum aviso se perder"). A página de apoio `como-ler` traz o glossário.
- **Marcas** (as mesmas do `.md`): ✅ 🟢 🟡 🔎 ⚪ e ♻️ 🔧 ❌. Toda marca vem com a palavra ao lado, para o leitor de tela.
- **Repositório público:** nada de caminho local (`C:\…`), segredo, e-mail, IP nem endereço real de ambiente (host e
  domínio ficam nas variáveis). O código da v1.xx se cita como `horus@318db52b:<caminho>`.
- **Sem estilo inline, sem imagem externa.** Imagem informativa leva `alt`; decorativa, `alt=""`.
- **Nada que o `.md` não diga.** O que o HTML precisa e o `.md` não tem volta ao arquiteto, e não vira texto.
- **Quem escreve o `.md` é o arquiteto.** O PO não escreve arquitetura, e o que a arquitetura achar do produto volta
  como `P-nnn` ou `I-nnn`. O DocX **não converte Markdown**: quem produz a página escreve o fragmento à mão (ou por
  agente).

## 12. As conferências antes de entregar

**Automáticas** (um script de conferência, a escrever junto com o piloto; enquanto isso, à mão):
1. `validar` com saída 0; ids únicos no site inteiro; nenhum link quebrado.
2. Os **19 `h3`**, na ordem da seção 2, com os `id` no padrão `arq-nnn-<sufixo>`.
3. **ADRs:** o número de `h4` `adr-nnn` é igual ao do `.md`, e o índice tem uma linha por ADR.
4. Todo `D-nnn`, `ARQ-nnn`, `ADR-nnn`, `P-nnn` e `I-nnn` citado **existe** (`### D-nnn` no backlog, `### ARQ-nnn` no
   registro, `### ADR-nnn` nas mfs) e diz o que a página afirma.
5. **Sem código:** nenhum `code-block`, `codetabs`, `<pre>` nem comando de banco ou rota no texto.
6. **Sem vazamento:** nenhum caminho local, segredo, e-mail nem IP.
7. Todo `<dx-diagrama ref>` está declarado em `diagrams`; cada página tem o diagrama de componentes; nenhum `<b>` em
   `<li>`.
8. Nenhum estouro horizontal no celular.

**Visuais** (a skill `documentar` exige olhar): abra por HTTP e veja desktop e celular, os temas claro e escuro, a busca
com e sem resultado, a navegação por teclado e a impressão. **Em cada diagrama:** clique numa caixa, use a roda do
mouse, arraste e abra "Tela cheia". 🪤 O Archify vive em iframe aninhado: para provar que o desenho carregou, conte o
`svg` no quadro **neto**.

**De conteúdo:** um link válido não prova que a afirmação é verdadeira. Releia cada exigência, componente e ADR contra o
`.md` e contra o documento de tema que ela cita.

## 13. Publicação e armadilhas

- **Gerar não é publicar.** Publicar só quando o dono mandar. O repositório é **público**: antes, varra o que vai subir
  (caminho local, segredo, e-mail, IP). Faça o commit **nomeando os caminhos** e confira com `git status --short`; nunca
  `git add -A`.
- 🪤 **Não rode `ferramentas/montar_fontes.py`** nem o `fontes/` antigo: geram o portal antigo por cima de `docs/`.
- 🪤 O DocX 0.4.0 põe um "v" na frente de `project.version`: escreva "em desenho", sem "v" na frente do número.
- 🪤 O `descobrir.py` do `kbr-docs` sugere o nome da **pasta** como nome do projeto e "uso interno" no rodapé: corrija à
  mão no `docs-brand.yml`.
- 🪤 Edição manual no `docs/arquitetura/` interrompe a próxima geração; a fonte é sempre o `content/` e o `docx.json`.
- 🪤 `site/` e os `*.archify.html` ficam fora do git (`.gitignore`).

## 14. Pronto quando

- [ ] o `.md` do documento está escrito com o esqueleto e a `situacao` dele está na ficha da página;
- [ ] a página tem os 19 `h3` da seção 2, e o assunto que não vale diz "Não se aplica" com o motivo;
- [ ] o diagrama de componentes e conexões existe, tem até uns 12 nós e passou no `finalize`;
- [ ] cada decisão da mf é uma ADR com os 8 campos, o selo certo e o índice no começo do assunto 15;
- [ ] o texto fala de componentes e conexões, e a página não tem código, esquema nem rota;
- [ ] as conferências da seção 12 passaram e a página foi aberta no navegador;
- [ ] o `docx.json`, o `README.md`, o `como-ler` e o `indice-de-adrs` foram atualizados;
- [ ] nada foi commitado nem publicado sem ordem do dono.

## 15. O manual irmão

Cada mf tem **dois** documentos, e cada um tem o seu manual: o **ARQ-xxx** (a arquitetura, para o time técnico), que é o
deste arquivo, e o **MF-xxx** (a explicação do produto, para quem vai usar ou contratar), que tem o [manual dos
documentos MF-xxx](manual-geracao-doc-mf.md). Os dois são sites separados e têm regras de escrita diferentes: **não
copie uma regra de um para o outro**. Quando uma página precisar apontar para a outra, use a URL pública do Pages e
confirme no piloto que o `validar` a aceita; se não aceitar, deixe só o texto ("Documentação de produto: MF-101").

---

## Anexo · O esqueleto do fragmento

Copie, troque o texto e **confira cada classe na referência de componentes**. Este é o desenho da estrutura, não a fonte
da verdade do CSS.

```html
<h3 id="arq-101-resumo">Resumo</h3>
<p><strong>Em uma frase:</strong> …</p>
<p>
  <span class="badge badge--solid">v2.0</span>
  <span class="badge badge--info">Módulo: Plataforma</span>
  <span class="badge badge--warning">Complexidade: média</span>
  <span class="badge">Situação: rascunho</span>
</p>
<div class="callout callout--warning">
  <span class="ico">!</span>
  <div><b>Rascunho</b><p>Este documento ainda não foi revisado pelo dono.</p></div>
</div>

<h3 id="arq-101-pontos-de-ataque">0 · Pontos de ataque</h3>
<div class="table-wrap">
  <table class="t">
    <thead><tr><th>Assunto</th><th>Por que pede decisão aqui</th><th>Quem decide</th></tr></thead>
    <tbody>
      <tr class="zebra"><td><a href="#arq-101-dados">4 · Dados e história</a></td><td>…</td><td>Arquiteto</td></tr>
    </tbody>
  </table>
</div>

<h3 id="arq-101-componentes">3 · Componentes, contratos e fluxos</h3>
<p>…</p>
<dx-diagrama ref="arq-101-componentes"></dx-diagrama>

<h3 id="arq-101-motor">7 · O motor e a IA</h3>
<div class="callout callout--neutral">
  <span class="ico">•</span>
  <div><b>Não se aplica</b><p>A MF-101 não pergunta ao motor: …</p></div>
</div>

<h3 id="arq-101-adrs">15 · Registro de decisão de arquitetura (ADR-xxx)</h3>
<h4 id="adr-001">ADR-001 · Título curto</h4>
<p>
  <span class="badge badge--warning">🟡 Proposta ao dono</span>
  <span class="badge">06/11/2026</span>
  <span class="badge">Alcance: MF-101</span>
</p>
<div class="table-wrap">
  <table class="t">
    <thead><tr><th>Campo</th><th>Registro</th></tr></thead>
    <tbody>
      <tr class="zebra"><td><strong>Quem decide</strong></td><td>Dono</td></tr>
      <tr class="zebra"><td><strong>Decisão</strong></td><td><strong>…</strong></td></tr>
    </tbody>
  </table>
</div>
<div class="callout callout--warning">
  <span class="ico">!</span>
  <div><b>Aguarda o dono</b><p>…</p></div>
</div>
```
