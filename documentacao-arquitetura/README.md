# Documentação de arquitetura do Horus v2

Situação: 🟡 proposta ao dono (a arquitetura geral da plataforma, em 10 diagramas, refeita em 08/11/2026 com a infraestrutura separada, `D-258` a `D-293`, e o registro até a `ARQ-127`; o texto foi reescrito em linguagem de leigo, em 13 páginas, com índice por macro tema; ainda não foi revisada) · Data: 08/11/2026

Esta pasta é a fonte do site de arquitetura descrito em [`../manuais/manual-geracao-doc-arq.md`](../manuais/manual-geracao-doc-arq.md). Por enquanto
tem **um** documento, em 13 páginas: a **arquitetura geral da plataforma**. Os documentos por mf (`ARQ-xxx`, começando pela MF-101) vêm depois.

## O que há aqui

```
documentacao-arquitetura/
├── docx.json                     ← a configuração do site (13 seções, 10 diagramas, índice por macro tema em `portal.macros`)
├── content/<página>.html          ← um fragmento por página (ver a lista abaixo)
├── diagramas/
│   ├── arq-geral-<tema>.html      ← a casca de cada diagrama (Archify + casca Maind, abas Diagrama e Explicações)
│   └── fontes/arq-geral-<tema>.json ← a fonte de cada diagrama (o que se edita: posições, ligações, cartões "Explicações")
└── .gitignore                    ← site/, *.archify.html e os recibos dos gates ficam fora do git
```

As 13 páginas, por macro tema: **Comece por aqui** (`quem-e-quem`); **A base: onde e como roda** (`infra-separada`, `modulos`, `execucao`, `implantacao`);
**O Horus em ação** (`pergunta-resposta`, `segundo-plano`, `integracoes`); **Organizações, dados e segurança** (`criar-organizacao`, `dados`, `seguranca`);
**Decisões e acompanhamento** (`falta-decidir`, `sobre`). Toda página de assunto segue o mesmo molde: *Em uma frase*, *O desenho*, *Como funciona* e
*O que falta decidir nesta parte*; cada pendência aparece por inteiro só na página onde nasce, e `falta-decidir` as reúne por papel.

As regras do texto (para quem não é da TI, sem "você", com o papel de quem age) estão nas skills `product-owner-horus` e `arquiteto-solucoes-horus`.

Os dez diagramas, em ordem de leitura: `infra-separada`, `criar-organizacao`, `modulos`, `execucao`, `dados-e-historia`, `pergunta-resposta`,
`segundo-plano`, `seguranca`, `integracoes` e `implantacao`.

## Como ver

- **O portal inteiro:** gere o site de teste e sirva a pasta `site/` por HTTP (o navegador não abre os diagramas por `file:`).
- **Um diagrama só:** abra `diagramas/arq-geral-<tema>.html` (é um arquivo autossuficiente).

```bash
python "<plugin docx>/scripts/docx.py" gerar --config docx.json     # gera em site/ (o git ignora)
python "<plugin docx>/scripts/docx.py" validar --site site
```

Para isolar a marca de qualquer configuração do usuário, aponte `CLAUDE_USER_HOME` para uma pasta vazia.

## Para mudar um diagrama

Edite o JSON em `diagramas/fontes/`, rode o `finalize` do Archify (saída `fontes/<tema>.archify.html`) e a casca `archify-maind`
(saída `diagramas/<tema>.html`), e gere o site de novo. A página de `diagramas/` é derivada; editá-la à mão se perde.

**Formato do bloco: o clássico do Archify.** Os diagramas usam a casca da versão **0.5.1** do plugin DocX, a de antes do cartão de componente
(CLOUD-CARD-001, que veio na 0.6.0). O cartão foi testado em 08/11/2026 e saiu por decisão do dono do Horus: dentro da largura máxima do desenho,
o texto do cartão ficava miúdo perto do resto da página. A casca 0.5.1 sai da tag `docx--v0.5.1` do repositório `Maindtech-Plugins`:

```bash
git -C <Maindtech-Plugins> show docx--v0.5.1:plugins/docx/skills/archify-maind/scripts/skin.mjs > skin-0.5.1.mjs
node skin-0.5.1.mjs --html fontes/<tema>.archify.html --spec fontes/<tema>.json --out <tema>.html
```

A casca de hoje (0.6 em diante) desenha o cartão em todo diagrama de arquitetura. Fora o cartão, a 0.5.1 é igual a ela.

## O que ainda não foi feito

- O dono não revisou nada. Onde os documentos 01 a 14 e o backlog divergem, os diagramas seguem o backlog; as divergências estão na página
  (página `sobre`, seção "O que mudou") e alimentam a `P-028`.
- A saída prevista é `docs/arquitetura/` (manual, seção 9), gerada com `--saida ../docs/arquitetura`; a publicação só sai com ordem do dono.
- Cada diagrama foi conferido pelos autores só por captura de tela; os cliques e popups da casca não foram testados um a um.
