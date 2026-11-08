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
│   ├── fontes/arq-geral-<tema>.json ← a fonte de cada diagrama (o que se edita: posições, ligações, cartões "Explicações")
│   └── cartoes/arq-geral-<tema>.json ← o conteúdo do cartão de cada bloco (só nos 7 diagramas de arquitetura)
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

Edite o JSON em `diagramas/fontes/` (e, nos de arquitetura, os cartões em `diagramas/cartoes/`), rode o `finalize` do Archify
(saída `fontes/<tema>.archify.html`) e a casca `archify-maind` com `--cartoes cartoes/<tema>.json` (saída `diagramas/<tema>.html`), e gere o
site de novo. A página de `diagramas/` é derivada; editá-la à mão se perde.

**Formato do bloco (casca 0.6.0, cartão CLOUD-CARD-001):** cada componente de um diagrama `architecture` vira um cartão de 500×200 reduzido à
caixa, então todo nó é declarado com `size` [250, 100] (proporção 2,5:1) e a largura total do desenho fica em até 1.794 px, desde que a
proporção largura/altura seja de pelo menos 1,55 (abaixo disso o `finalize` limita a 1.240 px). Em cada cartão: nome, tecnologia (só a comprovada na
`ARQ-001`), ícone, descrição com `**termo-chave**` (sem negrito colado em pontuação: a casca põe um espaço ali), nota e até 3 etiquetas. Os
diagramas de sequência e de fluxo não usam cartão.

## O que ainda não foi feito

- O dono não revisou nada. Onde os documentos 01 a 14 e o backlog divergem, os diagramas seguem o backlog; as divergências estão na página
  (página `sobre`, seção "O que mudou") e alimentam a `P-028`.
- A saída prevista é `docs/arquitetura/` (manual, seção 9), gerada com `--saida ../docs/arquitetura`; a publicação só sai com ordem do dono.
- Nos 7 diagramas de arquitetura o texto do cartão é miúdo na visão geral e se lê ao dar zoom (a roda do mouse); é o limite do formato dentro dos 1.794 px.
- Cada diagrama foi conferido pelos autores só por captura de tela; os cliques e popups da casca não foram testados um a um.
