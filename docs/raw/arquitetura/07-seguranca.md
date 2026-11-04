# Segurança do Horus v2

Situação: 🟢 escrito pelo arquiteto · nove decisões novas (`ARQ-038` a `ARQ-045` e `ARQ-090`): cinco 🟢, três ✅ do dono (`ARQ-043`, `ARQ-044` e `ARQ-090`, em 03/11/2026) e uma 🟡 com o dono (`ARQ-040`, adiada para a v2.1) · o alcance do espaço da organização (A-11) entra como hipótese de trabalho · dois itens a devolver ao PO (A-15 e A-16, no [documento 01](01-estrategia-da-solucao.md), seção 9).

Última atualização: 03/11/2026 (o anel na cópia fora do Horus e o segredo de prova, `ARQ-086` e `ARQ-087`; os segredos da instância nos Secrets do GitHub, pela `ARQ-044` ✅; os boards e as claims de exemplo pelo semeador, `ARQ-011` ✅ e `ARQ-089`; a segurança dos dados por pessoa fora da v2.0, de volta na v2.1, pela `ARQ-090` ✅; a busca na web pela conexão, `ARQ-027` ✅; o aviso do registro da abertura num documento da organização, pela `ARQ-043` ✅; os segredos nos Secrets do Kubernetes, pela `ARQ-094`).

Este documento diz **quem entra, o que cada pessoa pode fazer e o que cada uma vê**: o login e a sessão, os papéis, as roles e o tipo de assento dentro do avaliador de permissões, a quarentena e o corte, a segurança dos dados por pessoa nas duas etapas da `MF-106:Segurança dos dados por pessoa`, a liberação de dados do gestor, em nome de quem cada coisa roda, a LGPD e os segredos. O que se guarda e por quanto tempo está no [documento 06](06-dados.md).

- O **quê** e o **porquê** são do produto ([backlog estratégico](../produto/backlog-estrategico.md), [a v2.0 consolidada](../produto/05-v2.0-consolidada.md)). As decisões (`ARQ-nnn`) estão no [registro](02-registro-de-decisoes.md).
- O código da v1.xx se cita como `horus@318db52b:<caminho>`. As regras de segurança do repositório lidas aqui são `horus@318db52b:.claude/rules/seguranca/motor.md`, `superficies.md`, `planilha.md` e `guarda-de-rede.md`. Nada foi executado, e nenhum modelo foi chamado.
- ⚠️ A `D-138` e a `D-139` vêm sempre com o título curto: `D-138` ("A v1.xx fecha como MVP no HML…") e `D-139` ("Tabela de conversão das mfs…").

Legenda: 🟢 decidida pelo arquiteto · 🟡 proposta ao dono · 🔎 hipótese a confirmar · ♻️ vem da v1.xx · 🔧 vem e muda · 🆕 novo.

## 1. O que o tema precisa garantir

| Garantia | Objetivos | Decisões de produto |
| --- | --- | --- |
| 🔑 **Só entra quem foi convidado**, como hoje, e a sessão se revoga | O7 | `D-071` (o convite do gestor, aprovado pelo owner), `D-108`, `D-118` (na v2.0, a pessoa entra como hoje) |
| 🎫 **O tipo de assento vem antes de tudo**, e sem assento livre a pessoa não entra | O7 | `D-069`, `D-070`, `D-074`, `D-114` |
| 👥 **O papel e a carteira decidem sobre quem se age**; quem não tem gestor espera na quarentena | O7 | `D-042`, `D-046`, `D-047`, `D-048`, `D-049`, `D-056`, `D-059` |
| 🎛️ **A role decide o que se usa**, botão a botão, pela soma | O7 | `D-110` a `D-114` |
| 🛡️ **Cada um vê só o que pode**, nas perguntas, em todo canal | O2 | `D-025`, `D-026`, `D-028`, `D-053` |
| 📤 **Só o gestor libera dados**, dentro do board e no artefato, e a responsabilidade é dele | O2, O3, O4 | `D-051`, `D-053`, `D-054`, `D-059` |
| ✂️ **No corte, ninguém usa e nada roda** | O7 | `D-068`, `D-075` |
| 🧾 **O rastro prova quem entregou o quê a quem**, e a pessoa sabe que a abertura é registrada | O2 | `D-090` e a leitura `D-090.2`, `D-091`, `D-093` |
| 🏛️ **Na v2.1, o login e a segurança da empresa valem**, com a regra mais restritiva | O8 | `D-025`, `D-026`, `D-027`, `D-052`, `D-118` |
| 🔒 **Os segredos não saem da instância e não ficam legíveis** | O2, O8 | `D-001`, `D-010`, `D-017` |

## 2. As decisões

