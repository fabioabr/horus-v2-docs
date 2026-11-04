# Custo de operação do Horus v2

Situação: 🟢 escrito pelo arquiteto · três decisões novas (`ARQ-083` a `ARQ-085`): uma 🟢, uma ✅ do dono (`ARQ-084`, o custo fixo da Maind e os valores iniciais do aviso de custo, em 03/11/2026) e uma 🟡 com o dono (`ARQ-085`, o orçamento de operação) · quase todo número aqui é estimativa 🔎, com a fonte ao lado · três verificações novas (V-15, o custo real por função na PRD; V-17, a forma do plantão; V-18, os modelos do Bedrock que processam em São Paulo), no [documento 14](14-conferencia-do-produto.md).

Última atualização: 03/11/2026 (a homologação da v2 na máquina da PRD, pela `ARQ-055`, sem máquina própria; a cópia de segurança fora do Horus, pela `ARQ-086`, sem a máquina de cópias; nenhuma instância é produção real, pela `ARQ-056`: o plantão e a sonda só com a primeira produção real; o CI na VPS de hoje até a primeira produção real, pela `ARQ-082` ✅; o envelope, `ARQ-016` ✅; uma stack por máquina, `ARQ-069` ✅; o e-mail no plano gratuito até a primeira produção real, pela `ARQ-046` ✅; as funções da segurança só na v2.1, pela `ARQ-090` ✅; o custo no painel do owner da instância, pela `ARQ-017` ✅; o custo fixo da Maind, sem rateio no produto, pela `ARQ-084` ✅; a pesquisa na web pela busca nativa da conexão, `ARQ-027` ✅; a bateria com modelo real, pela `ARQ-081` ✅; a produção real numa nuvem pública com Kubernetes, pela `ARQ-092` ✅: o orçamento dela se refaz com a nuvem escolhida; o Kubernetes gerenciado e o Postgres gerenciado na produção real, pela `ARQ-093` ✅; a sonda de fora num serviço de outro provedor, pela `ARQ-070` ✅; o plantão fora do horário comercial, pela `ARQ-071` ✅; o preço da nuvem da produção real, pela V-19, e o orçamento refeito, na `ARQ-085` 🟡; a escolha da nuvem adiada pelo dono, com a solução sem ficar presa a ela, pela `ARQ-096` ✅).

Este documento diz **quanto custa operar o Horus v2, por organização e por componente**: a IA, por função e por modelo, partindo do que a v1.xx mede hoje; o WhatsApp, pela tabela da Meta; o e-mail; as máquinas; a cópia da instância SaaS, que fica fora do Horus, e as máquinas por hora; a sonda de fora e a observabilidade; o CI; e o plantão. Parte das metas do [documento 03](03-metas-de-qualidade.md) (o envelope da `ARQ-016` e a medida do custo da `ARQ-017`). Ele **não** diz o preço que a Maind cobra: o preço em reais fica fora dos documentos (`D-116`, `P-022`), e de quem é cada custo no SaaS é o impasse A-03.

- O **quê** e o **porquê** são do produto ([backlog estratégico](../produto/backlog-estrategico.md)). As decisões (`ARQ-nnn`) estão no [registro](02-registro-de-decisoes.md).
- O código e os documentos da v1.xx se citam como `horus@318db52b:<caminho>`. Nada foi executado e nenhum modelo foi chamado. Os preços públicos foram consultados na web em **02/11/2026** (os das cópias no provedor das VPS, em 03/11/2026), e cada um traz a página de onde veio; os da Meta, os da OpenRouter e os do GitHub mudam com frequência e precisam ser reconferidos na contratação.
- **As faixas.** Todo valor que depende de uso é uma faixa 🔎, montada com os tamanhos medidos na v1.xx e com os preços públicos. O câmbio usado para mostrar reais é **cerca de R$ 5,15 por dólar** 🔎, a proporção que a própria tabela da Meta em reais usa (a utilidade a R$ 0,0350 e a US$ 0,0068).
- Nenhum host, endereço de IP ou domínio aparece aqui.

Legenda: 🟢 decidida pelo arquiteto · 🟡 proposta ao dono · 🔎 estimativa ou hipótese a confirmar · ♻️ vem da v1.xx · 🔧 vem e muda · 🆕 novo.

## 1. O que o tema precisa garantir

| Garantia | Objetivos | Decisões |
| --- | --- | --- |
| 💸 **A Maind sabe quanto cada organização custa, por componente, antes da fatura** | O6, O7 | `ARQ-017` ✅; `D-062`, `D-063` (todo agente usa IA, e o consumo entra no custo da organização) |
| 🧮 **O custo se mede pelo registro do Horus, e não pelo painel do provedor** | O6 | `ARQ-017`, `ARQ-072`; a análise das métricas da v1.xx (60% das chamadas "sem organização" no painel do provedor) |
| 🚫 **Sem corte automático:** o owner controla o custo pelo modelo que escolhe e pela aprovação de criar agentes | O7 | `D-061`, `D-062`, `D-114` |
| 📱 **O custo do WhatsApp segue a categoria que a Meta cobra**, na conta da organização ou na da Maind | O1, O4 | `D-097`, `D-124`; `ARQ-047` 🟡, `ARQ-049` |
| 📦 **O envelope do primeiro ano cabe num orçamento conhecido**, e se sabe o que cresce com o uso | O1, O3, O4, O7 | `ARQ-016` ✅; `D-115` (o plano único), `D-117`, `D-123` (o assento de owner grátis) |
| 🧾 **O preço fica fora; o custo, dentro** | O7 | `D-116` (o preço em reais fora dos documentos de produto), `P-022` |

## 2. As decisões

| Decisão | O que decide | Situação |
| --- | --- | --- |
| `ARQ-016` | O envelope do primeiro ano: 30 organizações, 2.000 assentos, 500 pessoas que perguntam, 3.000 perguntas por dia útil, 1.000 execuções de agente e 1.500 mensagens de WhatsApp por dia | ✅ |
| `ARQ-017` | O custo por organização e por componente, no painel do owner da instância, com o aviso acima de um limiar e sem corte | ✅ |
| `ARQ-031` | O consumo de cada chamada leva a função, o canal e o agente | 🟢 |
| **`ARQ-083`** | **O custo de IA de cada chamada é o que o provedor informa; sem ele, o Horus estima pelo preço público do modelo e marca a estimativa** | 🟢 |
| **`ARQ-084`** | **O custo fixo é da Maind e não se rateia entre as organizações no produto; o aviso de custo começa com valores padrão que a Maind ajusta por organização** | ✅ |
| **`ARQ-085`** | **O orçamento de operação: a produção real na Google Cloud, os outros serviços nos planos já escolhidos e a VPS da construção, numa faixa mensal revista a cada trimestre contra as faturas** | 🟡 |

