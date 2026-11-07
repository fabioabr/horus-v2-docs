# Documentação de arquitetura do Horus v2

Situação: 🟡 proposta ao dono (a arquitetura geral da plataforma, em 10 diagramas, refeita em 07/11/2026 com a infraestrutura separada, `D-258` a `D-270`; ainda não foi revisada) · Data: 07/11/2026

Esta pasta é a fonte do site de arquitetura descrito em [`../manuais/manual-geracao-doc-arq.md`](../manuais/manual-geracao-doc-arq.md). Por enquanto
tem **um** documento: a **arquitetura geral da plataforma**. Os documentos por mf (`ARQ-xxx`, começando pela MF-101) vêm depois.

## O que há aqui

```
documentacao-arquitetura/
├── docx.json                     ← a configuração do site (1 página, 10 diagramas)
├── content/arquitetura-geral.html ← a página: texto de cada diagrama, divergências, decisões em aberto, lacunas
├── diagramas/
│   ├── arq-geral-<tema>.html      ← a casca de cada diagrama (Archify + casca Maind, abas Diagrama e Explicações)
│   └── fontes/arq-geral-<tema>.json ← a fonte de cada diagrama (o que se edita)
└── .gitignore                    ← site/, *.archify.html e os recibos dos gates ficam fora do git
```

Os dez diagramas, em ordem de leitura: `infra-separada`, `criar-organizacao`, `modulos`, `execucao`, `dados-e-historia`, `pergunta-resposta`,
`segundo-plano`, `seguranca`, `integracoes` e `implantacao`.

## Como ver

- **A página inteira:** gere o site de teste e sirva a pasta `site/` por HTTP (o navegador não abre os diagramas por `file:`).
- **Um diagrama só:** abra `diagramas/arq-geral-<tema>.html` (é um arquivo autossuficiente).

```bash
python "<plugin docx>/scripts/docx.py" gerar --config docx.json     # gera em site/ (o git ignora)
python "<plugin docx>/scripts/docx.py" validar --site site
```

Para isolar a marca de qualquer configuração do usuário, aponte `CLAUDE_USER_HOME` para uma pasta vazia.

## Para mudar um diagrama

Edite o JSON em `diagramas/fontes/`, rode o `finalize` do Archify (saída `fontes/<tema>.archify.html`) e a casca `archify-maind`
(saída `diagramas/<tema>.html`), e gere o site de novo. A página de `diagramas/` é derivada; editá-la à mão se perde.

## O que ainda não foi feito

- O dono não revisou nada. Onde os documentos 01 a 14 e o backlog divergem, os diagramas seguem o backlog; as divergências estão na página
  (seção "O que mudou desde os documentos de arquitetura") e alimentam a `P-028`.
- Nada foi publicado: a saída prevista é `docs/arquitetura/` (manual, seção 9), e a publicação só sai com ordem do dono.
- Cada diagrama foi conferido pelos autores só por captura de tela; os cliques e popups da casca não foram testados um a um.