| Decisão | O que decide | Situação |
| --- | --- | --- |
| `ARQ-008` | As permissões se calculam num ponto só do servidor, em três camadas | 🟢 |
| `ARQ-009` | O rastro é um registro só de acréscimo, fora da telemetria | 🟢 |
| `ARQ-032` | A segurança por pessoa entra no motor sem executor novo | 🟢 |
| **`ARQ-038`** | **O login e a sessão continuam os da v1.xx, e o login corporativo da v2.1 entra como mais um esquema externo, ligado por organização, na mesma sessão** | 🟢 |
| **`ARQ-039`** | **O avaliador lê quatro coisas, nesta ordem: o estado da organização e o tipo de assento, o papel e a carteira, as roles e, para os dados, o escopo; a quarentena e o corte são estados, e não exceções** | 🟢 |
| **`ARQ-040`** | **As claims ficam numa camada só, e a segurança dos dados por pessoa tem uma chave só por organização** | 🟡 adiada para a v2.1 |
| **`ARQ-090`** | **A segurança dos dados por pessoa sai do código da v2.0 e volta na v2.1, a partir do código da v1.xx; a guarda de rede e o ponto único de execução ficam** | ✅ |
| **`ARQ-041`** | **Em nome de quem cada coisa roda é uma lista fechada, decidida pela superfície: o escopo do autor só onde há liberação, e o acesso total só no board público da quarentena** | 🟢 (com a A-11 como hipótese) |
| **`ARQ-042`** | **A A14 da v1.xx e a liberação do gestor convivem pela regra do escopo único: cada board e cada artefato são calculados num escopo só, e liberar é mostrar esse escopo a quem recebe, com o registro no rastro** | 🟢 |
| **`ARQ-043`** | **O aviso de que a abertura é registrada fica num documento da organização, em PDF, que o owner publica e que fica sempre disponível para download no Horus** | ✅ |
| **`ARQ-044`** | **Os segredos da instância vêm dos Secrets de cada ambiente do GitHub, e o CD os grava no arquivo de ambiente da máquina; o anel de chaves é cifrado por certificado, com uma cópia no cofre da Maind; cada banco tem um login sem poder de dono** | ✅ |
| **`ARQ-045`** | **Cada dado pessoal tem dono, finalidade e prazo num inventário junto do código, e um teste reprova o dado novo sem eles** | 🟢 |

## 3. Os componentes e a responsabilidade de cada um

### 3.1 O login e a sessão (`ARQ-038`)

**Vem como está:**
- **A senha**, com o hash do ASP.NET Identity, e o **login com o Google**, pelo `sub` da conta (`horus@318db52b:apps/server/Horus.Core/Identity/IdentityEntities.cs`).
- **O cookie de sessão** `horus_sessao`, só HTTP, `SameSite=Lax`, de 14 dias que se renovam com o uso e com um teto absoluto de 30 dias desde o login, **revogável**: a conta guarda a geração das sessões, e trocar a senha ou "sair de todos" derruba todo cookie anterior na requisição seguinte (`horus@318db52b:apps/server/Horus.Api/Program.cs`, o achado C-07).
- **O cadastro fechado**: só cria conta quem tem convite para o próprio e-mail (por senha ou pelo Google), a instalação vazia (o primeiro administrador) e, por configuração, o cadastro aberto (`horus@318db52b:apps/server/Horus.Core/Identity/PortaDeCadastro.cs`). O convite segue o caminho da `D-071`: o gestor cria, o owner aprova, e a aprovação envia o e-mail e reserva o assento.
- **O papel relido a cada pedido**: tirar o poder de alguém vale no ato (`horus@318db52b:apps/server/Horus.Core/Identity/OrgScope.cs`).
- **O administrador da instância** é outra pergunta, fora da organização: ele configura a instância e não lê dado de organização nenhuma sem ser membro dela (`horus@318db52b:apps/server/Horus.Api/Endpoints/AdminEndpoints.cs`). O rastro de uma organização é só do owner dela (`D-091`, leitura `D-091.1`).

**O que é novo na v2.0:**
- **O WhatsApp identifica pela ligação do número**: a pessoa liga o número ao perfil no app e o confirma com o código que o Horus manda pelo WhatsApp (`D-094`); a mensagem que chega é da pessoa ligada àquele número, e o turno roda no escopo dela. O número é uma credencial: um número liga-se a uma pessoa só, e sair da organização ou perder o assento o desliga (leituras `D-094.2` e `D-094.3`). O detalhe da porta da Meta é do documento 08.
- **O "pode?" de quem trabalha sozinho**: o agendamento e o agente rodam "como quem criou", com as permissões e as claims lidas na hora (`D-060`; a agenda de hoje já lê as claims "agora", `horus@318db52b:apps/server/Horus.Core/Relatorios/EntregaDeRelatorio.cs`).

**Na v2.1, o login corporativo** (`D-027`, `D-118`): o owner liga, na organização dele, o login da empresa, e quem entra por ele cai **na mesma sessão** do Horus, com a mesma revogação. As roles chegam pelo mapeamento dos campos do token que o owner configura (`D-052`) e se gravam no cadastro a cada entrada; quem chega sem valor mapeado cai na role padrão (leitura `D-112.4`). Como uma pessoa pode estar em várias organizações e só algumas terem o login da empresa, entrar numa organização com login corporativo pede que a sessão tenha nascido por ele. O protocolo (OpenID Connect, que o ASP.NET Core já traz, ou outro que o cliente exija) se decide no documento 08, antes do M8.

### 3.2 O avaliador por dentro: papel, tipo de assento, roles e dados (`ARQ-008`, `ARQ-039`)

O avaliador de permissões é a porta única do "pode?" (`ARQ-008`). Por dentro, ele lê **quatro coisas, nesta ordem**, e a primeira que nega encerra a conta:

