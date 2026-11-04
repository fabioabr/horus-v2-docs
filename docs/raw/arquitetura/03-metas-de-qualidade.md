# Metas de qualidade do Horus v2

Situação: 🟢 a medição do tempo decidida pelo arquiteto (`ARQ-013`) · ✅ a recuperação fora do Horus, decidida pelo dono (`ARQ-086`, que substituiu a `ARQ-015`), com o contrato da cópia (`ARQ-087` 🟢) · ✅ o envelope de volume do primeiro ano, decidido pelo dono (`ARQ-016`) · ✅ o custo por organização, no painel do owner da instância (`ARQ-017`) · 🟡 disponibilidade à espera do dono (`ARQ-014`).

Última atualização: 03/11/2026 (a recuperação fora do Horus, `ARQ-086` e `ARQ-087`; a homologação da v2 na VPS de hoje, `ARQ-055`; nenhuma instância é produção real, `ARQ-056`; o envelope do primeiro ano, `ARQ-016` ✅; o custo no painel do owner da instância, `ARQ-017` ✅; 99,9% na produção real, `ARQ-014` ✅; a produção real numa nuvem pública, `ARQ-092` ✅).

Este documento diz **quanto** o Horus v2 precisa aguentar e **como se sabe** que aguentou: disponibilidade, recuperação depois de uma pane, volume e crescimento, rapidez da resposta comparada ao pedido ao time de dados (`D-125`) e custo por organização. As decisões estão no [registro](02-registro-de-decisoes.md), e a estratégia, em [01-estrategia-da-solucao.md](01-estrategia-da-solucao.md). O código da v1.xx se cita como `horus@318db52b:<caminho>`; nada foi executado nesta rodada.

Legenda: 🟢 decidida pelo arquiteto · 🟡 proposta ao dono · 🔎 hipótese a confirmar.

## 1. O que o tema precisa garantir

| Meta | O que precisa garantir | Objetivos | Decisões de produto |
| --- | --- | --- | --- |
| 📶 **Disponibilidade** | A pergunta na reunião e o aviso agendado acontecem com o Horus no ar | O1, O4 | `D-016` (SaaS primeiro), `D-107` (cobra desde o primeiro cliente), `D-122` (o aviso na v2.0) |
| 💾 **Recuperação** | Nenhuma organização perde o que configurou, e o rastro não some numa pane | O2, O7 | `D-075` e a leitura `D-075.3` (tudo fica guardado), `D-092` e `D-093` (o rastro dura o prazo do owner e não se altera) |
| 📦 **Volume e crescimento** | A instância aguenta o primeiro ano sem redesenho, e se sabe quando trocar de máquina | O1, O3, O4, O7 | `D-008`, `D-009`, `D-117`, `D-123`, `D-133` |
| ⚡ **Rapidez** | A resposta chega muito mais rápido que o pedido ao time de dados, sem um número de segundos como meta do produto | O1, O6 | `D-125`, `D-126`, a leitura `D-098.3` (avisar que está trabalhando), `D-132`; `P-002` |
| 💸 **Custo por organização** | A Maind sabe quanto cada organização custa, por componente, antes da fatura | O6, O7 | `D-062`, `D-063`, `D-097`, `D-114`, `D-115`, `D-116` |

## 2. As decisões

| Meta | Valor | Situação | Decisão |
| --- | --- | --- | --- |
| Disponibilidade da PRD SaaS | 99,9% por mês, medida de fora da máquina | 🟡 | `ARQ-014` |
| Recuperação | A cópia é da infra de cada instância, que escolhe a meta; o Horus diz o que copiar e confere a volta | ✅, 🟢 | `ARQ-086`, `ARQ-087` |
| Volume | O envelope do primeiro ano (2.3), com folga de dez vezes no desenho | ✅ | `ARQ-016` |
| Rapidez | Medida por etapa, modo e canal; limiares internos de regressão; nenhum número vira promessa | 🟢 | `ARQ-013` |
| Custo | Medido por organização e componente; no painel do owner da instância; a Maind é avisada acima de um limiar; sem corte automático | ✅ | `ARQ-017` |

