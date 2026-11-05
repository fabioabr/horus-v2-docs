# Fontes dos desenhos do archify

Os arquivos de `docs/archify/` saem daqui. Edite a fonte e gere de novo; editar o HTML à mão se perde.

**Terceira versão, de 05/11/2026: estado de hoje no transacional, história num banco de log, dimensões em vez de `enum`.** O MER da
MF-101 virou cinco diagramas, cada um com um assunto. O modelo lógico de origem é o `mf-101-gestao-da-instancia.md` do repositório
do backend (`src/backend/docs/modelo-de-dados/`).

| Fonte | Gera | O que é |
| --- | --- | --- |
| `mer-mf-101.erd.json` | `docs/archify/mer-mf-101.html` | **1 de 5.** A instância, as pessoas e as organizações: 10 tabelas do banco mestre, só com o estado de hoje e as dimensões |
| `mer-mf-101-assentos.erd.json` | `docs/archify/mer-mf-101-assentos.html` | **2 de 5.** O assento no banco da organização: 6 tabelas, com tipo, situação e ocupação em dimensões |
| `mer-mf-101-concessao.erd.json` | `docs/archify/mer-mf-101-concessao.html` | **3 de 5.** A concessão de assentos: 5 tabelas. O pedido de liberar ou reduzir, só enquanto pendente |
| `mer-mf-101-uso.erd.json` | `docs/archify/mer-mf-101-uso.html` | **4 de 5.** Uso e custo: 4 tabelas, só números |
| `mer-mf-101-log.erd.json` | `docs/archify/mer-mf-101-log.html` | **5 de 5.** O banco de log: 7 tabelas `log_*` tipadas, as 3 dimensões dos eventos, a dimensão de pessoas e a visão `log_geral` |
| `mf-101-modelo-de-dados.archify.md` | `docs/archify/mf-101-modelo-de-dados.html` | A documentação da MF-101. ⚠️ **Ainda descreve a primeira versão do modelo** (assento como número); só é refeita depois que o dono responder as duas pendências que restam (`P-030` e `P-031`) |

## Como gerar de novo

Da raiz do repositório, com as skills `archify` e `archify-maind` instaladas (`<archify>` e `<maind>` são as pastas delas). Os MERs saem em **duas etapas**:

1. O `finalize` valida o desenho e grava o **artefato dos gates** (`<nome>.archify.html`) numa pasta **fora da publicação**, por exemplo `$TMP/gates/`. Os gates (`validate`, `deliver`, `check` e `browser-check`) têm de passar.
2. A casca `archify-maind` gera a página **publicada** em `docs/archify/<nome>.html`, com as abas Diagrama, Dados, Links, Explicações e Descrição. O diagrama é o do próprio Archify, embutido, e ganha a roda do mouse para o zoom, a mãozinha para arrastar e a grade.

```
node <archify>/bin/archify.mjs finalize erd fontes/archify/<nome>.erd.json $TMP/gates/<nome>.archify.html --quality standard --json
node <maind>/scripts/skin.mjs --html $TMP/gates/<nome>.archify.html --spec fontes/archify/<nome>.erd.json --out docs/archify/<nome>.html
```

**Atalho:** `node fontes/archify/gerar-mers.mjs` faz as duas etapas para os cinco (ou só para os nomeados: `node fontes/archify/gerar-mers.mjs mer-mf-101-log`). O `finalize` roda num diretório temporário que some no fim, e o script para se um gate reprovar ou se o Archify mudar e a casca não achar uma âncora.

`<nome>` é cada um dos cinco: `mer-mf-101`, `mer-mf-101-assentos`, `mer-mf-101-concessao`, `mer-mf-101-uso` e `mer-mf-101-log`. Os MERs ficam no perfil `standard` (mais de 50 colunas no conjunto). Publique só o `docs/archify/<nome>.html`: ele é autossuficiente. Como o `finalize` grava fora de `docs/archify/`, não sobram recibos (`*.finalize*.json`, `*.browser-check.json`, `*.delivery.json`) ao lado da página.

O explicador (`mf-101-modelo-de-dados.archify.md`) **não passa pela casca** (é outro formato) e se gera direto: `node <archify>/bin/archify.mjs finalize explainer fontes/archify/mf-101-modelo-de-dados.archify.md docs/archify/mf-101-modelo-de-dados.html --json`. Olhe a página antes de publicar, porque ele não abre navegador.

Para conferir a casca, sirva a pasta por HTTP (`python -m http.server`): em `file://` o diagrama embutido não carrega.

## O que saber

- **A interface do explicador fica em inglês** ("Answer", "Applies to", "Export"). O archify empacota só en, zh-CN, zh-TW, es, ko e
  ar para o explicador, e `meta.translations` existe apenas nos diagramas nativos. O MER sai todo em português
  (`meta.translations` com o catálogo `pt` do archify e as chaves que faltavam). O texto da documentação é em português.
- **`docx.py validar --site docs` reprova a página do explicador** em dois pontos, ambos do runtime do archify embutido nela:
  um `${...}` dentro do JavaScript, lido como `href`, e o logo do rodapé em `data:image/svg+xml`. O MER passa.
- **O DocX não apaga `docs/archify/`**: o gerador só remove o que está no manifesto (`.docx-build.json`) e preserva arquivos alheios.
- O link do portal (`docs/raw/arquitetura/README.md`, seção "O modelo de dados (MER)") é absoluto, para o GitHub Pages: o
  `montar_fontes.py` transforma link relativo para fora do portal em texto.
- O modelo lógico de origem (os processos, as entidades, o banco de log, as regras, as respostas às perguntas Q1 a Q12 e as pendências
  `P-030` e `P-031`) é o documento `modelo-de-dados/mf-101-gestao-da-instancia.md` do repositório do backend, refeito em 05/11/2026 sobre
  as decisões `D-146` a `D-158` e a `ARQ-097`.
- Nos MERs 2, 3 e 4, as tabelas de outros bancos aparecem só como referência. As colunas `entidade_id`, `membro_id` e `ator_id` do banco de
  log e do banco da organização **não têm chave estrangeira** para o outro banco: dois bancos não fazem chave estrangeira entre si.