| Ordem | O que lê | O que decide | Decisões |
| --- | --- | --- | --- |
| 1 | **O estado da organização e o tipo de assento** | Assentos cortados: ninguém da organização usa nada e o que roda sozinho para. O tipo de assento é o teto: o membro leitor só vê boards de outras pessoas e recebe artefatos; não pergunta, não cria, não liga número | `D-068`, `D-069`, `D-075`, `D-079`, `D-089`, `D-114` |
| 2 | **O papel e a carteira** | Sobre quem a pessoa age: o owner sobre todos; o gestor sobre os que gere (abrir e desabilitar os boards deles, agendar para eles, montar grupos só com eles); o membro só sobre si. Quem não tem gestor está na **quarentena**: só o perfil e os boards públicos | `D-042`, `D-044`, `D-046`, `D-047`, `D-048`, `D-049`, `D-056`, `D-059` |
| 3 | **As roles** | O que a pessoa usa: os nove botões, pela soma, com a role padrão para quem não tem outra; o owner não depende de roles | `D-110` a `D-114`; os botões do WhatsApp e dos conectores pela `D-119` e pela `D-122` |
| 4 | **O escopo dos dados** | O que a pessoa vê em cada fonte, pela segurança dos dados por pessoa (3.3), e em nome de quem cada superfície roda (3.4) | `D-025`, `D-026`, `D-028`, `D-053`, `D-054` |

- **A quarentena e o corte são estados**, guardados no vínculo e na organização, que o avaliador lê na ordem 1 e 2. Nenhuma rota trata "está na quarentena?" por conta própria.
- **O papel aceita uma combinação só**: owner e gestor ao mesmo tempo (`D-048`), num assento só, o de owner (`D-074`). A organização aceita mais de um owner, como a v1.xx já aceita: ela recusa tirar o último (`horus@318db52b:apps/server/Horus.Core/Identity/OrgStore.cs`, `UltimoOwner`).
- **As permissões efetivas** (os botões ligados, o nível máximo, os modos, o tipo de assento e o estado) se calculam por pedido, para a tela e para o motor, como o papel de hoje; nada se guarda entre pedidos.
- **A falha fecha**: ação sem botão registrado, terceira camada sem registro ou leitura que falha respondem "não pode", nunca "pode" (documento 04, seção 5).
- **A matriz de hoje vira a primeira tabela** do avaliador: as 23 ações por papel (`horus@318db52b:apps/server/Horus.Core/Identity/PermissoesDaOrg.cs`) passam a ser a leitura 2, e o que nelas é botão da conversa passa às roles.

### 3.3 A segurança dos dados por pessoa (`MF-106`, as duas etapas)

⏭️ **Vai para a v2.1** (`ARQ-090` ✅, decisão do dono em 03/11/2026): a segurança dos dados por pessoa sai do código da v2.0, e o que vem abaixo descreve como ela volta na v2.1. Na v2.0, toda consulta roda com os dados da organização inteira, e ficam só a guarda de rede, o ponto único de execução e o cofre das credenciais.

**Etapa 1, na v2.0: a Semântica de Segurança da v1.xx, inteira** (`ARQ-032`). O owner escreve, por base, o documento de segurança; o compilador o transforma em regras, que o owner aprova; para quem tem acesso restrito, a consulta roda protegida, com as claims só como parâmetro, pelo ponto único de execução; toda falha fecha; as travas que leem o IL provam que nada chega ao banco do cliente por fora; a conferência diária roda sem modelo; o "ver como" e a caixa de revisão ficam como estão (`horus@318db52b:.claude/rules/seguranca/motor.md`, `superficies.md`). É a quarta leitura do avaliador.

**As duas camadas de claims** (pendência do documento 01). Pela leitura do código, a v1.xx tem duas chaves que, juntas, ligam a segurança por pessoa numa organização (`horus@318db52b:apps/server/Horus.Core/Seguranca/Motor/AvaliadorDeEscopo.cs`, a ordem "Semântica na organização → acesso por claims → versão vigente → quem executa"):

| Camada | O que é | Chave | Desde |
| --- | --- | --- | --- |
| **O acesso por claims** | O esqueleto das claims da organização e os valores de cada pessoa; também a régua de "quem abre" o painel corporativo, por uma condição sobre claims | `Orgs.AcessoPorClaimsAtivo`, do owner | 05/10/2026 (`horus@318db52b:apps/server/Horus.Core/Migrations/20261005163007_AcessoADadosPorClaims.cs`) |
| **A Semântica de Segurança** | As regras por base, compiladas do documento de segurança, e o motor | O interruptor geral da instância (o administrador: "permitida") **e** a bandeira da organização (o owner) | 10/10/2026 |

A decisão `ARQ-040` 🟡 propõe ao dono **uma camada de claims e uma chave por organização**: os valores de claim continuam num lugar só, lidos por um leitor só (o de hoje, com a simulação), e servem às regras e aos grupos dinâmicos (`D-019`); a régua de "quem abre" por condição sobre claims sai, porque a v2.0 publica pelas quatro visibilidades (`D-042`), e o "Quem abre" dos boards de exemplo vira, no semeador, um grupo dinâmico da organização (`ARQ-089`, A-14); o interruptor geral da instância continua com o administrador.