## 3. Os componentes e quanto custa cada um

### 3.1 Como o custo se mede (`ARQ-017`, `ARQ-083` 🟢)

| Componente | O que se registra | Onde nasce o número | Desde |
| --- | --- | --- | --- |
| **IA** | Cada chamada: a organização, a pessoa, a conversa, a função, o provedor, o modelo, o fornecedor, os tokens de entrada, de saída e do cache, e o custo em dólar; na v2, também o canal e o agente | O custo que o provedor informa na chamada (`horus@318db52b:apps/server/Horus.Core/Data/ConsumoDeIaEntity.cs`, gravado em lote por `horus@318db52b:apps/server/Horus.Api/GravadorDeConsumoDeIa.cs`) | ♻️ 29/09/2026; 🔧 o canal, o agente e a estimativa |
| **WhatsApp** | Cada mensagem enviada: a conta (da organização ou da Maind), a categoria que a Meta cobra e o desfecho | O aviso de status da Meta (`ARQ-048`) | 🆕 |
| **E-mail** | Cada envio aceito, por uso (recuperação, aviso, convite, conector) | O envio da instância | 🔧 hoje só o ritmo |
| **Infraestrutura** | A fatura de cada serviço do mês | O orçamento da `ARQ-085`, da Maind, sem rateio entre as organizações (`ARQ-084`) | 🆕 |