Sustentam as metas três decisões da estratégia: os dois papéis do executável (`ARQ-004`), a fila durável (`ARQ-005`) e o desenho fora da tela com concorrência limitada (`ARQ-007`).

### 2.1 Disponibilidade (`ARQ-014` ✅)

- **A meta:** a PRD SaaS fica no ar pelo menos **99,9% de cada mês**. Num mês de 30 dias, são no máximo 43 minutos fora; num de 31, 44 minutos. Para isso, a produção real roda numa nuvem pública, com Kubernetes ou algo do tipo, e a réplica e a troca vêm da plataforma (`ARQ-092` ✅).
- **Quando vale:** com a primeira produção real; hoje, nenhuma instância é produção real (o dono, em 03/11/2026, `ARQ-056`).
- **Como se mede:** uma sonda **de fora da máquina** chama a saúde da API a cada minuto, e "fora do ar" é a sonda falhar dois minutos seguidos (o mesmo critério do alerta de hoje). A publicação, que troca a versão em segundos, conta como tempo no ar se a sonda não a perceber.
- **O que fica fora da conta:** os serviços de fora (os provedores de IA, a Meta, o servidor de e-mail e os bancos dos clientes). O Horus mede cada um à parte, e a resposta diz que o serviço falhou, e nunca finge responder.
- **A homologação** não tem meta. No on-premises (v2.1), a máquina é do contratante, e a meta é dele; o Horus entrega a sonda e a saúde.
- **Hoje:** não há meta escrita. Entre 31/08 e 10/09/2026, a PRD ficou no ar 93,1% do tempo por causa de um incidente de 15h30; sem ele, seriam 99,86% (`horus@318db52b:docs/produto/observabilidade/analise-metricas.html` §7). A sonda de hoje roda na mesma máquina, a cada 30 segundos (`horus@318db52b:infra/observabilidade/alloy/config.alloy`), e não enxerga a máquina caída.

### 2.2 Recuperação (`ARQ-086` ✅, `ARQ-087`)

- **A meta é de cada instância.** O Horus não faz a cópia de segurança e não fixa quanto dado uma instância pode perder nem em quanto tempo ela volta: cada dono de instância a configura na infraestrutura dele (`ARQ-086`, decisão do dono de 03/11/2026). Na instância SaaS, quem escolhe é a Maind, ao configurar a cópia.
- **O que o Horus garante:** o contrato da cópia, que diz o que copiar (o banco da aplicação; o anel de chaves do Data Protection, sem o qual as credenciais das fontes e as chaves de IA não abrem; o certificado do anel, à parte) e o que não copiar; e a conferência da volta: a cada subida, o anel precisa abrir o segredo de prova do banco, ou o "pronto" falha (`ARQ-087`).
- **O que fica fora do contrato:** as bases de demonstração, que se refazem pelos geradores determinísticos de `horus@318db52b:data/`.
- **A volta numa máquina nova** usa o provisionamento automatizado (`horus@318db52b:infra/vps/provisionar-base.sh`), com o passo a passo no contrato (documento 10, 3.6).
- **Hoje:** não há rotina de cópia de segurança. O `pg_dump` só aparece no clone da PRD para o HML, na cópia de uma organização e como passo manual antes de um deploy, e do SQL Server há só duas cópias avulsas, de 30/08 (`horus@318db52b:docs/superpowers/plans/anexos/2026-10-27-inventario-vps-maind.md` §6).

### 2.3 Volume e crescimento (`ARQ-016` ✅)

O envelope é hipótese do arquiteto 🔎, a confirmar com o comercial da Maind. A conta parte dos exemplos que o próprio produto usa.