**Etapa 2, na v2.1: a segurança corporativa** (M8; `D-025`, `D-026`, `D-027`, `D-052`):
- **As claims e as roles do token**: o login corporativo (3.1) traz as claims e as roles, que o leitor de claims passa a espelhar ao lado das fixas, dadas pelo owner (a v1.xx já prevê: "o espelhamento do JWT entra com o SSO", `horus@318db52b:apps/server/Horus.Core/Seguranca/ClaimsEfetivas.cs`).
- **Os controles das tecnologias de dados**: a consulta passa a rodar, onde a tecnologia permite, com a identidade da pessoa na fonte, e a regra do Horus vai por cima. A "mais restritiva" (`D-026`) sai sozinha: a fonte só devolve o que a empresa deixa, e o Horus ainda filtra.
- ⚠️ **O que a etapa 2 complica**, para o M8: a execução deixa de se dividir entre pessoas com as mesmas claims (a chave do histórico ganha a identidade); a liberação do gestor (`D-054`) passa a pedir que a consulta rode com a identidade dele na fonte, o que exige delegação pelo login da empresa; e explicar a quem pergunta por que um dado não aparece passa a ter duas origens (a letra (d) da `P-008`, documento 14).

### 3.4 Em nome de quem (`ARQ-041`)

⏭️ **Na v2.0, sem a segurança por pessoa** (`ARQ-090` ✅), o em nome de quem decide as permissões, e o escopo dos dados é sempre o da organização inteira; o escopo por pessoa, descrito abaixo, volta na v2.1.

**A hipótese de trabalho da A-11** (o alcance do espaço da organização, letra (o) da `P-008`), explícita, é a recomendação que o documento 01 já registra: **o board do espaço da organização roda no escopo de quem o abre**, porque o owner não é dono de dados (`D-048`) e a liberação é do gestor (`D-054`); **os agendamentos e os agentes que vão para o espaço da organização ficam pausados** até a transferência e depois rodam em nome de quem os recebeu (`D-060`, `D-073`). A `ARQ-041` a completa com duas regras que ela não cobria, e que foram ao PO (A-15): o board de quem não libera, aberto por quem o supervisiona, e o envio do owner que não é gestor.

A regra numa frase: **um board mostra o escopo do autor só quando há liberação** (o autor é gestor e quem abre está na visibilidade publicada); **em qualquer outro caso, mostra o escopo de quem abre**; **o acesso total só existe no board público da quarentena** (consequência da `D-048`: "segue a regra de hoje do corporativo").

| Superfície | Em nome de quem | De onde vem |
| --- | --- | --- |
| A conversa, o popup, o WhatsApp, o "Filtrar"; o SQL, o CSV e "continuar no chat" a partir de um cartão | **A pessoa** que pergunta | `D-053`, a fronteira do board da `D-058` |
| Board de um **gestor** (ou do owner que acumula o papel), aberto pelo autor ou por quem está na visibilidade publicada | **O autor**: é a liberação | `D-051`, `D-054` |
| Board de um gestor aberto pelo owner sem estar na visibilidade (o acesso de abrir da `D-042`) | Quem abre 🔎 | A-15 |
| Board de um **membro full**, aberto por ele, pelo gestor dele ou pelo owner | Quem abre 🔎 | A-15; só o gestor libera (`D-053`) |
| Board do **espaço da organização** (criado pelo owner ou herdado de quem saiu) | Quem abre 🔎 | A-11 |
| **Board público da quarentena** | **Acesso total** | Consequência da `D-048` |
| Agendamento ou agente de um **gestor** | **O criador**, lido na hora; o artefato que vai a outros é a liberação | `D-059`, `D-060` |
| Agendamento ou agente de um **membro full** | **O criador**, só para si | `D-059` |
| Agendamento ou agente do **owner que não é gestor** | **Cada destinatário**, no próprio escopo 🔎 | A-15; o owner entrega (`D-059`), mas não é dono de dados (`D-048`) |
| Agendamento ou agente **herdado**, no espaço da organização | Pausado; depois da transferência, quem o recebeu | `D-060`, `D-073` |
| O pré-aquecimento das consultas protegidas | O sistema, com as claims do autor, sem executar | ♻️ `horus@318db52b:apps/server/Horus.Core/Seguranca/Motor/EmNomeDe.cs`, `Sistema` |
| A conferência diária | Fora da lista: liga direto no ponto único, sem o avaliador | ♻️ `horus@318db52b:.claude/rules/seguranca/motor.md` |

**Por dentro**, a lista de hoje (`EmNomeDe`: a pessoa, o painel corporativo com acesso total, o sistema) vira cinco formas: **a pessoa**, **o autor que libera** (com o board ou o artefato de onde vem a liberação), **o criador do trabalho**, **o acesso total do board público** e **o sistema**. O "painel corporativo" sai. Um pedido ao motor sem forma declarada não compila, e a forma que o avaliador não conhece fica bloqueada, como hoje. O escopo de cada forma se lê na hora, nunca se guarda.

