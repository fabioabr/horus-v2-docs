# Macro funcionalidades que o Horus já tem

Situação: 🔎 levantamento preliminar do **Horus de hoje, a v1.xx**: é a referência do que já existe e pode ser reaproveitado no Horus v2.xx (`D-134`). O arquiteto de soluções confere o que se reaproveita (`P-003`).

Última atualização: 05/11/2026 (as `MF-120` a `MF-123` entram na tabela de conversão).

Este documento responde: **o que o Horus já entrega hoje, em linguagem de valor**, e como isso se encaixa no [norte](02-norte-do-produto.md). Segue a `D-003`: o produto de hoje é o ponto de partida, não o limite. Ele não decide o que entra na v2.0; só mostra o terreno.


> Os caminhos de código e de documento citados aqui (`apps/…`, `docs/produto/horus-visao-geral.md`, `.backlog/` e outros) são do **repositório `horus`, a v1.xx**, e não da pasta da v2 (`D-140`).

## Como citar uma mf

“mf” é a abreviação de macro funcionalidade, adotada pelo dono. Cada mf tem **número fixo**, que nunca é reaproveitado, e se cita sempre assim: `MF-106:Segurança dos dados por pessoa` (número, dois-pontos e nome, sem espaço).

- Uma mf nova ganha o próximo número (hoje, `MF-124`).
- Se duas mfs se fundirem, a nova ganha número novo, e as antigas ficam marcadas como substituídas.
- **A numeração foi refeita duas vezes**: em 01/11/2026 (`D-100` a `D-102`), de `MF-01` a `MF-19`, em ordem de leitura; e em 02/11/2026 (`D-137` a `D-139`), **de `MF-101` a `MF-119`**, pela entrega em que a mf entra e pela importância para a fundação; e as mfs que nasceram em 05/11/2026 ganharam o número seguinte, da `MF-120` à `MF-123`. Os números anteriores só valem na [tabela de conversão](#tabela-de-conversão-da-numeração). Se uma conversa ou nota antiga cita `MF-005` ou `MF-13`, leia `MF-106:Segurança dos dados por pessoa`.

## Como este levantamento foi feito

- Leitura da `origin/main` (`c4ade983`, 31/10/2026): rotas do app, endpoints do servidor, `.backlog/` e as 75 specs de `docs/superpowers/specs`.
- Leitura do documento `docs/produto/horus-visao-geral.md` (29/09/2026) e dos registros de estado do projeto (até 28/10/2026).
- **Não executei o produto.** Onde digo “maduro”, falo do que o código e os registros mostram, e não de uma prova de uso.
- **Não conferi o que está na produção (PRD).** Os registros dizem que a PRD está em `1adeb7b6` (14/10/2026); o que veio depois está na main e no HML. Onde sei, indico.

Legenda: ✅ maduro · 🟡 existe em parte · 🧪 na main e no HML, ainda não na PRD.

## O mapa: 12 macro funcionalidades

Os números são os da nova numeração. A `MF-006` e a `MF-008`, substituídas, ficam com o número antigo, no fim da tabela.

| MF | O que entrega hoje | Situação | Problema do norte que atende |
| --- | --- | --- | --- |
| 💬 **MF-107:Perguntar aos dados em português** | Conversa de análise com várias fontes; três modos (dados, web, conversa); cinco níveis de inferência; “Análise avançada”; sugestões de próximas perguntas; ver o SQL; baixar o CSV e a imagem de um bloco da resposta (o PDF só existe no board; a v2.0 acrescenta a exportação da conversa em PDF ou HTML, `D-250`) | ✅ | nº 1, e nº 2 em parte |
| 🎨 **MF-108:Respostas visuais** | 15 variantes de gráfico, tabela, KPI, mapa de calor, chaveamento e fluxo (workflow); no máximo 2 blocos por resposta; tema dos gráficos por organização | ✅ | nº 1 (é o valor central da promessa) |
| 🔌 **MF-104:Conectar as fontes vivas** | SQL Server, PostgreSQL, Oracle, MongoDB e BigQuery respondem; Athena só conecta; páginas web; túnel SSH; idade mínima do dado; credencial conferida como somente leitura; modelo semântico por fonte | ✅ (Athena 🟡) | base de tudo |
| 🌐 **MF-109:A web como fonte** | Modo web lê as páginas cadastradas; a pesquisa web do compositor complementa a resposta | 🟡 | nº 1 (lacunas 5 e 6 do inventário) |
| 🤖 **MF-105:IA sob controle da organização** | Conexões de IA (OpenRouter e Bedrock); modelo por função (quinze funções); modelo padrão obrigatório; curadoria; consumo e custo | ✅ | confiança e custo; lacuna 16 (IA dentro de casa) |
| 🛡️ **MF-106:Segurança dos dados por pessoa** | Regras de acesso por pessoa (claims), escritas em linguagem natural e compiladas por IA; reescrita e verificação da consulta; “ver como outra pessoa”; caixa de revisão; planilha de convites e claims; homologação de modelos | ✅ | prova da confiança (o norte não a nomeia) |
| 👥 **MF-102:Organizações, pessoas e papéis** | Várias organizações; owner, gestor e membro; convite nominal por e-mail, link e QR; entrar com Google; recuperar senha; foto de perfil | ✅ | `D-008`, `D-013` |
| 🏷️ **MF-101:Administração da instância** | Nome e logos, rodapé, administradores, envio de e-mail, interruptor geral da segurança | 🟡 | `D-011` (marca branca) |
| 🏠 **MF-117:Home da organização** | Painel com cerca de 60 indicadores de uso (consumo, erros, adoção, fontes), grade editável pelo owner | ✅ | comprador (e base possível da medida de autonomia) |
| 🧪 **MF-118:Bases de demonstração** | Rede de lojas fictícia em quatro bases, frota e DRE de usina | ✅ | apoio à venda |
| 📌 **MF-006:Acompanhar em boards** | Grade livre, páginas, apresentação em laço, cartões que se recalculam sozinhos, filtros, temas, boards pessoais e corporativos, análise customizada | ✅ hoje · ⚪ substituída pela MF-112 (`D-058`) | acompanhamento recorrente (adiado pelo norte) |
| 📄 **MF-008:Relatórios em PDF agendados** | Editor, PDF, agenda e envio por e-mail. O botão saiu do cabeçalho em 28/10/2026; a rota segue existindo | 🧪 hoje · ⚪ substituída pela MF-112 (`D-058`) | acompanhamento recorrente; único “empurrão” do produto |

Fora do mapa, por não serem funcionalidade para o cliente: a observabilidade (Grafana, Prometheus, Loki, Tempo), os roteiros de publicação e o design system.

## Tabela de conversão da numeração

As 23 mfs vivas, na **ordem de construção do Horus v2**: primeiro a entrega em que entram, depois a importância para a fundação (`D-137` a `D-139`, 02/11/2026). A coluna "01/11" traz a numeração anterior, em ordem de leitura (`D-100` a `D-102`), e a "Original", a primeira, de três dígitos começando com zero.

| Novo | Mf | 01/11 | Original | Camada |
| --- | --- | --- | --- | --- |
| `MF-101` | Administração da instância | `MF-16` | `MF-011` | 🧱 Plataforma |
| `MF-102` | Organizações, pessoas e papéis | `MF-14` | `MF-010` | 🧱 Plataforma |
| `MF-103` | Licenças e planos | `MF-17` | `MF-018` | 🧱 Plataforma |
| `MF-104` | Conectar as fontes vivas | `MF-06` | `MF-003` | 🔌 Dados e IA |
| `MF-105` | IA sob controle da organização | `MF-08` | `MF-009` | 🔌 Dados e IA |
| `MF-106` | Segurança dos dados por pessoa | `MF-13` | `MF-005` | 🔌 Dados e IA |
| `MF-107` | Perguntar aos dados em português | `MF-01` | `MF-001` | 💬 Motor de análise |
| `MF-108` | Respostas visuais | `MF-02` | `MF-002` | 💬 Motor de análise |
| `MF-109` | A web como fonte | `MF-07` | `MF-004` | 💬 Motor de análise |
| `MF-110` | Pergunta rápida | `MF-03` | `MF-017` | 📲 Canais |
| `MF-111` | Chat pelo WhatsApp | `MF-04` | `MF-021` | 📲 Canais |
| `MF-112` | Boards e Relatórios | `MF-09` | `MF-016` | 📌 Acompanhar e avisar |
| `MF-113` | Conectores de Saída | `MF-12` | `MF-014` | 📌 Acompanhar e avisar |
| `MF-114` | Módulo de Agendamentos de Agentes | `MF-11` | `MF-015` | 📌 Acompanhar e avisar |
| `MF-115` | Agentes ativos | `MF-10` | `MF-013` | 📌 Acompanhar e avisar |
| `MF-116` | Auditoria | `MF-15` | `MF-020` | 📈 Prova e controle |
| `MF-117` | Home da organização | `MF-18` | `MF-007` | 📈 Prova e controle |
| `MF-118` | Bases de demonstração | `MF-19` | `MF-012` | 📈 Prova e controle |
| `MF-119` | Investigação guiada | `MF-05` | `MF-019` | 🔵 v2.1 |
| `MF-120` | Faixa de avisos e números (nome provisório) | — | — | 📌 Acompanhar e avisar |
| `MF-121` | Middleware na casa do contratante (nome provisório) | — | — | 🔌 Dados e IA |
| `MF-122` | Conectores de chat corporativo (nome provisório) | — | — | 📌 Acompanhar e avisar |
| `MF-123` | Fonte AWS Athena (nome provisório) | — | — | 🔌 Dados e IA |

Duas mfs foram substituídas e **não ganharam número novo**; ficam só aqui, com o número original:

| Original | Mf | Situação |
| --- | --- | --- |
| `MF-006` | Acompanhar em boards | ⚪ Substituída pela `MF-112:Boards e Relatórios` (`D-058`) |
| `MF-008` | Relatórios em PDF agendados | ⚪ Substituída pela `MF-112:Boards e Relatórios` (`D-058`) |

## O que o dono já disse sobre cada mf (31/10/2026)

> Esta tabela guarda o que o dono disse em 31/10/2026. Decisões posteriores mudam alguns pontos (por exemplo, os cinco tipos de assento, `D-194`; o Teams e o Google Chat na `MF-122`, `D-198`; a liberação de dados do gestor na `MF-106`, `D-199`; o fim da área da organização que recebia o que a pessoa deixava e da transferência: quem é excluído perde o que criou, e quem passa a prata ou a bronze o mantém desabilitado, `D-206` a `D-209`; os modos, que passam a ser dois, dados e conversa, com a web como o interruptor "pesquisar na web", `D-215`). Vale o [backlog estratégico](backlog-estrategico.md).

| MF | Direção | Onde está registrado |
| --- | --- | --- |
| MF-110:Pergunta rápida (nova) | **A criar**: um botão flutuante de chat que abre um popup para a pessoa fazer a pergunta sem sair da tela em que está, para um uso mais dinâmico das perguntas. O popup abre a conversa de análise e não sabe em que tela a pessoa está (`D-085`). A conversa fica no popup, e a pessoa pode limpá-la e escolher salvar (`D-086`). A pergunta limpa sem salvar conta na medida de autonomia e recebe retorno como as outras (`D-087`). O popup traz tudo o que a conversa oferece (`D-088`). O membro leitor não vê o botão, e ele aparece em todas as telas, menos na própria conversa de análise (`D-089`). O nome e o número são proposta do PO | `D-065` e `D-085` a `D-089` (definição macro decidida na `D-089`; a `P-013` está fechada) |
| MF-111:Chat pelo WhatsApp (nova) | **A criar**: a pessoa conversa com o Horus pelo WhatsApp e vê o conteúdo da resposta como no chat. É uma via de entrada, diferente dos conectores de saída (MF-113). A própria pessoa liga o seu número ao perfil e o confirma com um código recebido no WhatsApp (`D-094`). Tudo o que a pessoa pergunta pelo WhatsApp entra no histórico do app e pode ser continuado lá (`D-095`). A resposta chega com texto, imagens e um link para abrir a resposta no app (`D-096`). Cada organização usa o seu próprio número de WhatsApp, e pode autorizar o uso do número da Maind (`D-097`). A pessoa tem tudo o que a conversa de análise oferece (`D-098`). Só o owner liga o canal, só quem pergunta conversa, e o canal fica bloqueado em “tudo dentro” (`D-099`). O nome e o número são proposta do PO | `D-084` e `D-094` a `D-098` (a necessidade decidida; definição macro decidida na `D-099`, `P-020` fechada) |
| MF-119:Investigação guiada (nova) | **A criar**: a pessoa vê que algo mudou e o Horus a leva, passo a passo, até o porquê. Atende ao problema nº 2 do norte, que não tinha nenhuma candidata. O nome e o número são proposta do PO; o desenho ainda não foi definido | `D-081` (a necessidade decidida; definição macro na `P-018`) |
| MF-112:Boards e Relatórios (nova; substitui a MF-006 e a MF-008) | **Uma mf só**: o editor de relatórios também desenha boards, e as duas viram uma coisa só com formatos de saída diferentes (todo board é vivo e pode ser impresso em PDF, de qualquer tamanho, `D-057`); qualquer pessoa cria, o owner e o gestor veem os boards de quem gerem e publicam na organização, se o owner permitir aos gestores; ao publicar, o gestor, dono dos dados, entrega a quem abre o que ele mesmo vê, mesmo sobre as travas do banco da empresa, só dentro do board, e a responsabilidade é dele (`D-051`, `D-053`, `D-054`); só o autor edita, e o owner e o gestor podem desabilitar o board, mas não alterá-lo; a organização tem um espaço próprio de boards, que o owner edita (`D-048`); se o autor é removido da organização, os boards dele vão para uma área da organização, com o mesmo status, onde o owner transfere a propriedade a qualquer pessoa da organização ou exclui | `D-018`, `D-042` a `D-048`, `D-051`, `D-053`, `D-054`, `D-057` e `D-058` (definição macro decidida na `D-058`; a `P-005` está fechada) |
| MF-115:Agentes ativos (nova) | **A criar**: o agente é o trabalhador que o agendamento chama; analisa dados e entrega artefatos e alertas pelos conectores de saída. Todo agente usa IA (`D-063`). O usuário o cria com instruções em texto (digitadas, coladas ou em arquivo .md) e escolhe o nível de inferência; o owner configura o modelo de IA que os executa (`D-061`) | `D-020`, `D-022` a `D-024`, `D-037`, `D-061` e `D-063` (definição macro decidida na `D-062`; a `P-007` está fechada) |
| MF-114:Módulo de Agendamentos de Agentes (nova) | **A criar**: um agendador único que decide quando rodar o que o usuário escolheu: **o PDF de um board ou relatório**, ou **um agente** (os dois no mesmo nível, `D-064`), e entrega o artefato (PDF, JSON…) a um ou mais conectores, para os destinos escolhidos. Todo agente usa IA (`D-063`). Cada pessoa agenda para si; para outras pessoas, só o gestor (as que ele gere) e o owner (`D-059`). O agendamento segue ativo, e no lugar da saída de um board desabilitado entra um texto avisando (`D-044`, `D-045`). O owner da organização liga ou desliga, tipo por tipo, a aprovação automática da criação de agendamentos (e dos dados de contato dos conectores). Hoje só existe a agenda dos relatórios em PDF (MF-008) | `D-036` a `D-039`, `D-059` e `D-064` (definição macro decidida na `D-060`; a `P-011` está fechada) |
| MF-113:Conectores de Saída (nova) | **A criar**: os conectores só transportam (e-mail, WhatsApp, Teams, Google Chat…) o que lhes entregam, e só a usuários do Horus; o formato (PDF, JSON…) é outra coisa, o artefato. Só o owner da organização liga os conectores; no modo “tudo dentro”, ficam bloqueados até o owner da instância liberar cada tipo. Hoje a única saída é o e-mail, dentro da MF-008 e da MF-101 (hipótese a confirmar pelo arquiteto) | `D-033` a `D-035` e `D-038` a `D-041` (definição macro decidida na `D-041`; a `P-010` está fechada) |
| MF-106:Segurança dos dados por pessoa | **A redesenhar em duas etapas**: primeiro o acesso configurado dentro do Horus; depois a segurança corporativa integrada (controles de acesso das tecnologias de dados e claims e papéis do token do IDP). *Desde 03/11/2026, as duas etapas ficam na v2.1 (`D-145`).* | `D-025` a `D-028` (definição macro decidida; a `P-004` está fechada), `D-145` |
| MF-102:Organizações, pessoas e papéis | **A melhorar**: grupos estáticos e dinâmicos, por claims e/ou papéis (na v2.0, os dinâmicos só por papel; por claims, na v2.1, `D-145`), usados para permissão de acesso a boards, receber relatórios, destino de alertas e outros usos; as funcionalidades do Horus (os três modos, os cinco níveis de inferência, a Análise avançada, a escolha do modelo de IA, ver o SQL, baixar CSV, imagem e PDF, e a Pergunta rápida) são liberadas ou limitadas pelo owner por meio de roles, botão a botão: vale a soma quando a pessoa tem mais de uma role; a organização nasce com uma role padrão, que vale só para quem não tem outra; uma role nova começa do zero ou como cópia de outra (`D-110` a `D-114`); as roles só o owner cria e que podem vir do login corporativo pelo mapeamento que o owner configura (`D-050`, `D-052`); os gestores criam grupos só com as pessoas que gerem (`D-049`), e o owner cria os grupos da organização, com qualquer pessoa (`D-055`); o owner não é gestor, mas vê todos os membros; o convite passa a ser da organização e pode indicar o gestor, e quem fica sem gestor espera numa quarentena (só acessa o perfil e os boards públicos da organização), de onde o owner ou um gestor o adiciona; o owner não é dono de board, a menos que acumule o papel de gestor; só o owner transfere membros entre gestores; para efeito de assento, o membro é full ou leitor (`D-069`); o gestor também cria convites, com a aprovação do owner (`D-071`) (definição macro decidida na `D-056`; a `P-012` está fechada; as funcionalidades por role foram definidas na `D-114`, e a `P-009` está fechada) | `D-019`, `D-029`, `D-030` e `D-031` (substituídas), `D-042` e `D-046` a `D-052`, `D-055`, `D-056` e `D-110` a `D-114` (definição macro decidida nas `D-032`, `D-056` e `D-114`; a `P-006`, a `P-009` e a `P-012` estão fechadas) |
| MF-116:Auditoria (nova) | **A criar**: o rastro de quem viu e de quem entregou o quê a quem, para comprovar a responsabilidade do gestor (`D-054`) e o que os agentes enviam por conectores. O nome e o número são proposta do PO; o rastro registra as entregas e quem as abriu, e não o conteúdo (`D-090`); só o owner da organização consulta o rastro (`D-091`) e define por quantos dias ele fica guardado (`D-092`); nem o owner altera ou apaga um registro (`D-093`) | `D-082` e `D-090` a `D-093` (definição macro decidida na `D-093`; a `P-019` está fechada) |
| MF-103:Licenças e planos (nova) | **A criar**: a cobrança por quantidade de usuários e por plano (por exemplo, Básico, Gold e Diamond). Os assentos são liberados e desativados pelo administrador do SaaS num painel de controle, só no modo SaaS (o on-premises fica para depois); não há data de expiração no produto, porque a validade é assunto comercial; e a permissão dos usuários é desabilitada quando os assentos são desativados. Os assentos têm quatro tipos: owner, gestor, membro full (pergunta, cria boards e alertas) e membro leitor (só vê boards de outras pessoas); cada organização traz um assento de owner grátis (`D-123`), e o cliente pode solicitar mais. Sem assento livre do tipo, a pessoa não entra até o administrador liberar mais. O gestor cria o convite e escolhe o tipo de assento; o owner aprova; a aprovação envia o e-mail e reserva o assento por N dias, e depois o convite expira e o assento volta a ficar livre. A troca do tipo de assento de quem já entrou segue o mesmo caminho: o gestor pede, o owner aprova, e precisa haver assento livre do tipo novo. Quando alguém passa de full a leitor, o que ela criou (boards, alertas e agendamentos) vai para a área da organização, como quando o autor sai. Quem acumula owner e gestor ocupa um assento só, o de owner. Quando o administrador desativa os assentos, os agendamentos, alertas e agentes da organização também param, e as configurações ficam guardadas. O painel não deixa reduzir os assentos de um tipo abaixo do que está ocupado; o owner libera antes. O owner pede mais assentos fora do produto, por contato comercial com a Maind. O owner define, nas preferências da organização, por quantos dias o assento fica reservado para um convite. O membro leitor também recebe alertas e PDFs pelos conectores. O nome e o número são proposta do PO; a v2.0 abre com um plano só, com todas as funcionalidades da v2.0 (`D-115`); o preço fica fora dos documentos de produto (`D-116`, `P-022`) | `D-066` a `D-080` (a necessidade decidida; definição macro decidida na `D-080`; a `P-014` está fechada; os planos na `P-015`, que já decidiu o plano único (`D-115`), o preço fora dos documentos (`D-116`) e confirmou a definição dos planos (`D-117`), com a `P-015` fechada; o on-premises na `P-016`) |
| As oito mfs que o dono não mencionou (ver `D-021`) | **Base herdada**: não passam pela pontuação; as lacunas delas seguem pelas candidatas à v2.0 | `D-021` |

## Os três problemas do norte contra o que existe

| Problema | O que o Horus tem | Situação |
| --- | --- | --- |
| ⚡ nº 1 · A pergunta de análise na hora | MF-107:Perguntar aos dados em português, MF-108:Respostas visuais, MF-104:Conectar as fontes vivas e MF-109:A web como fonte | ✅ a base está de pé; faltam retorno do usuário, web completa e a medida de autonomia (ver [inventário](03-inventario-de-lacunas.md)). *A velocidade deixou de ser lacuna em 02/11/2026: "em segundos" é comparação com o pedido ao time de dados (`D-125`)* |
| 🔍 nº 2 · A investigação | Só pela conversa: perguntas em sequência, sugestões, “Análise avançada” e os níveis explicativo e de hipótese | 🟡 não há um caminho guiado de “o que mudou e por quê” (a MF-119:Investigação guiada nasceu para preencher esta lacuna) |
| 🔔 nº 3 · O aviso | Nada que avise sem ninguém perguntar. O relatório agendado por e-mail (MF-008:Relatórios em PDF agendados) se aproxima, mas é acompanhamento recorrente | ❌ (a MF-115:Agentes ativos nasceu para preencher este vazio) |

## O que salta aos olhos

- ✅ **A base é grande.** Dez das doze macro funcionalidades estão de pé. O problema nº 1 está quase todo coberto; o que falta são as lacunas do inventário.
- 🛡️ **A segurança por pessoa é um ativo que o norte não nomeia.** A MF-106:Segurança dos dados por pessoa sustenta a “prova da confiança” e é o que deixa o CEO ver tudo e o gestor ver só a área dele (e cada cliente ver só o dele, quando a organização é um cliente). Hipótese do PO: é essencial, e não lacuna.
- 📌 **O maior volume construído é o acompanhamento** (boards, Home, relatórios), e o norte o adiou. Isso não é um erro, mas a v2.0 precisa dizer o que faz com ele. *(Respondido em 02/11/2026: o dono trouxe o redesenho dos boards e relatórios, a `MF-112:Boards e Relatórios`, para a v2.0, `D-119`.)*
- 🔔 **O problema nº 3 está vazio.** É a maior distância entre o norte e o produto.
- 📈 **A Home já grava eventos de uso.** Hipótese, a confirmar com o arquiteto: essa base (MF-117:Home da organização) serve à medida de autonomia (candidata nº 4 à v2.0).
- ⚠️ **O documento `docs/produto/horus-visao-geral.md` está velho** (29/09/2026): diz que só o OpenRouter existe, e não cita a segurança por pessoa, os relatórios, o fluxo nem o Bedrock.

## Previsto e ainda não construído

O que os planos e o `.backlog/` já registram e ainda não existe:

- 🔌 **Athena responder perguntas** (hoje só conecta) e a **tela de redes privadas** da organização (plano de conexões em nuvem).
- 🧠 **Assistente de modelagem**: o chat ajudar a montar o modelo semântico da fonte (spec seguinte à da segurança). O dono deixou a melhoria do modelo semântico com o time de dados por enquanto (`D-083`).
- 🤖 **Outros provedores de IA** além do OpenRouter e do Bedrock.
- 🕐 **Filtro de período com hora**: construído, mas desligado até os testes.
- 🧱 **Board em container único** (task 045, em revisão) e **recalcular perguntando num cartão de outra pessoa** (task 026).
- 🚀 **Promoção para a produção** do que está só na main e no HML (decisão do dono: “ainda não”).

Nenhum item do `.backlog/` aberto é uma macro funcionalidade nova: são ajustes e correções.

## Próximo passo

Confirmar o mapa (`P-003`) e abrir as pendências de desenho no [backlog estratégico](backlog-estrategico.md), seção “Pendências e impasses”.
