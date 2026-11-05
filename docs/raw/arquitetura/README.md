# Arquitetura do Horus v2

Pasta do **arquiteto de soluções**: as **decisões de tecnologia** e a **estratégia** que o Horus v2 deve usar para atingir os objetivos (`D-141`, `D-142`). Quem a escreve é a skill `arquiteto-solucoes-horus`.

O que se constrói, e por quê, está em [`../produto/`](../produto/), a começar pelo [mapa de objetivos e funcionalidades](../produto/07-mapa-de-objetivos-e-funcionalidades.md). Esta pasta trata do **como**, no nível das decisões. As atividades (épicos, histórias e tasks) não ficam aqui: vêm depois, em [`../backlog/`](../backlog/).

**Restrição do dono:** a v2 mantém a stack da v1.xx (`D-143`). As decisões escolhem como usar a stack, nunca trocam uma peça dela.

Última atualização: 02/11/2026 (sexta rodada: os documentos 12, 13 e 14; os catorze documentos da lista estão escritos).

**Em números:** 96 decisões no [registro](02-registro-de-decisoes.md) (30 ✅, 54 🟢, 6 🟡 e 6 ⚪); as 6 🟡 esperam o dono na [fila por urgência](01-estrategia-da-solucao.md) (seção 8.1); 30 itens a devolver ao PO (A-01 a A-30) e 19 verificações pendentes (V-01 a V-19), consolidados na [conferência do produto](14-conferencia-do-produto.md).

## Os documentos

A lista foi aprovada pelo dono em 02/11/2026.