**A liberação termina quando o gestor sai.** A saída apaga os valores de claim dele, na mesma transação (`horus@318db52b:apps/server/Horus.Core/Identity/OrgStore.cs`, `RemoveMemberAsync`), e o escopo dele deixa de existir. O board publicado que vai para o espaço da organização continua publicado (`D-045`) e passa a mostrar o escopo de quem abre.

**O envio no escopo de cada destinatário** desenha um artefato por recorte de acesso, e não por pessoa: dois destinatários com as mesmas claims recebem o mesmo, como a execução de hoje já se divide entre quem tem os mesmos valores (`horus@318db52b:.claude/rules/seguranca/motor.md`, M8a). O contrato do artefato (`ARQ-022`) passa a aceitar vários, um por recorte, na mesma rodada.

### 3.5 A liberação do gestor e a A14 (`ARQ-042`)

⏭️ **Vai para a v2.1** (`ARQ-090` ✅, decisão do dono em 03/11/2026): a segurança dos dados por pessoa sai do código da v2.0, e o que vem abaixo descreve como ela volta na v2.1.

**A colisão.** A regra A14 da v1.xx diz que o conteúdo calculado com restrição não vai a painel corporativo nem a uma lista (`horus@318db52b:.claude/rules/seguranca/superficies.md`, "O cartão trazido e a A14"): o fixar e o repuxar num corporativo respondem 409, a promoção de um painel com cartão restrito é recusada, e a agenda de relatório do gestor restrito **pausa** ("o conteúdo calculado com restrição não vai para uma lista de e-mail", `horus@318db52b:apps/server/Horus.Core/Relatorios/EntregaDeRelatorio.cs`). A `D-054` e a `D-059` mandam o contrário para o gestor: o board publicado e o artefato enviado levam o que ele vê, por cima até das travas da empresa, e a responsabilidade é dele.

**Por que a A14 existia.** O painel corporativo da v1.xx roda com acesso total para quem o abre (`EmNomeDe.PainelCorporativo`). Um cartão calculado no escopo restrito de alguém, dentro dele, misturaria dois escopos no mesmo painel: o número restrito ao lado dos números da rede, e a prosa restrita sobrevivendo ao recálculo com acesso total. A lista de e-mail tinha o mesmo problema: um escopo restrito entregue a quem o gestor não escolheu como responsável.

**Como as duas convivem: a regra do escopo único.**
1. **Cada board e cada artefato são calculados num escopo só**, o que a 3.4 dá para aquela superfície e aquela pessoa. Todo cartão, todo texto, todo PDF e todo recálculo do board saem desse escopo.
2. **A conferência de procedência da v1.xx se generaliza.** Hoje ela compara o bloco gravado com o escopo de quem olha no painel pessoal, e a marca "calculado com restrição" barra o corporativo. Na v2.0, ela compara o bloco gravado com o escopo do board para quem olha: o bloco de outro escopo sai "em revisão" e é recalculado no escopo certo; o que não se recalcula sai "não disponível". Nunca se mostra o número de um escopo dentro de um board de outro.
3. **A A14 continua inteira no único lugar com acesso total**: o board público da quarentena. Marcar um board como público, com cartão de procedência restrita ou com a marca, é recusado até o cartão ser recalculado ou tirado, como a promoção de hoje.
4. **Liberar é mostrar o escopo do autor a quem recebe**, e só existe onde a 3.4 diz "o autor": o gestor que publica (`D-051`, `D-054`) e o gestor que agenda para outros (`D-059`). O membro full não publica (`D-042`) e agenda só para si (`D-059`): o conteúdo restrito dele nunca vai a outra pessoa, que é o que restava da A14 para ele.
5. **A agenda do gestor não pausa mais por restrição.** A pausa da A14 vira a regra de quem agenda para quem, no avaliador (`D-059`).
6. **Toda liberação grava no rastro, na mesma transação**: a publicação (quem, com que visibilidade, quando, `D-058`) e cada entrega de artefato por destino (`D-090`), com a marca de que houve liberação e o **recorte de acesso** do autor naquele cálculo (as claims que a consulta protegida cita, com os valores, como a faixa "Resposta limitada aos dados que você pode ver: regiao Sul." de hoje, §16 A104). É o que deixa o owner responder "quem recebeu o board de vendas com os dados do Sul?" (a prova de valor da `D-093`). O recorte fica no banco da aplicação, como hoje; nunca vai a log, trace nem métrica.
7. **A fronteira do board** (`D-058`): ver o SQL, baixar o CSV de um cartão e continuar no chat rodam no escopo de quem pede, pela operação "reexecutar" do motor, e o SQL segue o corte de hoje para quem tem restrição.
8. **A cópia da resposta reportada** (`ARQ-028`) só o owner lê (`D-014`), com o recorte de acesso de quem reportou.

### 3.6 A LGPD

A qualificação jurídica (quem é controlador, quem é operador, o contrato com cada cliente) é do jurídico da Maind. A arquitetura garante o que se segue.

**O que sai da instância, e para onde:**

