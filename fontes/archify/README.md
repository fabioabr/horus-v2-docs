# Fontes dos desenhos do archify

Os dois arquivos de `docs/archify/` saem daqui. Edite a fonte e gere de novo; editar o HTML à mão se perde.

| Fonte | Gera | O que é |
| --- | --- | --- |
| `mer-mf-101.erd.json` | `docs/archify/mer-mf-101.html` | O MER da MF-101: onze tabelas, todas as colunas, as chaves e a opcionalidade de cada ponta |
| `mf-101-modelo-de-dados.archify.md` | `docs/archify/mf-101-modelo-de-dados.html` | A documentação da MF-101: onde cada dado mora, as entidades, os assentos, o uso e o custo, as regras e as dúvidas respondidas pelo dono em 05/11/2026 |

## Como gerar de novo

Da raiz do repositório, com a skill `archify` instalada (`<archify>` é a pasta dela):

```
node <archify>/bin/archify.mjs finalize erd fontes/archify/mer-mf-101.erd.json docs/archify/mer-mf-101.html --quality standard --json
node <archify>/bin/archify.mjs finalize explainer fontes/archify/mf-101-modelo-de-dados.archify.md docs/archify/mf-101-modelo-de-dados.html --json
```

O MER tem mais de 8 tabelas e mais de 50 colunas, por isso sai no perfil `standard`. Os gates (`validate`, `deliver`, `check` e,
no MER, `browser-check`) têm de passar; o explicador não abre navegador, então olhe a página antes de publicar.

## O que saber

- **A interface do explicador fica em inglês** ("Answer", "Applies to", "Export"). O archify empacota só en, zh-CN, zh-TW, es, ko e
  ar para o explicador, e `meta.translations` existe apenas nos diagramas nativos. O MER sai todo em português
  (`meta.translations` com o catálogo `pt` do archify e as chaves que faltavam). O texto da documentação é em português.
- **`docx.py validar --site docs` reprova a página do explicador** em dois pontos, ambos do runtime do archify embutido nela:
  um `${...}` dentro do JavaScript, lido como `href`, e o logo do rodapé em `data:image/svg+xml`. O MER passa.
- **O DocX não apaga `docs/archify/`**: o gerador só remove o que está no manifesto (`.docx-build.json`) e preserva arquivos alheios.
- O link do portal (`docs/raw/arquitetura/README.md`, seção "O modelo de dados (MER)") é absoluto, para o GitHub Pages: o
  `montar_fontes.py` transforma link relativo para fora do portal em texto.
- O modelo lógico de origem (entidades, regras, as respostas às perguntas Q1 a Q12 e as abertas Q13 e Q14) é o documento
  `modelo-de-dados/mf-101-gestao-da-instancia.md` do repositório do backend, atualizado em 05/11/2026 com as decisões `D-146` a `D-156`.