| Nº | Documento | O que responde | Precisa existir | Situação |
| --- | --- | --- | --- | --- |
| 01 | Estratégia da solução | A solução numa página; como cada objetivo é atingido; o que se reaproveita da v1.xx; os marcos | Antes de começar | 🟢 Escrito e atualizado em 02/11/2026 · a fila do dono com as 31 decisões 🟡, por urgência e com o que cada uma trava · os itens a devolver ao PO apontados para o documento 14 |
| 02 | Registro de decisões (`ARQ-nnn`) | Cada decisão de tecnologia, quem decidiu e por quê | Antes de começar, e vivo | 🟢 Vivo · `ARQ-001` a `ARQ-096` (30 ✅, 54 🟢, 6 🟡, 6 ⚪) · notas datadas: três de 02/11/2026 (na `ARQ-049`, na `ARQ-051` e na `ARQ-073`) e cento e vinte e duas de 03/11/2026, em sessenta e duas decisões, pelas escolhas do dono no dia |
| 03 | Metas de qualidade | Disponibilidade, volume, crescimento, rapidez e custo por organização | Antes de começar | 🟢 Escrito em 02/11/2026 · 4 metas 🟡 com o dono (`ARQ-014` a `ARQ-017`) · os preços e o rateio do custo saíram no documento 13 |
| 04 | Software | Os módulos, os componentes e os contratos, camada a camada | Antes de começar | 🟢 Escrito em 02/11/2026 · 5 decisões (`ARQ-018` a `ARQ-022`): 4 🟢 e a `ARQ-021` ⚪, substituída em 03/11/2026 pela `ARQ-095` 🟢 (os dois papéis em várias réplicas) |
| 05 | Motor de análise e IA | Como a pergunta vira resposta | Antes do marco do motor | 🟢 Escrito em 02/11/2026 · 10 decisões (`ARQ-023` a `ARQ-032`), nenhuma 🟡 com o dono · a `ARQ-027` ✅ pelo dono em 03/11/2026 (a pesquisa na web pela busca nativa da conexão) |
| 06 | Dados | O que se guarda, o isolamento entre organizações, a vinda dos dados da v1.xx | Antes de começar | 🟢 Escrito em 02/11/2026 · 6 decisões (`ARQ-033` a `ARQ-037` e `ARQ-089`), nenhuma 🟡 com o dono, 1 ⚪ · a `ARQ-035` ✅ pelo dono em 03/11/2026 (os prazos da organização nas preferências dela) · a `ARQ-010` ✅ pelo dono em 03/11/2026 (um banco por organização), com a `ARQ-088` · a `ARQ-011` ✅ pelo dono em 03/11/2026 (uma instância nova, com as organizações de exemplo semeadas), com a `ARQ-089` |
| 07 | Segurança | O login, os papéis, a segurança dos dados por pessoa, a LGPD e os segredos | Antes de começar | 🟢 Escrito em 02/11/2026 · 9 decisões (`ARQ-038` a `ARQ-045` e `ARQ-090`), 1 🟡 com o dono (a `ARQ-040`, adiada para a v2.1) · a `ARQ-043` ✅ pelo dono em 03/11/2026 (o aviso num documento da organização, em PDF) · a `ARQ-044` ✅ pelo dono em 03/11/2026 (os segredos pelos Secrets do GitHub) · a `ARQ-090` ✅ pelo dono em 03/11/2026 (a segurança por pessoa fora da v2.0, de volta na v2.1) · a A-11 como hipótese de trabalho |
| 08 | Integrações | E-mail, WhatsApp, IA, fontes de dados, login corporativo | Antes do marco de cada uma | 🟢 Escrito em 02/11/2026 · 9 decisões (`ARQ-046` a `ARQ-054`), 2 🟡 com o dono · a `ARQ-046` ✅ pelo dono em 03/11/2026 (o e-mail) · corrigido na sexta rodada: o custo das mensagens da Meta desde 01/10/2026 e o Bedrock de São Paulo |
| 09 | Infraestrutura e ambientes | SaaS, homologação, produção e o on-premises | Antes de começar | 🟢 Escrito em 02/11/2026 · 6 decisões (`ARQ-055` a `ARQ-060`), 1 🟡 com o dono · a `ARQ-055`, a `ARQ-056`, a `ARQ-058` e a `ARQ-059` ✅ pelo dono em 03/11/2026 (a homologação da v2 na VPS de hoje, a máquina dividida sem teto, o endurecimento no lugar e uma base de demonstração só) · a `ARQ-057` ⚪, substituída em 03/11/2026 pela `ARQ-094` 🟢 (a imagem e o chart), e a `ARQ-060` refeita sobre o chart, com o Kubernetes da `ARQ-093` ✅ |
| 10 | Publicação e operação | Publicar, voltar uma versão, o contrato da cópia de segurança e incidentes | Antes da primeira homologação | 🟢 Escrito em 02/11/2026 · 10 decisões (`ARQ-061` a `ARQ-068`, `ARQ-086` e `ARQ-087`), nenhuma 🟡 com o dono · os incidentes e a abertura da v2.0 num subdomínio pelo dono em 03/11/2026 (`ARQ-068` ✅, `ARQ-065` ✅) · a cópia fora do Horus pelo dono em 03/11/2026 (`ARQ-086` ✅, que substituiu a `ARQ-064`), o acesso às máquinas (`ARQ-066` ✅) e a troca dos segredos (`ARQ-067` ✅) |
| 11 | Observabilidade | O que se mede, os alertas e o que a telemetria nunca carrega | Antes da primeira homologação | 🟢 Escrito em 02/11/2026 · 6 decisões (`ARQ-069` a `ARQ-074`), 1 🟡 com o dono · a `ARQ-069`, a `ARQ-070` e a `ARQ-071` ✅ pelo dono em 03/11/2026 (uma stack por máquina; a sonda de fora num serviço de outro provedor; o plantão só para o que não pode esperar) · a citação do teste da ordem dos processadores corrigida |
| 12 | Qualidade e testes | Os testes, sem chamar modelo pago | Antes de começar | 🟢 Escrito em 02/11/2026 · 8 decisões (`ARQ-075` a `ARQ-082`), nenhuma 🟡 com o dono · a `ARQ-081` ✅ pelo dono em 03/11/2026 (a bateria com modelo real) · a `ARQ-082` ✅ pelo dono em 03/11/2026 (o CI na VPS de hoje até a primeira produção real) · o CI, as travas, o contrato com a tela, o catálogo de provas e a prova dos alertas |
| 13 | Custo de operação | Quanto custam a IA, o WhatsApp e a infraestrutura | Antes do marco dos agentes | 🟢 Escrito em 02/11/2026 e atualizado em 03/11/2026 (a cópia da instância SaaS fora do Horus) · 3 decisões (`ARQ-083` a `ARQ-085`), 2 🟡 com o dono · os números em faixas 🔎, com a fonte e a data de cada preço |
| 14 | Conferência do produto | As respostas às `P-002`, `P-003` e `P-008`, e o que volta ao PO | Vivo | 🟢 Vivo, escrito em 02/11/2026 · a `P-008` inteira (14 ✅, 13 ⚠️, nenhuma ❌) · a `P-002` e a `P-003` conferidas · 30 itens ao PO, sem número `P-nnn` ou `I-nnn` (o backlog está congelado) · 19 verificações |

## O modelo de dados (MER)

A arquitetura para no componente (documento 06, [Dados](06-dados.md)); o **modelo de dados** é o passo seguinte e mostra, tabela a tabela, o que cada componente guarda. O primeiro é o da **MF-101**, a administração da instância, que vive no banco mestre (`ARQ-010`, `ARQ-088`).

- [O MER da MF-101](https://fabioabr.github.io/horus-v2-docs/archify/mer-mf-101.html): onze tabelas, com todas as colunas, as chaves e a opcionalidade de cada ponta, em cinco visões (marca e logos, administração e pessoas, assentos, uso e custo, aviso da instância). Duas delas, `pessoa` e `vinculo_pessoa_organizacao`, são da MF-102 e entram só para fechar as chaves.
- [A documentação da MF-101](https://fabioabr.github.io/horus-v2-docs/archify/mf-101-modelo-de-dados.html): onde cada dado mora, as entidades, os assentos, o ciclo de uma organização, o uso e o custo, as regras de integridade, o que muda no backend e as dúvidas respondidas pelo dono em 05/11/2026.

**Situação:** 🟢 modelo com as decisões do dono de 05/11/2026 (`D-146` a `D-152`); restam duas perguntas pequenas (Q13, quando o aviso sai da faixa, e Q14, o formato do relatório da organização) e as propostas `D-153` a `D-156`. Os desenhos saem do archify, e as fontes estão em `fontes/archify/`.