| Destino | O que vai | Quando | Quem autoriza |
| --- | --- | --- | --- |
| Provedores de IA (OpenRouter, Amazon Bedrock) | A pergunta, o documento semântico, o SQL, o histórico até 60.000 caracteres e, na leitura depois da consulta, até 12.000 caracteres do resultado do banco do cliente; no agente, a prosa e os números dos blocos | Toda resposta com modelo | A organização, pela conexão de IA dela, no modo "com serviços externos autorizados" (`D-010`) |
| A busca na web | Só a pergunta (`ARQ-027` ✅) | Com a pesquisa ligada | A role (`D-110`) |
| A Meta (WhatsApp) | As mensagens, o texto da resposta e as imagens dos blocos | No canal e no conector de WhatsApp | O owner, que liga o canal (`D-097`, `D-099`) |
| O servidor de e-mail | Os convites, os avisos e os artefatos entregues por e-mail | Nos envios | A instância (o envio) e o owner (o conector, `D-034`) |
| O Google | O login | Quando a pessoa entra pelo Google | A pessoa |

⚠️ O resultado do banco do cliente que vai ao modelo na leitura depois da consulta pode conter dado pessoal da base do cliente (um nome de funcionário, um CPF numa tabela). É dado que sai do país quando o provedor está fora dele. O modo "tudo dentro" da v2.1 (`D-010`) é a resposta para quem não aceita isso; até lá, o contrato do cliente precisa dizer que esse trecho sai.

**O que a arquitetura garante:**
- **Minimização**: o Horus guarda os blocos, e não as linhas do cliente (`ARQ-033`); a telemetria nunca carrega conteúdo de conversa nem pessoa como rótulo; o rastro não guarda conteúdo (`D-090`); os valores de claim só viajam como parâmetro e nunca vão a SQL, log, trace nem métrica.
- **Finalidade e prazo**: cada dado pessoal tem dono, finalidade e prazo no **inventário dos dados** (`ARQ-045`), e a faxina aplica o prazo (`ARQ-035`, documento 06).
- **Segurança**: o isolamento entre organizações (`ARQ-010`, `ARQ-034`), a cifra dos segredos (3.7), a sessão revogável e o rastro.
- **Transparência**: o aviso de que a abertura é registrada (`ARQ-043` ✅); o aviso de privacidade da instância, que não existe hoje, foi ao PO (A-16).
- **Direitos do titular**: a pessoa vê e corrige o próprio perfil; a saída da organização apaga o vínculo, as claims, o número e os contatos (documento 06). O pedido de exclusão da própria conta não existe na v1.xx e foi ao PO (A-16), junto com a leitura das conversas dos membros pelo owner, que a v1.xx permite (`horus@318db52b:apps/server/Horus.Core/Identity/PermissoesDaOrg.cs`, `VerConversasDaOrg`, decisão do dono de 22/09/2026).
- **Incidente**: o que se faz e quem avisa (a organização, a ANPD) é do documento 10.

**O aviso de que a abertura é registrada** (leitura `D-090.2`, `ARQ-043` ✅): a decisão do dono, em 03/11/2026, é um documento da organização, em PDF, que o owner da organização publica e que fica sempre disponível para download no Horus; a frase do registro entra nele, e o board e o relatório não ganham linha nova. Onde o documento fica, o texto padrão e a ciência no primeiro acesso foram ao PO (A-30).

### 3.7 Os segredos e os privilégios (`ARQ-044` ✅)

| Segredo | Onde vive hoje | Na v2.0 |
| --- | --- | --- |
| **O anel de chaves do Data Protection**, que abre as credenciais das fontes, as chaves de IA, as credenciais do Bedrock, os tokens de convite e o selo das versões de segurança, cada um com o seu propósito (`horus@318db52b:apps/server/Horus.Core/Data/Connections/CofreDeCredencial.cs`, `Llm/CofreDeChaveDeProvider.cs`, `Identity/CofreDeConvite.cs`, `Llm/Bedrock/CofreDeCredencialDoBedrock.cs`, `Seguranca/Semantica/SeloDaVersao.cs`) | No diretório de dados, **sem cifra própria** (`horus@318db52b:apps/server/Horus.Api/Program.cs`, `PersistKeysToFileSystem` sem `ProtectKeysWith…`) | Cifrado por um certificado guardado fora do diretório de dados, que o CD instala a partir de um Secret do ambiente, com uma cópia no cofre da Maind, porque o GitHub não deixa ler um Secret de volta; o anel e o certificado se guardam separados, como pede o contrato da cópia (`ARQ-087`), e a cópia do diretório sozinha não abre nada; a cada subida, o anel precisa abrir o segredo de prova do banco (`ARQ-087`). Ganha um propósito novo: a credencial da conta da Meta de cada organização |
| **A configuração com segredos**: a cadeia do Postgres, o SMTP, o segredo do Google, as cadeias das bases de demonstração | `/etc/horus/api.env`, só do root (600), lido pelo systemd; a API roda como o usuário `horus` (`horus@318db52b:infra/vps/provisionar-base.sh`) | Os Secrets do Kubernetes da instância, gravados pelo CD a partir dos Secrets do ambiente de cada instância no GitHub, a cada publicação (`ARQ-044`, `ARQ-094`), mais a senha do certificado; no contratante, a TI dele os preenche; os segredos do login corporativo de cada organização (v2.1) ficam no cofre, por organização, e não no arquivo |
| **O login do banco da aplicação** | O dono do banco do container, que é superusuário | Um login sem privilégio de dono em cada banco, só com leitura e escrita nas tabelas: o do mestre e o de cada organização, este só no banco dela (`ARQ-010`); o das migrações, só no passo da publicação (`ARQ-036`); e o de provisionamento, que só cria banco e login (`ARQ-088`) |
| **As credenciais das fontes** | Cifradas no cofre; o Horus confere se são só de leitura (`D-001`) | Iguais |
| **Os segredos da publicação** (a chave SSH da VPS) | Nos ambientes do GitHub (`horus@318db52b:infra/github/`) | Iguais, ao lado dos segredos da instância, que passam a morar ali também; só o workflow de publicação, nos executores hospedados do GitHub, os alcança, e nunca o executor do CI na VPS (`ARQ-082`) |

