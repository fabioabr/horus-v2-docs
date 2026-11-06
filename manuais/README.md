# Manuais de geração dos documentos de cada mf

Data: 06/11/2026 · A situação de cada família está na tabela abaixo.

Cada macro funcionalidade (mf) tem **dois** documentos em HTML, e cada um tem o seu manual. Os dois manuais moram aqui,
juntos, para quem for gerar as páginas (uma pessoa ou um agente) achar tudo num lugar só.

**O objetivo dos manuais** é ser, ao mesmo tempo, o **roteiro** (a ordem em que a documentação é criada, fase a fase e
etapa a etapa) e a **forma padrão** (como cada documento é, igual nas 23 mfs). Os dois têm a mesma estrutura em três
partes: **1 · A forma padrão**, **2 · O roteiro** e **3 · A régua** (as regras, as conferências e as armadilhas).

| | **MF-xxx** · produto | **ARQ-xxx** · arquitetura |
| --- | --- | --- |
| **Situação** | ✅ **published**: as 23 páginas estão finalizadas e no ar | 🟡 proposta ao dono: nenhum documento escrito ainda |
| **Para quem é** | Quem vai usar ou contratar o Horus | O time técnico, o arquiteto e o dono |
| **O manual** | [`manual-geracao-doc-mf.md`](manual-geracao-doc-mf.md) | [`manual-geracao-doc-arq.md`](manual-geracao-doc-arq.md) |
| **O que copiar** | O molde `documentacao/content/mf-101.html` | O esqueleto [`_modelo.md`](../docs/raw/arquitetura/mfs/_modelo.md) e o fragmento do anexo do manual |
| **A fonte** | `docs/leitura/mfs/mf-nnn-*.md`, o backlog e o registro de decisões | O `.md` do documento: `docs/raw/arquitetura/mfs/mf-nnn-*.md` |
| **Onde grava** | `documentacao/content/mf-nnn.html` e `documentacao/diagramas/` | `documentacao-arquitetura/content/arq-nnn.html` e `documentacao-arquitetura/diagramas/` |
| **Códigos `D-`, `ARQ-`, `ADR-`** | **Proibidos** no texto (só na tabela de fontes do `README`) | **Obrigatórios**, sempre em `<code>` |

## Como um agente começa

1. Leia **o manual da sua família** inteiro e o que ele manda copiar (o molde ou o esqueleto). Não leia o outro manual.
2. Leia a fonte da **sua** mf, e só dela.
3. Escreva **só** o fragmento HTML da sua mf e os arquivos do seu diagrama. **Não edite** `docx.json`, `README.md`,
   `como-ler.html` nem a página de outra mf: devolva os trechos para quem integra.
4. Rode o `gerar` e o `validar` numa **cópia**, e devolva o relatório na ordem que o manual pede.
5. Subagente sempre com `model:` explícito. **Nada de git**: gerar não é publicar.

**Regra das duas famílias:** não copie uma regra de um manual para o outro. As regras de escrita são diferentes de
propósito.