| Grandeza | Primeiro ano | Como se chegou | O desenho aguenta |
| --- | --- | --- | --- |
| Organizações | 30 | De 3 a 6 clientes, com 5 a 10 setores cada; cada setor é uma organização (`D-009`, `D-123`) | 300 |
| Pessoas com assento | 2.000 | Cerca de 65 por organização, abaixo do exemplo da `D-117` (1 owner, 30 membros full e 100 leitores) | 20.000 |
| Pessoas que perguntam | 500 | Owner, gestor e membro full, um quarto dos assentos | 5.000 |
| Perguntas de análise por dia útil | 3.000 | Seis por pessoa que pergunta. O exemplo da `D-133` (1.200 por mês numa organização, cerca de 55 por dia útil) dá 1.650 em 30 organizações; o envelope quase dobra isso | 30.000 |
| Respostas ao mesmo tempo, no pico | 15 | Um quinto das perguntas na hora mais cheia (600 por hora, ou 10 por minuto), cada resposta levando de 30 segundos a 2 minutos | 150 |
| Execuções de agente por dia | 1.000 | Duas por pessoa que pergunta; metade cai na primeira hora de segunda-feira | 10.000 |
| PDFs e imagens por dia | 2.000 | Os PDFs dos agendamentos e as imagens das respostas pelo WhatsApp | 20.000 |
| Mensagens de WhatsApp por dia | 1.500 | Um quinto das perguntas vindo pelo WhatsApp, com as respostas, mais os avisos dos agentes | 15.000 |
| Banco da aplicação | De 15 a 40 GB por ano | 3.000 respostas por dia útil, de 20 a 50 KB cada (texto, blocos e SQL), mais o consumo, os eventos de uso e o rastro | 400 GB |
| Registros do rastro por dia | 10.000 | Cinco aberturas de board por pessoa com assento, mais as entregas | 100.000 |

- **Como o desenho aguenta dez vezes:** trocando a máquina por uma maior e separando os papéis "atender" e "trabalhar" (`ARQ-004`), sem mudar código. Acima de dez vezes, o documento 09 decide a próxima forma.
- **Hoje, muito abaixo do envelope:** em 25/09/2026, a PRD tinha 14 usuários e 12 organizações; entre 31/08 e 10/09, houve 41 mensagens de chat, no máximo uma requisição ao mesmo tempo, CPU no máximo em 26,4% e memória entre 19% e 21% (`horus@318db52b:docs/superpowers/specs/2026-09-25-ambientes-hml-e-prd-design.md` §1; `horus@318db52b:docs/produto/observabilidade/analise-metricas.html`). O banco da aplicação tinha 59 MB em 27/10/2026.
- **A máquina de hoje:** 8 vCPU, 31 GB de memória, 387 GB de disco (47 GB usados) e **sem swap**, com a PRD, o HML, o Postgres, o SQL Server das bases de demonstração (cerca de 13,8 GB, sem limite de memória) e a observabilidade (`horus@318db52b:docs/superpowers/plans/anexos/2026-10-27-inventario-vps-maind.md` §1, §2 e §6).

### 2.4 Rapidez (`ARQ-013` 🟢)

A promessa "em segundos" é uma **comparação** com o pedido ao time de dados, que às vezes leva dias (`D-125`), e a definição da candidata nº 1 exclui "um número de segundos como meta do produto" (`D-126`). Por isso o que se segue são **medidas e alarmes internos**, para achar regressão, e não metas a anunciar.

**O que se mede, em toda resposta:**

| Medida | Por modo | Por canal | Por etapa |
| --- | --- | --- | --- |
| Primeiro sinal de progresso (o primeiro evento de etapa) | Dados, web, conversa e Análise avançada | App, Pergunta rápida, WhatsApp e agente | — |
| Primeiro texto | Idem | Idem | — |
| Resposta completa | Idem | Idem | Triagem, Planejador, consulta ao banco do cliente, montagem e leitura pós-consulta |