- **Nenhum segredo no repositório**, como hoje (as credenciais vivem fora dele e fora do systemd, no arquivo de ambiente: `horus@318db52b:infra/vps/provisionar-base.sh`), e nenhum segredo em claro no banco. A v2.0 acrescenta ao CI uma varredura que reprova segredo escrito no repositório (documento 12).
- **A rotação**: o Data Protection troca a chave de trabalho a cada 90 dias e guarda as antigas para abrir o que já foi cifrado; o certificado, a senha do banco e o segredo do Google trocam pelo Secret do ambiente e por uma publicação nova (documento 10). Perder o anel ou o certificado é perder todas as credenciais das organizações: por isso o anel entra na cópia da instância (`ARQ-087`), e o certificado tem uma cópia no cofre da Maind.
- **A conta do GitHub guarda os segredos de todas as instâncias da Maind**: segundo fator e poucas pessoas com acesso de administrador ao repositório (`ARQ-066`) 🔎; a proteção dos ambientes (a restrição à `main` e a aprovação de outra pessoa) é a V-16.
- **A guarda de rede continua** (`horus@318db52b:.claude/rules/seguranca/guarda-de-rede.md`): a fonte da organização não alcança a rede interna, e a saída da guarda nunca vai ao `api.env` do HML nem da PRD.

### 3.8 Os componentes

| Componente | Módulo | Responsabilidade | Situação |
| --- | --- | --- | --- |
| Sessão e login | Plataforma | Senha, Google, cookie revogável, cadastro fechado; na v2.1, o login corporativo por organização | ♻️ `horus@318db52b:apps/server/Horus.Api/Sessao.cs`, `Horus.Core/Identity/` |
| Ligação do número de WhatsApp | Canais | Liga o número ao perfil com código e o desliga na saída | 🆕 (documento 08) |
| Avaliador de permissões | Plataforma | As quatro leituras, as permissões efetivas, a falha fechada | 🔧 `horus@318db52b:apps/server/Horus.Core/Identity/PermissoesDaOrg.cs` |
| Leitor de claims | Dados e IA | O único que lê os valores de claim, com a simulação do owner; na v2.1, espelha o token | ♻️ `horus@318db52b:apps/server/Horus.Core/Seguranca/LeitorDeClaimsComSimulacao.cs` |
| Avaliador de escopo | Dados e IA | O escopo de cada forma de "em nome de quem" em cada fonte | 🔧 `horus@318db52b:apps/server/Horus.Core/Seguranca/Motor/AvaliadorDeEscopo.cs`, `EmNomeDe.cs` |
| Motor da Semântica de Segurança | Dados e IA | O preparo protegido, o ponto único de execução, as travas, a conferência diária | ♻️ `horus@318db52b:apps/server/Horus.Core/Seguranca/Motor/` |
| Corte do que sai | Acompanhar e avisar | A conferência de procedência de cada cartão contra o escopo do board para quem olha | 🔧 `horus@318db52b:apps/server/Horus.Core/Seguranca/Superficies/CorteDoQueSai.cs` |
| Registro do rastro | Plataforma | A publicação, a liberação com o recorte, cada entrega e cada abertura | 🆕 (`ARQ-009`) |
| Cofre | Fundação | Cifra e abre os segredos de cada organização, um propósito por segredo | ♻️ ASP.NET Core Data Protection |
| Inventário dos dados | Fundação | Dono, categoria, finalidade e prazo de cada dado (`ARQ-045`) | 🆕 |

## 4. O que vem da v1.xx e o que não vem

