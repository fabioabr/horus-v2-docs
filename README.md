# Visão de produto do Horus

Esta pasta reúne os documentos de visão e as decisões de produto do **Horus v2.xx**, que vamos desenvolver ao repensar o Horus desde o início, aproveitando os aprendizados e as funcionalidades do produto de hoje, a v1.xx (`D-134`). As entregas se chamam v2.0 e v2.1 (`D-135`).

O objetivo é explicitar para quem o Horus existe, quais problemas resolve, que valor entrega e quais escolhas devem orientar seu desenvolvimento.

Início deste trabalho: 30/10/2026.

## Documentos

Este repositório (`horus-v2-docs`) guarda **toda a documentação do Horus v2**: os documentos em Markdown e o **portal HTML** feito
a partir deles, publicado com o GitHub Pages. O código da v2 mora no repositório `horus-v2` (privado) (`D-140`). A estrutura (`D-144`, `D-142`):

```
horus-v2-docs/
├── README.md              ← este índice
├── docs/
│   ├── leitura/           ← a documentação de leitura: a visão geral e uma página por mf, em linguagem simples (o PO)
│   ├── raw/               ← o inventário, fonte da leitura
│   │   ├── produto/           ← visão, decisões e mapa de produto (o PO)
│   │   ├── arquitetura/       ← as decisões de tecnologia e a estratégia para atingir os objetivos (o arquiteto)
│   │   └── backlog/           ← as atividades (épicos, histórias e tasks), depois da arquitetura (o dono com um agilista)
│   ├── marca/             ← os logos do Horus, que o conversor copia para o portal
│   └── *.html, assets/, media/   ← o portal pronto, que o GitHub Pages serve (gerado: não se edita à mão)
├── fontes/                ← a origem do portal: docx.json, os fragmentos HTML de content/, os diagramas de media/ e a galeria modelos-mf/
└── ferramentas/
    └── montar_fontes.py   ← o conversor: Markdown → fontes do portal
```

Os documentos de produto:

| Documento | Conteúdo | Situação |
| --- | --- | --- |
| [Temas para a visão de produto](docs/raw/produto/01-temas-da-visao-do-produto.md) | Os 20 temas e as perguntas que orientam a discussão inicial. | Proposta em discussão |
| [Norte do produto](docs/raw/produto/02-norte-do-produto.md) | Propósito, público inicial, problemas em ordem, promessa, medidas de sucesso e limites. | Decidido em 30/10/2026 (`D-001` a `D-015`, `D-017`, `D-022` e `D-024`) |
| [Inventário de lacunas](docs/raw/produto/03-inventario-de-lacunas.md) | O norte comparado com o produto de hoje, a começar pelo problema nº 1. | Levantamento preliminar (30/10/2026) |
| [Macro funcionalidades de hoje](docs/raw/produto/04-macro-funcionalidades-de-hoje.md) | O que o Horus já entrega, em 12 macro funcionalidades, contra os três problemas do norte. | Levantamento preliminar (31/10/2026) |
| [A v2.0 consolidada](docs/raw/produto/05-v2.0-consolidada.md) | A v2.0 num lugar só: o que entra, o que fica fora, as regras decididas, os riscos, o que falta e as leituras do PO a confirmar. | Composição decidida (02/11/2026); aguarda a conferência do arquiteto |
| [As versões](docs/raw/produto/06-versoes.md) | Uma tabela por versão, mf a mf: a v2.0 e a v2.1, que reúne tudo o que ficou fora da v2.0. | v2.0 e v2.1 decididas (`D-119`, `D-121`, 02/11/2026) |
| [Mapa de objetivos e funcionalidades](docs/raw/produto/07-mapa-de-objetivos-e-funcionalidades.md) | O mapa para iniciar o desenvolvimento: o objetivo do produto, os objetivos de cada entrega e as funcionalidades de cada um, com a entrega e a decisão. | Funcionalidades e objetivos decididos (`D-136`, 02/11/2026) |
| [Backlog estratégico](docs/raw/produto/backlog-estrategico.md) | Registro das decisões de produto: macro funcionalidades, versões, cortes e pendências do dono. | Em uso |

## Como o portal é feito

Os fragmentos de `fontes/` são **gerados** a partir dos Markdown de `docs/leitura/` e `docs/raw/` (editar um à mão se perde na próxima
montagem), e o portal de `docs/` é gerado das fontes com o plugin DocX. Mude o Markdown e monte de novo, da raiz deste repositório:

```
python ferramentas/montar_fontes.py . fontes <caminho do mermaid.min.js>               # Markdown → fontes
python <plugin docx>/scripts/docx.py gerar --config fontes/docx.json --saida docs       # fontes → portal
python <plugin docx>/scripts/docx.py validar --site docs                                # confere o portal
```

## Organização dos próximos documentos

Os temas serão aprofundados conforme avançarmos nas conversas. Cada documento deve deixar claras as hipóteses, as decisões tomadas e as questões que continuam em aberto, com a data da última atualização.

Este índice será atualizado à medida que novos documentos forem criados. A numeração dos arquivos organiza a leitura; a prioridade de desenvolvimento será definida durante a discussão de produto.

## Ponto de partida

A proposta inicial é começar por visão e propósito, público-alvo, problemas prioritários, posicionamento e escopo. Essas escolhas orientarão os demais temas.