**Os limiares internos (🔎 hipóteses, a calibrar com a primeira medição da `P-002`):**

| O que | Limiar interno | Por quê |
| --- | --- | --- |
| Primeiro sinal de progresso no app | Até 2 segundos no p95 | É o que diz à pessoa que o Horus começou, e não depende do modelo |
| Confirmação de recebimento no WhatsApp | Até 10 segundos no p95 | A leitura `D-098.3` pede avisar que está trabalhando quando a resposta demora |
| Primeiro texto e resposta completa, por modo | Alarme quando o p95 da semana passar 1,5 vez o p95 de referência | Regressão, e não promessa; a referência é a primeira medição da `P-002` |
| Começo da rodada de um agendamento | Até 10 minutos depois do horário marcado, inclusive no pico de segunda de manhã | A fila espalha o pico; passar disso é fila atrasada |

**A comparação da `D-125`:** o tempo da resposta completa, por modo, é o lado do Horus. O outro lado, quanto leva o pedido ao time de dados, vem de cada cliente, e a conta se faz fora do produto, com a Maind (`D-132` e a leitura `D-132.1`).

**A medição da `P-002`:** no M0, sobre as bases de demonstração. Com o modelo falso, mede-se o tempo do próprio Horus (a montagem, a consulta e a materialização) sem custo. O tempo com modelo real só se mede com a autorização do dono e o custo declarado antes.

**Hoje:** a v1.xx mede o tempo até o primeiro token. Nas 41 respostas medidas na PRD entre 31/08 e 10/09/2026, nenhuma chegou em até 5 segundos, 12,3% chegaram de 5 a 10, 60% de 10 a 30 e **27,6% passaram de 30 segundos**, e a média por hora chegou a 96 segundos (`horus@318db52b:docs/produto/observabilidade/analise-metricas.html` §4 e §6). O histograma para nos 30 segundos (`horus@318db52b:apps/server/Horus.Api/Telemetria.cs`), então o p95 do painel fica preso no teto, e o alerta "Endpoint lento" exclui a rota das mensagens (`horus@318db52b:infra/observabilidade/grafana/provisioning/alerting/regras.yml`). As outras rotas da API respondem com mediana de 19 milissegundos.

### 2.5 Custo por organização (`ARQ-017` ✅)

| Componente | Como se mede | Onde nasce o número | Quem paga hoje |
| --- | --- | --- | --- |
| IA | Tokens e custo por chamada, por função, por conversa e por agente | O custo que o provedor informa por chamada, gravado em `ConsumosDeIa` (`horus@318db52b:apps/server/Horus.Api/GravadorDeConsumoDeIa.cs`); o gasto do mês da conta, pelo resumo da conexão (créditos no OpenRouter, Cost Explorer no Bedrock) | A conta da chave de cada conexão de IA da organização; de quem é essa conta no SaaS foi ao PO (A-03 do documento 01) |
| WhatsApp | Mensagens, pela categoria que a Meta cobra | O registro de cada mensagem enviada e recebida | A conta da organização, ou a da Maind quando a organização a autoriza (`D-097`) |
| E-mail | Mensagens enviadas | O envio da instância | A Maind |
| Infraestrutura | A máquina, o banco, a guarda das cópias e a observabilidade | A fatura do provedor, rateada por assento ativo | A Maind |