| Peça da v1.xx | Destino | Por quê |
| --- | --- | --- |
| O login por senha e pelo Google, o cookie revogável e o cadastro fechado | ♻️ Ficam | `ARQ-038` |
| A matriz de 23 ações e três papéis fixos | 🔧 Vira a leitura do papel no avaliador; os botões da conversa vão às roles | `ARQ-039` |
| A Semântica de Segurança inteira, com as travas, a conferência diária, a simulação e a caixa de revisão | ♻️ Fica, como a quarta leitura do avaliador | `ARQ-032` |
| A chave "acesso por claims" e a bandeira da Semântica, separadas | 🔧 Viram uma chave por organização, se o dono aprovar | `ARQ-040` 🟡 |
| A régua de "quem abre" o painel corporativo por condição sobre claims | ❌ Sai: a publicação usa as quatro visibilidades, e a condição dos boards de exemplo vira um grupo dinâmico no semeador | `ARQ-040`, `ARQ-089`, A-14 |
| O "em nome de quem" com o painel corporativo de acesso total | 🔧 Vira a lista de cinco formas; o acesso total fica só no board público da quarentena | `ARQ-041` |
| A A14: o 409 no corporativo, a recusa da promoção e a pausa da agenda do gestor restrito | 🔧 A conferência de procedência vale em todo board; a recusa fica no board público; a pausa da agenda sai, pela `D-059` | `ARQ-042` |
| O recorte de acesso gravado com o selo (§16 A104) | ♻️ Fica, e vai também ao rastro da liberação | `ARQ-042` |
| A leitura das conversas de todos os membros pelo owner | ♻️ Fica como está até o PO decidir | A-16 |
| O anel de chaves sem cifra própria e o login do banco como superusuário | ❌ Saem | `ARQ-044` ✅ |
| A guarda de rede | ♻️ Fica | `horus@318db52b:.claude/rules/seguranca/guarda-de-rede.md` |

**A conferência das letras da `P-008` que este documento toca** (a resposta final é do documento 14):
- **(c)** O que a `MF-106` cobre da etapa 1: ✅ tudo — as claims, o documento de segurança compilado, o motor, a simulação e a revisão. Da etapa 2, nada (não há SSO nem identidade na fonte).
- **(e)** Os grupos generalizam o "Quem abre": ⚠️ viável com restrição — a condição sobre claims vira um grupo dinâmico da organização (`D-019`, `D-055`), e as pessoas escolhidas, "Pessoas específicas"; a combinação das duas numa visibilidade só é do PO (A-14).
- **(h)** O painel corporativo roda com acesso total e o pessoal no escopo do autor: ✅ confirmado (`horus@318db52b:apps/server/Horus.Core/Seguranca/Motor/EmNomeDe.cs`, `DoPainel`).
- **(k)** Acumular owner e gestor, e a organização dona de boards: ⚠️ viável com restrição — hoje cada pessoa tem um papel só e todo painel tem um criador; a combinação e o espaço da organização são novos (`ARQ-039`, `ARQ-041`).
- **(m)** O cadastro guarda o que as roles carregam: ⚠️ hoje não há roles no cadastro; elas nascem na v2.0; o mapeamento do token é da v2.1.
- **(o)** O alcance do espaço da organização e dos agendamentos do owner: ⚠️ viável, com a hipótese da 3.4 à espera do PO (A-11 e A-15).
- **(t)** Mais de um owner e os quatro tipos de assento: ✅ mais de um owner já existe; os tipos de assento são novos.
- **(w)** Registrar quem viu e quem entregou o quê sem conteúdo: ✅ viável, no banco da aplicação, fora da telemetria (`ARQ-009`).

## 5. Os riscos e o que falta decidir

| Risco | Por quê | O que se faz |
| --- | --- | --- |
| 🔐 Reescrever as travas do motor | O "em nome de quem" muda de três para cinco formas e os executores, de quatro para duas operações | As travas que leem o IL listam as formas novas, e a bateria do `Horus.Evals` roda antes de cada marco, sem modelo pago (documento 12) |
| 📉 Os boards de exemplo mudam de escopo | Na v1.xx, o painel corporativo mostra a rede inteira a quem o abre; no espaço da organização, cada um vê o seu escopo | O semeador grava os boards de exemplo no espaço da organização (`ARQ-089`), e o PO confirma o que a vitrine mostra (A-14) |
| 📨 O envio do owner em vários recortes custa mais | Um artefato por recorte de acesso, em vez de um só | O desenho fora da tela já tem concorrência limitada (`ARQ-007`); a hipótese espera o PO (A-15) |
| 🔑 Perder o certificado é perder o anel | O certificado passa a ser a chave das chaves | O certificado e o anel vão separados à cópia fora da máquina, e a volta é ensaiada (documento 10) |
| 📱 O número de WhatsApp é uma credencial | Quem tem o celular pergunta como a pessoa | O código na ligação, o desligamento na saída e, a decidir com o produto no documento 08, o desligamento no "sair de todos" |
| 🌍 O resultado do cliente vai ao modelo | Até 12.000 caracteres por leitura, a provedores fora do país | O contrato do cliente e o modo "tudo dentro" da v2.1 (`D-010`) |
| 🧑‍⚖️ A pessoa não sabe o que se guarda dela | Não há aviso de privacidade, e o owner lê as conversas | A-16 com o PO |
| 🔢 Sem segundo fator na v2.0 | A TI de um cliente pode exigir | A v2.1 traz o login da empresa, que tem o segundo fator dela (`D-118`) |

**O que falta decidir:**
- 🟡 Com o dono: `ARQ-040` (a chave única, adiada para a v2.1).
- Ao PO: A-11 (aqui como hipótese de trabalho), A-14 (os painéis corporativos de hoje), A-15 (o escopo onde não há liberação) e A-16 (a LGPD).
- Documento 08: o protocolo do login corporativo (v2.1) e o desligamento do número de WhatsApp.
- Documento 10: a rotação dos segredos, o incidente e a comunicação à ANPD.
- Documento 12: as travas do motor com as cinco formas, o teste de cada leitura do avaliador e o teste do escopo único em cada superfície.