**A chamada sem custo informado** (`ARQ-083`). Hoje o custo fica nulo quando o provedor não o informa, e o painel soma só o que veio, marcando o total como "parcial" (`horus@318db52b:apps/server/Horus.Core/Data/PainelDaOrg.cs`). O **Bedrock nunca informa**: toda chamada dele grava o custo nulo (`horus@318db52b:apps/server/Horus.Core/Llm/Bedrock/BedrockProvider.cs`), e uma organização só com o Bedrock apareceria sem custo nenhum. Na v2.0:
- **Sem o custo do provedor, o Horus estima** pelos tokens da própria chamada e pelo preço público do modelo, e marca a linha como **estimada**. No OpenRouter, o preço vem do catálogo de modelos que a v1.xx já lê, com cache de uma hora (`horus@318db52b:apps/server/Horus.Core/Llm/CatalogoOpenRouter.cs`); no Bedrock, de uma tabela de preço por modelo e região, ao lado da tabela de capacidades que já existe (`CapacidadesDoBedrock.cs`), atualizada a cada pacote.
- **A conferência do mês** compara a soma do registro com a conta do provedor: os créditos do OpenRouter e o gasto do Cost Explorer no Bedrock, que a v1.xx já lê (o Cost Explorer cobra US$ 0,01 por pedido, e o resumo dele fica seis horas em cache: `horus@318db52b:apps/server/Horus.Core/Llm/Bedrock/ResumoDoBedrock.cs`; preço na [página do AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/), consultada em 02/11/2026).
- **A taxa do OpenRouter sobre a compra de créditos** (5,5% no plano Standard e 8% no Business; sem taxa na chave própria até US$ 25.000 por mês, [openrouter.ai/pricing](https://openrouter.ai/pricing), consultada em 02/11/2026) não aparece no custo da chamada: ela entra na conferência do mês, sobre o total.

### 3.2 A IA, por função e por modelo

**O que a v1.xx mediu** (todas com o Claude Sonnet, pelo OpenRouter):

| Data | O que se mediu | Número | Fonte |
| --- | --- | --- | --- |
| 17/09/2026 | Uma rodada da bateria NL→SQL, 106 perguntas | US$ 5,49, cerca de **US$ 0,052 por pergunta** só no Planejador | `horus@318db52b:docs/superpowers/specs/2026-09-17-filtro-perdido-na-janela-design.md` §4 |
| 03/10/2026 | Seis rodadas da mesma bateria, com o Sonnet 5.5, no nível 2 | 636 chamadas e US$ 42,70: cerca de **US$ 0,067 por pergunta** | `horus@318db52b:docs/superpowers/specs/2026-10-03-resposta-e-raciocinio-medicao.md` |
| 03/10/2026 | O Planejador, chamada a chamada | Cerca de **US$ 0,061 por chamada** (10 chamadas, US$ 0,61) | `horus@318db52b:docs/superpowers/plans/2026-10-06-card-de-workflow.md` |
| 03/10/2026 | O tamanho de um segundo turno | 49.141 tokens de entrada; a resposta bruta, cerca de mil tokens; mediana de 20,8 segundos | `…-medicao.md`; `horus@318db52b:docs/superpowers/specs/2026-10-03-resposta-e-raciocinio-critica/critica-llm.md` |
| 06/10/2026 | A estimativa do workflow | A primeira pergunta de fluxo entre US$ 0,12 e 0,14 (Sonnet) e entre 0,20 e 0,23 (Opus); a seguinte, com cache, US$ 0,06 e 0,11; a troca de período, US$ 0,01 a 0,03 | `horus@318db52b:docs/superpowers/plans/2026-10-06-card-de-workflow.md` |
| 04 a 09/09/2026 | O cache de prompt | O acerto subiu de 32% para 84% depois de tirar o nível e a web da parte estável | `horus@318db52b:docs/produto/chat-interno/chat-por-dentro.html` |

**Os preços públicos** (por milhão de tokens, no OpenRouter, consultados em 02/11/2026 na API pública de modelos que alimenta [openrouter.ai/models](https://openrouter.ai/models); os endpoints regionais custam 10% a mais):

| Classe | Modelo de referência | Entrada | Saída | Leitura do cache |
| --- | --- | --- | --- | --- |
| **Topo** | Claude Opus 5.5 | 4,00 | 20,00 | 0,20 |
| **Médio** (o medido na v1.xx) | Claude Sonnet 5.5 | 2,00 | 10,00 | 0,10 |
| **Médio** | GPT-6 Sol | 2,00 | 10,00 | 0,20 |
| **Rápido** | Gemini 3.8 Flash | 0,75 | 3,75 | 0,075 |
| **Barato** | Gemini 3.5 Flash Lite | 0,30 | 2,50 | 0,03 |
| **Mínimo** | GPT-6 Luna; Claude Haiku 5.5 | 0,10 | 0,50 | 0,01 |

**A pesquisa na web** (`ARQ-027` ✅): o motor padrão do OpenRouter custa **US$ 0,007 por pesquisa**, com até 10 resultados, e o padrão é 5; a busca nativa de cada fabricante, cerca de US$ 0,01; os tokens dos resultados se cobram à parte ([documentação da pesquisa na web do OpenRouter](https://openrouter.ai/docs/guides/features/web-search), consultada em 02/11/2026). A v1.xx não escolhe o número de resultados (`horus@318db52b:apps/server/Horus.Core/Llm/OpenRouterProvider.cs`).

**O custo por função** 🔎, por chamada, a partir dos tetos e dos tamanhos de entrada da v1.xx (`horus@318db52b:apps/server/Horus.Core/Llm/FuncoesDeIa.cs`, `Chat/ChatEngine.cs`, `Planner/`) e dos preços acima:

| Função | Quando roda | Tamanho típico 🔎 | Classe média | Classe mínima | Classe topo |
| --- | --- | --- | --- | --- | --- |
| `planejador` | Toda pergunta com fonte | 11.500 a 49.000 tokens de entrada, parte do system no cache; cerca de mil de saída | US$ 0,03 a 0,07 (medido: 0,05 a 0,07) | US$ 0,002 a 0,004 | US$ 0,07 a 0,14 |
| `analise-avancada` | Com a Análise avançada ou a web ligadas | De 6.000 a 10.000 de entrada (o resultado vai até 12.000 caracteres); até 2.000 de saída | US$ 0,02 a 0,04 | US$ 0,001 a 0,002 | US$ 0,05 a 0,08 |
| 🆕 `pesquisa-na-web` | Com a pesquisa ligada | A pergunta e os resultados, cerca de 5.000 de entrada; mil de saída | US$ 0,02 a 0,03, com a pesquisa | US$ 0,008 | US$ 0,05 |
| `reparo-de-consulta` e `gerador-de-plano` | Quando a consulta falha ou volta vazia, de 10% a 20% das perguntas 🔎 | O documento e o SQL; o system do Planejador | US$ 0,03 a 0,05 cada | US$ 0,002 | US$ 0,06 a 0,10 |
| `resposta-conversa` | A conversa sem fonte | O histórico, até 60.000 caracteres | US$ 0,02 a 0,05 | US$ 0,001 a 0,003 | US$ 0,04 a 0,10 |
| `planejamento-` e `renderizacao-de-workflow` | A pergunta de fluxo | Medido na estimativa de 06/10 | US$ 0,06 a 0,07 juntas | US$ 0,004 | US$ 0,11 |
| `triagem-`, `resumo-de-fontes`, `titulo-por-ia` | Raras ou curtas | Até 300 tokens de saída no título | Menos de US$ 0,01 | Menos de US$ 0,001 | Menos de US$ 0,02 |
| `reescritor-` e `verificador-de-seguranca` | Só na v2.1 (`ARQ-090`): uma vez por consulta protegida nova (fonte, gabarito e versão), e não por pergunta: a protegida é a mesma para todas as pessoas e se reaproveita | Até 30.000 caracteres de regras e SQL; até 8.000 tokens de saída | US$ 0,04 a 0,15 por consulta protegida nova | US$ 0,003 | US$ 0,08 a 0,30 |
| `compilador-de-seguranca` | Quando o owner compila o documento de segurança de uma base | Até 20.000 tokens de saída | US$ 0,10 a 0,30 por compilação | — | US$ 0,20 a 0,60 |
| 🆕 `interpretacao-do-agente` | Quando o autor cria ou muda as instruções | As instruções e as fontes | US$ 0,01 a 0,05 por agente | Menos de US$ 0,005 | US$ 0,03 a 0,10 |
| 🆕 `ciclo-do-agente` | Cada volta do ciclo, até 16 (`ARQ-030`) | A interpretação e as respostas já recebidas | US$ 0,01 a 0,03 por volta | Menos de US$ 0,002 | US$ 0,02 a 0,06 |

**O custo por pergunta e por execução** 🔎, com a classe média em todas as funções:

| O que | Composição | Faixa 🔎 |
| --- | --- | --- |
| Pergunta de dados | O Planejador, e o reparo de vez em quando | US$ 0,04 a 0,08 |
| Pergunta de dados com a Análise avançada | Mais a leitura depois da consulta | US$ 0,07 a 0,11 |
| Pergunta de dados com a web | Mais a pesquisa e a leitura | US$ 0,10 a 0,14 |
| Pergunta sem fonte | A resposta da conversa, com ou sem a web | US$ 0,02 a 0,08 |
| **A pergunta média do envelope** | A mistura dos modos | **US$ 0,05 a 0,15** |
| **Uma execução de agente** | De 2 a 4 perguntas ao motor e de 3 a 6 voltas, tipicamente | **US$ 0,15 a 0,60** |
| O teto técnico de uma execução | 8 perguntas e 16 voltas (`ARQ-030`) | Cerca de US$ 1,70 no máximo |

Com a classe mínima, os mesmos números caem de 15 a 25 vezes; com a classe topo, dobram. **O modelo que o owner escolhe para cada função é a maior alavanca de custo do produto** (`D-061`, `MF-105:IA sob controle da organização`).

**No envelope do primeiro ano** (`ARQ-016`), com a classe média 🔎:

| Uso | Volume por mês 🔎 | Custo por mês 🔎 |
| --- | --- | --- |
| Perguntas de análise | 3.000 por dia útil, cerca de 66.000 | US$ 3.300 a 9.900 |
| Execuções de agente | 1.000 por dia útil, cerca de 22.000 | US$ 3.300 a 13.200 |
| **A IA da instância** | | **US$ 6.600 a 23.100** (R$ 34 mil a 119 mil) |
| **Por organização** (1/30) | | **US$ 220 a 770** |
| **Por pessoa que pergunta** (1/500) | 132 perguntas e 44 execuções | **US$ 13 a 46** |
| **Por membro leitor** | Só recebe artefatos | Perto de zero de IA |

O exemplo da `D-133` (1.200 perguntas por mês numa organização) dá de US$ 60 a 180 por mês só em perguntas. **Os agentes podem custar tanto quanto a conversa, ou mais**, porque cada execução faz várias perguntas inteiras ao motor; o teto técnico por execução (`ARQ-030`) é o que limita o pior caso, já que o produto deixou o teto de custo de fora (`D-062`, `D-114`).

**O Bedrock e o dado no país** ⚠️: pela documentação da Anthropic consultada em 02/11/2026, o Claude no Bedrock na região de São Paulo só existe pelo **endpoint global**, sem acréscimo de preço; o endpoint regional custa 10% a mais e não existe na América do Sul ([Claude in Amazon Bedrock](https://platform.claude.com/docs/build-with-claude/claude-in-amazon-bedrock); [AWS, Global cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html)). Para os modelos Claude, escolher São Paulo **não mantém o processamento no país**. Isso corrige a hipótese 🔎 do documento 08 (3.4) e da `ARQ-051`, e foi à A-16 e à verificação V-18.

### 3.3 O WhatsApp (`ARQ-047` a `ARQ-050`)

**A tabela da Meta para o Brasil**, por mensagem entregue (consultada em 02/11/2026):

| Categoria | Preço | Fonte |
| --- | --- | --- |
| **Utilidade** (o aviso do agente, o PDF de um agendamento, o "sua resposta ficou pronta") | **US$ 0,0068**, ou R$ 0,0350 na cobrança em reais | A [página de preços da Meta](https://developers.facebook.com/docs/whatsapp/pricing) ("Meta's current rate for utility and authentication messages to users in Brazil"); o valor em reais, pela [ChatMaxima](https://chatmaxima.com/whatsapp-api-pricing/brazil/), que cita o rate card da Meta vigente em 01/10/2026 |
| **Autenticação** (o código de ligação do número) | **US$ 0,0068**, ou R$ 0,0350 | Idem |
| **Marketing** | US$ 0,0625, ou R$ 0,3217 🔎 | Só fontes de terceiros ([Whautomate](https://whautomate.com/whatsapp-business-api-pricing-brazil), ChatMaxima); bate com a tabela da Gallabox de 01/10/2026 menos a margem dela |
| **Serviço** (o que o Horus responde dentro da janela de 24 horas: o texto, as imagens, o "trabalhando") | **Grátis até 1.000 mensagens por número por mês**; da 1.001ª em diante, cerca de US$ 0,0068 🔎 | A página de preços da Meta (a franquia, vigente desde 01/10/2026); o preço acima dela, por terceiros |
| As faixas de desconto por volume (utilidade e autenticação) | De 5% a 25% sobre a tabela; os volumes de corte não foram encontrados | ChatMaxima |

**O que mudou desde o documento 08** ⚠️: até 30/09/2026, o modelo de utilidade entregue dentro de uma janela aberta e as mensagens de serviço eram grátis; **desde 01/10/2026**, o modelo de utilidade é cobrado também dentro da janela, e as mensagens de serviço só são grátis até 1.000 por número por mês ([página de preços da Meta](https://developers.facebook.com/docs/whatsapp/pricing)). A Meta também passou a faturar as contas do Brasil em reais desde 01/07/2026, e as contas em outra moeda precisam migrar até 30/06/2027. A decisão da `ARQ-049` (o conector envia sempre por modelo) continua, pela previsibilidade da entrega, mas o custo dela deixa de ser zero dentro da janela: cada aviso custa US$ 0,0068 em qualquer caso. O documento 08 (3.3) e a `ARQ-049` ganharam a nota.

**Os outros limites públicos** (a V-04 e a V-13, respondidas em parte): o corpo de um modelo vai até 1.024 caracteres, e a mensagem de texto livre, até 4.096 ([componentes dos modelos](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/components); [mensagens de texto](https://developers.facebook.com/documentation/business-messaging/whatsapp/messages/text-messages)); a notificação sem resposta é reenviada, com frequência decrescente, por até sete dias ([webhooks](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/set-up-webhooks)); o teto de mensagens iniciadas é do **portfólio de negócio**, e não do número (250, 2.000, 10.000, 100.000 ou ilimitado), e a mudança dele chega por notificação ([messaging limits](https://developers.facebook.com/docs/whatsapp/messaging-limits)); tudo consultado em 02/11/2026.

**No envelope do primeiro ano** 🔎 (1.500 mensagens por dia, cerca de 40.000 por mês):

| Mensagem | Parcela 🔎 | Por mês 🔎 | Custo por mês 🔎 |
| --- | --- | --- | --- |
| As respostas dentro da janela (serviço) | 70% | 28.000 | Contas das organizações: de zero a US$ 30, porque cada número tem a franquia de 1.000; só a conta da Maind: cerca de US$ 180 |
| Os avisos de agente e os PDFs (utilidade) | 25% | 10.000 | US$ 68 |
| Os códigos de ligação (autenticação) | Poucos | 100 a 500 | Até US$ 3,40 |
| **O WhatsApp da instância** | | | **US$ 70 a 250** |
| Se a Meta classificar o aviso do agente como marketing (A-19) | | 10.000 | Cerca de US$ 560 a mais: o aviso passa de US$ 68 a US$ 625 |

**Quem paga** (A-03): na conta da organização, a organização paga à Meta, pelo meio de pagamento da conta dela; na conta da Maind, a Maind paga, e o registro dá a parte de cada organização, porque os envios pela conta da Maind são uma das medidas com a organização como rótulo (`ARQ-073`). **Por organização**, no envelope: de US$ 2 a 8 por mês 🔎, ou até US$ 30 se o aviso virar marketing.

### 3.4 O e-mail (`ARQ-046` ✅)

| Plano do serviço de hoje | Preço por mês | O que inclui | Fonte |
| --- | --- | --- | --- |
| Gratuito | US$ 0 | 3.000 por mês, **100 por dia**, 3 domínios | [resend.com/pricing](https://resend.com/pricing), consultada em 02/11/2026 |
| Pro | US$ 20 (50 mil por mês) ou US$ 35 (100 mil) | Sem teto diário; excedente a US$ 0,90 por mil; 10 domínios | Idem |
| Scale | A partir de US$ 90 (100 mil) | Até 1.000 domínios; o IP dedicado por US$ 30 | Idem |

Cada mensagem vai até **40 MB, com os anexos** já codificados ([anexos no Resend](https://resend.com/docs/dashboard/emails/attachments)): é o teto que a A-19 usa para o PDF que não cabe. No envelope, cerca de 2.000 e-mails por dia útil (documento 08, 3.2) dão uns 44.000 por mês: **o plano gratuito não serve**, e o Pro de 100 mil (US$ 35) cabe com folga 🔎. **Por organização:** cerca de US$ 1 por mês 🔎. A marca completa da v2.1, com o domínio de cada contratante, pede o Pro (10 domínios) ou o Scale. O plano da conta da Maind é a V-02.

### 3.5 As máquinas (`ARQ-055` e `ARQ-056` ✅)

| Máquina | Para quê | Custo por mês 🔎 | Fonte |
| --- | --- | --- | --- |
| **A da PRD** (8 vCPU, 32 GB, 400 GB) | A PRD SaaS, com os dois papéis na v2.0; até a v2.0, também o HML da v1.xx; a homologação da v2, desde o M0 (`ARQ-055`); os dois bancos, as bases de demonstração e a observabilidade | **R$ 120 a 260** (US$ 26 a 50): R$ 119,99 no contrato de 24 meses, e R$ 259,99 na renovação | A tabela pública do provedor das VPS de hoje (o plano de 8 vCPU e 32 GB da Hostinger), consultada em 02/11/2026 |
| **A segunda VPS** | A instância dedicada de um cliente | A mesma faixa; 🔎 é um custo daquele contrato, e não do SaaS | Idem |

**A homologação da v2 não custa máquina** (`ARQ-055` ✅): ela é uma terceira instância na máquina da PRD. Se o uso medido com ela de pé chegar ao gatilho da troca (V-07; documento 09, 3.3), a máquina maior entra neste orçamento. O provisionamento do zero de uma máquina se prova numa máquina por hora antes do M7 (3.7).

A máquina é o menor custo por pessoa: dividida pelos 2.000 assentos do envelope, a da PRD sai a menos de R$ 0,15 por assento por mês 🔎. **A troca para uma máquina maior** (os gatilhos do documento 09, 3.3) muda pouco a conta.

**A licença do SQL Server das bases de demonstração** (`ARQ-059` ✅, uma base só para todas as instâncias): o Developer não custa nada, e o Express, a primeira alternativa se a V-05 disser que o Developer não cabe, também não. Só a terceira opção, o Standard licenciado por núcleo, teria custo, e ele não está orçado aqui: entra nesta seção se a V-05 levar a ela.

### 3.6 A cópia da instância SaaS, fora do Horus (`ARQ-086` ✅)

O Horus não faz a cópia de segurança: cada dono de instância a configura na infra dele (`ARQ-086`). Na instância SaaS, a dona é a Maind, e o ponto de partida é a cópia do próprio provedor das VPS. O custo entra aqui como custo de operar a instância SaaS, e não do produto.

| O que | Por mês 🔎 | O que guarda | Fonte |
| --- | --- | --- | --- |
| **A cópia semanal da máquina inteira** | Já vem no plano | As duas últimas semanas | As páginas de ajuda do provedor das VPS de hoje, consultadas em 03/11/2026 |
| **A cópia diária da máquina inteira** | De US$ 6 a 12, à parte (as páginas divergem) | As duas últimas diárias, que não se apagam à mão | Idem |
| **Uma máquina pequena só de cópias** (1 a 2 vCPU, 4 a 8 GB, 50 a 100 GB de disco), se a Maind quiser perder menos que um dia | R$ 30 a 90 (US$ 6 a 18): o plano de entrada sai a US$ 6,49 por mês no contrato de 24 meses e a US$ 11,99 sem ele | A cópia do banco por dia e o registro contínuo, pelo prazo que a infra escolher | A página de planos do provedor, em dólar, e um levantamento de terceiros em reais, consultados em 03/11/2026 |

**O volume** 🔎: hoje o banco tem 59 MB; no fim do primeiro ano, de 15 a 40 GB. A cópia do provedor leva a máquina inteira, e o preço da diária segue o plano da máquina, e não o volume 🔎. A máquina de cópias, se entrar, começa com o disco de 100 GB e se revê pelo gatilho da troca de máquina (documento 09, 3.3).

O armazenamento de objetos de outro provedor sairia de US$ 1 a 6 por mês (a tabela da AWS em São Paulo, consultada em 02/11/2026). Fica registrado para a infra de uma instância que queira as cópias fora do provedor da máquina.

### 3.7 As máquinas por hora

O ensaio da volta é da infra de cada instância (`ARQ-086`): na SaaS, ele pode restaurar o banco e o anel numa instância de prova da máquina da PRD, **sem máquina nova**. O provisionamento do zero de uma máquina, que a homologação na VPS de hoje não prova (`ARQ-055`), se prova numa máquina por hora antes do M7. A conferência da volta do Horus (`ARQ-087`) se prova no CI, sem máquina. Quando um ensaio precisar de máquina própria, uma máquina por hora sai de US$ 2 a 4 por ensaio, de 4 a 6 horas 🔎, num provedor com essa cobrança; no provedor das VPS, que cobra por mês, seria um mês do plano.

| O que | Preço por hora | Fonte |
| --- | --- | --- |
| AWS EC2, 8 vCPU e 32 GB, em São Paulo | US$ 0,64 🔎 | Terceiros (DoiT, aws-pricing.com), consultados em 02/11/2026 |
| Uma máquina de 8 vCPU e 32 GB num provedor com cobrança por hora (DigitalOcean) | US$ 0,375 | [digitalocean.com/pricing/droplets](https://www.digitalocean.com/pricing/droplets), consultada em 02/11/2026 |

O pacote numa máquina sem saída, antes do M10, custa o mesmo que um ensaio numa máquina por hora.

### 3.8 A sonda de fora e a observabilidade (`ARQ-069` ✅ e `ARQ-070` ✅)

**A conta da sonda** 🔎: três instâncias (a PRD, a segunda VPS e a homologação) conferidas a cada minuto, de duas regiões, e três sinais de vida por instância (a stack, o papel "trabalhar" e a faxina) dão 3 conferências de saúde e 9 sinais de vida; a cópia de cada instância pode mandar o seu, se a infra dela quiser (`ARQ-086`).

| Serviço | O que serve | Preço por mês | Fonte |
| --- | --- | --- | --- |
| UptimeRobot Team | 100 monitores a cada 30 segundos, com sinais de vida e várias regiões; relatório mensal por e-mail | US$ 41 (US$ 35 no anual) | [uptimerobot.com/pricing](https://uptimerobot.com/pricing/), consultada em 02/11/2026 |
| Better Stack | A licença de quem atende, US$ 34; 10 monitores e sinais de vida grátis, e mais 10 sinais de vida por US$ 20; relatório de disponibilidade | Cerca de US$ 54 🔎 | [betterstack.com/pricing](https://betterstack.com/pricing), consultada em 02/11/2026 |
| Grafana Cloud Synthetic Monitoring | Cobra por execução: as 259.200 do mês passam do plano gratuito | Cerca de US$ 99 🔎, sem sinais de vida | [grafana.com/pricing](https://grafana.com/pricing/), consultada em 02/11/2026 |

O plano gratuito do UptimeRobot confere a cada 5 minutos e não tem sinal de vida, e por isso não cumpre a `ARQ-070`. **A sonda: de US$ 40 a 60 por mês** 🔎 (a V-12).

**A observabilidade** não tem licença: a stack é de código aberto e roda em cada máquina (`ARQ-069`). O custo dela é a memória: os 4 GB da stack são cerca de um oitavo da máquina da PRD, uns R$ 15 a 33 por mês 🔎, já dentro do custo da máquina. O Broadcast do OpenRouter não cobra nada.

### 3.9 O CI e a bateria com modelo real (`ARQ-081` ✅ e `ARQ-082` ✅)

**Até a primeira produção real, o CI roda num executor próprio na VPS de hoje e não custa nada por minuto** (`ARQ-082`, a escolha do dono em 03/11/2026). A conta abaixo é a dos executores hospedados do GitHub, que entram com a primeira produção real.

| Item | Preço | Fonte |
| --- | --- | --- |
| Os minutos do Actions, executor Linux padrão | **US$ 0,006 por minuto**, desde 01/01/2026 | [Cobrança do GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions), consultada em 02/11/2026 |
| O que cada plano inclui em repositório privado | Free: US$ 12 por mês de computação (cerca de 2.000 minutos Linux); Team: US$ 18 (cerca de 3.000); Enterprise: US$ 300 | Idem |
| Os artefatos e os Packages | US$ 0,25 por GB por mês, acima do incluído | Idem |
| As versões publicadas (onde fica o pacote) | Cada arquivo abaixo de 2 GiB, até 1.000 por versão, sem teto total | [Sobre as versões no GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases), consultada em 02/11/2026 |
| O executor próprio | Sem taxa: a de US$ 0,002 por minuto foi adiada sem data | A página de cobrança do Actions |

**O uso** 🔎: com 2 a 4 pessoas no time, cerca de 15 execuções por dia útil (os pedidos de mudança e as entradas na `main`), de 50 a 120 minutos cobrados cada uma (as etapas em paralelo somam minutos) dão de 15.000 a 40.000 minutos por mês: **de US$ 75 a 225 por mês**, menos o que o plano inclui. O pacote nas versões publicadas não paga armazenamento.

**A bateria com modelo real** (`ARQ-081`), uma vez por marco que muda o que vai ao modelo: de US$ 5,49 a 7 por rodada de 106 casos (3.2), três rodadas de cada lado, **de US$ 33 a 45 por comparação** 🔎; nos oito marcos da v2.0, de US$ 300 a 700 no total 🔎, cada rodada autorizada pelo dono. A conta de ensaio da Meta no M4 e a prova do Bedrock no M2 custam poucos dólares cada.

### 3.10 O plantão (`ARQ-071` ✅)

A classe de alertas que acorda alguém a qualquer hora (`ARQ-071`) pede uma pessoa de sobreaviso fora do horário comercial. **A regra de referência é a CLT:** a hora de sobreaviso vale um terço da hora normal, numa escala de até 24 horas (art. 244, § 2º, [Decreto-lei nº 5.452/1943](https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452.htm)); a Súmula 428 do TST estende o sobreaviso a quem fica à distância, controlado por meios telemáticos, aguardando o chamado (redação de 14/09/2012, Res. 185/2012); e a hora em que a pessoa é chamada e trabalha se paga como hora extra, com 50% a mais, pela jurisprudência 🔎. A forma (empregado, rodízio, outro arranjo) é da Maind, com o jurídico (V-17).

**A conta** 🔎: o horário comercial da decisão do dono vai das 10h às 17h, todos os dias (49 horas por semana), e sobram cerca de 515 horas de sobreaviso por mês. Para quem ganha de R$ 8.000 a 15.000 por mês (220 horas), um terço da hora sobre 515 horas dá de **R$ 6.200 a 11.700 por mês**, antes dos encargos; com os encargos de um empregado, de R$ 10.000 a 20.000 🔎. Um rodízio entre duas ou mais pessoas divide a escala, mas não as horas, e não muda o total. **Por organização** (1/30), de R$ 200 a 670 por mês 🔎.

**O plantão é o maior custo fixo da operação**, maior que as máquinas, as cópias, a sonda, o e-mail e o CI somados. As alavancas: ampliar o horário comercial em que o alerta espera (das 8h às 22h, por exemplo, reduz as horas de sobreaviso quase à metade); acordar alguém só no S1 (`ARQ-068`); ou contratar o primeiro atendimento fora. Cada uma é decisão do dono, dentro da `ARQ-085`.

### 3.11 A soma, por organização e por componente

**No envelope do primeiro ano** (30 organizações, 2.000 assentos, 500 pessoas que perguntam), com a classe média de modelo 🔎:

| Componente | Quem paga hoje | A instância, por mês 🔎 | Por organização, por mês 🔎 | Cresce com |
| --- | --- | --- | --- | --- |
| **IA da conversa** | A conta da conexão de IA da organização (A-03) | US$ 3.300 a 9.900 | US$ 110 a 330 | As perguntas e o modelo escolhido |
| **IA dos agentes** | Idem | US$ 3.300 a 13.200 | US$ 110 a 440 | As execuções, as perguntas por execução e o modelo do agente |
| **WhatsApp** | A organização, na conta dela; a Maind, na conta da Maind (A-03) | US$ 70 a 250 | US$ 2 a 8 | As respostas fora da franquia e os avisos |
| **E-mail** | A Maind | US$ 35 | Cerca de US$ 1 | Os avisos e os PDFs |
| **Máquina** (a da PRD, com a homologação) | A Maind | US$ 25 a 50 | US$ 1 a 2 | A troca de máquina, pelos gatilhos |
| **Cópia da instância SaaS** (fora do Horus) | A Maind, dona da instância | De nada a US$ 12 | Menos de US$ 1 | O plano do provedor |
| **Sonda** | A Maind | US$ 40 a 60 | US$ 1 a 2 | O número de instâncias |
| **Observabilidade** | A Maind, dentro da máquina | — | — | — |
| **CI** | A Maind; até a primeira produção real, na VPS de hoje, sem custo | US$ 75 a 225 | US$ 3 a 8 | O ritmo do time, e não o uso |
| **Plantão** | A Maind | R$ 6.200 a 20.000 | R$ 200 a 670 | A forma do plantão, e não o uso |

Nas linhas do custo fixo (as máquinas, a cópia, a sonda, o e-mail, o CI e o plantão), a coluna "por organização" é só uma média para o comercial: o produto não rateia o fixo (`ARQ-084`).

**O que salta aos olhos:**
- **A IA é quase todo o custo variável**, e a parte dos agentes pode passar a da conversa. Quem paga a conta da IA (A-03) é a pergunta comercial que mais pesa.
- **O custo fixo de ferramentas e máquinas é pequeno por assento**: de R$ 5.160 a 6.300 por mês para a produção real, com a nuvem sob demanda 🔎, cerca de US$ 940 a 1.150. Dividido pelos 2.000 assentos, menos de US$ 0,60 por assento.
- **O plantão é o maior custo fixo**, e não cresce com o uso: no primeiro cliente pesa muito por assento, e no envelope cheio pesa pouco.
- **O custo por assento muda com o tipo**: a pessoa que pergunta custa de US$ 13 a 46 por mês de IA 🔎, e o membro leitor, quase nada. É um dado para o preço por tipo de assento (`P-022`), que fica fora dos documentos (`D-116`).

### 3.12 O aviso de custo (`ARQ-084` ✅)

| Ponto | Proposta |
| --- | --- |
| **O custo fixo** | Da Maind, e não se rateia entre as organizações no produto (`ARQ-084`): como a Maind o cobre é assunto comercial e financeiro, fora dos documentos (`D-116`). A IA e o WhatsApp pela conta da Maind vão direto à organização, pelo registro (3.1); o e-mail conta em número de envios |
| **O limiar do mês, padrão** 🔎 | US$ 30 por assento que pergunta (owner, gestor e membro full), ajustável pela Maind em cada organização; uma organização de 20 pessoas que perguntam avisa acima de US$ 600 no mês |
| **O sinal da semana** | A semana acima do dobro da média das quatro anteriores (`ARQ-017`), só acima de US$ 20 na semana, para a organização pequena não avisar por centavos |
| **O sinal da execução** 🔎 | Uma execução de agente acima de US$ 2: é o teto técnico estourado ou um modelo caro escolhido sem querer |
| **Quem é avisado** | A Maind, pela classe do horário comercial (`ARQ-071`); nunca acorda ninguém. O que o owner recebe é a A-22 |
| **O que não faz** | Não corta nada (`D-062`, `D-114`) |

### 3.13 O orçamento de operação da v2.0 (`ARQ-085` 🟡)

| Item | Plano recomendado | Por mês 🔎 | Decisão |
| --- | --- | --- | --- |
| VPS de hoje | O plano de 8 vCPU e 32 GB do provedor de hoje, no contrato longo, com a v1.xx, a homologação da v2 e a v2.0 da construção (`ARQ-065`) | R$ 120 a 260 | `ARQ-055`, `ARQ-056` |
| Cópia da instância SaaS | Fora do Horus, na infra da instância: a semanal do provedor das VPS, no plano, ou a diária, à parte (V-09) | De nada a R$ 62 | `ARQ-086` |
| Nuvem da produção real | A Google Cloud: o GKE regional e o Cloud SQL Enterprise com alta disponibilidade, em São Paulo, já com a cópia do Postgres (V-19), a partir da primeira produção real | US$ 767 sob demanda (R$ 4.214); US$ 634 com o compromisso de um ano (R$ 3.482) | `ARQ-085`, `ARQ-093` |
| Sonda | Um plano com conferência a cada minuto, duas regiões, sinais de vida e relatório mensal (V-12) | US$ 40 a 60 | `ARQ-070` |
| E-mail | O Pro de 100 mil do serviço de hoje (V-02), a partir da primeira produção real; até lá, o gratuito | US$ 35 | `ARQ-046` |
| CI | Os executores hospedados, no plano do GitHub da Maind (V-16), a partir da primeira produção real; até lá, o executor na VPS de hoje | US$ 75 a 225 | `ARQ-082` |
| Bateria com modelo real | Por marco, autorizada a cada rodada | US$ 33 a 45 por comparação, fora do mês | `ARQ-081` |
| Plantão | A forma com o jurídico (V-17) | R$ 6.200 a 20.000 | `ARQ-071` |
| **Total sem o plantão** | | **R$ 5.160 a 6.300** com a nuvem sob demanda; R$ 4.430 a 5.570 com o compromisso; fora os impostos do faturamento | |
| **Total com o plantão** | | **R$ 11.360 a 26.300** | |

A faixa se revê a cada trimestre contra as faturas, e qualquer item que passe do dobro do previsto volta ao dono.

**Até a primeira produção real**, nenhuma instância precisa do plantão nem da sonda de fora (`ARQ-056`: todas as instâncias de hoje são de teste, pelo dono, em 03/11/2026). O CI roda na VPS de hoje (`ARQ-082`), o e-mail fica no plano gratuito (`ARQ-046`), e o mês fica na máquina e na cópia, de R$ 120 a 330 🔎.

**Na primeira produção real**, a PRD sai da VPS e vai para um Kubernetes gerenciado, com o Postgres gerenciado da mesma nuvem (`ARQ-092` ✅, `ARQ-093` ✅). A V-19 comparou a mesma forma nas três nuvens, em São Paulo: 3 nós de 2 vCPU e 8 GB, um por zona; o Postgres 17 de 2 vCPU e 8 GB com a espera noutra zona, 100 GB e as cópias de 7 dias; a entrada HTTPS, o NAT e 100 GB de saída. Por mês 🔎, pela PTAX de R$ 5,4935:

| Nuvem | Sob demanda | Com o compromisso de um ano | O que pesa |
| --- | --- | --- | --- |
| **Google Cloud** (o GKE regional e o Cloud SQL Enterprise HA) | US$ 767 (R$ 4.214) | US$ 634 (R$ 3.482) | A operação mais simples, com o balanceador, o certificado e o NAT integrados; no modo Autopilot, por volta de US$ 711; a saída mais cara, sem franquia |
| **AWS** (o EKS e o RDS Multi-AZ) | US$ 890 (R$ 4.890) | US$ 642 (R$ 3.528) | Mais peças para operar no cluster; o NAT a US$ 81 por mês |
| **Azure** (o AKS Standard e o Flexible Server) | US$ 891 (R$ 4.897) | US$ 623 (R$ 3.424) | A espera do Postgres noutra zona está bloqueada para servidores novos em Brazil South, e não cumpre a `ARQ-093` hoje |

As três dão 99,95% no plano de controle e têm o Postgres 17. Os números não têm os impostos do faturamento no Brasil. Fontes, consultadas em 03/11/2026: cloud.google.com/kubernetes-engine/pricing e cloud.google.com/sql/pricing; os arquivos de preço da AWS para sa-east-1 (EKS, EC2, RDS, ELB e NAT); a API de preços da Azure para brazilsouth (prices.azure.com) e a tabela de regiões do Flexible Server (learn.microsoft.com/azure/postgresql/flexible-server/overview); a PTAX do Banco Central. O dono adiou a escolha para a primeira produção real, com a regra de não ficar preso à nuvem (`ARQ-096` ✅): a proposta (`ARQ-085` 🟡) continua a Google Cloud, mas a entrada e o certificado passam a ser do cluster em qualquer nuvem, e o compromisso de um ano só entra com a decisão do dono. A VPS de hoje continua no orçamento, com a construção e as instâncias de teste.

### 3.14 Os componentes

| Componente | Módulo | Responsabilidade | Situação |
| --- | --- | --- | --- |
| Registro do consumo de IA | Dados e IA | Grava cada chamada, com a função, o canal e o agente; estima e marca a que veio sem custo | 🔧 `horus@318db52b:apps/server/Horus.Api/GravadorDeConsumoDeIa.cs` |
| Tabela de preços | Dados e IA | O preço público de cada modelo: o catálogo do OpenRouter e a tabela do Bedrock | 🔧 `CatalogoOpenRouter.cs`; 🆕 a tabela do Bedrock |
| Registro das mensagens da Meta | Fundação | A categoria e o desfecho de cada mensagem, por conta | 🆕 (`ARQ-048`) |
| Conferência do mês | Dados e IA | Compara o registro com a conta do provedor | 🔧 o resumo da conexão de hoje |
| Medidas do custo | Fundação | O custo do dia por organização e componente, para o aviso (`ARQ-072`) | 🆕 |
| Orçamento e rateio | Fora do produto | As faturas do mês, da Maind, sem rateio | 🆕 (`ARQ-084`, `ARQ-085`) |

## 4. O que vem da v1.xx e o que não vem

| Peça da v1.xx | Destino | Por quê |
| --- | --- | --- |
| O custo gravado por chamada, com o valor do provedor | ♻️ Fica | `ARQ-017` |
| O custo nulo quando o provedor não informa, e o Bedrock sempre nulo | 🔧 Vira a estimativa marcada | `ARQ-083` |
| O painel do provedor e o Broadcast como medida do custo | 🔧 Ficam como conferência; a medida é o registro do Horus | `ARQ-017`, `ARQ-069` |
| O Cost Explorer no resumo da conexão | ♻️ Fica, com o cache de seis horas | `ARQ-083` |
| O cache de prompt por organização | ♻️ Fica: é o que deixa o Planejador perto dos US$ 0,06 por pergunta | `ARQ-031` |
| O consumo sem prazo | 🔧 Passa a 25 meses | `ARQ-035` ✅ |
| A falta de medida do WhatsApp, do e-mail e da infraestrutura por organização | ❌ Sai | `ARQ-017`, `ARQ-084` |

## 5. Os riscos e o que falta decidir

| Risco | Por quê | O que se faz |
| --- | --- | --- |
| 🤖 **Os agentes custam mais que a conversa** | Cada execução faz várias perguntas inteiras, e o produto não tem teto de custo | O teto técnico por execução (`ARQ-030`), o sinal da execução (`ARQ-084`) e o modelo do agente escolhido pelo owner (`D-061`) |
| 📈 **Os preços dos modelos mudam** | O OpenRouter e os fabricantes mudam a tabela, e um modelo novo pode custar o dobro | O custo é o que o provedor informa na chamada; a tabela se atualiza a cada pacote; a conferência do mês pega a diferença |
| 📱 **A Meta muda a tabela** | Quatro atualizações em 2026, e a cobrança da utilidade dentro da janela desde 01/10/2026 | A tabela reconferida no M4 (V-04); o registro por categoria (3.3) |
| 🏷️ **O aviso do agente vira marketing** | A categoria é da Meta | Cerca de US$ 560 a mais por mês no envelope; a A-19 |
| 🧑‍🚒 **O plantão pesa no primeiro cliente** | É fixo e não cresce com o uso | As alavancas de 3.10; a V-17 |
| 💱 **O câmbio** | Quase todo custo variável é em dólar, e o cartão internacional paga imposto | A conferência do mês em reais; a cobrança da Meta em reais desde 01/07/2026 |
| 🔎 **O envelope é hipótese** | Os volumes saem de exemplos do produto (`ARQ-016`) | O custo por unidade (por pergunta, por execução, por mensagem) vale qualquer que seja o volume; a V-15 dá o primeiro número real |
| 🌍 **O Bedrock em São Paulo não guarda o dado no país** | Os modelos Claude só têm o endpoint global ali | A A-16 e a V-18; o "tudo dentro" da v2.1 (`D-010`) para quem exige |

**O que falta decidir:**
- 🟡 Com o dono: `ARQ-085` (o orçamento de operação, com a forma do plantão).
- O impasse **A-03** (de quem é cada custo no SaaS), com o PO e o dono: este documento mostra que a IA é quase todo o custo variável.
- As verificações **V-15** (o custo real por função na PRD), **V-16** (o plano do GitHub), **V-17** (a forma do plantão) e **V-18** (os modelos do Bedrock que processam em São Paulo), além das que já estavam abertas e mexem no custo: V-02, V-07, V-09 e V-12.
