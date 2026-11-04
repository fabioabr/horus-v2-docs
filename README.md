# Horus v2 — documentação

O portal HTML da documentação de produto e de arquitetura do Horus v2, publicado com o GitHub Pages.

| Pasta | O que é |
|---|---|
| `docs/` | O site pronto, o que o GitHub Pages serve. |
| `fontes/` | A origem do site: `docx.json`, os fragmentos HTML de `content/`, os diagramas de `media/` e a galeria `modelos-mf/`. |

## Como o site é feito

O conteúdo nasce dos documentos em Markdown do repositório `horus-v2`. Os fragmentos de `fontes/` são **gerados** a partir
deles (editar um à mão se perde na próxima montagem), e o site de `docs/` é gerado das fontes com o plugin DocX.

```
python docs/montar_fontes.py . ../v2-docs/fontes <caminho do mermaid.min.js>      # no horus-v2: Markdown → fontes
python <plugin docx>/scripts/docx.py gerar --config fontes/docx.json --saida docs  # aqui: fontes → site
```