- **O aviso à Maind** 🔎: quando o custo do mês de uma organização passar do limiar ajustado para ela, ou quando o custo de uma semana passar o dobro da média das quatro anteriores (o sinal de um agente em laço). Os valores iniciais e o rateio ficam para o documento 13, e o alerta, para o 11.
- **Sem corte automático:** o limite de custo ficou fora do produto (`D-062`, `D-114`). O owner controla pelo modelo que escolhe e pela aprovação de criar agentes (`D-061`, `D-062`).
- **Hoje:** o custo de IA é gravado por chamada desde 29/09/2026, com o valor que o provedor informa (nulo se ele não informar), e não por tabela de preço. O painel do OpenRouter mostra 60% das chamadas como "sem-org" e cerca de 85% de consumo que não passou pela API de produção (`horus@318db52b:docs/produto/observabilidade/analise-metricas.html` §5 e §7); por isso a medida da v2 parte do registro do próprio Horus. A única medida de custo por pergunta que existe cobre só o Planejador: cerca de US$ 0,05 por pergunta (`horus@318db52b:docs/superpowers/specs/2026-09-17-filtro-perdido-na-janela-design.md`). Não há teto de custo no código.

## 3. Os componentes e a responsabilidade de cada um

| Componente | Responsabilidade | Meta que sustenta | Na v1.xx |
| --- | --- | --- | --- |
| Sonda externa | Testa de fora da máquina, a cada minuto, se o Horus responde | Disponibilidade | Não existe; a sonda é interna |
| Saúde da API | Diz se a API e o banco estão de pé; passa a dizer também se a fila anda | Disponibilidade | Existe, só com o banco (`horus@318db52b:apps/server/Horus.Api/Endpoints/HealthEndpoints.cs`) |
| Troca de versão com volta automática | Publica sem parada perceptível e volta sozinha se a saúde reprovar | Disponibilidade | Existe (`horus@318db52b:infra/redeploy.sh`) |
| Contrato da cópia e conferência da volta | O que a instância copia, e a subida que acusa o anel trocado | Recuperação | Não existe: na v1.xx, o anel trocado deixa a fonte como não configurada, sem aviso (`horus@318db52b:apps/server/Horus.Core/Data/Connections/CofreDeCredencial.cs`) |
| Provisionamento do zero | Sobe uma máquina nova pronta para receber a volta | Recuperação | Existe (`horus@318db52b:infra/vps/`) |
| Fila durável | Espalha o pico e não perde nem duplica trabalho | Volume; rapidez dos agendamentos | Não existe como peça geral; a fila de convites é o molde |
| Dois papéis | Separa a carga de quem espera da carga do que roda sozinho | Volume; rapidez | Não existe: o código supõe um processo só |
| Medidor de tempo por etapa | Mede o primeiro sinal, o primeiro texto e o fim, por modo, canal e etapa | Rapidez | Em parte: o primeiro token, com teto de 30 segundos |
| Registro de consumo e custo | Grava o custo de cada chamada de IA e de cada mensagem, por organização | Custo | Existe para a IA; não para o WhatsApp nem para a infraestrutura |
| Alertas da observabilidade | Avisam a Maind da API fora, da fila atrasada, do tempo que piorou e do custo acima do limiar | Todas | Em parte: cinco regras, sem o tempo do chat e sem custo |

## 4. O que vem da v1.xx e o que não vem

**Vem, como está:**
- A troca de versão por diretório, com até 24 tentativas de saúde em dois minutos e a volta automática, guardando os cinco últimos pontos de volta (`horus@318db52b:infra/redeploy.sh`).
- A retenção da observabilidade: métricas por 30 dias, logs por 14 e traces por 7; os eventos de uso por 400 dias (`horus@318db52b:apps/server/Horus.Core/Uso/RetencaoDeEventosDeUso.cs`).
- O registro do consumo de IA por chamada e por organização.
- Os tetos técnicos de hoje, que continuam até uma decisão dizer o contrário:

| Teto | Valor | Onde |
| --- | --- | --- |
| Linhas e tempo por consulta ao banco do cliente | 500 linhas e 30 segundos | `horus@318db52b:apps/server/Horus.Core/Data/Connections/IDataConnector.cs` |
| Documento semântico | 20.000 caracteres por fonte; 160.000 no total | `horus@318db52b:apps/server/Horus.Core/Data/Connections/ConnectionCatalog.cs`, `Chat/ChatEngine.cs` |
| Histórico enviado ao modelo | 60.000 caracteres | `horus@318db52b:apps/server/Horus.Core/Chat/ChatEngine.cs` |
| Pergunta | 12.000 caracteres | `horus@318db52b:apps/server/Horus.Api/Endpoints/ConversationEndpoints.cs` |
| Espera pelo modelo | 5 minutos (OpenRouter e Bedrock) | `horus@318db52b:apps/server/Horus.Api/Program.cs`, `Horus.Core/Llm/Bedrock/TetosDoBedrock.cs` |
| Mensagens por minuto | 20 por pessoa e 60 por organização | `horus@318db52b:apps/server/Horus.Api/Program.cs` |
| PDFs gerados ao mesmo tempo | 2 | `horus@318db52b:apps/server/Horus.Core/Relatorios/GeradorDePdfDeRelatorio.cs` |
| Espera do Nginx por uma resposta | 300 segundos | `horus@318db52b:infra/vps/provisionar-base.sh` |

**Não vem:**
- A suposição de um processo só, com filas e controles em memória.
- O teto de 30 segundos do histograma do primeiro token, e o alerta de lentidão que exclui a rota das mensagens.
- O painel do provedor como fonte do custo por organização: ele fica como conferência da conta, e a medida passa a ser o registro do Horus.
- A cópia de segurança como passo manual antes de todo deploy: ela fica só na publicação de corte, e a cópia de rotina é da infra de cada instância (documento 10).

## 5. Os riscos e o que falta decidir

| Risco | Por quê | O que se faz |
| --- | --- | --- |
| 💾 Hoje não há cópia de segurança | Uma pane da máquina leva o banco da aplicação e as chaves | A cópia é da infra de cada instância (`ARQ-086`): na SaaS, a Maind a configura no provedor das VPS; a falta dela no MVP foi ao PO (A-06 do documento 01) |
| 🖥️ Uma máquina para tudo | A PRD, o HML, os dois bancos e a observabilidade dividem a mesma VPS, sem swap; o SQL Server não tem limite de memória, e a PRD também não; na construção, a homologação da v2 entra nela (`ARQ-055`) | Sem teto: todas as instâncias dividem a máquina, porque nenhuma é produção real (`ARQ-056`); a swap segura o pico raro (documento 09) |
| 👀 A observabilidade vigia a máquina em que roda | Se a máquina cai, cai junto quem avisaria | A sonda de fora da máquina (`ARQ-014`); o fornecedor fica para o documento 11 |
| 📅 O pico de segunda de manhã | Metade das execuções de agente pode cair na mesma hora | A fila durável espalha o pico, e o limiar da rodada atrasada avisa (2.4) |
| 🔎 O envelope é hipótese | Os números saem de exemplos do produto, e não de uma previsão comercial | Reabrir a `ARQ-016` quando o comercial trouxer a previsão, ou quando o uso passar da metade do envelope |
| 🧮 O custo depende do provedor informar | Se o provedor não devolve o custo da chamada, o registro fica nulo | O documento 13 decide o que fazer com a chamada sem custo |
| ⚖️ A comparação da `D-125` depende do cliente | O tempo do pedido ao time de dados não está no Horus | A Maind faz a conta com cada cliente (`D-132`) |

**O que falta decidir:**
- 🟡 Com o dono: `ARQ-014`.
- No documento 09: onde roda cada papel e os limites de memória da PRD e do SQL Server.
- No documento 10: o contrato da cópia e a volta numa máquina nova.
- No documento 11: o fornecedor da sonda externa, o horário em que um alarme acorda alguém (hoje, o celular só é avisado das 10h às 17h) e o alerta de custo.
- No documento 13: os preços, o rateio da infraestrutura e os valores iniciais do aviso de custo.
- No M0: a medição da `P-002`, que calibra os limiares de 2.4.
