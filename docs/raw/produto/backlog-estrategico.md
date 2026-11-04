# Backlog estratégico do Horus

Registro das decisões de produto: o que o Horus entrega, para quem e em que ordem. Mantido pela skill `product-owner-horus`.

Aqui entram decisões de **valor** (visão, público, macro funcionalidades, versões, preço, cortes). Tarefas e escolhas de **como construir** pertencem ao arquiteto de soluções e não são registradas neste arquivo.

Última atualização: 03/11/2026.

## Como ler e manter

- Uma decisão por entrada, com número fixo (`D-001`, `D-002`…). O número nunca é reaproveitado.
- **Não se reescreve decisão antiga.** Se mudou, cria-se uma nova entrada que a substitui; a antiga passa a `substituída por D-nnn`.
- Situações: 🟡 `proposta` (recomendada, aguardando o dono) · 🟢 `decidida` (confirmada pelo dono) · ⚪ `substituída` · 🔴 `revogada`.
- Hipótese não vira decisão sem validação com cliente ou confirmação do dono.
- Impasses e pendências também têm número fixo: `I-001`, `I-002`… para impasses e `P-001`, `P-002`… para pendências. O número nunca é reaproveitado. Ao fechar, o item sai de “Abertos” e vai para “Fechados”, com a data e a decisão que o fechou.
- **“Definição macro”** (nas pendências do PO) é preencher o formato da mf: quem ganha, que decisão passa a ser possível, prova de valor, retorno para o negócio, o que não inclui e do que depende. **Nunca é arquitetura.** O que for “como construir” vira pendência separada, com o arquiteto de soluções como responsável (ex.: `P-008`).
- **mf** é a abreviação de macro funcionalidade. Cada mf tem número fixo e se cita sempre como `MF-nnn:Nome` (ex.: `MF-106:Segurança dos dados por pessoa`). Os números e os nomes vêm do [mapa das mfs de hoje](04-macro-funcionalidades-de-hoje.md).
- **As versões foram renomeadas em 02/11/2026** (`D-135`): a primeira entrega do Horus v2 é a **v2.0**, e a segunda, a **v2.1**, com um terceiro número na versão completa (por exemplo, v2.1.0000). O que os documentos chamavam “V1”, “V2” e “V3” foi trocado, e o conteúdo das decisões não mudou.
- **Onde ficam os documentos** (`D-140`, `D-141`): na pasta da v2, que vai virar um repositório próprio. O produto fica em `docs/produto/` e a arquitetura em `docs/arquitetura/`; `docs/backlog/` fica reservada para as atividades, que o dono e um agilista definem depois da arquitetura (`D-142`); as skills ficam em `.claude/skills/`. Os caminhos de código citados nos documentos de produto são do repositório `horus`, a v1.xx.
- **Estes documentos definem o Horus v2.xx** (`D-134`). O Horus de hoje é a v1.xx: ponto de partida e fonte de reaproveitamento. O entregável é um mapa de objetivos e funcionalidades para iniciar o desenvolvimento de forma estruturada.
- **Este trabalho é só documentação.** O dono deixou claro (01/11/2026) que nada de desenvolvimento começa aqui. “Fechar a v2.0” quer dizer **fechar a definição da v2.0** nos documentos; construir é assunto de outro momento e do arquiteto de soluções.
- **A numeração das mfs foi refeita duas vezes.** Em 01/11/2026 (`D-100` a `D-102`), em ordem de leitura, de `MF-01` a `MF-19`. Em 02/11/2026 (`D-137` a `D-139`), pela entrega em que a mf entra e pela importância para a fundação do novo Horus: **de `MF-101` a `MF-119`**. A regra de número fixo vale a partir desta última, e a próxima mf nova é a `MF-120`. Os números anteriores (os de dois dígitos e os de três que começam com zero, `MF-001` a `MF-021`) só valem na tabela de conversão do mapa. Em todas as decisões, as citações de mf foram trocadas pelos números novos, e o conteúdo das decisões não mudou; as decisões das próprias renumerações (`D-100` a `D-102` e `D-137` a `D-139`) mantêm os números da época. A `MF-006` e a `MF-008`, substituídas, não ganharam número novo e aparecem com o número mais antigo.

## Pendências e impasses

Tudo o que está aberto, num lugar só. A skill **lista esta seção no início de toda conversa nova**.

- 🛑 **Impasse:** definição estratégica sem resolução (opções empatadas, discordância, norte contra realidade). **Nunca fica para depois**: resolve-se na conversa, uma pergunta por vez, antes de avançar para outro assunto.
- 🕓 **Pendência:** falta uma informação de fora da conversa (um dado, uma validação). Tem responsável e o que é preciso para fechar.

### Abertos

| Nº | Tipo | O que está aberto | Origem | Depende de | Desde |
| --- | --- | --- | --- | --- | --- |
| `P-002` | 🕓 Pendência | Confirmar o inventário de lacunas com o arquiteto de soluções e medir o tempo de resposta. *Com a `D-125`, a medição deixou de ser condição para escrever uma meta: “em segundos” é uma comparação com o pedido ao time de dados* | `D-003` | Arquiteto de soluções | 30/10/2026 |
| `P-003` | 🕓 Pendência | Confirmar o mapa das mfs de hoje e o que está previsto e não construído (levantado pelo PO em 31/10/2026). *Com a `D-134`, o mapa de hoje é a referência do que a v1.xx já tem; a parte do dono deixou de ser necessária (leitura confirmada em 02/11/2026), e fica a do arquiteto: o que da v1.xx se reaproveita* | Pedido do dono, 30/10/2026; `D-134` | Arquiteto de soluções | 30/10/2026 |
| `P-008` | 🕓 Pendência | **Para o arquiteto de soluções:** confirmar vinte e sete hipóteses técnicas levantadas pelo PO. (a) O editor de relatórios comporta o que o board faz hoje (`D-018`). (b) Os eventos de uso da MF-117:Home da organização servem à medida de autonomia ([mapa](04-macro-funcionalidades-de-hoje.md)). (c) O que a MF-106:Segurança dos dados por pessoa já cobre de cada etapa da `D-025` (documento semântico de segurança, claims de origem SSO, controles de acesso das tecnologias de dados). (d) Calcular e explicar o “vale a mais restritiva” quando as duas fontes de regra divergem (`D-026`). (e) Os grupos generalizam o “Quem abre” que o board corporativo já tem (`D-029`). (f) A saída por e-mail que existe hoje (o relatório agendado) serve de ponto de partida para os conectores de saída, e confirmar para quem esse relatório vai hoje, já que o conector só entrega a usuários do Horus (`D-033`, `D-035`). (g) A agenda que o relatório em PDF já tem hoje (MF-008) serve de base para o agendador único (`D-036`). (h) O painel corporativo ainda roda com acesso total e o pessoal, no escopo do autor, como no registro de 01/10/2026, o que decide quem pode publicar um board (`P-005`). (i) O que muda no código ao tirar do owner a edição do painel corporativo e criar o “desabilitar” (`D-043`). (j) O convite (nominal, por link e QR) e a planilha de convites comportam a indicação do gestor, e dá para ter uma área de quarentena para quem ainda não tem gestor (`D-047`). (k) Um mesmo usuário pode acumular os papéis de owner e de gestor, e a organização pode ser dona de boards num espaço próprio (`D-048`). (l) A matriz de permissões por papel que o código já tem comporta roles que o owner configura para liberar ou limitar funcionalidades (`D-050`), botão a botão (os sete interruptores da `D-110`), com a soma quando a pessoa tem mais de uma role (`D-111`), a role padrão para quem não tem outra, que o owner edita e não apaga (`D-112`), e a cópia de uma role ao criar outra (`D-113`). (m) O cadastro do usuário já guarda a informação que as roles e as claims do login corporativo carregam, e o owner consegue configurar o mapeamento dos campos do JWT para o cadastro (`D-052`); com a `D-118`, na v2.0 vale só a parte do cadastro, e o mapeamento do JWT fica para a etapa 2 da segurança. (n) Todo board, de qualquer tamanho, pode ser impresso em PDF a partir da mesma montagem (`D-057`). (o) Com que alcance de dados rodam os boards da organização e os agendamentos do owner, que não é dono de dados (`D-048`, `D-059`). (p) Renderizar gráficos em segundo plano, nos agentes, com as mesmas bibliotecas do front (`D-061`). (q) O ciclo de consultas e análise controlado pelo modelo, com um JSON final de instruções de renderização por tipo de saída do agendamento, é viável com a configuração de IA por função (`D-061`). (r) O motor de conversa responde de um popup, em qualquer tela do app (`D-065`), com todos os controles da conversa de análise (`D-088`). (s) O produto comporta guardar os assentos da organização, conferi-los contra as pessoas e desabilitar os usuários e pausar os agendamentos, alertas e agentes quando o administrador do SaaS desativa os assentos (`D-075`), liberados por um painel de controle da instância, no modo SaaS e sem data de expiração (`D-066` a `D-068`). (t) A organização comporta mais de um owner e os quatro tipos de assento: owner, gestor, membro full e membro leitor, este último só vendo boards de outras pessoas (`D-069`). (u) O gestor pode criar o convite (hoje o papel de gestor nasce sem a chave dos convites), com fluxo de aprovação do owner e reserva do assento por N dias, e o mesmo fluxo vale para trocar o tipo de assento de quem já entrou (`D-071`, `D-072`). (v) O motor de conversa decompõe uma variação nas partes que mais a explicam (por loja, produto, período) e guia a pessoa passo a passo (`D-081`). (w) O produto registra quem viu e quem entregou o quê sem guardar conteúdo de conversa, já que a telemetria hoje nunca carrega conteúdo (`D-082`). (x) O produto recebe a pergunta do WhatsApp, liga o número à pessoa e devolve a resposta com gráficos e tabelas em imagem (aproveitando a hipótese (p)), tanto pela conta de WhatsApp Business de cada organização quanto pela conta compartilhada da Maind, quando a organização a autoriza, e o custo do canal oficial do WhatsApp, incluindo as respostas demoradas da Análise avançada dentro das janelas de resposta (`D-084`, `D-097`, `D-098`); e as mensagens que o Horus inicia pelo conector de WhatsApp, os avisos e os PDFs, com os modelos aprovados e o custo próprio (`D-124`). (y) O produto conta a pergunta respondida sem guardar o conteúdo da conversa descartada na pergunta rápida, e guarda a resposta reportada até o owner analisá-la (`D-087`). (z) O produto tem, ou passa a ter, uma área de avisos dentro do Horus, na conta da pessoa, e uma preferência no perfil para receber esses avisos por e-mail, enviados pelo e-mail da instância (`D-128`). (aa) O motor de conversa consegue separar o fato vindo da web, que entra em qualquer nível de inferência com link e data, da causa vinda de fora dos dados, que só entra a partir do nível 4 (`D-130`) | `D-018`, `D-025`, `D-026`, `D-029`, `D-033`, `D-036`, `D-065` a `D-072`, `D-081`, `D-082`, `D-084`, `D-087`, `D-097`, `D-098`, `D-110` a `D-114`, `D-118`, `D-128`, `D-130` e mapa das mfs | Arquiteto de soluções | 31/10/2026 |
| `P-016` | 🕓 Pendência | Definir como ativar os assentos numa instalação **on-premises**, na infraestrutura do cliente (o arquivo com chave foi deixado de lado por ora). Até lá, o on-premises fica sem o controle de assentos | `D-067` | Dono, com o arquiteto de soluções para a viabilidade. Não trava a v2.0, que é SaaS primeiro (`D-016`). **Trava a v2.1**, porque o on-premises (a nº 5) entrou nela (`D-121`) | 31/10/2026 |
| `P-018` | 🕓 Pendência | Definição macro da **MF-119:Investigação guiada** (nova): quem ganha, que decisão passa a ser possível, prova de valor, retorno, o que não inclui e do que depende | `D-081` | Dono. **Adiada pelo dono em 01/11/2026**, porque pede muita conversa. Pode esperar: não trava as outras definições. Ponto de partida quando voltar: “por onde a pessoa começa a investigação na v2.0?” ficou sem resposta (A, pelo número ou gráfico que mudou, recomendada; B, pela pergunta em texto; C, pelo aviso de um agente). **Se a `MF-119` entrar na v2.0, a definição vira condição para fechar a v2.0** (`D-104`); com o alcance da v2.0 só no problema nº 1 (`D-106`), ela fica para a versão seguinte. **Com a `D-121`, a `MF-119` está na v2.1, e esta definição trava a v2.1** | 01/11/2026 |
| `P-022` | 🕓 Pendência | Definir o **preço em reais** do plano único, por tipo de assento. Precisa da visão de mercado, que segue em aberto para o PO, e do primeiro cliente | `D-116` | Dono e comercial da Maind, com a visão de mercado (o PO pode pesquisar o mercado se o dono pedir, opção C da `D-116`). **Pode esperar:** o preço fica fora dos documentos de produto e não trava a v2.0 | 02/11/2026 |

### Fechados

| Nº | O que era | Como fechou | Em |
| --- | --- | --- | --- |
| `P-023` | Definição macro das quatro candidatas essenciais do problema nº 1, que entraram na v2.0 sem definição no formato da mf | O dono decidiu que “em segundos” é comparação com o pedido ao time de dados (`D-125`), os motivos do reporte (`D-127`), o aviso de “recebido” a quem reporta (`D-128`), que o fato da web entra em qualquer nível (`D-130`) e que o saving se calcula fora do produto (`D-132`), e confirmou as quatro definições: nº 1 (`D-126`), nº 2 (`D-129`), nº 3 (`D-131`) e nº 4 (`D-133`) | 02/11/2026 |
| `P-024` | Quais conectores de saída entram na v2.0 | O dono escolheu a opção A: o e-mail e o WhatsApp (`D-124`) | 02/11/2026 |
| `I-013` | O assento de owner grátis é um por instalação (`D-069`) ou um por organização (`D-074`, `D-080`, `D-117`)? | O dono escolheu a opção A: um por organização (`D-123`) | 02/11/2026 |
| `I-014` | Como sai o PDF automático dos boards na v2.0, já que a `MF-112` depende da `MF-114` e da `MF-113`, que estavam fora | O dono trouxe para a v2.0 a `MF-115:Agentes ativos`, a `MF-114:Módulo de Agendamentos de Agentes` e a `MF-113:Conectores de Saída` (`D-122`): o PDF automático sai pelo agendador e pelos conectores da v2.0, com as regras novas | 02/11/2026 |
| `I-012` | Quais regras de board valem na v2.0, já que os boards “continuavam como hoje” (`D-105`) e a `MF-102` e a `MF-103` inteiras traziam regras de board | O dono trouxe a `MF-112:Boards e Relatórios` inteira para a v2.0, junto com a `MF-111:Chat pelo WhatsApp` e a `MF-116:Auditoria` (`D-119`): valem todas as regras de board | 02/11/2026 |
| `I-011` | O login corporativo está na v2.0? A `D-114` trazia a role pelo JWT, e a leitura da `D-108` e a `D-025` punham o login corporativo na etapa 2 da segurança, fora da v2.0 | O dono escolheu a opção A: o login corporativo fica fora da v2.0, a pessoa entra como hoje e o owner atribui as roles no cadastro (`D-118`) | 02/11/2026 |
| `P-015` | Definir os planos: quantos são, os nomes, o que cada um inclui e o preço | O dono decidiu que a v2.0 abre com um plano só, com todas as funcionalidades (`D-115`), e que o preço em reais fica fora dos documentos de produto (`D-116`; o valor virou a `P-022`), e confirmou a definição completa (`D-117`) | 02/11/2026 |
| `P-009` | Definir quais funcionalidades do Horus se ativam ou desativam por role (por exemplo, acesso à web, Análise avançada e escolha do modelo de IA no chat) e como as roles se combinam quando a pessoa tem mais de uma | O dono decidiu a lista de botões que o owner liga e desliga por role (`D-110`), que vale a soma quando a pessoa tem mais de uma role (`D-111`), que a organização nasce com uma role padrão para quem não tem outra (`D-112`) e que uma role nova começa do zero ou como cópia de outra (`D-113`), e confirmou a definição completa (`D-114`) | 02/11/2026 |
| `I-010` | O que da MF-102:Organizações, pessoas e papéis entra na v2.0, já que a `MF-103` depende de papéis, convites e quarentena? | O dono escolheu a opção C: a gestão de pessoas completa da `D-056` (carteira de gestor, quarentena, grupos e roles) entra na v2.0 (`D-108`). Isso fez a `P-009` deixar de poder esperar | 01/11/2026 |
| `I-009` | A v2.0 cobra por assentos (`MF-103:Licenças e planos`) desde o primeiro cliente? | O dono escolheu a opção B: a v2.0 inclui a `MF-103` inteira (`D-107`). Isso abriu o `I-010` e fez a `P-015` deixar de poder esperar | 01/11/2026 |
| `I-008` | Como pontuar a MF-119:Investigação guiada, que ainda não tem definição macro (`P-018`)? | O dono escolheu a opção B: pontuar já, com premissas do PO marcadas, e a nota é provisória; se a `MF-119` entrar na v2.0, a definição vira condição para fechar a v2.0 (`D-104`) | 01/11/2026 |
| `P-021` | Renumerar as mfs | O dono decidiu renumerar (`D-100`), que a nova numeração é uma sequência simples de 1 a 19 em ordem de leitura (`D-101`), e confirmou a tabela de conversão (`D-102`). O PO trocou as citações no backlog, no mapa (04), no inventário (03) e na skill | 01/11/2026 |
| `P-020` | Definição macro da MF-111:Chat pelo WhatsApp | O dono decidiu como a pessoa liga o número (`D-094`), que a conversa é a mesma do app (`D-095`), que a resposta traz texto, imagens e um link (`D-096`), que cada organização usa o seu número e pode autorizar o da Maind (`D-097`) e que a pessoa tem tudo o que a conversa oferece (`D-098`), e confirmou a definição completa (`D-099`) | 01/11/2026 |
| `P-019` | Definição macro da MF-116:Auditoria | O dono decidiu o que o rastro registra (`D-090`), que só o owner da organização o consulta (`D-091`) e que o owner define por quantos dias ele fica guardado (`D-092`), e confirmou a definição completa (`D-093`) | 01/11/2026 |
| `P-013` | Definição macro da MF-110:Pergunta rápida | O dono decidiu que o popup é um atalho para a conversa, independente da tela (`D-085`), que a conversa fica no popup e pode ser limpa e salva (`D-086`), que a pergunta conta na medida de autonomia salva ou não (`D-087`) e que o popup oferece tudo o que a conversa oferece (`D-088`), e confirmou a definição completa (`D-089`) | 01/11/2026 |
| `P-017` | Três possíveis candidatas à v2.0 que o PO apontou como lacunas do norte: a investigação guiada, a melhoria do modelo semântico e o rastro de auditoria | O dono incluiu a investigação guiada (`D-081`) e a auditoria (`D-082`) e deixou a melhoria do modelo semântico com o time de dados por enquanto (`D-083`). As definições macro das duas novas foram para a `P-018` e a `P-019` | 01/11/2026 |
| `P-014` | Definição macro da MF-103:Licenças e planos | O dono decidiu a cobrança por assentos e por plano, pelo painel, só no SaaS (`D-066` a `D-068`), os quatro tipos de assento e as regras de entrada, troca, contagem, corte e entrega (`D-069` a `D-079`), e confirmou a definição completa (`D-080`). Os planos foram para a `P-015` e o on-premises para a `P-016` | 01/11/2026 |
| `P-007` | Definição macro da MF-115:Agentes ativos | O dono decidiu como o agente é criado e roda (`D-061`) e que todo agente usa IA (`D-063`), e confirmou a definição completa (`D-062`). Os pontos de canais foram para a `P-010` | 31/10/2026 |
| `I-007` | Se todo agente usa IA (`D-063`), como sai o PDF agendado de um board, que não precisa interpretar nada? | O dono explicou que o agente e o PDF de um board estão no mesmo nível: o agendamento escolhe um ou outro (`D-064`) | 31/10/2026 |
| `P-011` | Definição macro da MF-114:Módulo de Agendamentos de Agentes | O dono decidiu a cadeia e o nome (`D-036`, `D-037`), a aprovação do owner (`D-038`, `D-039`), o efeito do board desabilitado (`D-044`, `D-045`) e quem entrega dados a outros (`D-059`), e confirmou a definição completa (`D-060`) | 31/10/2026 |
| `P-005` | Definição macro da mf única que une MF-006:Acompanhar em boards e MF-008:Relatórios em PDF agendados | O dono decidiu quem cria, vê, publica, edita e desabilita (`D-042` a `D-045`), o espaço da organização (`D-048`), a liberação de dados (`D-051`, `D-053`, `D-054`) e o formato do board (`D-057`), e confirmou a definição completa (`D-058`). A mf ganhou o número `MF-112`, e a MF-006 e a MF-008 ficam substituídas | 31/10/2026 |
| `P-012` | Definição da gestão de pessoas, dos grupos e das roles na MF-102:Organizações, pessoas e papéis | O dono decidiu a gestão por pessoa (`D-046`), a quarentena e o convite da organização (`D-047`, `D-048`), os grupos do gestor e da organização (`D-049`, `D-055`) e as roles (`D-050`, `D-052`), e confirmou a definição completa (`D-056`) | 31/10/2026 |
| `I-006` | A liberação de dados do gestor (`D-051`, `D-053`) vale também sobre as regras da empresa (banco, IDP), ou a `D-026` continua valendo por cima? | O dono escolheu a opção B: dentro do board, vale a permissão do gestor, e a responsabilidade é dele (`D-054`) | 31/10/2026 |
| `P-010` | Definição macro da MF-113:Conectores de Saída | O dono decidiu quem liga os conectores (`D-034`), que eles só transportam e só entregam a usuários do Horus (`D-035`), o interruptor de aprovação por tipo (`D-038`, `D-039`) e o encaixe com o “tudo dentro” (`D-040`), e confirmou a definição completa (`D-041`) | 31/10/2026 |
| `I-005` | Onde mora o agendamento (quando gerar um ou mais artefatos e enviá-los por um ou mais conectores)? | O dono escolheu a opção A: uma mf nova, só de agendamentos, a MF-114:Módulo de Agendamentos de Agentes (`D-036`) | 31/10/2026 |
| `P-006` | Definição macro dos grupos de pessoas, estáticos e dinâmicos (MF-102:Organizações, pessoas e papéis) | O dono decidiu os usos (`D-029`, `D-030`) e que só o owner da organização cria e edita os grupos (`D-031`), e confirmou a definição completa (`D-032`) | 31/10/2026 |
| `P-004` | Definição macro do redesenho da MF-106:Segurança dos dados por pessoa | O dono deu a direção (`D-025`), decidiu como as regras convivem (`D-026`) e onde se liga o IDP (`D-027`), e confirmou a definição completa (`D-028`) | 31/10/2026 |
| `I-004` | A interpretação que o usuário configura no agente fica dentro do nível de inferência que a organização autorizou (`D-001`)? | O dono escolheu a opção B: o usuário define o nível do agente livremente (`D-024`) | 31/10/2026 |
| `P-001` | Quantos chamados a área de dados atende hoje (ponto de partida do saving, `D-001`) | Dispensada pelo dono: é irrelevante agora, porque o número depende do cliente que usa o Horus. O ponto de partida será medido em cada cliente | 31/10/2026 |
| `I-003` | O Horus “só lê” (`D-001`), mas o agente ativo envia alertas a canais externos: como fica esse limite? | O dono escolheu a opção A: o “só lê” vale para as fontes, e o Horus pode enviar alertas (`D-022`) | 31/10/2026 |
| `I-002` | As oito mfs que o dono não mencionou (lista na `D-021`) ficam como base herdada ou entram na pontuação? | O dono escolheu a base herdada (`D-021`) | 31/10/2026 |
| `I-001` | Falta alguma mf na lista de candidatas à v2.0? | O dono respondeu que sim e acrescentou três: agentes ativos, mf única de boards e relatórios e grupos de pessoas (`D-018`, `D-019`, `D-020`) | 31/10/2026 |

## Decisões

Mais recente no topo. Formato de cada entrada:

```markdown
### D-000 · Título curto da decisão
Situação: proposta | decidida | substituída por D-nnn | revogada · Data: dd/mm/aaaa · Versão: v2.n ou “geral”

**Decisão:** uma frase.
**Contexto:** o problema e o objetivo da versão contra o qual foi pontuado.
**Opções avaliadas:** quadro com nota total de cada uma (as 3 melhores detalhadas com prós e contras; eliminadas com o motivo).
**Por que esta:** critério que decidiu e o que se abre mão.
**Fica de fora / adiado:** o que saiu e por quê.
**Hipóteses a validar:** o que ainda não é fato e como validar.
**Prova de valor:** sinal observável que mostrará se acertamos.
**Reabrir quando:** condição que justifica rever.
```

### D-139 · No MVP da v1.xx, as seis peças pela metade saem todas da tela
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v1.xx (MVP)

**Decisão:** as seis peças que hoje aparecem na tela e não funcionam até o fim **saem todas da tela** no MVP (`D-138`): a fonte AWS Athena; a fonte de páginas web; a dica do campo Rede que anuncia redes privadas; os três provedores de IA "em breve" (Anthropic, OpenAI e Gemini); as preferências "Tabela-gêmea sempre aberta" e "Animação ao desenhar"; o campo "Período" do cabeçalho do relatório.
**Contexto:** a `D-138` escolheu tirar da tela, em vez de terminar, o que está pela metade. Faltava saber se alguma peça era condição de uso de algum cliente.
**Opções avaliadas:** todas saem (recomendação do PO, escolhida) · alguma fica e é terminada no MVP (não escolhida).
**Por que esta:** nenhuma das seis funciona até o fim hoje, e terminá-las é trabalho da v2.0, não conserto.
**Fica de fora / adiado:** terminar qualquer uma delas. Saem da tela, ficam no código e voltam quando estiverem prontas.
**Hipóteses a validar:** 🔎 nenhuma organização do HML usa uma fonte Athena ou de páginas web.
**Prova de valor:** a rodada de uso no HML da `D-138` não encontra nenhuma das seis.
**Reabrir quando:** um cliente pedir uma delas como condição de uso.

### D-138 · A v1.xx fecha como MVP no HML: o que existe funciona bem, e o que está pela metade sai da tela
Situação: 🟢 decidida (o dono escolheu a opção A em 02/11/2026) · Data: 02/11/2026 · Versão: v1.xx (MVP)

**Decisão:** fechar o Horus de hoje (v1.xx) como MVP no HML com uma promessa só: *pergunte e receba a resposta certa, com a origem, sem nada na tela que prometa e não entregue*. Entram quatro frentes, nesta ordem: (1) a confiança da resposta; (2) a vitrine limpa, em que o que está pela metade na tela **sai da tela** em vez de ser terminado; (3) a segurança mínima de quem pergunta e de onde o Horus roda; (4) a operação que sustenta o HML. Nenhuma mf nova entra, e o que está desligado continua desligado.

**Contexto:** o dono quer entregar um MVP fazendo o que já existe funcionar bem. A auditoria de 02/11/2026 do código que roda no HML (`8bf62e4f`) levantou 80 pendências, sem contar o que está desligado de propósito (o filtro de período, o ajuste fino da aparência do painel, os alertas do HML). Como a v1.xx é a base herdada da v2.0 (`D-021`, `D-134`), cada conserto daqui também vale para a v2.0. Objetivo do MVP, suposto pelo PO (hipótese): um cliente usa a v1.xx no HML sem encontrar nada que prometa e não entregue e sem receber uma resposta que engane sobre a origem.

**Opções avaliadas** (pesos da `D-015`; notas de 0 a 5, quase todas hipótese do PO):

| Opção | Missão (25) | Tempo (25) | Confiança (20) | Retorno (15) | Aprendizado (5) | Alavancagem (10) | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A. Confiança e vitrine limpa | 4 | 4 | 5 | 3 | 4 | 3 | **79** |
| C. Só a vitrine limpa | 2 | 5 | 2 | 2 | 3 | 1 | 54 |
| B. Terminar tudo o que está pela metade | 3 | 1 | 3 | 3 | 2 | 4 | 51 |

- **A. Confiança e vitrine limpa.** Prós: cabe em semanas; ataca primeiro o que derruba a confiança. Contras: tira da tela o que já foi prometido (o Athena, a fonte de páginas web, os três provedores de IA "em breve", duas preferências da conta e o "Período" do relatório). Certa quando o objetivo é um cliente usando já.
- **C. Só a vitrine limpa.** Prós: o caminho mais curto. Contras: deixa no ar resposta que engana (o selo da web que diz ter pesquisado sem pesquisar) e as falhas de segurança de operação. Certa só para uma demonstração conduzida pela Maind.
- **B. Terminar tudo o que está pela metade.** Prós: produto mais completo; adianta peças da v2.0. Contras: meses de trabalho e mistura conserto com projeto novo (a reestruturação dos cartões, o Athena, as ondas de nuvem). Certa se não houvesse uma v2.0 em definição.

**Por que esta:** ganha ao mesmo tempo em tempo até o valor e em confiança, os dois critérios mais pesados depois da missão. Abre-se mão de entregar agora as peças que saem da tela.

**Fica de fora / adiado:** a reestruturação dos cartões (fatias 2 e 3) e os objetivos 2 e 3 da unificação dos boards; as conexões em nuvem além do BigQuery como está; a prova do Amazon Bedrock na AWS real e as medições do Planejador; as evoluções dos relatórios (cor do fundo, PDF guardado, nova tentativa); bases de demonstração novas; tudo o que está desligado. Vão ao arquiteto de soluções como insumo da v2.0.

**Hipóteses a validar:** 🔎 o objetivo do MVP acima; 🔎 que tirar da tela não fere quem já usa o HML (nenhuma organização com fonte Athena ou de páginas web).

**Prova de valor:** uma rodada de uso no HML, pelo dono ou por um cliente, sem encontrar tela que prometa e não entregue; nenhuma resposta com a origem errada; os testes rodando antes de cada publicação.

**Reabrir quando:** um cliente pedir uma das peças tiradas da tela como condição de uso, ou o desenvolvimento da v2.0 começar antes de o MVP fechar.

### D-145 · A MF-106 inteira na v2.1 e, na v2.0, a organização como fronteira dos dados
Situação: 🟢 decidida · Data: 03/11/2026 · Versão: v2.0 e v2.1

**Decisão:** a `MF-106:Segurança dos dados por pessoa`, nas duas etapas, vai inteira para a v2.1, e o código dela sai da v2.0 (`ARQ-090`, confirmada pelo dono em 03/11/2026). Na v2.0, **a organização é a fronteira dos dados**: quem pode perguntar alcança todas as fontes da sua organização, e quem precisar separar os dados de dois setores usa uma organização para cada um (`D-008`).

**Contexto:** o dono decidiu a `ARQ-090` com o arquiteto, para a v2.0 nascer sem encaixar a segurança por pessoa no modelo novo. O produto ainda não tinha absorvido a decisão: o arquiteto devolveu o assunto ao PO como o item A-28 da conferência (`docs/arquitetura/14-conferencia-do-produto.md`). Ao fazer a correção, o PO levou ao dono a consequência que muda a promessa da v2.0: sem o escopo dos dados, o Horus confere o assento, o papel e as roles (`ARQ-039`), e nada disso limita fontes.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. A organização é a fronteira** | Quem pode perguntar alcança todas as fontes da organização; a separação entre setores se faz com uma organização por setor. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: nada novo na v2.0, que é o que a `ARQ-090` buscou. Contra: “cada um vê só o que pode ver” vale só entre organizações até a v2.1. |
| B. Uma trava por fonte na v2.0 | O owner da organização escolhe, nas roles, quem usa cada fonte. | ⚪ Não escolhida. Contra: é uma peça nova na v2.0, que a `ARQ-090` quis enxugar, e repete o que a `MF-106` faz na v2.1. |

**Consequências:**
- **O objetivo da v2.0** (`D-136`) troca “cada um vê só o que pode ver” por “cada organização vê só os próprios dados”. O objetivo O2 (confiar no que vê) fica, na v2.0, com a `MF-116:Auditoria`; a `MF-106` o completa na v2.1.
- **A etapa 1 sai da v2.0** e vai para a v2.1, junto com a etapa 2: muda a `D-025`, a `D-028` e a `D-105` nesse ponto. A candidata nº 10 deixa a lista da v2.0, e a prova de valor da v2.0 perde o passo “o Marcos define quem vê quais dados”.
- **Os grupos dinâmicos** (`D-019`) são, na v2.0, só por papel; por claims, na v2.1.
- **A planilha da `MF-102:Organizações, pessoas e papéis`** serve, na v2.0, só aos convites em lote, sem as colunas de claims.
- **A liberação de dados do gestor no board** (`D-051`, `D-053`, `D-054`) não tem efeito na v2.0, porque todo board mostra os dados da organização inteira; ela volta a valer na v2.1. Na v2.0, a `MF-116:Auditoria` registra as publicações e quem as abriu, e as liberações entram no rastro na v2.1 (muda a `D-090`, a `D-093` e a leitura `D-119.2` nesse ponto).
- **O interruptor geral da segurança**, na `MF-101:Administração da instância`, vai para a v2.1 com a `MF-106`.
- **A demonstração da segurança por pessoa** fica fora até a v2.1.
- **As dependências da `MF-106`** na `MF-102`, na `MF-110:Pergunta rápida`, na `MF-111:Chat pelo WhatsApp`, na `MF-112:Boards e Relatórios`, na `MF-114:Módulo de Agendamentos de Agentes` e na `MF-115:Agentes ativos` caem na v2.0 e voltam na v2.1.
- **Fecha o item A-28** da conferência do arquiteto. A A-11, que discutia o alcance do board, perde a urgência pelo mesmo motivo.

**Hipóteses a validar:** 🔎 que o primeiro cliente aceite a v2.0 sem restrição por pessoa, separando com organizações o que precisar separar.

**Prova de valor:** nenhum cliente da v2.0 deixa de comprar por falta da restrição por pessoa.

**Reabrir quando:** um cliente da v2.0 precisar de dado restrito por pessoa antes da v2.1 (o mesmo gatilho da `ARQ-090`).

### D-144 · A documentação da v2 se divide em inventário (`docs/raw/`) e leitura (`docs/leitura/`)
Situação: 🟢 decidida · Data: 03/11/2026 · Versão: geral

**Decisão:** a documentação que existe hoje (o produto, a arquitetura e o backlog) é o **inventário** e vai para `docs/raw/`, sem mudar de conteúdo: `docs/raw/produto/`, `docs/raw/arquitetura/` e `docs/raw/backlog/`. Ao lado, `docs/leitura/` guarda a **documentação de leitura**, a versão para pessoas: simplificada, em `.md`, com começo, meio e fim para cada tema. Primeiro a visão geral do Horus, depois uma página por mf. O objetivo de cada página é o leitor entender o que a mf faz e quais são as características dela.

**Contexto:** o dono achou a documentação difícil de ler: “não é bem uma documentação, mas sim um inventário completo sobre o desejo do produto v2 e comparação com o que temos na v1”. Pediu uma versão para leitura humana, sem eliminar o que existe, e que o PO ganhe a capacidade de escrevê-la. Substitui a `D-141` na organização de `docs/`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Mover o inventário para `docs/raw/`** | `docs/raw/` com o produto, a arquitetura e o backlog; `docs/leitura/` ao lado. Era a recomendação. | ✅ Escolhida pelo dono. Pró: fica óbvio o que ler primeiro. Contra: mudam os caminhos das skills, do `README.md` e do conversor do portal. |
| B. Manter o inventário e somar `docs/leitura/` | Nada muda de lugar. | ⚪ Não escolhida. Contra: a separação entre inventário e leitura fica só no nome de uma pasta. |

**Consequências:**
- A página de leitura nunca decide: sai do inventário e diz de onde saiu. Quando uma decisão muda o que uma mf faz ou como ela é, a página dela é reescrita no mesmo trabalho.
- A skill do PO ganhou a seção “Documentação de leitura”, e o modelo da página de mf fica em `docs/leitura/mfs/_modelo.md`.
- Nos textos antigos do inventário, as menções a `docs/produto/`, `docs/arquitetura/` e `docs/backlog/` da v2 passam a valer como `docs/raw/…`; as entradas antigas não se reescrevem.
- ⚠️ A mudança das pastas ainda não foi feita (03/11/2026): a sessão em que o dono decidiu roda dentro de `docs/arquitetura/`, e o Windows não deixa mover uma pasta em uso. O roteiro `docs/mover_para_raw.py` faz a mudança e acerta os caminhos; roda numa sessão aberta fora dessas pastas.
  - ✅ Feita em 03/11/2026, a pedido do dono. Como `docs/arquitetura/` seguia em uso, o roteiro moveu o conteúdo dela e deixou na pasta vazia um `LEIA-ME.md`; a pasta se apaga quando o processo que a usa fechar.

**Reabrir quando:** a migração para o repositório próprio pedir outra organização, ou a documentação de leitura deixar de acompanhar o inventário.

### D-143 · O Horus v2 mantém a stack da v1.xx
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: geral

**Decisão:** o Horus v2 é construído com **a mesma stack do Horus v1.xx**. A arquitetura recebe essa escolha pronta: não a reabre e não propõe outra.

**Contexto:** o dono decidiu enquanto o PO montava a skill do arquiteto de soluções (`D-142`), cujo desenho previa levar a escolha da stack ao dono.

**Por que esta:** o dono não detalhou o motivo. Leitura do PO 🔎: aproveita o que o time já domina e o que a v1.xx já tem de pé (`D-134`), e tira da v2 o risco de trocar de tecnologia junto com o desenho novo.

**Leituras do PO** *(a confirmar)*:
- 🔎 “A stack” inclui o servidor em .NET (C#), o front em Vue com TypeScript e o design system próprio, e o Postgres como banco da aplicação. A lista exata, com versões, bibliotecas, ferramentas de teste, observabilidade e publicação, o arquiteto levanta no repositório `horus` e registra como a primeira decisão de arquitetura.
- 🔎 Manter a stack não obriga a reaproveitar o código: o que se reaproveita da v1.xx continua sendo conferido mf a mf (`P-003`).

**Consequências:** a escolha da stack sai da lista do que o arquiteto leva ao dono. Continuam com o dono a infraestrutura, os fornecedores externos, o custo de operação e a segurança dos dados.

**Reabrir quando:** uma mf da v2 exigir algo que a stack da v1.xx não suporte.

### D-142 · O arquiteto de soluções documenta as decisões de tecnologia e a estratégia; as atividades vêm depois, com um agilista
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: geral

**Decisão:** o **arquiteto de soluções** é só arquiteto da solução: documenta as **decisões de tecnologia** e a **estratégia** que o Horus v2 deve usar para atingir os objetivos (`D-136`). **Não** desdobra as mfs em épicos, histórias e tasks. Só depois da arquitetura, o dono, junto com um **agilista**, define as atividades.

**Contexto:** ao pedir a skill do arquiteto, o dono tinha incluído o desdobramento em épicos, histórias e tasks, e a `D-140` e a `D-141` reservaram a pasta `docs/backlog/` para isso. O dono corrigiu: “eu me enganei quando pedi pro arquiteto pensar no backlog”.

**Consequências:**
- Corrige o escopo da `D-140` e da `D-141`: a pasta `docs/backlog/` fica reservada para as atividades, que o dono e o agilista definem depois da arquitetura. 🔎 Leitura do PO *(a confirmar)*: o agilista é um papel novo, que pode virar uma terceira skill.
- A ordem do trabalho fica: produto (o PO), depois arquitetura (o arquiteto), depois atividades (o dono com o agilista).
- A fronteira da skill do PO muda numa linha: as tarefas deixam de ser do arquiteto.

**Reabrir quando:** o dono quiser que a arquitetura e as atividades andem juntas.

### D-141 · A estrutura da pasta da v2: a documentação em docs/, por disciplina, e as skills junto
Situação: ⚪ substituída por D-144 · Data: 02/11/2026 · Versão: geral

**Decisão:** a pasta da v2 se organiza assim: `README.md` na raiz; `.claude/skills/` com as skills do PO e do arquiteto; e `docs/` com três pastas, `produto/` (os documentos de produto), `arquitetura/` (software, infraestrutura, dados, segurança, integrações e decisões técnicas) e `backlog/` (cada mf desdobrada em épicos, histórias e tasks).

**Contexto:** segunda dúvida do PO ao criar a skill do arquiteto, aberta pela `D-140`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Tudo em `docs/`, por disciplina** | `docs/produto/`, `docs/arquitetura/` e `docs/backlog/`, com as skills junto. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: é o padrão de um repositório, e a raiz fica livre para o código. Contra: os documentos de produto mudaram de pasta mais uma vez. |
| B. As disciplinas na raiz | `docs/` como produto, com `arquitetura/` e `backlog/` ao lado. | ⚪ Não escolhida. Contra: o nome `docs/` ficaria ambíguo. |
| C. Uma pasta por mf | Com a arquitetura e o backlog de cada mf, e uma pasta para o que é comum. | ⚪ Não escolhida. Contra: o que é transversal se espalha. |

**Consequências:** os oito documentos de produto foram para `docs/produto/`; a skill do PO saiu da raiz do repositório `horus` e foi para `.claude/skills/` da pasta da v2, com os caminhos reescritos a partir da raiz da v2. ⚠️ No repositório `horus` também existe uma `docs/produto/`, a da v1.xx; a skill do PO avisa da diferença.

**Reabrir quando:** a migração para o repositório próprio pedir outra organização.

### D-140 · A pasta produto v2 é o espaço de desenho do Horus v2 e vai virar um repositório próprio
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: geral

**Decisão:** a partir da pasta `docs/produto v2/`, cria-se a **estrutura de pastas usada para desenhar a v2**: o produto, a arquitetura e o desdobramento de cada mf em épicos, histórias e tasks. Depois, o dono **migra essa pasta para um repositório próprio**.

**Contexto:** ao criar a skill do arquiteto de soluções, o PO perguntou onde ficariam os épicos, as histórias e as tasks: em documentos dentro desta pasta, no `.backlog` do projeto (que guarda as tasks da v1.xx) ou nas issues do GitHub. O dono respondeu com esta direção, que equivale a documentos dentro desta pasta.

**Consequências:**
- Os épicos, as histórias e as tasks da v2 ficam em documentos, e não no `.backlog` da v1.xx.
- Tudo o que a pasta cita dentro dela usa caminhos relativos a ela, para sobreviver à migração. 🔎 O que ela cita do código da v1.xx precisa dizer o repositório, porque o caminho relativo deixa de existir depois da migração.
- A estrutura das pastas virou dúvida do PO.

**Reabrir quando:** o dono decidir manter a v2 no repositório da v1.xx.

### D-139 · Tabela de conversão das mfs: a ordem de construção do Horus v2
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026) · Data: 02/11/2026 · Versão: geral

**Decisão:** a numeração nova (`D-137`, `D-138`) fica assim, por camadas da fundação.

| Novo | Mf | Hoje | Camada | Por que nesta posição |
| --- | --- | --- | --- | --- |
| `MF-101` | Administração da instância | `MF-16` | 🧱 Plataforma | É onde tudo nasce: a instância, os administradores, o e-mail e o painel dos assentos |
| `MF-102` | Organizações, pessoas e papéis | `MF-14` | 🧱 Plataforma | Toda tela e toda regra dependem de quem é a pessoa e do papel dela |
| `MF-103` | Licenças e planos | `MF-17` | 🧱 Plataforma | O tipo de assento decide o que cada pessoa pode fazer |
| `MF-104` | Conectar as fontes vivas | `MF-06` | 🔌 Dados e IA | Sem fonte, não há resposta |
| `MF-105` | IA sob controle da organização | `MF-08` | 🔌 Dados e IA | Todo modelo que responde, analisa ou avisa vem daqui |
| `MF-106` | Segurança dos dados por pessoa | `MF-13` | 🔌 Dados e IA | Decide o que cada pessoa vê em qualquer resposta, board ou agente |
| `MF-107` | Perguntar aos dados em português | `MF-01` | 💬 Motor de análise | A conversa que transforma a pergunta em resposta |
| `MF-108` | Respostas visuais | `MF-02` | 💬 Motor de análise | Os blocos que a conversa, os boards, o WhatsApp e os agentes usam |
| `MF-109` | A web como fonte | `MF-07` | 💬 Motor de análise | Completa a resposta com fatos de fora |
| `MF-110` | Pergunta rápida | `MF-03` | 📲 Canais | Outro jeito de chegar à mesma conversa |
| `MF-111` | Chat pelo WhatsApp | `MF-04` | 📲 Canais | Idem, pelo celular |
| `MF-112` | Boards e Relatórios | `MF-09` | 📌 Acompanhar e avisar | Precisa do motor e dos blocos, e é o que o agendamento envia |
| `MF-113` | Conectores de Saída | `MF-12` | 📌 Acompanhar e avisar | O carteiro: o agendamento e os agentes entregam por ele |
| `MF-114` | Módulo de Agendamentos de Agentes | `MF-11` | 📌 Acompanhar e avisar | O relógio: funciona já com os PDFs de board, antes dos agentes |
| `MF-115` | Agentes ativos | `MF-10` | 📌 Acompanhar e avisar | Precisa de quase tudo acima: IA, fontes, blocos, relógio e carteiro |
| `MF-116` | Auditoria | `MF-15` | 📈 Prova e controle | Registra o que as peças de entrega fizeram |
| `MF-117` | Home da organização | `MF-18` | 📈 Prova e controle | Mede o uso de tudo o que vem antes |
| `MF-118` | Bases de demonstração | `MF-19` | 📈 Prova e controle | Apoio à venda e às provas, sem que nada dependa dela |
| `MF-119` | Investigação guiada | `MF-05` | 🔵 v2.1 | A única mf que entra só na v2.1 |

**Contexto:** o dono decidiu renumerar pela entrega e pela importância para a fundação (`D-137`) e escolheu o formato de três dígitos (`D-138`). A ordem dentro da v2.0 é proposta do PO, pela dependência entre as mfs: o que as outras precisam vem antes.

**Consequências:** o PO trocou as citações de mf em todos os documentos e na skill em 02/11/2026, como na renumeração anterior (`D-100`), sem mudar o conteúdo das decisões. A `MF-006` e a `MF-008`, substituídas, continuam só na tabela de conversão, com o número antigo.

**Reabrir quando:** o arquiteto mostrar uma dependência que inverta a ordem de duas mfs.

### D-138 · O número novo das mfs tem três dígitos, de MF-101 a MF-119
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: geral

**Decisão:** a numeração nova (`D-137`) usa **três dígitos, começando em 101**: as mfs vão de `MF-101` a `MF-119`. Uma mf nova ganha o próximo número livre, a partir de `MF-120`. A citação continua no formato `MF-nnn:Nome`.

**Contexto:** os números de hoje (`MF-01` a `MF-19`) e os novos cairiam na mesma faixa, e o mesmo número passaria a indicar outra mf (`D-137`).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Três dígitos, de `MF-101` a `MF-119`** | Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: não se confunde com o número de hoje (dois dígitos) nem com o mais antigo (`MF-001`, que começa com zero). Contra: um dígito a mais. |
| B. Dois dígitos, na ordem nova | `MF-01` a `MF-19`. | ⚪ Não escolhida. Contra: o mesmo número mudaria de dono. |
| C. A entrega dentro do número | `MF-20.01` e `MF-21.01`. | ⚪ Não escolhida. Contra: se uma mf mudar de entrega, o número passa a mentir. |

**Por que esta:** o formato denuncia, só de olhar, de qual numeração o número é. O que se abre mão é um número mais curto.

**Reabrir quando:** a faixa 101 a 199 acabar.

### D-137 · As mfs serão renumeradas pela entrega em que entram e pela importância para a fundação do novo Horus
Situação: 🟢 decidida (o critério; o formato do número e a tabela de conversão seguem com o dono) · Data: 02/11/2026 · Versão: geral

**Decisão:** as macro funcionalidades serão **renumeradas** com dois critérios, nesta ordem:
1. **A entrega em que a mf entra**: primeiro as da v2.0, depois as da v2.1.
2. **Dentro da entrega, a importância para a estrutura base (a fundação) do novo Horus**: o que as outras mfs precisam para existir vem antes.

**Contexto:** com a definição fechada, o dono pediu a renumeração para que a ordem dos números siga a ordem de construção. A numeração atual (`D-100` a `D-102`) segue a ordem de leitura, por tema.

**Consequências:**
- **Reabre a regra de número fixo** da `D-100` e da `D-101`, por decisão do dono. A regra volta a valer a partir da numeração nova.
- Segue o caminho da renumeração anterior: o formato do número, a tabela de conversão, que o PO propõe e o dono confirma, e a troca das citações em todos os documentos, sem mudar o conteúdo das decisões.
- ⚠️ Os números de hoje (`MF-01` a `MF-19`) e os novos vão cair na mesma faixa, e o mesmo número passaria a indicar outra mf. O formato do número novo virou dúvida do PO.

**Leitura do PO** *(confirmada pelo dono em 02/11/2026)*: 🔎 uma mf “entra” na entrega em que aparece primeiro. As que têm partes na v2.1 (`MF-06`, `MF-08`, `MF-12`, `MF-13`, `MF-16` e `MF-17`) contam como da v2.0, e só a `MF-05:Investigação guiada` é da v2.1.

**Reabrir quando:** a ordem de construção que o arquiteto definir for muito diferente da ordem dos números.

### D-136 · Os objetivos do Horus v2 ficam confirmados: o da v2.0, o da v2.1 e os oito objetivos do mapa
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026) · Data: 02/11/2026 · Versão: geral

**Decisão:** valem os objetivos propostos pelo PO no [mapa de objetivos e funcionalidades](07-mapa-de-objetivos-e-funcionalidades.md):
- **v2.0:** o gestor e o executivo **perguntam e têm a resposta na hora**, **acompanham o negócio** em boards e **são avisados** quando algo muda. A resposta é confiável, com a fonte à vista, e cada um vê só o que pode ver. A empresa mede a adoção e paga por assento.
- **v2.1:** a pessoa **descobre o porquê** de uma mudança, passo a passo, e o Horus **chega a empresas mais exigentes**: com login e segurança corporativos, com a própria marca ou com os dados dentro de casa.
- **Os oito objetivos:** O1 ⚡ Perguntar e ter a resposta na hora; O2 🛡️ Confiar no que vê; O3 📌 Acompanhar o negócio; O4 🔔 Ser avisado sem perguntar; O5 🔍 Descobrir o porquê; O6 📈 Provar o valor e vender; O7 🏢 Organizar as pessoas e cobrar; O8 🏛️ Atender empresas com exigências próprias. Cada funcionalidade fica no objetivo que o mapa indica.

**Contexto:** o objetivo que o dono confirmou para a primeira entrega (`D-106`) falava só do problema nº 1; a `D-119` e a `D-122` ampliaram o alcance. O objetivo da v2.1 nunca tinha sido escrito.

**Consequências:** o objetivo da v2.0 substitui, como texto, o da `D-105` e o da `D-106`, que continuam valendo como registro do alcance original.

**Reabrir quando:** uma entrega mudar de alcance, ou uma funcionalidade nova não couber em nenhum dos oito objetivos.

### D-135 · As entregas do Horus v2 se chamam v2.0 e v2.1, e a versão completa tem um terceiro número
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: geral

**Decisão:** a primeira entrega do Horus v2 se chama **v2.0**, e a segunda, **v2.1**. A versão completa tem também um terceiro número, por exemplo **v2.1.0000**. Nos documentos, o que se chamava “V1” passou a “v2.0”, o que se chamava “V2” passou a “v2.1”, e a “V3” da proposta substituída (`D-120`) passou a “v2.2”.

**Contexto:** os nomes “V1” e “V2” destes documentos colidiam com a numeração do produto de hoje, a v1.xx (v1.13, v1.14…), como a `D-134` apontou.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. v2.0 e v2.1** | Troca dos nomes em todos os documentos. Era a recomendação do PO. | ✅ Escolhida pelo dono, que acrescentou o terceiro número (v2.1.0000). Pró: segue o versionamento da casa e não confunde com a v1.xx. Contra: “2.1” pode soar como uma entrega pequena. |
| B. “Entrega 1” e “Entrega 2” | Sem sugerir tamanho. | ⚪ Não escolhida. Contra: foge do padrão de versões da casa. |
| C. Manter “V1” e “V2”, com uma nota | Nenhum texto muda. | ⚪ Não escolhida. Contra: a confusão com a v1.xx continuaria. |

**Por que esta:** quem ler os documentos não confunde a entrega nova com o produto de hoje. O que se abre mão é um nome que não sugira o tamanho da entrega.

**Consequências:**
- Como na renumeração das mfs (`D-100`), as citações foram trocadas em todos os documentos, e o conteúdo das decisões não mudou. O documento `05-v1-consolidada.md` passou a `05-v2.0-consolidada.md`.
- Ficam com os nomes antigos só a `D-134` e esta decisão, que precisam deles para explicar a troca.
- A skill do PO continua usando “V1” no sentido genérico de “primeira versão” de um produto, e não como nome de entrega do Horus.

**Leitura do PO** *(confirmada pelo dono em 02/11/2026)*: 🔎 o terceiro número (o `.0000` de `v2.1.0000`) é a numeração das entregas técnicas dentro de cada versão, assunto do time técnico; os documentos de produto citam só v2.0 e v2.1.

**Reabrir quando:** o time técnico adotar outra regra de numeração.

### D-134 · A documentação é do Horus v2.xx; o Horus de hoje (v1.xx) é ponto de partida e fonte de reaproveitamento
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: geral

**Decisão:** estes documentos definem o **Horus v2.xx**. O Horus de hoje é a **v1.xx**: já tem diversas funcionalidades, que muito provavelmente serão reaproveitadas, mas não é o que se está especificando. O objetivo é **criar a documentação para iniciar o desenvolvimento de forma estruturada**, com um **mapa de objetivos e funcionalidades**.

**Contexto:** resposta do dono à dúvida do PO sobre a confirmação do mapa das mfs de hoje (`P-003`). O PO tinha apresentado o mapa como “o Horus de hoje” para o dono confirmar.

**Consequências:**
- Reforça a `D-003` (o produto de hoje é ponto de partida, e não o limite) e o pedido do dono de 01/11/2026 (só documentação).
- O [mapa das mfs de hoje](04-macro-funcionalidades-de-hoje.md) passa a ser a **referência do que a v1.xx já tem**, para o reaproveitamento.
- O entregável pedido é um **mapa de objetivos e funcionalidades** do Horus v2.xx, que o PO monta a partir do que está decidido.
- ⚠️ Os nomes “V1” e “V2” destes documentos colidiam com a numeração do produto de hoje (v1.13, v1.14…). Virou dúvida do PO, decidida na `D-135`: as entregas passaram a se chamar v2.0 e v2.1.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 O dono não precisa confirmar o mapa de hoje. O que fica da `P-003` é do arquiteto: conferir o que da v1.xx se reaproveita em cada mf.
- 🔎 A “base herdada” (`D-021`) passa a ser lida como o que a v1.xx já entrega e a v2 reaproveita.

**Reabrir quando:** o dono decidir começar a v2 do zero, sem reaproveitar a v1.xx.

### D-133 · Definição macro da candidata nº 4, a medida de autonomia (MF-117:Home da organização)
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026) · Data: 02/11/2026 · Versão: v2.0

**Decisão:** a candidata nº 4 fica definida assim. É a quarta e última parte da `P-023`, a letra (d). Com ela, a `P-023` se fechou.

- **Nome:** Medida de autonomia (mantido). Continua sendo parte da `MF-117:Home da organização`.
- **O que é** ✅: o Horus mostra **quantas perguntas de análise respondeu** (`D-004`) e a **qualidade** das respostas, pela proporção de 👍🏻, 👎🏻 e 🚫 (`D-005`, `D-129`).
- **O que conta** ✅: toda pergunta de análise respondida, na conversa, na Pergunta rápida, salva ou não (`D-087`), e no WhatsApp (`D-095`).
- **O saving** ✅: é calculado **fora do produto**, com cada cliente (`D-132`).
- **Onde aparece** 🔎: na Home da organização. O owner vê o total e a divisão por gestor e por pessoa.
- **Quem ganha** 🆕: o comprador, que acompanha quantas perguntas se resolvem no Horus; o owner, que vê onde o Horus é usado e onde a qualidade cai.
- **Decisão que passa a ser possível** 🆕: decidir onde expandir o uso (as áreas que perguntam pouco) e onde corrigir (onde se concentram os 👎🏻 e os reportes), com o número na mão.
- **Prova de valor** 🆕: o owner Marcos abre a Home e vê que, em outubro, a organização teve 1.200 perguntas de análise respondidas, com 85% de 👍🏻 entre as avaliadas, e que a área do Sul pergunta pouco. Com a Maind, ele compara esse número com os pedidos que o time de dados atendia antes e chega ao saving.
- **Retorno para o negócio** 🆕: a adoção vira um número que o comprador acompanha, o que sustenta a renovação e a compra de mais assentos (`MF-103:Licenças e planos`).
- **O que não inclui** 🆕: o saving calculado dentro do produto; um ponto de partida informado pelo owner; a integração com o sistema de chamados do cliente; contar como respondida a pergunta que o Horus não conseguiu responder (`D-004`).
- **Depende de:** a `MF-117:Home da organização` (a Home e os eventos de uso); a `MF-107:Perguntar aos dados em português`, a `MF-110:Pergunta rápida` e a `MF-111:Chat pelo WhatsApp` (onde se pergunta); o retorno do usuário (`D-129`).

**Contexto:** reúne a `D-004`, a `D-005`, a `D-087`, a `D-095`, a `D-129` e a `D-132`. Os campos marcados com ✅ vêm delas; os marcados com 🆕 foram propostos pelo PO e confirmados pelo dono; a leitura marcada com 🔎 (onde aparece e o que o owner vê) também foi confirmada com a definição.

**Hipóteses a validar:** as letras (b) e (y) da `P-008` (os eventos de uso da Home servem à medida; contar a pergunta sem guardar a conversa descartada).

**Reabrir quando:** o comprador pedir o saving dentro do produto, ou a contagem de respondidas subir sem os pedidos ao time de dados caírem (`D-004`).

### D-132 · O produto mostra só o que mede; o saving é calculado fora do produto, com cada cliente
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** a medida de autonomia mostra **só o que o Horus mede**: as perguntas de análise respondidas e a qualidade das respostas. O **saving** e o “sem chamado” são calculados **fora do produto**, com cada cliente.

**Contexto:** primeira dúvida da `P-023`, letra (d), sobre a candidata nº 4. A medida do norte (`D-001`) são as perguntas respondidas sem chamado e o saving, mas o Horus não sabe quantos chamados deixaram de existir nem quanto cada um custava. A `P-001` foi dispensada porque esse número muda de cliente para cliente.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. O produto mostra só o que mede** | As respondidas e a qualidade; o saving é calculado fora, com cada cliente. | ✅ Escolhida pelo dono. Pró: nenhum número estimado dentro do produto. Contra: o comprador não vê o saving no Horus. |
| B. O owner informa o ponto de partida | O Horus mostra o saving estimado na Home. Era a recomendação do PO. | ⚪ Não escolhida. Pró: o saving aparece no produto, sem integração. Contra: é uma estimativa, que supõe que cada pergunta evitou um pedido. |
| C. Integrar com o sistema de chamados | Jira, ServiceNow e outros. | ⚪ Não escolhida. Contra: integração por cliente, e a v2.0 cresceria. |

**Por que esta:** o dono não detalhou o motivo. Leitura do PO 🔎: não pôr dentro do produto um número que não se mede. O que se abre mão é o comprador ver o saving no Horus.

**Leitura do PO** *(confirmada pelo dono em 02/11/2026)*: 🔎 quem faz a conta do saving com o cliente é a **Maind**, na implantação e no acompanhamento comercial, comparando as perguntas respondidas com os pedidos que o time de dados atendia antes.

**Consequências:**
- A prova de valor da `D-105` (“o comprador vê a autonomia e o saving subirem”) se cumpre em duas partes: a autonomia, no produto; o saving, fora dele.
- A comparação da `D-125` (o tempo do Horus contra o prazo do pedido ao time de dados) também se faz fora do produto, com o mesmo cliente.

**Hipóteses a validar:** 🔎 que o comprador aceite ver o saving num relatório da Maind, e não no produto.

**Prova de valor:** a Home mostra 1.200 perguntas respondidas em outubro. Com a Maind, o comprador compara com os cerca de 300 pedidos por mês que o time de dados atendia antes e calcula o saving.

**Reabrir quando:** o comprador exigir o saving dentro do produto.

### D-131 · Definição macro da candidata nº 3, a web como fonte viva completa (MF-109:A web como fonte)
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026) · Data: 02/11/2026 · Versão: v2.0

**Decisão:** a candidata nº 3 fica definida assim. É a terceira parte da `P-023`, a letra (c), que está resolvida.

- **Nome:** A web como fonte viva completa (mantido). Continua sendo parte da `MF-109:A web como fonte`.
- **O que é** ✅: o que vem da web entra na resposta como fonte viva, com o **link da fonte** e a **data de publicação**; sem data, o Horus **avisa** que não conseguiu identificá-la (`D-006`).
- **Em que nível** ✅: o **fato** da web entra em **qualquer nível** de inferência. A **causa** vinda de fora dos dados só entra a partir do nível 4 (`D-130`).
- **Quem usa** ✅: quem tem o modo web ligado na role, já que “o acesso à web” é o modo web e a pesquisa web (`D-110`).
- **Em todos os usos** 🔎: na conversa, na Pergunta rápida, no WhatsApp (o link e a data vão no texto da mensagem), nos cartões dos boards e no que os agentes entregam.
- **Quem ganha** 🆕: o gestor e o executivo, que cruzam o número da empresa com o que acontece fora (inflação, clima, concorrência) sem sair da conversa; e quem recebe a resposta, que distingue à vista o dado da empresa do fato de fora.
- **Decisão que passa a ser possível** 🆕: explicar um resultado com o contexto de fora, sabendo de onde ele veio e de quando é, antes de mostrá-lo ao CEO.
- **Prova de valor** 🆕: no nível padrão, com a pesquisa web ligada, a Carla pergunta “as vendas de outubro acompanharam a inflação?”. Recebe o gráfico das vendas e “inflação de outubro: 0,4%”, com o link do IBGE e a data de publicação. Uma notícia sem data aparece com o aviso de que a data não foi identificada.
- **Retorno para o negócio** 🆕: menos pedidos ao time de dados para buscar um índice de fora, e respostas mais completas sem perder a confiança (`D-006`).
- **O que não inclui** 🆕: os selos de confiança das fontes e a lista de fontes aprovadas pela organização, que a `D-006` deixou de fora; a causa vinda da web abaixo do nível 4; guardar cópias das páginas; buscar em sites que pedem login.
- **Depende de:** a `MF-109:A web como fonte` (o modo web e a pesquisa web); a `MF-107:Perguntar aos dados em português` (a conversa e os níveis); a `MF-102:Organizações, pessoas e papéis` (o botão do modo web nas roles); a `MF-105:IA sob controle da organização` (o modelo que busca); a `MF-111:Chat pelo WhatsApp`, a `MF-112:Boards e Relatórios` e a `MF-115:Agentes ativos` (os outros usos).

**Contexto:** reúne a `D-006`, a `D-110` e a `D-130`. Os campos marcados com ✅ vêm delas; os marcados com 🆕 foram propostos pelo PO e confirmados pelo dono; a leitura marcada com 🔎 (em todos os usos) também foi confirmada com a definição.

**Hipóteses a validar:** a letra (aa) da `P-008` (separar o fato da web da causa de fora dos dados) e a lacuna 6 do inventário (a data de publicação e o aviso, que hoje não existem).

**Reabrir quando:** as pessoas confundirem o fato de fora com o dado da empresa, ou os clientes pedirem controle sobre as fontes.

### D-130 · O fato da web entra em qualquer nível de inferência; o nível limita só a causa vinda de fora dos dados
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** com a pesquisa web ligada, o **fato** que vem da web entra na resposta em **qualquer nível** de inferência, sempre com o link e a data (`D-006`). O nível continua limitando só a **explicação**: a **causa** vinda de fora dos dados só aparece a partir do nível 4 (hipótese).

**Contexto:** primeira dúvida da `P-023`, letra (c), sobre a candidata nº 3. Hoje, abaixo do nível 4, o que vem da web não aparece na resposta e só ajuda o Horus a entender as palavras; o próprio produto pede “suba para o nível 4”. Como o padrão é o nível 2, quem liga a pesquisa web no padrão não recebe nada da web.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. O fato entra em qualquer nível** | O nível limita só a causa vinda de fora. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: quem liga a pesquisa web recebe o que pediu já no nível padrão; o link e a data separam, à vista, o dado da empresa do fato de fora. Contra: muda o que o produto faz hoje, e o nível 1 passa a aceitar fatos da web. |
| B. Como hoje | O que vem da web só entra a partir do nível 4. | ⚪ Não escolhida. Contra: no nível padrão, a pesquisa web ligada não entrega nada visível. |
| C. O owner escolhe | A partir de que nível, por organização. | ⚪ Não escolhida. Contra: mais uma configuração, somada ao teto da organização e das roles. |

**Por que esta:** separa o fato, que é verificável pelo link e pela data, da explicação, que é o que os níveis medem. O que se abre mão é a régua de hoje, em que a web inteira esperava o nível 4.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 Vale para a pesquisa web na conversa e para o modo web, que lê as páginas cadastradas.
- 🔎 A descrição do nível 1 muda: passa a ser “só o que a consulta devolveu e, com a pesquisa web ligada, os fatos da web, com link e data”.

**Consequências:** surge a letra (aa) da `P-008`: o motor de conversa consegue separar o fato vindo da web, que entra em qualquer nível, da causa vinda de fora dos dados, que só entra a partir do nível 4.

**Hipóteses a validar:** a letra (aa) da `P-008`.

**Prova de valor:** no nível 2, com a pesquisa web ligada, a Carla pergunta como as vendas se comparam à inflação e recebe o índice com o link e a data. Se pergunta por que as vendas caíram, a resposta não atribui a queda à inflação, a não ser que ela suba para o nível 4.

**Reabrir quando:** as pessoas confundirem o fato de fora com a explicação, ou o modelo não conseguir manter a separação.

### D-129 · Definição macro da candidata nº 2, o retorno do usuário sobre a resposta (MF-107:Perguntar aos dados em português)
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026) · Data: 02/11/2026 · Versão: v2.0

**Decisão:** a candidata nº 2 fica definida assim. É a segunda parte da `P-023`, a letra (b), que está resolvida.

- **Nome:** Retorno do usuário sobre a resposta (mantido). Continua sendo parte da `MF-107:Perguntar aos dados em português`.
- **O que é** ✅: em cada resposta, a pessoa dá **👍🏻 Gostei**, **👎🏻 Não gostei** ou **🚫 Reportar** (`D-005`).
- **Ao reportar** ✅: ela escolhe um de três motivos: “Os dados parecem errados ou desatualizados”, “O Horus entendeu ou calculou errado” ou “Outro motivo”, com texto livre (`D-127`).
- **Para onde vai o reporte** ✅: para o **owner da organização** em que a resposta foi dada, que analisa e confirma a causa (`D-014`, `D-127`).
- **O que quem reportou recebe** ✅: um **aviso automático de “recebido”**, dentro do Horus e por e-mail, se as preferências dele permitirem (`D-128`).
- **Onde vale** ✅: em toda resposta de análise: na conversa, na Pergunta rápida (`D-087`) e no WhatsApp (`D-095`).
- **A resposta reportada fica guardada** 🔎: o owner a encontra mesmo que a pessoa limpe a conversa depois (leitura `D-087.1`).
- **Quem ganha** 🆕: o owner, que descobre onde o modelo semântico ou os dados falham; quem pergunta, que tem um canal para dizer que algo está errado; o comprador, que passa a ver a qualidade das respostas, e não só a quantidade.
- **Decisão que passa a ser possível** 🆕: corrigir o modelo semântico ou a carga de dados a partir do que as pessoas apontam, em vez de descobrir o erro no meio de uma reunião.
- **Prova de valor** 🆕: a Carla reporta “Os dados parecem errados ou desatualizados” e vê, no Horus, que o reporte foi recebido; como a preferência dela permite, recebe também o e-mail. O owner Marcos vê o reporte entre os de dados, acha a carga atrasada e a corrige. A proporção de 👍🏻 e 👎🏻 aparece na Home da organização, ao lado da medida de autonomia.
- **Retorno para o negócio** 🆕: a qualidade passa a ser medida, e não só a cobertura (`D-004`, `D-005`): uma resposta ruim deixa de contar como sucesso sem ninguém perceber.
- **O que não inclui** 🆕: o owner responder a quem reportou, já que o aviso é só de “recebido” (`D-128`); delegar a análise dos reportes a outras pessoas, que fica com o owner (`D-014`); pedir motivo no 👎🏻; os reportes de falha geral do produto ao owner da instância (`D-014`); a melhoria do modelo semântico, que fica com o time de dados (`D-083`).
- **Depende de:** a `MF-107:Perguntar aos dados em português` (a conversa); a `MF-110:Pergunta rápida` e a `MF-111:Chat pelo WhatsApp` (os outros lugares onde se pergunta); a `MF-102:Organizações, pessoas e papéis` (o owner e as preferências da pessoa); a `MF-101:Administração da instância` (o envio de e-mail); a `MF-117:Home da organização` (onde aparece a qualidade).

**Contexto:** reúne a `D-005`, a `D-014`, a `D-127` e a `D-128`. Os campos marcados com ✅ vêm delas; os marcados com 🆕 foram propostos pelo PO e confirmados pelo dono; a leitura marcada com 🔎 (a resposta reportada fica guardada) também foi confirmada com a definição.

**Hipóteses a validar:** a letra (y) da `P-008` (guardar a resposta reportada até o owner analisá-la) e a letra (z) (o lugar de avisos e a preferência de e-mail). E 🔎 que uma parcela razoável das respostas receba avaliação (`D-005`).

**Reabrir quando:** poucas pessoas avaliarem, os reportes se acumularem sem análise, ou as pessoas pedirem para saber se o reporte foi corrigido.

### D-128 · Quem reporta recebe um aviso automático de “recebido”, dentro do Horus e por e-mail
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** quem reporta uma resposta recebe **só um aviso automático de “recebido”**; o owner não precisa responder. O aviso chega **dentro do próprio Horus** e **por e-mail**, se as **preferências do usuário** permitirem receber e-mails de avisos do Horus.

**Contexto:** segunda dúvida da `P-023`, letra (b). A `D-014` diz que todo reporte deve levar “a uma correção ou a uma resposta”, mas não dizia se quem reportou fica sabendo.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. O owner fecha o reporte com um retorno | “Corrigido” ou “não procede”, com uma nota curta. Era a recomendação do PO. | ⚪ Não escolhida. Pró: fecha o ciclo, e a pessoa continua reportando. Contra: trabalho a mais para o owner. |
| B. O reporte só chega ao owner | Quem reportou não recebe nada. | ⚪ Não escolhida. Contra: a pessoa não sabe se adiantou. |
| **C. Só um aviso automático de “recebido”** | Sem retorno do owner. | ✅ Escolhida pelo dono, que acrescentou o canal: dentro do Horus e por e-mail, conforme as preferências do usuário. Pró: a pessoa sabe que chegou, e o owner não tem trabalho extra. Contra: ela nunca sabe se foi corrigido. |

**Por que esta:** o dono não detalhou o motivo. Leitura do PO 🔎: não pôr trabalho novo no owner, que já cuida de muita coisa na v2.0. O que se abre mão é a pessoa saber o desfecho.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 O aviso dentro do Horus chega numa **área de avisos da conta da pessoa**, que pode servir a outros avisos do Horus.
- 🔎 A preferência de receber e-mails de avisos do Horus fica no **perfil da pessoa** (`MF-102:Organizações, pessoas e papéis`).
- 🔎 O e-mail de aviso sai pelo **envio de e-mail da instância** (`MF-101:Administração da instância`), como o convite e a recuperação de senha, e não pelo conector de e-mail que o owner liga (`MF-113:Conectores de Saída`).

**Consequências:** surge a letra (z) da `P-008`: o produto tem, ou passa a ter, uma área de avisos dentro do Horus e uma preferência no perfil para receber esses avisos por e-mail.

**Fica de fora / adiado:** o valor padrão da preferência (ligada ou desligada); quais outros avisos usam o mesmo caminho.

**Hipóteses a validar:** a letra (z) da `P-008`.

**Prova de valor:** a Carla reporta uma resposta e vê, no Horus, “Recebemos o seu reporte”. Como a preferência dela está ligada, recebe também o e-mail.

**Reabrir quando:** as pessoas pedirem para saber se o reporte foi corrigido, ou os reportes caírem por falta de retorno.

### D-127 · Ao reportar, a pessoa escolhe entre três motivos em linguagem simples
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** ao reportar uma resposta (🚫), a pessoa escolhe **um de três motivos**, escritos na língua de quem pergunta:
- “**Os dados parecem errados ou desatualizados**”, que aponta para os dados;
- “**O Horus entendeu ou calculou errado**”, que aponta para o modelo semântico;
- “**Outro motivo**”, com texto livre.

O owner da organização recebe o reporte já separado pela causa provável e confirma a causa (`D-005`, `D-014`).

**Contexto:** primeira dúvida da `P-023`, letra (b), sobre a candidata nº 2, o retorno do usuário. A `D-005` diz que a pessoa “escolhe o que está reportando” entre falhas no modelo semântico e nos dados, mas quem pergunta não sabe o que é modelo semântico.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Três motivos em linguagem simples** | Os dois da `D-005`, traduzidos, mais “Outro motivo”. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: a pessoa não precisa saber o que é modelo semântico; o owner recebe o reporte separado pela causa provável. Contra: a pessoa pode escolher o motivo errado, e quem confirma a causa é o owner. |
| B. Os dois motivos com os nomes técnicos | “Modelo semântico” e “Dados”. | ⚪ Não escolhida. Contra: quem pergunta não sabe a diferença e tende a chutar. |
| C. Só texto livre | Sem lista. | ⚪ Não escolhida. Contra: o owner não consegue separar nem contar os reportes por causa. |

**Por que esta:** quem reporta descreve o sintoma, e quem diagnostica é o owner. O que se abre mão é a precisão da causa no momento do reporte.

**Hipóteses a validar:** 🔎 que as pessoas escolham o motivo certo na maior parte das vezes, e que o “Outro motivo” não vire a opção mais usada.

**Prova de valor:** a Carla reporta “Os dados parecem errados ou desatualizados”. O owner Marcos vê o reporte entre os de dados, confere a fonte e acha a carga atrasada.

**Reabrir quando:** o “Outro motivo” dominar os reportes, ou surgir uma causa que não seja de dados nem do modelo semântico.

### D-126 · Definição macro da candidata nº 1, a resposta em segundos na reunião (MF-107:Perguntar aos dados em português)
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026) · Data: 02/11/2026 · Versão: v2.0

**Decisão:** a candidata nº 1 fica definida assim. É a primeira parte da `P-023`, a letra (a), que está resolvida.

- **Nome:** Resposta em segundos na reunião (mantido). Continua sendo parte da `MF-107:Perguntar aos dados em português`.
- **O que é** ✅: a pessoa faz a pergunta de análise e tem a resposta **na hora**, muito mais rápido do que se pedisse ao time de dados da empresa, que às vezes leva dias (`D-125`).
- **O que “em segundos” quer dizer** ✅: uma **comparação** com o pedido ao time de dados, e não um tempo cronometrado nem garantido (`D-125`).
- **A que respostas vale** 🔎: a **todas**, inclusive à Análise avançada, que demora mais, mas continua sendo de minutos contra dias.
- **Quem ganha** 🆕: o gestor e o executivo, que decidem na própria reunião; o time de dados, que deixa de atender o pedido que se repete.
- **Decisão que passa a ser possível** 🆕: decidir na reunião, com o número na mão, em vez de marcar outra reunião para quando o time de dados responder.
- **Prova de valor** 🆕: na reunião de resultado, a gestora Carla pergunta “e se tirarmos as lojas do Sul, como fica a margem?” e recebe o gráfico na hora. Antes, ela mandaria o pedido ao time de dados e teria a resposta dias depois, com a reunião já encerrada.
- **Retorno para o negócio** 🆕: menos pedidos ao time de dados (o saving, `D-001`) e decisões que não esperam dias.
- **O que não inclui** 🆕: um tempo de resposta garantido em contrato; um número de segundos como meta do produto; acelerar o banco de dados do cliente, já que o Horus só lê (`D-022`); as perguntas que o Horus não consegue responder, que não contam como respondidas (`D-004`).
- **Depende de:** a `MF-107:Perguntar aos dados em português` (a conversa); a `MF-108:Respostas visuais`; a `MF-104:Conectar as fontes vivas`; a `MF-106:Segurança dos dados por pessoa` (o que cada um vê); a `MF-105:IA sob controle da organização` (o modelo que a organização escolhe, que pesa no tempo).

**Contexto:** a `D-125` respondeu à dúvida do PO sobre a meta. Os campos marcados com ✅ vêm dela; os marcados com 🆕 foram propostos pelo PO e confirmados pelo dono; a leitura marcada com 🔎 (vale para todas as respostas, inclusive a Análise avançada) também foi confirmada com a definição.

**Hipóteses a validar:** 🔎 que, em cada cliente, a resposta do Horus seja de fato muito mais rápida que o pedido ao time de dados. O tempo do Horus o arquiteto mede (`P-002`); o tempo do pedido vem de cada cliente, como o ponto de partida do saving (`P-001`).

**Reabrir quando:** a resposta do Horus ficar lenta a ponto de as pessoas voltarem a pedir ao time de dados.

### D-125 · “Em segundos” é uma comparação com o pedido ao time de dados, e não um tempo cronometrado
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: geral

**Decisão:** a promessa “resposta em segundos” **não é descritiva**. Ela quer dizer **resposta rápida em comparação com o pedido de dados ao time de dados da empresa**, que às vezes leva dias. O produto não promete um número de segundos.

**Contexto:** primeira dúvida do PO na `P-023`, letra (a): a meta “em segundos” vale também para a Análise avançada? As opções eram: A, a meta vale só para a resposta comum; B, duas metas; C, a mesma meta para todas. O dono não escolheu uma delas e explicou o sentido da promessa, o que tira a base da pergunta.

**Por que esta:** a dor do norte é a espera de dias pelo time de dados (`D-001`), e não a diferença entre 5 e 50 segundos. O que se abre mão é uma meta numérica que pudesse ser cobrada.

**Consequências:**
- A dúvida sobre a Análise avançada perde o sentido: comparada a dias, ela também é rápida.
- A medição do tempo de resposta (`P-002`) deixa de ser condição para escrever uma meta. Continua útil para o arquiteto confirmar o inventário.
- A descrição da candidata nº 1 no inventário (“a velocidade medida e garantida”) deixa de valer no “garantida”.
- A prova da promessa passa a ser uma comparação: o tempo da resposta no Horus contra o tempo do pedido ao time de dados, que vem de cada cliente, como o saving (`P-023`, d).

**Reabrir quando:** a comunicação da Maind ou um cliente exigirem um tempo garantido.

### D-124 · Os conectores de saída da v2.0 são o e-mail e o WhatsApp
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** na v2.0, a `MF-113:Conectores de Saída` traz **dois conectores**: o **e-mail** e o **WhatsApp**. Com ela, a `P-024` se fechou.

**Contexto:** a `P-024` foi aberta pela `D-122`, quando os conectores entraram na v2.0. A `D-041` tinha deixado “a lista de conectores que entram em cada versão” a pontuar. Hoje a única saída do produto é o e-mail.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. E-mail e WhatsApp** | O e-mail de hoje e o WhatsApp, cuja conta por organização já entra com o chat (`D-097`). Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: reaproveita duas coisas que a v2.0 já tem; o aviso chega onde a pessoa já olha. Contra: quem usa Teams ou Google Chat fica sem o canal dele; no WhatsApp, as mensagens que a empresa inicia têm custo e pedem modelos aprovados pela Meta. |
| B. Só e-mail | O que já existe. | ⚪ Não escolhida. Pró: o menor esforço. Contra: o aviso fica preso à caixa de entrada. |
| C. E-mail, WhatsApp, Teams e Google Chat | Cobre a maior parte das empresas. | ⚪ Não escolhida. Pró: o maior alcance. Contra: duas integrações novas a mais, cada uma dependendo da aprovação da TI do cliente. |

**Por que esta:** reaproveita o que a v2.0 já traz e leva o aviso ao canal mais usado. O que se abre mão é o Teams e o Google Chat.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 O conector de WhatsApp usa a **mesma conta da organização** que o chat pelo WhatsApp (`D-097`): o número próprio, ou o da Maind quando a organização o autoriza.
- 🔎 Pela `D-121`, o Teams, o Google Chat e os outros conectores vão para a v2.1.

**Consequências:** a letra (x) da `P-008` passa a cobrir também as mensagens que o Horus inicia pelo conector (avisos e PDFs), que no WhatsApp pedem modelos aprovados e têm custo próprio.

**Hipóteses a validar:** as letras (f) e (x) da `P-008`. E 🔎 que os primeiros clientes aceitem receber os avisos por e-mail e WhatsApp, sem Teams.

**Prova de valor:** o agente da Carla avisa pelo WhatsApp que as vendas do Sul caíram 10%, e o PDF da semana chega por e-mail ao grupo “Vendas Sul”.

**Reabrir quando:** um cliente-âncora exigir o Teams ou o Google Chat.

### D-123 · O assento de owner grátis é um por organização
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** **cada organização** nasce com **um assento de owner grátis**, o do primeiro owner. Os demais assentos, inclusive outros de owner, são pagos (`D-069`). Com ela, o `I-013` se fechou.

**Contexto:** impasse `I-013`, aberto na repassada do PO de 02/11/2026. A `D-069` diz que “a instalação vem com um assento de owner grátis”. A `D-074` e as provas de valor da `D-080` e da `D-117` o tratam como um por organização. No SaaS, a instalação é uma só, com várias organizações (`D-008`), e cada setor de uma empresa é uma organização (`D-009`).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Um por organização** | Cada organização nasce com o primeiro owner grátis. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: casa com a `D-074`, a `D-080` e a `D-117`; cada setor começa sem custo; é fácil de explicar. Contra: uma empresa com muitos setores ganha muitos assentos grátis, um risco baixo, porque no SaaS quem cria as organizações é a Maind. |
| B. Um por empresa contratante | Vale para todas as organizações da empresa. | ⚪ Não escolhida. Pró: protege a receita. Contra: o produto não tem a figura de “empresa” acima das organizações; seria um conceito novo. |
| C. Nenhum grátis no SaaS | O grátis vale só para uma instalação própria. | ⚪ Não escolhida. Pró: leitura literal da `D-069`. Contra: contradiz a `D-074`, a `D-080` e a `D-117` e tira a entrada sem custo. |

**Por que esta:** é a que as decisões posteriores já usavam e a única que faz sentido no SaaS. O que se abre mão é a receita do primeiro owner de cada setor.

**Consequências:**
- Corrige a leitura da palavra “instalação” na `D-069`: o assento grátis é da organização.
- A leitura `D-069.1` (“só o primeiro assento de owner é grátis”) deixa de depender de impasse e volta a poder ser confirmada.

**Hipóteses a validar:** 🔎 que o assento grátis por organização não prejudique a receita (`D-074`, `D-107`).

**Prova de valor:** uma empresa com cinco setores cria cinco organizações. Cada uma nasce com o seu owner grátis, e os gestores e membros de cada setor são pagos.

**Reabrir quando:** algum cliente multiplicar organizações para ganhar assentos grátis, ou o comercial pedir outra regra.

### D-122 · O aviso entra na v2.0: a MF-115:Agentes ativos, a MF-114:Módulo de Agendamentos de Agentes e a MF-113:Conectores de Saída
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** saem da v2.1 e entram na v2.0, **por decisão do dono e acima do corte da pontuação**, as três candidatas do aviso:
- a nº 7, `MF-115:Agentes ativos` (49), como definida na `D-062`;
- a nº 13, `MF-114:Módulo de Agendamentos de Agentes` (47), como definida na `D-060`;
- a nº 12, `MF-113:Conectores de Saída` (47), como definida na `D-041`.

A v2.0 passa a ter **catorze candidatas**, e a v2.1, **quatro** (as nº 5, 6, 11 e 16). Com ela, o `I-014` se fechou: o PDF automático dos boards sai pelo agendador e pelos conectores da v2.0, com as regras novas.

**Contexto:** o dono viu a tabela da v2.1 (`D-121`) e mandou primeiro a `MF-115` e a `MF-113` para a v2.0. Em seguida, acrescentou a `MF-114`. As três só valem juntas (`D-105`): o agendamento decide quando o agente roda, e o conector entrega (`D-060`, `D-062`). O `I-014` estava aberto à espera do dono.

**Opções avaliadas:** não houve dúvida do PO; o dono decidiu direto.

**Por que esta:** o dono não detalhou o motivo. Leitura do PO 🔎: com os boards e o PDF na v2.0 (`D-119`), o aviso é a continuação natural, e o relatório por e-mail de hoje vira geral (`D-060`). O que se abre mão é, de novo, o tamanho da v2.0.

**Consequências:**
- Fecha o `I-014`.
- **Amplia o alcance de novo** (`D-106`, `D-119`). A v2.0 resolve o problema nº 1, o acompanhamento recorrente e o **problema nº 3, o aviso**. Só o problema nº 2, a investigação, fica para a v2.1.
- **Oito das catorze candidatas** entraram acima do corte por decisão do dono: as nº 15, 9, 8, 18, 17, 7, 12 e 13.
- A leitura `D-119.2`, de que a auditoria registraria só o que existia na v2.0, fica superada. Com os agentes, os agendamentos e os conectores na v2.0, o rastro registra também o que eles enviam, por qual conector e a quem, como manda a `D-090`.
- 🔎 Leitura do PO *(confirmada pelo dono em 02/11/2026)*: pela leitura já confirmada da `D-110` (os interruptores dos conectores entram quando eles entrarem), as roles ganham um **nono botão: enviar pelos conectores de saída**. A `D-041` já dizia que “quem pode usar cada conector” é candidato a interruptor.
- A `D-041` deixou “a lista de conectores que entram em cada versão” a pontuar: e-mail, WhatsApp, Teams, Google Chat e outros. Com a `MF-113` na v2.0, essa lista virou a `P-024`, que trava a v2.0.
- Os agentes usam IA em toda execução (`D-063`), e o custo entra na v2.0. O owner controla o custo pelo modelo que configura e pela aprovação de criar agentes (`D-038`, `D-061`, `D-062`).

**Fica de fora / adiado:** continuam na v2.1 a investigação guiada (nº 16), a segurança corporativa com o login corporativo (nº 11), a marca completa (nº 6) e o Horus dentro da infraestrutura do contratante (nº 5).

**Hipóteses a validar:** as letras (f), (g), (p) e (q) da `P-008`: a saída por e-mail e a agenda de hoje como ponto de partida, gerar os gráficos fora da tela e o ciclo do agente controlado pelo modelo.

**Prova de valor:** a gestora Carla importa um .md com as perguntas da semana. Toda segunda, o agente consulta, analisa e entrega ao grupo “Vendas Sul” um PDF com gráficos, pelo conector de e-mail. Quando as vendas caem mais de 10%, ele avisa, e o owner Marcos vê na auditoria o que saiu e para quem.

**Reabrir quando:** o arquiteto estimar a v2.0 inteira acima do que o dono tolera, ou o custo de IA dos agentes surpreender os owners.

### D-121 · Tudo o que ficou fora da v2.0 vai para a v2.1
Situação: 🟢 decidida (as nº 7, 12 e 13, o aviso, voltaram para a v2.0 pela `D-122`; a v2.1 ficou com quatro candidatas) · Data: 02/11/2026 · Versão: v2.1

**Decisão:** as mfs e as partes de mf que ficaram fora da v2.0 **vão todas para a v2.1**. A v2.1 reúne sete candidatas:
- a nº 16, `MF-119:Investigação guiada` (61, provisória);
- a nº 11, a etapa 2 da `MF-106:Segurança dos dados por pessoa` (58), com o login corporativo (`D-118`);
- o aviso, que são as nº 7, 12 e 13: `MF-115:Agentes ativos` (49), `MF-113:Conectores de Saída` (47) e `MF-114:Módulo de Agendamentos de Agentes` (47);
- a nº 6, a marca completa do contratante, na `MF-101:Administração da instância` (29);
- a nº 5, o Horus dentro da infraestrutura do contratante: a fonte alcançando a rede interna (`MF-104:Conectar as fontes vivas`), o modo “tudo dentro” (`MF-105:IA sob controle da organização`) e a ativação dos assentos no on-premises (`MF-103:Licenças e planos`, `P-016`).

Não há v2.2 por ora.

**Contexto:** o PO propôs dividir o que ficou fora da v2.0 em v2.1, v2.2 e “sem versão” (`D-120`). Ao ver as tabelas ([as versões](06-versoes.md)), o dono mandou as mfs restantes para a v2.1.

**Opções avaliadas:** a proposta do PO, na `D-120` (v2.1 do porquê e da segurança corporativa, v2.2 do aviso, e as nº 5 e 6 sem versão), não foi escolhida. O dono decidiu direto.

**Por que esta:** o dono não detalhou o motivo. Leitura do PO 🔎: ele quer o produto inteiro planejado em duas versões, e não uma fila longa de versões.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 “As mfs restantes” inclui as nº 5 e 6, que estavam na tabela “sem versão” como partes da `MF-104`, da `MF-105`, da `MF-101` e da `MF-103`. A melhoria do modelo semântico, que não é mf, continua com o time de dados (`D-083`).
- 🔎 A forma de entrega da v2.1 (de uma vez só ou em ondas) não foi decidida; a da v2.0 foi de uma vez só (`D-109`).

**Consequências:**
- A `D-120` passa a substituída.
- A definição macro da `MF-119` (`P-018`) passa a ser **condição para fechar a v2.1**, pela mesma regra da `D-104`.
- A ativação dos assentos no on-premises (`P-016`) passa a ser **condição para fechar a v2.1**, porque a nº 5 entrou nela.
- O `I-014` muda de leitura: se o envio de hoje continuar na v2.0, ele continua só até a v2.1, onde entram a `MF-114` e a `MF-113`.
- A v2.1 fica grande, como a v2.0: são sete candidatas, e a nº 5 (o on-premises) é a de maior esforço e depende da infraestrutura de cada cliente.

**Fica de fora / adiado:** a forma de entrega da v2.1; a repontuação das candidatas contra o objetivo da v2.1, quando ela for a próxima.

**Hipóteses a validar:** as letras (c), (d), (f), (g), (p), (q) e (v) da `P-008`, além da `P-016` e da `P-018`.

**Reabrir quando:** a v2.0 for entregue e o uso real mostrar outra prioridade, ou o arquiteto estimar a v2.1 inteira acima do que o dono tolera.

### D-120 · O backlog dividido em versões: a v2.1 do porquê e da segurança corporativa, a v2.2 do aviso
Situação: ⚪ substituída pela `D-121` (era proposta do PO; o dono mandou tudo para a v2.1) · Data: 02/11/2026 · Versão: v2.1 e v2.2

**Decisão proposta:** as sete candidatas que ficaram fora da v2.0 se dividem assim:
- **v2.1:** a nº 16, `MF-119:Investigação guiada` (61, provisória), e a nº 11, a etapa 2 da `MF-106:Segurança dos dados por pessoa` (58), com o login corporativo (`D-118`).
- **v2.2:** o aviso, ou seja, as nº 7, 12 e 13 juntas (`MF-115:Agentes ativos`, `MF-113:Conectores de Saída` e `MF-114:Módulo de Agendamentos de Agentes`, 54 juntas).
- **Sem versão, com gatilho:** a nº 5, o Horus dentro da infraestrutura do contratante (eliminada da v2.0, `D-016`), quando um cliente-âncora exigir os dados dentro de casa; a nº 6, a marca completa (29), quando um contratante quiser oferecer o Horus com a própria marca 🔎; e a melhoria do modelo semântico, que fica com o time de dados (`D-083`).

**Contexto:** o dono pediu uma tabela por versão ([as versões](06-versoes.md)). Só a v2.0 está decidida. Esta divisão é proposta do PO, feita com a pontuação da `D-105` (pesos da `D-015`) e a ordem dos problemas do norte (`D-001`: o porquê antes do aviso). ⚠️ A pontuação foi feita contra o objetivo da v2.0; quando a v2.1 for a próxima, o certo é repontuar as candidatas contra o objetivo dela.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. v2.1 do porquê e da segurança corporativa; v2.2 do aviso** | Segue a pontuação: 61 e 58 são as maiores notas fora da v2.0. Segue a ordem do norte. | 🟡 Recomendada pelo PO. Pró: segue o método; a segurança corporativa responde ao risco do cliente cuja TI exige o login corporativo (`D-118`). Contra: a nota da investigação é provisória, e a definição dela está adiada (`P-018`); a v2.1 não fecha sem essa conversa longa. |
| B. v2.1 do aviso e da segurança corporativa; v2.2 do porquê | O aviso continua o que a v2.0 começa com os boards e o PDF. | Pró: as três mfs do aviso já têm definição macro completa (`D-041`, `D-060`, `D-062`); é a continuação natural dos boards e do `I-014`. Contra: nota menor (54 juntas, contra 61); inverte a ordem do norte. |
| C. Versões curtas | v2.1 só com a segurança corporativa; v2.2 com o porquê; V4 com o aviso. | Pró: o valor chega em passos menores. Contra: mais entregas para coordenar; o dono preferiu a v2.0 de uma vez só (`D-109`). |

**Sensibilidade:** a B passa a ser a melhor se a definição da investigação baixar a nota dela para menos de 54, ou se o `I-014` puxar parte da `MF-114` e da `MF-113` para a v2.0.

**Por que esta:** é a que segue a pontuação e a ordem do norte. O que se abre mão é começar a v2.1 por definições já prontas.

**Hipóteses a validar:** a nota provisória da nº 16, que depende da `P-018`; as letras (c) e (d) da `P-008`, para a nº 11; as letras (f), (g), (p) e (q), para o aviso.

**Prova de valor:** na v2.1, a gestora Carla vê a margem do Sul cair, e o Horus a guia, passo a passo, até a loja que explica a queda. Na mesma versão, a TI do cliente liga o login corporativo, e as roles chegam pelo crachá.

**Reabrir quando:** a v2.0 for entregue e o uso real mostrar outra prioridade, um cliente-âncora exigir o aviso ou os dados dentro de casa, ou a definição da investigação mudar a nota dela.

### D-119 · A MF-112:Boards e Relatórios, a MF-111:Chat pelo WhatsApp e a MF-116:Auditoria entram na v2.0
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** entram na v2.0, **por decisão do dono e acima do corte da pontuação**, três candidatas:
- a nº 8, `MF-112:Boards e Relatórios` (59), com o redesenho inteiro definido na `D-058`;
- a nº 18, `MF-111:Chat pelo WhatsApp` (50), como definida na `D-099`;
- a nº 17, `MF-116:Auditoria` (41), como definida na `D-093`.

A v2.0 passa de oito para **onze candidatas**, mais a base herdada. Com ela, o `I-012` se fechou: com a `MF-112` inteira na v2.0, **valem todas as regras de board**.

**Contexto:** o dono pediu o resumo do que ficou dentro e fora da v2.0 e respondeu trazendo as três mfs para dentro. O `I-012` (quais regras de board valem numa v2.0 com os boards “como hoje”) estava aberto, e o redesenho inteiro era uma das opções; a decisão o resolve por esse caminho.

**Opções avaliadas:** não houve dúvida do PO; o dono decidiu direto. A pontuação da `D-105` continua como registro: nº 8 com 59, nº 18 com 50 e nº 17 com 41.

**Por que esta:** o dono não detalhou o motivo. Leitura do PO 🔎: os boards são o maior volume já construído do produto ([mapa](04-macro-funcionalidades-de-hoje.md)); o WhatsApp é a leitura mais literal da promessa “informação na palma da mão” (`D-099`); a auditoria dá a prova que as liberações de dados do gestor pedem (`D-093`). O que se abre mão é o tamanho da v2.0 e o tempo até o primeiro valor.

**Consequências:**
- Fecha o `I-012`. As leituras da `D-073` e da `D-076` que dependiam dele voltam a poder ser confirmadas. A leitura da `D-108` sobre os grupos (“servem aos boards e relatórios que existem hoje”) fica superada: os grupos servem aos boards da `MF-112`.
- **Amplia o alcance da `D-106`.** A v2.0 continua resolvendo o problema nº 1, e o WhatsApp e a auditoria servem a ele. Ela passa a entregar também o **acompanhamento recorrente**, que o norte havia adiado (`D-001`, `D-058`). A investigação (problema nº 2) e o aviso (problema nº 3) seguem fora.
- **Amplia a composição da `D-105`.** As onze candidatas são as nº 1, 2, 3, 4, 8, 9, 10, 14, 15, 17 e 18. Cinco entraram acima do corte por decisão do dono: as nº 15, 9, 8, 18 e 17. Ficam fora a nº 16 (61) e a nº 11 (58), com nota maior que a de três das que entraram; isso é registro, e não objeção.
- 🔎 Leitura do PO *(confirmada pelo dono em 02/11/2026)*: pela leitura já confirmada da `D-110` (os interruptores do WhatsApp entram quando ele entrar), as roles ganham um **oitavo botão: conversar pelo WhatsApp**. O que a `D-114` deixava de fora (“os botões do chat pelo WhatsApp”) passa a entrar.
- 🔎 Leitura do PO *(encerrada em 02/11/2026: superada pela `D-122`, que trouxe os agentes, os agendamentos e os conectores para a v2.0)*: na v2.0, a auditoria registra **o que existe na v2.0**: os boards e relatórios publicados, as liberações de dados do gestor e quem os abriu. O que os agentes, os agendamentos e os conectores enviam entra no rastro quando essas mfs entrarem.
- ⚠️ A `MF-112` depende da `MF-114:Módulo de Agendamentos de Agentes` e da `MF-113:Conectores de Saída` para o PDF automático (`D-058`), e as duas seguem fora. Hoje o relatório em PDF tem agenda e envio por e-mail. Virou o `I-014`.
- O WhatsApp traz para a v2.0 dependências de fora do produto: a conta de WhatsApp Business de cada organização e a aprovação na Meta (`D-097`). Traz também a hipótese (x) da `P-008`, que se apoia na (p): gerar os gráficos como imagem, fora da tela.

**Fica de fora / adiado:** continuam fora a nº 16 (investigação guiada), a nº 11 (segurança corporativa e login corporativo, `D-118`), o aviso (nº 7, 12 e 13), a nº 6 (marca completa) e a nº 5 (on-premises).

**Hipóteses a validar:** as letras (a), (h), (i), (n) e (o) da `P-008` (boards), a (w) (auditoria) e a (x), com a (p) (WhatsApp). E 🔎 que a v2.0 maior não atrase o primeiro valor além do que o dono tolera.

**Prova de valor:** a gestora Carla monta o board de vendas, publica-o para “Pessoas geridas por mim” e o leva em PDF para a reunião. No carro, pergunta pelo WhatsApp e recebe o gráfico. O owner Marcos vê, na auditoria, quem publicou o board e quem o abriu.

**Reabrir quando:** o arquiteto estimar a v2.0 inteira acima do que o dono tolera, ou a aprovação na Meta travar a entrega.

### D-118 · O login corporativo fica fora da v2.0: na v2.0, as roles vêm do cadastro
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** o **login corporativo fica fora da v2.0**. Na v2.0, a pessoa entra **como hoje** (e-mail e senha ou Google), e o **owner atribui as roles no cadastro**. O trecho da `D-114` em que a role chega pelo mapeamento dos campos do JWT, e a dependência da ligação do IDP em cada organização (`D-027`), passam a valer quando a etapa 2 da segurança entrar (candidata nº 11, `D-025`). Com ela, o `I-011` se fechou.

**Contexto:** impasse `I-011`, aberto na repassada do PO de 02/11/2026. A `D-114`, que é da v2.0, trazia a role pelo JWT. Já a leitura da `D-108` e a `D-025` punham o login corporativo na etapa 2 da segurança, que ficou fora da v2.0 (`D-105`, nota 58).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Fora da v2.0** | A pessoa entra como hoje; o owner atribui as roles no cadastro; o JWT fica para a etapa 2. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: mantém o corte da `D-105` e a ordem da `D-025`; a v2.0 não cresce nem depende do sistema de login de cada cliente. Contra: numa empresa grande, o owner atribui as roles à mão, e a área de TI de um cliente pode exigir o login corporativo para aprovar a compra. |
| B. Só a entrada com a conta do trabalho | O login corporativo entra para autenticar; as roles continuam no cadastro. | ⚪ Não escolhida. Pró: atende a TI que exige o login corporativo. Contra: traz para a v2.0 a ligação do login em cada organização, parte da etapa 2. |
| C. Entrada e roles pelo JWT | Como a `D-114` escreveu. | ⚪ Não escolhida. Pró: a `D-114` valeria como está. Contra: traz quase toda a candidata nº 11 para a v2.0, que passaria do corte pela terceira vez. |

**Por que esta:** protege o tamanho da v2.0 e a ordem das etapas da segurança. O que se abre mão é a entrada com a conta do trabalho e as roles automáticas já na v2.0.

**Consequências:**
- A leitura da `D-108` (na v2.0, as roles vêm do cadastro) passa a ser decisão, por esta entrada.
- A leitura da `D-112` (quem entra pelo login corporativo sem valor de role mapeado cai na role padrão) só vale quando o login corporativo entrar.
- A letra (m) da `P-008` se divide: a parte do cadastro é da v2.0, e o mapeamento dos campos do JWT fica para a etapa 2.

**Fica de fora / adiado:** o login corporativo inteiro (a entrada e as roles pelo JWT), que vai junto com a etapa 2 da segurança (candidata nº 11).

**Hipóteses a validar:** 🔎 que o primeiro cliente aceite a v2.0 sem login corporativo.

**Prova de valor:** o owner Marcos atribui, no cadastro, a role “Analista” à Ana. Ela entra com e-mail e senha e usa a Análise avançada. Nenhuma organização precisa ligar o sistema de login da empresa para começar.

**Reabrir quando:** um cliente-âncora exigir o login corporativo para comprar, ou atribuir as roles à mão pesar demais nas organizações grandes.

### D-117 · Definição macro dos planos da v2.0 na MF-103:Licenças e planos
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026) · Data: 02/11/2026 · Versão: v2.0

**Decisão:** os planos da v2.0 ficam definidos assim. Com ela, a `P-015` se fechou. Esta definição completa o que a `D-080` deixou de fora (“os planos”) e reúne a `D-115` e a `D-116`.

- **Nome:** continua sendo parte da MF-103:Licenças e planos. 🔎 O plano único não tem nome próprio no produto.
- **O que é** ✅: a v2.0 abre com **um plano só**, com **todas as funcionalidades da v2.0** (`D-115`).
- **Como se cobra** ✅: **por assento, por tipo** (owner, gestor, membro full e membro leitor), com o assento de owner grátis (`D-069`, `D-115`).
- **O preço** ✅: o valor em reais **fica fora dos documentos de produto**. É da Maind e se fecha com o primeiro cliente (`D-116`, `P-022`).
- **O que o plano controla** 🔎: **só os assentos**. O que a pessoa **usa** continua com as roles (`D-110` a `D-114`), e o que ela **vê** dos dados, com a MF-106:Segurança dos dados por pessoa. O painel de controle (`MF-101`) **não tem seletor de plano**.
- **Quem ganha** 🆕: a Maind, que abre a cobrança já no primeiro cliente, sem esperar a visão de mercado; e o cliente, que não precisa escolher entre planos para começar.
- **Decisão que passa a ser possível** 🆕: fechar o primeiro contrato só com a conta de assentos e aprender o que o cliente valoriza antes de cortar um segundo plano.
- **Prova de valor** 🆕: a Maind libera, para a organização da Carla, o assento de owner grátis, 30 de membro full e 100 de membro leitor, no plano único. A Carla começa a usar sem escolher plano, e o valor é combinado em contrato, fora do produto.
- **Retorno para o negócio** 🆕: a v2.0 é vendável desde o primeiro cliente, sem atrasar por causa de preço, e o primeiro cliente mostra onde cortar um segundo plano.
- **O que não inclui** 🆕: o valor em reais (`P-022`); nomes e conteúdo de planos futuros (como “Básico, Gold e Diamond”, `D-066`); limitar as funcionalidades da organização por plano; um seletor de plano no painel; a cobrança por uso do mês (`D-069`); o on-premises (`P-016`).
- **Depende de:** a MF-103:Licenças e planos (os assentos); a MF-101:Administração da instância (o painel); a MF-102:Organizações, pessoas e papéis (as roles).

**Contexto:** reúne as `D-115` e `D-116`, que o dono decidiu. Os campos marcados com ✅ vieram do dono; os marcados com 🆕 foram propostos pelo PO e confirmados pelo dono; as leituras marcadas com 🔎 (o plano único sem nome próprio e o plano que controla só os assentos, sem seletor no painel) também foram confirmadas com a definição.

**Hipóteses a validar:** as letras (s), (t) e (u) da `P-008`, já ligadas à `D-080`. E 🔎 que o primeiro cliente aceite pagar só por assento e por tipo.

**Reabrir quando:** um cliente pedir uma versão menor e mais barata, a Maind quiser cobrar à parte uma funcionalidade da v2.0, ou o comercial exigir mais de um plano.

### D-116 · O preço em reais fica fora dos documentos de produto
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** a documentação registra a **regra de cobrança** (um plano só, cobrado por assento e por tipo, `D-069`, `D-115`), mas o **valor em reais fica fora dos documentos de produto**. Ele é da Maind, no comercial, e se fecha com o primeiro cliente. Fica registrado como a `P-022`, que **não trava a v2.0**.

**Contexto:** segunda pergunta da `P-015`. A `D-080` já deixou a cobrança e o pagamento fora do produto. O PO não tem visão de mercado, e qualquer número que propusesse seria um chute.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. O preço fica fora dos documentos de produto** | Só a regra de cobrança entra; o valor é comercial. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: coerente com a `D-080`; não põe um número sem base num documento de referência. Contra: a documentação não responde “quanto custa”, e a conta do retorno da v2.0 fica sem número. |
| B. O dono dá um preço de partida | Por tipo de assento, registrado como hipótese. | ⚪ Não escolhida. Pró: documentação completa e número para a conta do retorno. Contra: um número sem base de mercado pode virar âncora. |
| C. O PO pesquisa o mercado | Traz uma faixa de referência de produtos parecidos. | ⚪ Não escolhida por ora. Pró: dá base à decisão. Contra: o preço de outros produtos não é o do Horus; leva tempo e continua sendo hipótese. Pode ser pedida a qualquer momento. |

**Por que esta:** o preço é assunto comercial da Maind e se aprende com o primeiro cliente. O que se abre mão é o número na conta do retorno.

**Fica de fora / adiado:** o valor em reais (`P-022`).

**Hipóteses a validar:** 🔎 que o primeiro cliente aceite o preço que a Maind propuser; isso se valida no comercial, e não nestes documentos.

**Reabrir quando:** o dono quiser o número nos documentos, ou a conta do retorno da v2.0 exigir um preço.

### D-115 · A v2.0 abre com um plano só, com todas as funcionalidades
Situação: 🟢 decidida (as três primeiras leituras do PO foram confirmadas com a `D-117`, e a quarta pelo dono em 02/11/2026; nota de correção de 02/11/2026 logo abaixo das opções) · Data: 02/11/2026 · Versão: v2.0

**Decisão:** a v2.0 abre com **um plano só**, que traz **todas as funcionalidades da v2.0**. O cliente paga pelos assentos, por tipo (`D-069`). Os nomes “Básico, Gold e Diamond”, que o dono deu como exemplo (`D-066`), ficam para quando houver mais de um plano.

**Contexto:** primeira pergunta da `P-015`, que deixou de poder esperar com a `MF-103` na v2.0 (`D-107`). Limite do PO: a visão de mercado, que diria onde cortar um plano, é um item que segue em aberto.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Um plano só** | Todas as funcionalidades da v2.0; paga-se pelos assentos. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: a v2.0 não espera a visão de mercado; o primeiro cliente (a própria Maind, por dentro, `D-009`) mostra o que vale cobrar a mais; mudar o preço depois é fácil, porque ninguém tem um plano antigo. Contra: não há escada de venda; a ideia de o plano limitar as funcionalidades da organização inteira (leitura da `D-066`) fica para depois. |
| B. Dois planos | Um básico e um completo. | ⚪ Não escolhida. Pró: já tem uma primeira escada. Contra: decide o que separa os dois sem dado de mercado; se errar, o básico pode vir sem algo de que o cliente precisa no primeiro dia. |
| C. Três planos | Básico, Gold e Diamond, como o exemplo do dono. | ⚪ Não escolhida. Pró: é a escada completa que o dono imaginou. Contra: é a decisão com menos base; são sete botões (`D-110`) espalhados por três planos, e é a mais difícil de explicar ao cliente. |

*(Nota de correção, 02/11/2026, na repassada do PO: o “Pró” da opção A diz “a própria Maind, por dentro”, e isso está errado. Pela `D-009`, o primeiro contratante é **a empresa que usa o Horus por dentro**, para os próprios setores, e não a Maind. O erro também estava na pergunta que o dono respondeu. A decisão não muda: o argumento de aprender com o primeiro cliente vale do mesmo jeito.)*

**Por que esta:** protege o “tempo até o valor” e o “aprendizado e reversibilidade”: o plano é a decisão comercial mais fácil de errar sem dado, e a mais barata de corrigir enquanto há um plano só. O que se abre mão é a escada de venda.

**Leituras do PO** *(as três primeiras confirmadas com a `D-117`, e a quarta pelo dono em 02/11/2026)*:
- 🔎 O plano único inclui **tudo da v2.0 e a base herdada**. O que cada pessoa **usa** continua com as roles (`D-110`) e o que **vê**, com a `MF-106:Segurança dos dados por pessoa`.
- 🔎 O painel de controle (`MF-101`) **não tem seletor de plano** na v2.0: a Maind libera só os assentos, por tipo.
- 🔎 O plano único **não tem nome próprio** no produto.
- 🔎 Quando houver mais de um plano, a leitura da `D-066` (o plano limita as funcionalidades da organização inteira, acima das roles) volta a valer e abre uma pendência nova.

**Fica de fora / adiado:** o preço, que fica fora dos documentos de produto (`D-116`, `P-022`); o nome e o conteúdo de planos futuros.

**Hipóteses a validar:** 🔎 que o primeiro cliente aceite pagar só por assento e por tipo, e que o que ele pedir a mais mostre onde cortar um segundo plano.

**Prova de valor:** a Maind libera, para a organização da Carla, 30 assentos de membro full e 100 de membro leitor no plano único. Ninguém precisa escolher plano para começar.

**Reabrir quando:** um cliente pedir uma versão menor e mais barata, ou a Maind quiser cobrar à parte uma funcionalidade da v2.0.

### D-114 · Definição macro das funcionalidades por role na MF-102:Organizações, pessoas e papéis
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026) · Data: 02/11/2026 · Versão: v2.0

**Decisão:** as funcionalidades por role ficam definidas assim. Com ela, a `P-009` se fechou. Esta definição completa o que a `D-056` deixou de fora (“a lista de funcionalidades por role”) e reúne a `D-110`, a `D-111`, a `D-112` e a `D-113`.

- **Nome:** continua sendo parte da MF-102:Organizações, pessoas e papéis. O nome da peça é **“role”**, o mesmo do login corporativo e do cadastro (`D-052`). 🔎 O nome comercial que a `P-009` ainda listava ficou fechado pela `D-052`; o dono pode renomear.
- **O que é** ✅: o **owner liga e desliga, por role, tudo o que a conversa oferece, botão a botão** (`D-050`, `D-110`).
- **Os botões** ✅: 1) os três modos (dados, web e conversa); 2) os cinco níveis de inferência; 3) a Análise avançada; 4) a escolha do modelo de IA; 5) ver o SQL; 6) baixar CSV, imagem e PDF; 7) a Pergunta rápida (`MF-110`). (`D-110`)
- **Quando a pessoa tem mais de uma role** ✅: **vale a soma**, botão a botão. Se qualquer role liga, a pessoa usa. Nos níveis de inferência vale o maior nível liberado, dentro do teto da organização (`D-111`).
- **Quando a pessoa não tem nenhuma role** ✅: a organização **nasce com uma role padrão**, com tudo o que a conversa oferece ligado, que vale só para quem não tem outra role. O owner a edita, mas não a apaga (`D-112`).
- **Como nasce uma role nova** ✅: o owner escolhe, na criação, **começar do zero ou copiar uma role que já existe** (`D-113`).
- **Quem cria e quem atribui** ✅: só o owner cria roles (`D-052`). 🔎 Atribuir também é do owner. Com login corporativo, a role chega pelo mapeamento dos campos do JWT que o owner configura (`D-052`).
- **O que a role controla** ✅: o que a pessoa **usa**. O que ela **vê** dos dados continua com a MF-106:Segurança dos dados por pessoa (`D-056`).
- **O tipo de assento vem antes** 🔎: o membro leitor (`D-069`) não ganha a conversa mesmo que a role a ligue; a role só limita ou libera dentro do que o tipo de assento já permite.
- **O owner não depende de roles** 🔎: usa tudo, para nunca se trancar fora (`D-112`).
- **Quem ganha** 🆕: o owner, que controla o que cada pessoa usa, inclusive o que custa mais (a Análise avançada e os modelos), sem fechar a porta de quem só precisa perguntar; o membro, que entra já com a conversa liberada pela role padrão.
- **Decisão que passa a ser possível** 🆕: o owner liberar a análise a todos sem medo de exportação, de custo ou de resposta especulativa, porque tem o botão para cada um desses casos.
- **Prova de valor** 🆕: o owner Marcos cria a role “Temporário” **copiando a padrão** e desligando a Análise avançada, o ver o SQL e o baixar. Ele a atribui ao estagiário Léo, que pergunta na conversa, mas não vê o SQL nem baixa nada. Depois atribui a role “Analista” à Ana, que soma as duas e passa a usar a Análise avançada.
- **Retorno para o negócio** 🆕: o owner confia em abrir o Horus a mais pessoas porque controla custo e risco de uso, o que sustenta organizações maiores e mais assentos (`MF-103`).
- **O que não inclui** 🆕: dar ou tirar acesso a **dados** (é da `MF-106`); os botões do chat pelo WhatsApp (`MF-111`) e dos conectores de saída (`MF-113`), que entram quando essas mfs entrarem; role que **tira** o que outra role deu; ordem ou prioridade entre roles; gestor atribuir ou criar roles; o limite por número de perguntas ou por custo.
- **Depende de:** a MF-102:Organizações, pessoas e papéis (owner, gestor, membro e o tipo de assento); a MF-106:Segurança dos dados por pessoa (o que a pessoa vê); o login corporativo de cada organização, para a role que vem do JWT (`D-027`, `D-052`); a MF-103:Licenças e planos (tipo de assento, `D-069`).

**Contexto:** reúne as `D-110` a `D-113`, que o dono decidiu. Os campos marcados com ✅ vieram do dono; os marcados com 🆕 foram propostos pelo PO e confirmados pelo dono; as leituras marcadas com 🔎 (atribuir é do owner, o tipo de assento vem antes, o owner não depende de roles e o nome “role”) também foram confirmadas com a definição.

**Notas da repassada do PO** *(02/11/2026)*:
- O trecho “com login corporativo, a role chega pelo mapeamento dos campos do JWT” e a dependência da `D-027` contradizem a leitura da `D-108` (na v2.0, as roles vêm do cadastro). A contradição foi o `I-011`, fechado pela `D-118`: o login corporativo fica fora da v2.0, e esse trecho vale a partir da etapa 2 da segurança.
- 🔎 Leitura do PO *(confirmada pelo dono em 02/11/2026)*: na role, os cinco níveis de inferência funcionam como **um teto**. A role diz até que nível a pessoa pode ir, e não liga cada nível sozinho; por isso, na soma, vale o maior (`D-111`).
- Com a `D-119`, a `MF-111:Chat pelo WhatsApp` entrou na v2.0, e o “O que não inclui” acima deixa de valer para os botões do WhatsApp. 🔎 As roles ganham um oitavo botão, conversar pelo WhatsApp (leitura confirmada na `D-119`).
- Com a `D-122`, a `MF-113:Conectores de Saída` também entrou na v2.0, e o mesmo vale para os botões dos conectores. 🔎 As roles ganham um nono botão, enviar pelos conectores de saída (leitura confirmada na `D-122`).

**Hipóteses a validar:** a letra (l) da `P-008` (a matriz de permissões por papel comporta roles que o owner configura, a soma, a role padrão e todos os botões). E 🔎 que o owner prefira ligar botão a botão a ter pacotes prontos.

**Reabrir quando:** o arquiteto mostrar que algum botão não pode ser desligado sozinho, o owner achar a configuração pesada demais, ou um owner precisar de uma role que tire funcionalidades.

### D-113 · Uma role nova começa do zero ou como cópia de outra role, à escolha do owner
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v2.0

**Decisão:** ao criar uma role, o **owner escolhe** se ela **começa do zero** (tudo desligado) ou **como cópia de uma role que já existe** (inclusive a padrão). Depois, liga e desliga os botões (`D-110`).

**Contexto:** quarta pergunta da `P-009`. A role “Analista” **libera** coisas, e a role “Temporário”, quando é a única da pessoa, **limita**, porque a pessoa deixa de usar a role padrão (`D-112`). Cada uso pede um começo diferente.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Nasce com tudo desligado | O owner liga o que quer liberar. | ⚪ Não escolhida. Pró: simples e segura. Contra: para criar uma role que limita, o owner liga quase tudo à mão. |
| B. Nasce igual à role padrão | O owner desliga o que quer tirar. | ⚪ Não escolhida. Pró: uma role que limita fica rápida. Contra: uma role que libera poucas coisas obriga a desligar quase tudo. |
| **C. O owner escolhe na criação** | Do zero ou como cópia de outra role. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: cobre os dois usos sem trabalho extra; é um gesto comum em sistemas de permissão. Contra: uma escolha a mais na tela de criar role. |

**Por que esta:** o uso da role vai nos dois sentidos, e a cópia resolve o que o “do zero” deixa pesado. O que se abre mão é uma escolha a mais na criação.

**Hipóteses a validar:** a letra (l) da `P-008`.

**Reabrir quando:** o owner achar a escolha da criação confusa.

### D-112 · A organização nasce com uma role padrão, que vale só para quem não tem outra role
Situação: 🟢 decidida (as leituras do PO foram confirmadas com a `D-114`) · Data: 02/11/2026 · Versão: v2.0

**Decisão:** toda organização **já nasce com uma role padrão**, com os botões que a conversa oferece hoje ligados (`D-110`). Ela vale **só para quem não tem nenhuma outra role**. O owner pode editá-la.

**Contexto:** terceira pergunta da `P-009`, aberta pela `D-111`: pela soma, quem não tem nenhuma role não teria nenhum botão ligado. Isso acontece com o membro recém-chegado e com quem entra pelo login corporativo com um valor de role que o owner não mapeou (`D-052`).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Role padrão desde o nascimento** | A organização nasce com uma role (por exemplo, “Membro”) que vale para quem não tem outra. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: a pessoa pergunta no primeiro dia, sem esperar o owner (tempo até o valor); cobre o login corporativo sem mapeamento. Contra: um conceito a mais; ao receber uma role, a pessoa perde a padrão, e isso pode surpreender. |
| B. Sem role, sem nada | A pessoa entra e não usa nenhum botão até o owner atribuir uma role. | ⚪ Não escolhida. Pró: regra única e a mais segura. Contra: toda pessoa nova fica parada, e o owner atribui uma role a cada convite. |
| C. Sem role, tudo ligado | Como o Horus é hoje. | ⚪ Não escolhida. Pró: simples; nada muda para quem já usa. Contra: não combina com a soma (`D-111`); quem recebe a role “Temporário” teria menos que quem não tem role nenhuma. |

**Por que esta:** protege o “tempo até o valor” sem quebrar a soma: a role padrão é uma role como as outras, só que vale quando não há outra. O que se abre mão é um conceito a mais para o owner entender.

**Leituras do PO** *(confirmadas com a `D-114`)*:
- 🔎 A role padrão **nasce com todos os botões da `D-110` ligados**, e o owner a edita depois. O nome “Membro” é só um exemplo; o nome fica para a organização ou para o dono.
- 🔎 A role padrão **pode ser editada, mas não apagada**: sempre existe uma para quem não tem outra.
- 🔎 Ao receber **qualquer** role, a pessoa **deixa de usar** a padrão. Para somar a padrão, o owner atribui a ela também.
- 🔎 Quem entra pelo login corporativo sem valor de role mapeado **cai na padrão**.
- 🔎 O **owner não depende de roles**: usa tudo, para nunca se trancar fora.

*(Nota de 02/11/2026: com a `D-118`, o login corporativo fica fora da v2.0. A quarta leitura só vale quando ele entrar, com a etapa 2 da segurança.)*

**Hipóteses a validar:** a letra (l) da `P-008` (a matriz de permissões comporta uma role padrão para quem não tem outra e o owner fora das roles).

**Prova de valor:** o owner convida a Ana sem atribuir role. Ela entra e já pergunta na conversa. O owner atribui a role “Temporário”, e ela passa a ter só o que essa role liga.

**Reabrir quando:** o owner se confundir com a perda da role padrão ao atribuir outra, ou um contratante exigir que ninguém use nada sem role atribuída.

### D-111 · Quando a pessoa tem mais de uma role, vale a soma
Situação: 🟢 decidida (as leituras do PO foram confirmadas com a `D-114`) · Data: 02/11/2026 · Versão: v2.0

**Decisão:** quando a pessoa tem **mais de uma role** e elas divergem, **vale a soma**: se **qualquer** das roles liga um interruptor (`D-110`), a pessoa **usa** a funcionalidade. A role é um **pacote do que se libera**; para tirar uma funcionalidade da pessoa, o owner tira a role que a dá.

**Contexto:** segunda pergunta da `P-009`. Com os sete interruptores da `D-110`, a divergência entre roles passa a ser comum. Exemplo: a Ana tem a role “Analista”, que liga a Análise avançada, e a role “Temporário”, que não a liga.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Vale a soma** | Se qualquer role liga, a pessoa usa. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: fácil de explicar; não abre dados, que seguem na `MF-106:Segurança dos dados por pessoa`. Contra: uma role “Temporário” não consegue tirar o que outra role deu. |
| B. Vale a mais restritiva | Se qualquer role desliga, a pessoa não usa (mesmo princípio da `D-026` para os dados). | ⚪ Não escolhida. Pró: é a mais segura. Contra: surpreende o owner, e fica difícil entender por que um botão está desligado. |
| C. Vale a role de maior prioridade | O owner ordena as roles, e a de cima ganha. | ⚪ Não escolhida. Pró: é a mais flexível. Contra: o owner mantém uma ordem, e é a mais difícil de explicar. |

**Por que esta:** a role já é o pacote do que se libera (`D-050`), e a soma é a regra que o owner prevê sem consultar manual. O que se abre mão é a role que “tira”: o limite vem de não dar.

**Leituras do PO** *(confirmadas com a `D-114`)*:
- 🔎 A soma vale **botão a botão**: cada interruptor da `D-110` é decidido sozinho, somando as roles da pessoa.
- 🔎 Nos **níveis de inferência**, vale o **maior nível** que qualquer role libera, sempre **dentro do teto da organização** (`D-001`, `D-110`).
- 🔎 A soma vale só para o que a pessoa **usa**. O que ela **vê** dos dados segue a regra da `D-026` (a mais restritiva) na `MF-106`; as duas regras não se misturam.

**Consequência:** surge um ponto novo, que entra na `P-009`: **o que vale para quem não tem nenhuma role**, já que, somando, quem não tem role não teria nenhum interruptor ligado.

**Hipóteses a validar:** a letra (l) da `P-008` (a matriz de permissões comporta o cálculo da soma, botão a botão, para quem tem várias roles).

**Prova de valor:** a Ana, com as roles “Analista” e “Temporário”, usa a Análise avançada. O owner tira dela a role “Analista”, e ela deixa de usar.

**Reabrir quando:** um owner precisar de uma role que **tire** funcionalidades de quem já as tem por outra role.

### D-110 · O owner liga e desliga, por role, tudo o que a conversa oferece, botão a botão
Situação: 🟢 decidida (as leituras do PO foram confirmadas com a `D-114`) · Data: 01/11/2026 · Versão: v2.0

**Decisão:** o owner pode ligar e desligar **por role** **tudo o que a conversa de análise oferece**, **botão a botão** (`D-050`). É uma regra de produto, e não uma tela.

**Contexto:** primeira pergunta da `P-009`, que voltou a travar a definição da v2.0 porque as roles entraram nela (`D-108`). O dono tinha dado três exemplos: o acesso à web, a Análise avançada e a escolha do modelo de IA (`D-030`, `D-050`).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Só as três citadas | Acesso à web, Análise avançada e escolha do modelo. Era a recomendação do PO. | ⚪ Não escolhida. Pró: lista curta. Contra: exportar e ver o SQL ficam liberados para todos. |
| B. As três, mais o nível máximo de inferência | O owner limita quem pode pedir resposta especulativa. | ⚪ Não escolhida. |
| **C. Tudo o que a conversa oferece, botão a botão** | Todos os controles da conversa. | ✅ Escolhida pelo dono. Pró: é o maior controle para o owner. Contra: são muitos interruptores, e o owner configura cada um. |

**A lista dos interruptores** *(leitura do PO a partir do mapa das mfs; o arquiteto confere contra a tela, na letra (l) da `P-008`)*:
1. Os três modos: **dados**, **web** e **conversa** (o “acesso à web” é o modo web e a pesquisa web).
2. Os cinco **níveis de inferência**.
3. A **Análise avançada**.
4. A **escolha do modelo de IA**.
5. **Ver o SQL**.
6. **Baixar CSV, imagem e PDF** da resposta e da conversa.
7. A **Pergunta rápida** (`MF-110`), o interruptor que a `D-089` deixou para a `P-009`.

**Por que esta:** o dono quis o controle por botão. O PO recomendava a A, mais curta; o que se abre mão é a simplicidade da configuração.

**Leituras do PO** *(confirmadas com a `D-114`)*:
- 🔎 A role limita os níveis de inferência **dentro do teto da organização** (`D-001`); ela nunca o ultrapassa.
- 🔎 O chat pelo WhatsApp (`MF-111`) e os conectores de saída (`MF-113`) ficam fora da v2.0; os interruptores deles entram quando eles entrarem.
- 🔎 Os interruptores controlam o que a pessoa **usa**. O que ela **vê** dos dados continua com a `MF-106:Segurança dos dados por pessoa` (`D-056`).

**Hipóteses a validar:** a letra (l) da `P-008` (a matriz de permissões por papel comporta roles que o owner configura, e todos esses botões).

**Reabrir quando:** o owner achar a configuração pesada demais, ou o arquiteto mostrar que algum botão não pode ser desligado sozinho.

### D-109 · A v2.0 sai de uma vez só, com as oito candidatas juntas
Situação: 🟢 decidida (com a `D-119` e a `D-122`, as candidatas passaram a catorze, e a entrega continua sendo uma só) · Data: 01/11/2026 · Versão: v2.0

**Decisão:** a v2.0 sai numa **entrega só**, com as oito candidatas e a base herdada juntas (`D-105`). Não há ondas dentro da v2.0.

**Contexto:** a v2.0 ficou grande pelas escolhas do dono de incluir a cobrança inteira (`D-107`) e a gestão de pessoas inteira (`D-108`). O PO perguntou se ela sai de uma vez ou em duas ondas, com o problema nº 1 primeiro.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. De uma vez só** | A v2.0 sai com as oito candidatas juntas. | ✅ Escolhida pelo dono. Pró: a versão é coesa, e há uma entrega só para coordenar. Contra: o primeiro valor só aparece quando tudo está pronto, e a aprendizagem com o uso real começa tarde. |
| B. Em duas ondas dentro da v2.0 | Onda 1, o problema nº 1; onda 2, a cobrança e a gestão de pessoas, antes do primeiro cliente pagante. Era a recomendação do PO. | ⚪ Não escolhida. Pró: o primeiro valor chega mais cedo. Contra: duas entregas para coordenar. |

**Por que esta:** o dono não detalhou o motivo. Leitura do PO: ele quer a versão coesa, entregue inteira.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 A ordem de construção dentro da v2.0 é assunto do arquiteto de soluções (o como), e a entrega ao cliente é uma só.
- 🔎 O uso real começa depois da v2.0 completa; até lá, o aprendizado vem das bases de demonstração (`MF-118`) e do uso interno da Maind.

**Reabrir quando:** o arquiteto estimar a v2.0 inteira acima do que o dono tolera, ou um cliente-âncora pedir uma demonstração do problema nº 1 antes da v2.0 completa.

### D-108 · A v2.0 inclui a MF-102 redesenhada inteira: gestão de pessoas, quarentena, grupos e roles
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: v2.0

**Decisão:** a v2.0 inclui a `MF-102:Organizações, pessoas e papéis` **redesenhada inteira**, como está na `D-056`: cada membro com um gestor, a quarentena de quem entra sem gestor, os grupos do gestor e da organização e as roles. A candidata **nº 9** (Grupos de pessoas e roles) passa a ser da v2.0, a oitava, **acima do corte da pontuação** (55).

**Contexto:** impasse `I-010`, aberto pela `D-107`. A `MF-103` depende da `MF-102` em papéis, convites e quarentena (`D-080`).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Só o que a `MF-103` exige | O convite do gestor aprovado pelo owner, com o tipo de assento (`D-071`, `D-072`). Era a recomendação do PO. | ⚪ Não escolhida. Pró: o mínimo para a cobrança funcionar. Contra: quem entra sem gestor ficaria sem a quarentena. |
| B. O convite e a quarentena | Sem grupos nem roles (`D-047`, `D-048`, `D-071`). | ⚪ Não escolhida. |
| **C. A gestão de pessoas completa** | Carteira de gestor, quarentena, grupos e roles (`D-056`). | ✅ Escolhida pelo dono. Pró: entrega a `MF-102` como o dono a definiu. Contra: é a maior das três, e a v2.0 deixa de ser enxuta; os grupos e as roles servem a boards e alertas, que a v2.0 quase não renova. |

**Por que esta:** o dono quis a `MF-102` completa na v2.0. O PO recomendava a A, mais enxuta; o que se abre mão é o tamanho da v2.0.

**Leituras do PO** *(a quarta foi confirmada pelo dono em 02/11/2026; a primeira virou decisão na `D-118`, a segunda ficou superada pela `D-119`, e a terceira se encerrou com o fechamento da `P-009`)*:
- 🔎 Na v2.0 as **roles vêm do cadastro**. O mapeamento dos campos do login corporativo (`D-050`, `D-052`) pertence à segurança corporativa integrada (candidata nº 11, etapa 2 da `D-025`), que está fora da v2.0.
- 🔎 Os **grupos** servem aos boards e relatórios que existem hoje (`D-029`). Os agentes e os alertas novos ficam fora da v2.0.
- 🔎 A lista de funcionalidades por role (`P-009`) **deixou de poder esperar**: com as roles na v2.0, é preciso definir quais funcionalidades se ligam e desligam (por exemplo, o acesso à web, a Análise avançada e a escolha do modelo).
- 🔎 A v2.0 fica grande: a `MF-102` completa, a `MF-103` inteira, a segurança etapa 1 e os quatro itens do problema nº 1. O primeiro valor pode atrasar por causa da parte organizacional.

**Hipóteses a validar:** as letras (j), (k), (l) e (m) da `P-008`.

**Reabrir quando:** o arquiteto mostrar que a `MF-102` completa atrasa o primeiro valor mais do que o dono tolera, ou o dono preferir entregar a v2.0 em duas ondas.

### D-107 · A v2.0 cobra por assentos desde o primeiro cliente: a MF-103:Licenças e planos entra inteira
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: v2.0

**Decisão:** a `MF-103:Licenças e planos` entra na v2.0 **inteira**, como está definida na `D-080` (o painel de controle, os quatro tipos de assento e as regras de convite, `D-066` a `D-079`). A v2.0 cobra por assentos desde o primeiro cliente. A candidata nº 15 passa a ser a sétima da v2.0, **acima do corte da pontuação** (42).

**Contexto:** impasse `I-009`, aberto pela `D-105`. A pontuação subestima a mf, porque os pesos medem a ajuda a decidir melhor, e a cobrança sustenta o negócio da Maind.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Não, a v2.0 não cobra | O primeiro contrato é fechado comercialmente, e a `MF-103` entra na versão seguinte. Era a recomendação do PO. | ⚪ Não escolhida. Pró: a v2.0 fica no menor conjunto. Contra: a Maind controla os acessos à mão e corre o risco de liberar mais assentos do que vendeu. |
| **B. Sim, a `MF-103` inteira** | O painel, os quatro tipos de assento e as regras de convite (`D-066` a `D-080`). | ✅ Escolhida pelo dono. Pró: a Maind cobra e corta o acesso desde o primeiro dia. Contra: é uma mf grande e nova, que mexe até no convite da `MF-102`, e a v2.0 cresce e atrasa o primeiro valor. |
| C. Só o painel mínimo | Ligar e desligar assentos (`D-066` a `D-068`), sem os quatro tipos nem o fluxo do gestor. | ⚪ Não escolhida. Contra: parte uma mf que o dono decidiu inteira. |

**Por que esta:** o dono não detalhou o motivo. Leitura do PO: a cobrança sustenta o negócio e dá à Maind o controle do acesso desde o primeiro dia.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026, menos a segunda e a terceira, encerradas porque a `P-015` e o `I-010` se fecharam)*:
- 🔎 O tamanho da v2.0 cresce: a `MF-103` é grande, e o PO alertou que ela atrasaria o primeiro valor.
- 🔎 Os **planos** (`P-015`) deixam de poder esperar: a `MF-103` cobra por assento e por plano. Antes de fechar a v2.0 é preciso saber quantos planos há e o que cada um inclui, ou abrir a v2.0 com um plano só.
- 🔎 A `MF-103` depende da `MF-102:Organizações, pessoas e papéis` (papéis, convites e quarentena) e da `MF-101:Administração da instância` (o painel). A `MF-101` já é base herdada; a `MF-102` puxa uma parte do redesenho para a v2.0, e quanto é o assunto do `I-010`.
- 🔎 A `MF-110:Pergunta rápida` passa a ter o membro leitor (`D-069`), que não vê o botão.
- 🔎 O on-premises continua fora (`P-016`).

**Hipóteses a validar:** as letras (s), (t) e (u) da `P-008`. E 🔎 que os clientes aceitem a cobrança por assento e por tipo (`D-066`) e que o assento de owner grátis não prejudique a receita (`D-074`).

**Reabrir quando:** o primeiro cliente não aceitar a cobrança por assento, ou o tamanho da v2.0 atrasar o primeiro valor.

### D-106 · O alcance da v2.0 é o problema nº 1 do norte: a pergunta de análise na hora, com confiança e prova
Situação: 🟢 decidida (alcance ampliado pela `D-119`, em 02/11/2026: a v2.0 entrega também o acompanhamento recorrente; e pela `D-122`, no mesmo dia: entrega também o aviso, o problema nº 3; o texto do objetivo foi atualizado na `D-136`) · Data: 01/11/2026 · Versão: v2.0

**Decisão:** a **v2.0 resolve só o problema nº 1** do norte (`D-001`): a pessoa faz a pergunta de análise na hora e recebe uma resposta visual, confiável, com a fonte à vista, vendo só o que pode ver; e a empresa consegue medir a autonomia e o saving. A investigação (problema nº 2) e o aviso (problema nº 3) ficam para as versões seguintes.

**Contexto:** a pontuação da `D-105` foi feita sobre um objetivo da v2.0 que o PO supôs, porque o norte não o escreve. O PO pediu ao dono que dissesse o alcance da v2.0. Confirma o objetivo da `D-105`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Só o problema nº 1** | Resposta na hora, confiável, com prova. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: é o menor conjunto que entrega a promessa, e tudo o que entra existe em parte hoje. Contra: quem esperava investigação ou aviso na v2.0 não os encontra. |
| B. Problemas nº 1 e nº 2 | Inclui a Investigação guiada (`MF-119`). | ⚪ Não escolhida. Contra: a definição da `MF-119` viraria condição da v2.0 (`D-104`), e a conversa longa que o dono adiou voltaria agora. |
| C. Os três problemas | Inclui também o aviso (agentes, agendamentos e conectores). | ⚪ Não escolhida. Contra: três peças novas sem nada pronto, e a v2.0 de maior prazo. |

**Por que esta:** a regra do dono é priorizar o que traz valor mais rápido, e o problema nº 1 é o primeiro do norte. O que se abre mão é a investigação e o aviso na primeira versão.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 “Fora da v2.0” não é “descartado”: as candidatas que ficaram abaixo do corte entram na pontuação da versão seguinte, com as definições macro que já estão decididas.
- 🔎 A condição da `D-104` (a definição da `MF-119` para fechar a v2.0) só vale se a `MF-119` voltar para dentro da v2.0.

**Hipóteses a validar:** 🔎 que o cliente adote o Horus pelo problema nº 1 sozinho, sem a investigação nem o aviso.

**Reabrir quando:** um cliente-âncora exigir a investigação ou o aviso para comprar, ou a medida de autonomia mostrar que a pergunta na hora já é resolvida.

### D-105 · A v2.0 resolve o problema nº 1 com confiança e prova de valor
Situação: 🟢 decidida (composição confirmada pelo dono em 01/11/2026; o objetivo foi confirmado na `D-106`, e a definição da v2.0 só fecha depois da conferência do arquiteto; a `P-009` e a `P-015` se fecharam em 02/11/2026, `D-114` e `D-117`; a repassada do PO de 02/11/2026 abriu os `I-011` a `I-013` e a `P-023`, que também travam a definição; o `I-011` se fechou com a `D-118`; a composição passou a onze candidatas com a `D-119`, que também fechou o `I-012`, e a catorze com a `D-122`, que fechou o `I-014`; o `I-013` se fechou com a `D-123`; a `P-023` se fechou com a `D-133`) · Data: 01/11/2026 · Versão: v2.0

**Decisão:** a **v2.0** reúne **oito candidatas** (nº 1, 2, 3, 4, 9, 10, 14 e 15), mais a base herdada (`D-021`). A nº 15 (Licenças e planos) e a nº 9 (Grupos e roles, com a gestão de pessoas) entram por **decisão do dono** (`D-107`, `D-108`), acima do corte da pontuação. As outras nove candidatas pontuadas ficam para depois, cada uma com o seu motivo. A v2.0 sai de uma vez só (`D-109`).

**Objetivo da v2.0 (hipótese do PO, confirmada pelo dono na `D-106`):** o gestor e o executivo de uma empresa que usa o Horus por dentro (`D-009`), em SaaS (`D-016`), fazem sozinhos a pergunta de análise na hora (problema nº 1 do norte) e recebem uma resposta visual, confiável, com a fonte à vista, vendo só o que podem ver; e a empresa consegue **medir** a autonomia e o saving (`D-004`, `D-005`). Os problemas nº 2 (investigação) e nº 3 (aviso) entram na medida em que a pontuação os trouxer. O norte não escreve o objetivo da v2.0; esta é a suposição sobre a qual a pontuação foi feita.

**Eliminatória:** a candidata **nº 5** (Horus dentro da infraestrutura do contratante) **não cabe na promessa da v2.0**: a `D-016` já deixou a entrega on-premises, o modo “tudo dentro” da IA e a fonte alcançando a rede interna para depois. Reabre quando um cliente-âncora exigir os dados dentro da casa desde o início.

**Quadro** *(nota de 0 a 5 por critério; total = soma de peso × nota ÷ 5; pesos da `D-015`)*:

| Pos. | Nº | Candidata | Mf | Missão 25 | Tempo 25 | Confiança 20 | Retorno 15 | Aprend. 5 | Alavanc. 10 | **Total** | Base da nota |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2 | Retorno do usuário sobre a resposta | `MF-107` | 4 | 4 | 4 | 4 | 5 | 4 | **81** | Fato: lacuna comprovada (inventário, linhas 7 e 8). Impacto: hipótese |
| 2 | 10 | Acesso configurado dentro do Horus | `MF-106` | 4 | 3 | 5 | 4 | 3 | 4 | **78** | Fato: a `MF-106` é madura. Hipótese: o que ela já cobre da etapa 1 (`P-008`, c) |
| 3 | 1 | Resposta em segundos na reunião | `MF-107` | 5 | 4 | 2 | 4 | 4 | 4 | **77** | Hipótese: o tempo de resposta não está medido (`P-002`) |
| 4 | 14 | Pergunta rápida | `MF-110` | 3 | 4 | 3 | 4 | 4 | 2 | **67** | Hipótese (`P-008`, r) |
| 5 | 3 | A web como fonte viva completa | `MF-109` | 4 | 3 | 4 | 3 | 3 | 2 | **67** | Fato: lacuna comprovada (inventário, linhas 5 e 6) |
| 6 | 4 | Medida de autonomia | `MF-117` | 3 | 3 | 2 | 5 | 5 | 4 | **66** | Hipótese (`P-008`, b) |
| 7 | 16 | Investigação guiada (**provisória**, `D-104`) | `MF-119` | 4 | 2 | 3 | 4 | 3 | 2 | **61** | Hipótese: premissas do PO (`P-008`, v) |
| 8 | 8 | Boards e relatórios como uma coisa só | `MF-112` | 2 | 3 | 3 | 4 | 2 | 4 | **59** | Fato: os boards existem hoje. Hipótese: a unificação (`P-008`, a e n) |
| 9 | 11 | Segurança corporativa integrada | `MF-106` | 3 | 2 | 4 | 3 | 2 | 3 | **58** | Hipótese (`P-008`, c); só vem depois da etapa 1 (`D-025`) |
| 10 | 9 | Grupos de pessoas e roles (**entra na v2.0 por decisão do dono**, `D-108`) | `MF-102` | 2 | 2 | 4 | 3 | 2 | 4 | **55** | Hipótese (`P-008`, e, l e m) |
| 11 | 18 | Chat pelo WhatsApp | `MF-111` | 3 | 2 | 2 | 4 | 3 | 1 | **50** | Hipótese (`P-008`, x) |
| 12 | 7 | Agentes ativos | `MF-115` | 3 | 1 | 2 | 4 | 3 | 3 | **49** | Hipótese (`P-008`, p e q) |
| 13 | 12 | Conectores de saída | `MF-113` | 2 | 2 | 2 | 3 | 2 | 4 | **47** | Hipótese (`P-008`, f) |
| 14 | 13 | Módulo de agendamentos | `MF-114` | 2 | 2 | 2 | 3 | 2 | 4 | **47** | Hipótese (`P-008`, g) |
| 15 | 15 | Licenças e planos (**entra na v2.0 por decisão do dono**, `D-107`) | `MF-103` | 1 | 1 | 2 | 5 | 3 | 3 | **42** | Hipótese (`P-008`, s, t e u); os planos dependem do dono (`P-015`) |
| 16 | 17 | Auditoria | `MF-116` | 1 | 1 | 4 | 3 | 2 | 2 | **41** | Hipótese (`P-008`, w) |
| 17 | 6 | Marca completa do contratante | `MF-101` | 1 | 2 | 1 | 2 | 2 | 1 | **29** | Fato: a marca parcial existe (inventário, linha 13) |

⚠️ **Quase todas as notas são hipótese.** Só as três lacunas do inventário (nº 2, 3 e 6) e a existência dos boards são fato. Nota baseada em hipótese vale menos do que o número sugere, e o arquiteto (`P-002`, `P-003`, `P-008`) pode mexer em várias delas. A escala não ficou frouxa: são seis notas 5 em 102 (17 candidatas × 6 critérios).

**Os 3 melhores:**
1. **Retorno do usuário (81).** *Prós:* é o que permite saber se a resposta presta e levar o reporte ao owner (`D-005`, `D-014`); é barato e reversível; alimenta a medida. *Contras:* sozinho não responde nada mais rápido. *Escolha certa quando* a confiança for a condição para o cliente adotar.
2. **Acesso configurado dentro do Horus (78).** *Prós:* deixa o CEO ver tudo e o gestor ver só a área dele; sustenta a prova da confiança; destrava os boards, os alertas e os canais. *Contras:* o que falta da etapa 1 está por medir. *Escolha certa quando* o cliente não tiver controle de acesso próprio.
3. **Resposta em segundos (77).** *Prós:* é a cena-âncora do norte; melhora a experiência de todo o resto. *Contras:* o tempo nunca foi medido, então a nota é a mais incerta do trio. *Escolha certa quando* o tempo atual estiver longe de “na hora”.

**Por que o corte fica entre 66 e 61:** as seis primeiras formam o menor conjunto que entrega a promessa (resposta rápida, confiável, com a fonte, só do que a pessoa pode ver, e uma prova de que funciona). Todas as seis são sobre o problema nº 1. A diferença para a sétima é de 5 pontos, curta mas fora do empate técnico. A nº 15 e a nº 9 foram acrescentadas pelo dono (`D-107`, `D-108`) mesmo abaixo do corte: a pontuação mede a ajuda a decidir melhor, e a cobrança e a gestão de pessoas são condições do negócio e da organização, e não ajudam diretamente a decidir melhor.

**Classificação do valor:** **essenciais** (sem elas a v2.0 não entrega a promessa): nº 1, 2, 3, 4 e 10. **Acelera:** nº 14 (Pergunta rápida). **Expande:** nenhuma, como deve ser numa v2.0. A nº 15 (Licenças e planos) e a nº 9 (Grupos e roles) não são valor direto para quem pergunta: são **condições do negócio e da organização** (a cobrança e a gestão de quem entra).

**Composição da v2.0** *(promessa → público → mfs → prova de valor → fora do escopo)*:
- **Promessa:** “informação na palma da mão”: a pessoa pergunta e recebe, na hora, uma resposta visual, confiável e com a fonte à vista.
- **Público:** o gestor de área e o executivo; o comprador, que vê o saving. A empresa que usa o Horus por dentro, em SaaS.
- **Mfs:** as seis candidatas acima, mais a nº 15, `MF-103:Licenças e planos` (`D-107`), e a nº 9, com a `MF-102:Organizações, pessoas e papéis` redesenhada inteira: gestão de pessoas, quarentena, grupos e roles (`D-108`); mais a base herdada (`D-021`): `MF-107:Perguntar aos dados em português`, `MF-108:Respostas visuais`, `MF-104:Conectar as fontes vivas`, `MF-109:A web como fonte`, `MF-117:Home da organização`, `MF-105:IA sob controle da organização`, `MF-101:Administração da instância` e `MF-118:Bases de demonstração`. Os boards e os relatórios **continuam como hoje**, sem o redesenho.
- **Prova de valor:** a gestora Carla, na reunião de resultado, pergunta “e se tirarmos as lojas do Sul, como fica a margem?” e recebe em segundos o gráfico, com a fonte, vendo só a área dela; dá 👍🏻. O comprador vê a autonomia (`D-004`) e o saving subirem semana a semana. A Maind libera os assentos da organização da Carla e corta o acesso se o cliente deixar de pagar (`D-107`).
- **Fora do escopo, e por quê:**

| Candidata | Total | Fica para depois porque |
| --- | --- | --- |
| nº 16 Investigação guiada | 61 (prov.) | É o problema nº 2, mas a nota é provisória e a definição está adiada (`D-104`). Fica a 5 pontos do corte |
| nº 8 Boards e relatórios unificados | 59 | Os boards e os relatórios de hoje seguem funcionando; o ganho da unificação não é da v2.0 |
| nº 11 Segurança corporativa integrada | 58 | A etapa 2 só vem depois da 1 (`D-025`) e depende do IDP de cada cliente |
| nº 18 Chat pelo WhatsApp | 50 | Canal novo, com conta por organização e aprovação na Meta (`D-097`); o celular já é atendido pelo app (`D-002`) |
| nº 7, 12 e 13 (o aviso) | 49, 47, 47 | São três peças que só valem juntas, e nenhuma existe pronta. **Juntas marcam 54**, abaixo do corte |
| nº 17 Auditoria | 41 | Só há o que registrar quando houver entregas (boards, agentes e conectores) |
| nº 6 Marca completa | 29 | O primeiro contratante usa por dentro (`D-009`), e a marca parcial já existe |
| nº 5 On-premises | — | Eliminada: `D-016` |

**Sensibilidade:**
- A **Investigação guiada** (61) passa para 66 com Tempo 3, e para 70 com Tempo 3 e Confiança 4. A definição macro pode, portanto, trazê-la para dentro da v2.0; neste caso vale a condição da `D-104`.
- Os **boards** precisariam de Tempo 4 para chegar a 64, e continuariam fora.
- O **aviso**, mesmo com Missão 5 e Tempo 2, chega a 64, abaixo do corte. Só entraria se a v2.0 passasse a incluir o problema nº 3.
- A **Pergunta rápida** e a **web** empatam em 67; desempata o aprendizado (4 contra 3). As duas entram de qualquer jeito. A **Medida** (66) está a um ponto das duas.

**Pendências** *(dependem do dono ou de validação)*:
- ~~Confirmar o objetivo da v2.0 acima~~: o dono confirmou que o alcance é só o problema nº 1 (`D-106`).
- ~~`I-009`~~: o dono decidiu que a v2.0 cobra por assentos, com a `MF-103` inteira (`D-107`).
- ~~`I-010`~~: o dono decidiu que a `MF-102` entra inteira (`D-108`).
- `P-015` e `P-009`: os planos e a lista de funcionalidades por role deixaram de poder esperar; precisam estar definidos (ou a v2.0 abre com um plano só) antes de fechar a v2.0. *(A `P-009` e a `P-015` se fecharam em 02/11/2026, com a `D-114` e a `D-117`.)*
- O arquiteto confirma as hipóteses da `P-008` e mede o tempo de resposta (`P-002`).
- *(Nota da repassada do PO, 02/11/2026.)* A definição da v2.0 também depende de três impasses e de uma pendência. O `I-011` trata do login corporativo na v2.0, contra a `D-114`. O `I-012` trata das regras de board que valem na v2.0, já que os boards “continuam como hoje”. O `I-013` trata do assento de owner grátis, por instalação ou por organização. A `P-023` é a definição macro das candidatas essenciais nº 1 a 4, que entraram sem definição no formato da mf.
- *(Nota de 02/11/2026.)* A `D-119` trouxe para a v2.0 as nº 8 (`MF-112:Boards e Relatórios`), 18 (`MF-111:Chat pelo WhatsApp`) e 17 (`MF-116:Auditoria`), acima do corte. A v2.0 passa a ter onze candidatas. O `I-011` se fechou com a `D-118`, e o `I-012` com a `D-119`; a `D-119` abriu o `I-014`.

**Reabrir quando:** o arquiteto derrubar uma hipótese que sustente uma nota do corte, o dono mudar o alcance da v2.0, ou a definição da `MF-119` mudar a nota dela.

### D-104 · A MF-119:Investigação guiada é pontuada já, com premissas do PO, e a nota é provisória
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** a `MF-119:Investigação guiada` entra na pontuação **agora**, com premissas do PO marcadas como 🆕 e como hipótese, e a nota dela é **provisória**. Se a `MF-119` entrar na v2.0, a definição macro dela (`P-018`) passa a ser **condição para fechar a v2.0**, e a nota é refeita com a definição.

**Contexto:** impasse `I-008`, aberto pela `D-103`. A pontuação precisa de quem ganha, tempo até o valor, confiança e retorno, e a `MF-119` só tem a necessidade decidida (`D-081`); o dono adiou a definição (`P-018`).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Definir a `MF-119` agora | Retomar a `P-018` antes de pontuar. | ⚪ Não escolhida. Pró: nota justa. Contra: pede a conversa longa que o dono preferiu adiar. |
| **B. Pontuar já, com premissas marcadas** | Nota provisória, refeita depois da definição. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: a pontuação anda no ritmo do dono, e a investigação não é decidida por omissão. Contra: a nota vale menos e pode errar para mais ou para menos. |
| C. Pontuar só as 17 | A `MF-119` fica para uma rodada seguinte. | ⚪ Não escolhida. Contra: a v2.0 poderia sair sem a investigação por falta de ficha, e não por decisão. |

**Por que esta:** o problema nº 2 do norte não pode ficar de fora por falta de definição, e o dono não quer a conversa longa agora.

**Reabrir quando:** a definição macro da `MF-119` mudar a nota o bastante para ela trocar de lado do corte da v2.0.

### D-103 · A lista das 18 candidatas à v2.0 está fechada
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** a lista de candidatas à v2.0 fica **fechada com as 18**, como está no [inventário](03-inventario-de-lacunas.md). Ela segue para a pontuação com os pesos da `D-015`. A melhoria do modelo semântico fica de fora (`D-083`).

**Contexto:** a confirmação final da lista vinha antes da pontuação e foi guardada durante a renumeração das mfs (`D-100` a `D-102`). As candidatas: 1 a 6, do inventário de lacunas; 7 a 9, do mapa de hoje; 10 e 11, da segurança; 12 e 13, da saída e da agenda; 14 e 15, de uso e negócio; 16 a 18, os três problemas do norte (`MF-119:Investigação guiada`, `MF-116:Auditoria` e `MF-111:Chat pelo WhatsApp`).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Fechada com as 18** | A lista como está. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: os três problemas do norte têm candidata, e as lacunas apontadas pelo PO e pelo dono viraram candidatas (`D-081`, `D-082`, `D-084`). Contra: uma lacuna que ainda não vimos só entra por uma reabertura. |
| B. Mudar a lista | O dono diz o que incluir ou tirar. | ⚪ Não escolhida. |

**Por que esta:** a lista cobre os três problemas do norte e as lacunas conhecidas, e fechá-la deixa a pontuação comparar sempre as mesmas candidatas.

**Fica de fora / adiado:** as oito mfs herdadas (`D-021`), que não passam pela pontuação, e a melhoria do modelo semântico (`D-083`).

**Reabrir quando:** a pontuação, o arquiteto (`P-002`, `P-003`) ou um cliente mostrar uma lacuna que justifique uma candidata nova.

### D-102 · Tabela de conversão das mfs: a ordem de leitura da nova numeração
Situação: 🟢 decidida (confirmada pelo dono em 01/11/2026) · Data: 01/11/2026 · Versão: geral

**Decisão:** a nova numeração das 19 mfs vivas fica nesta ordem, agrupada por tema para se ler como um produto: começa pelo que o cliente faz (perguntar), segue pelo que alimenta as respostas (fontes e IA), pelo acompanhar e avisar, pela segurança e pelas pessoas, e termina na administração e no negócio.

| Novo | Mf | Antigo | Tema |
| --- | --- | --- | --- |
| `MF-01` | Perguntar aos dados em português | `MF-001` | 💬 Perguntar e responder |
| `MF-02` | Respostas visuais | `MF-002` | 💬 Perguntar e responder |
| `MF-03` | Pergunta rápida | `MF-017` | 💬 Perguntar e responder |
| `MF-04` | Chat pelo WhatsApp | `MF-021` | 💬 Perguntar e responder |
| `MF-05` | Investigação guiada | `MF-019` | 💬 Perguntar e responder |
| `MF-06` | Conectar as fontes vivas | `MF-003` | 🔌 Fontes e IA |
| `MF-07` | A web como fonte | `MF-004` | 🔌 Fontes e IA |
| `MF-08` | IA sob controle da organização | `MF-009` | 🔌 Fontes e IA |
| `MF-09` | Boards e Relatórios | `MF-016` | 📌 Acompanhar e avisar |
| `MF-10` | Agentes ativos | `MF-013` | 📌 Acompanhar e avisar |
| `MF-11` | Módulo de Agendamentos de Agentes | `MF-015` | 📌 Acompanhar e avisar |
| `MF-12` | Conectores de Saída | `MF-014` | 📌 Acompanhar e avisar |
| `MF-13` | Segurança dos dados por pessoa | `MF-005` | 🛡️ Segurança e pessoas |
| `MF-14` | Organizações, pessoas e papéis | `MF-010` | 🛡️ Segurança e pessoas |
| `MF-15` | Auditoria | `MF-020` | 🛡️ Segurança e pessoas |
| `MF-16` | Administração da instância | `MF-011` | 🏷️ Administração e negócio |
| `MF-17` | Licenças e planos | `MF-018` | 🏷️ Administração e negócio |
| `MF-18` | Home da organização | `MF-007` | 🏷️ Administração e negócio |
| `MF-19` | Bases de demonstração | `MF-012` | 🏷️ Administração e negócio |

**Substituídas:** a `MF-006:Acompanhar em boards` e a `MF-008:Relatórios em PDF agendados` não ganham número novo. Ficam só na tabela de conversão do mapa (04), marcadas como substituídas pela `MF-09:Boards e Relatórios`.

**Contexto:** reúne as `D-100` e `D-101`. A ordem e os temas são proposta do PO; o dono ajusta o que quiser antes de confirmar.

**O que foi feito** (01/11/2026): o PO trocou as citações no backlog, no mapa (04), no inventário (03) e na skill; guardou esta tabela no mapa (04) como tabela de conversão; atualizou a regra de número fixo (a próxima mf nova é a `MF-20`); e fechou a `P-021`. Estas três entradas (`D-100` a `D-102`) são as únicas que ainda citam os números antigos, de propósito, porque explicam a troca. A lista das 18 candidatas tem numeração própria (nº 1 a 18) e não muda.

### D-101 · A nova numeração das mfs é uma sequência simples, de 1 a 19, em ordem de leitura
Situação: 🟢 decidida (o esquema; a ordem e a tabela de conversão estão na `D-102`) · Data: 01/11/2026 · Versão: geral

**Decisão:** a nova numeração das mfs é uma **sequência simples, de 1 a 19**, em **ordem de leitura**.

**Contexto:** segunda pergunta da `P-021`. Refina a `D-100`. O PO apontou que a sequência simples **colide** com os números de hoje (um número antigo passaria a apontar para outra mf), recomendou a numeração por tema com uma centena por tema, e o dono escolheu mesmo assim a sequência simples.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Por tema, uma centena por tema | Números de `MF-101` a `MF-504`, sem colisão com os velhos. Era a recomendação do PO. | ⚪ Não escolhida. Pró: sem colisão, e o número diz o tema. Contra: o número carrega o tema, e os três dígitos de `101` a `504` parecem “pulados”. |
| **B. Sequência simples de 1 a 19** | Em ordem de leitura. | ✅ Escolhida pelo dono. Pró: a lista mais curta e limpa. Contra: colide com os números velhos. |
| C. Só fechar os buracos | `MF-001` a `MF-019`, mantendo a ordem de hoje. | ⚪ Não escolhida. Contra: colide da mesma forma e não agrupa por assunto. |

**Por que esta:** o dono preferiu a lista curta e limpa. O que se abre mão é a garantia de que nenhum número novo colida com um velho.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 O número novo tem **dois dígitos** (`MF-01` a `MF-19`), e o antigo tinha três (`MF-001` a `MF-021`), para a diferença saltar aos olhos.
- 🔎 Como toda mf se cita com o nome (`MF-nn:Nome`), um número antigo citado por engano se denuncia pelo nome que não confere, e a tabela de conversão do mapa (04) resolve a dúvida.
- 🔎 As mfs substituídas (`MF-006` e `MF-008`) não ganham número novo: ficam só na tabela de conversão, apontando para a `MF-09:Boards e Relatórios`.
- 🔎 Uma mf nova ganha o próximo número livre (depois da troca, `MF-20`), e a fusão continua gerando número novo.

**Hipóteses a validar:** 🔎 que as citações antigas fora destes documentos (notas, resumos de conversa) não sejam lidas como números novos.

**Reabrir quando:** uma citação antiga lida como número novo causar um erro de entendimento.

### D-100 · As mfs serão renumeradas, numa sequência nova e sem buracos
Situação: 🟢 decidida (a necessidade; o esquema foi refinado pela `D-101`, e a ordem e a tabela de conversão estão na `D-102`) · Data: 01/11/2026 · Versão: geral

**Decisão:** as macro funcionalidades serão **renumeradas** numa sequência nova, sem os buracos das substituídas (`MF-006` e `MF-008`) e em **ordem de leitura**, e não mais na ordem em que foram descobertas. O mapa (04) guardará uma **tabela de conversão** do número antigo para o novo. A regra “o número da mf é fixo e nunca é reaproveitado” passa a valer **a partir da nova sequência**.

**Contexto:** antes de pontuar a v2.0, o dono pediu para reorganizar a numeração consolidada das mfs. Hoje são 21 números (`MF-001` a `MF-021`), dos quais 19 estão vivas, na ordem de descoberta: as 12 do produto de hoje e, depois delas, as novas. Este é o momento mais barato para trocar: só o backlog, o mapa (04), o inventário (03) e a skill citam os números, e o arquiteto ainda não começou a usá-los.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Renumerar de verdade** | Sequência nova e limpa, tabela de conversão no mapa e regra de número fixo a partir dela. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: a lista fica limpa, e é o momento mais barato. Contra: revoga a regra de número fixo de hoje, e as cerca de 200 citações precisam ser trocadas sem erro. |
| B. Manter os números e só consolidar a lista | Um quadro único, agrupado por tema, com o status de cada mf. | ⚪ Não escolhida. Contra: continuam os buracos e a ordem de descoberta. |
| C. Renumerar depois da pontuação | Evita renumerar duas vezes se a pontuação fundir ou dividir mfs. | ⚪ Não escolhida. Contra: cada decisão nova aumenta as citações a trocar. |

**Por que esta:** o dono quer a lista arrumada antes de começar a pontuação. O que se abre mão é a regra de número fixo, que passa a valer da nova sequência em diante.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 As decisões antigas (`D-nnn`) não mudam de conteúdo. Só as citações de mf dentro delas passam para os números novos, e uma nota no topo do backlog explica a troca.
- 🔎 Depois da troca, o número antigo só vale na tabela de conversão do mapa (04).

**Risco apontado pelo PO:** se a sequência nova reaproveitar números de `001` a `021`, um número antigo citado em conversas e notas passa a apontar para outra mf. O esquema de numeração que evita isso é o assunto da `P-021`.

**Reabrir quando:** a troca gerar citações erradas que atrapalhem a leitura dos documentos.

### D-099 · Definição macro da MF-111:Chat pelo WhatsApp
Situação: 🟢 decidida (confirmada pelo dono em 01/11/2026; entra na v2.0 pela `D-119`, de 02/11/2026) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** a MF-111:Chat pelo WhatsApp fica definida assim. Com ela, a `P-020` se fechou.

- **Nome:** MF-111:Chat pelo WhatsApp (proposta do PO; o dono pode renomear).
- **O que é** ✅: a pessoa **conversa com o Horus pelo WhatsApp** e vê o conteúdo da resposta **como no chat** do produto (`D-084`).
- **Como a pessoa se identifica** ✅: ela **liga o seu número ao perfil**, no app, e o confirma com um **código recebido no WhatsApp** (`D-094`).
- **Qual é a conversa** ✅: **a mesma do app**. Tudo o que a pessoa pergunta entra no histórico, pode ser continuado na tela de análise, conta na medida de autonomia e recebe retorno (`D-095`, `D-004`, `D-005`).
- **O que a resposta traz** ✅: o **texto**, os **gráficos, tabelas e KPIs como imagem** e um **link para abrir a resposta no app** (`D-096`).
- **De quem é o número** ✅: **cada organização usa o seu próprio número** de WhatsApp, por privacidade, e **pode autorizar o uso do número da Maind** (`D-097`).
- **O que a pessoa controla** ✅: **tudo o que a conversa de análise oferece**: os modos, os níveis de inferência, a Análise avançada e a escolha do modelo (`D-098`).
- **Quem liga o canal** 🆕: **só o owner da organização**, como nos conectores (`D-034`). É ele também quem autoriza o número da Maind (`D-097`).
- **Quem conversa** 🆕: o owner, o gestor e o membro full. O **membro leitor não conversa** (`D-069`). Os controles obedecem às roles do owner (`D-050`), e o que a pessoa vê continua sendo o que a MF-106:Segurança dos dados por pessoa deixa.
- **Em “tudo dentro”** 🆕: o canal fica **bloqueado**, porque o WhatsApp é serviço de fora (`D-010`, como os conectores na `D-040`).
- **Só conversa individual** 🆕: a pessoa conversa **a sós com o Horus**. Um grupo de WhatsApp fica de fora, porque a resposta com dados iria para quem não passou pela segurança do Horus.
- **Só WhatsApp na v2.0** 🆕: outros mensageiros (Teams, Google Chat…) entram depois, se o dono quiser.
- **Fica separada da MF-113** 🆕: o chat pelo WhatsApp é uma **via de entrada**; os conectores de saída (MF-113) só transportam e só entregam a usuários do Horus (`D-035`). São mfs diferentes.
- **O que fica só no app** 🆕: o que não é conversa de análise, como criar boards, relatórios, agentes e agendamentos, e configurar a organização.
- **Quem ganha** 🆕: o gestor e o executivo que perguntam longe da mesa; e o comprador, porque mais perguntas se resolvem sem chamado.
- **Decisão que passa a ser possível** 🆕: decidir na hora, antes de entrar na reunião ou na loja, com o dado na mão, sem abrir o computador.
- **Prova de valor** 🆕: o gestor Pedro, no carro, manda pelo WhatsApp “como foram as vendas de ontem por região?”. Em segundos, recebe o texto e o gráfico, abre o link no app para ver a série e dá 👍🏻. A pergunta aparece no histórico e conta na medida.
- **Retorno para o negócio** 🆕: mais perguntas por pessoa, que movem a medida-norte (`D-004`) e o saving da área de dados; é a leitura mais literal da promessa “informação na palma da mão” (`D-001`, `D-002`). Pode pesar nos planos (`P-015`), por causa do custo do canal.
- **O que não inclui** 🆕: outros mensageiros; grupos de WhatsApp; criar ou editar board, relatório, agente ou agendamento pelo WhatsApp; ligar o canal pelo gestor ou pelo membro; mensagens de áudio e arquivos enviados pela pessoa (a pergunta é em texto); a investigação guiada (MF-119).
- **Depende de:** a MF-107:Perguntar aos dados em português (a conversa); a MF-108:Respostas visuais (o que vira imagem); a MF-106:Segurança dos dados por pessoa; a MF-102:Organizações, pessoas e papéis (roles, tipos de assento e o perfil que guarda o número); a MF-103:Licenças e planos (o leitor não pergunta); a MF-116:Auditoria (se o que a pessoa vê pelo WhatsApp entra no rastro, é desenho).

**Contexto:** reúne as `D-084` e as `D-094` a `D-098`. O que veio do dono está marcado com ✅; os campos marcados com 🆕 foram propostos pelo PO e confirmados pelo dono.

**Hipóteses a validar:** a letra (x) da `P-008` (receber a pergunta, ligar o número à pessoa, devolver imagens, atender a conta própria de cada organização e a da Maind, e o custo e as janelas de resposta do canal). E 🔎 que o gestor pergunte mais, e em mais lugares, quando a pergunta está no WhatsApp que ele já usa; e que a resposta em imagem entregue o conforto visual que a promessa pede.

**Reabrir quando:** o arquiteto mostrar que o WhatsApp não comporta a resposta visual ou a Análise avançada, o custo do canal inviabilizar a oferta, ou os dados de uso mostrarem que ninguém usa os controles ali.

### D-098 · Pelo WhatsApp a pessoa tem tudo o que a conversa de análise oferece
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** no chat pelo WhatsApp (MF-111), a pessoa tem **tudo o que a conversa de análise oferece**: os modos, os níveis de inferência, a Análise avançada e a escolha do modelo de IA. O WhatsApp não é um canal menor que o app.

**Contexto:** quinta pergunta da definição macro da `P-020`. Responde ao ponto 3 da `D-084` (o que o WhatsApp faz e o que fica só no app). É a mesma escolha que o dono fez para o popup (`D-088`).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Só pergunta e resposta | Com os ajustes padrão da pessoa; quem quer mais abre o app pelo link (`D-096`). Era a recomendação do PO. | ⚪ Não escolhida. Pró: simples e cabe no jeito de usar o WhatsApp. Contra: quem quer trocar o modo ou o modelo não consegue pelo WhatsApp. |
| B. O essencial | Pergunta e resposta, mais o modo e o nível; o resto só no app. | ⚪ Não escolhida. Pró: ajusta o que mais muda a resposta. Contra: é preciso desenhar como pedir o ajuste numa conversa de texto. |
| **C. Tudo o que a conversa oferece** | Modos, níveis, Análise avançada e escolha do modelo. | ✅ Escolhida pelo dono. Pró: o WhatsApp fica igual ao app, e a pessoa não troca de canal para usar a conversa inteira. Contra: a Análise avançada pode demorar e custar mais, o WhatsApp tem janelas de resposta, e o desenho fica mais pesado. |

**Por que esta:** o dono quis que a pessoa tenha a conversa inteira onde ela já está, sem trocar de canal. O PO recomendava a A, mais simples; o que se abre mão é a simplicidade do desenho.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 Os controles obedecem às roles do owner (`D-050`): quem não tem a Análise avançada na role não a tem no WhatsApp.
- 🔎 Como a pessoa pede cada ajuste numa conversa de texto (comando, botão ou menu) é desenho.
- 🔎 Quando a resposta demora (Análise avançada), o Horus avisa que está trabalhando e entrega quando ficar pronta, se o WhatsApp permitir.

**Hipóteses a validar:** 🔎 que a pessoa use mesmo os controles pelo WhatsApp, e não só no app. 🔎 *(técnica, vai ao arquiteto na `P-008`, letra (x))* Entregar pelo WhatsApp as respostas demoradas da Análise avançada, dentro das janelas de resposta do canal, e o custo disso.

**Reabrir quando:** o custo ou as janelas do WhatsApp inviabilizarem a Análise avançada, ou os dados de uso mostrarem que ninguém usa os controles ali (e então a opção A ou B volta à mesa).

### D-097 · No chat pelo WhatsApp, cada organização usa o seu próprio número, e pode autorizar o uso do número da Maind
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** na MF-111:Chat pelo WhatsApp, **cada organização usa o seu próprio número de WhatsApp** (a conta de WhatsApp Business dela), **por privacidade dos dados**. A Maind permite que a organização **escolha autorizar o uso do número da Maind** no lugar do seu.

**Contexto:** quarta pergunta da definição macro da `P-020`. Refina a `D-084`. Ela mexe com a marca do contratante (`D-011`) e com o trabalho de montar o canal.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Um número só, da Maind, para todas as organizações | O Horus reconhece a organização pelo número de quem escreve (`D-094`). Era a recomendação do PO para o SaaS. | ⚪ Não escolhida como padrão; **fica como opção que a organização autoriza**. Pró: simples, e a organização não monta nada. Contra: leva a marca do Horus e as mensagens passam por uma conta que é da Maind. |
| **B. Cada organização usa o seu número** | A organização cadastra a conta de WhatsApp Business dela. | ✅ Escolhida pelo dono como **padrão**. Pró: a marca é do contratante, os dados não passam por conta alheia e serve ao on-premises. Contra: cada organização abre e mantém a conta junto à Meta, o que dá trabalho e tem custo. |

**Por que esta:** o dono pesou a privacidade dos dados. Com o número próprio, as perguntas e respostas trafegam só pela conta da organização; com o da Maind, trafegam por uma conta de fora dela. Por isso o padrão é o número próprio, e o da Maind é um atalho que a organização autoriza de olhos abertos, para quem não quer abrir a conta na Meta. É uma composição das duas opções: B como regra e A como exceção autorizada.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 Quem autoriza o número da Maind é o owner da organização, como só o owner liga um conector (`D-034`). A autorização diz, com todas as letras, que as mensagens passam pela conta da Maind.
- 🔎 Uma organização usa um número ou o outro, não os dois ao mesmo tempo. Com o número da Maind, o Horus reconhece a organização pelo número de quem escreve (`D-094`).
- 🔎 No on-premises vale só o número próprio, porque ali o dado fica na infraestrutura do cliente (`D-017`).

**Hipóteses a validar:** 🔎 que o trabalho de abrir a conta de WhatsApp Business não trave a adoção. 🔎 *(técnica, vai ao arquiteto na `P-008`, letra (x))* O produto atende a conta própria de cada organização e também a conta compartilhada da Maind, e o custo e o prazo de aprovação de cada uma.

**Prova de valor:** a maioria dos clientes ativa o canal sem pedir ajuda para abrir a conta.

**Reabrir quando:** quase todos os clientes autorizarem o número da Maind (a privacidade pesa menos do que se supôs), ou o trabalho com a Meta travar a adoção.

### D-096 · No WhatsApp, a resposta chega com texto, imagens e um link para abrir a resposta no app
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** no chat pelo WhatsApp (MF-111), a resposta chega com o **texto**, com os **gráficos, tabelas e KPIs como imagem** fiel ao chat, e com um **link para abrir a resposta no app**.

**Contexto:** terceira pergunta da definição macro da `P-020`. Refina a `D-084` (“exibindo o conteúdo como no chat”). O WhatsApp não roda o gráfico vivo, então o link recupera o que a imagem não mostra.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Texto e imagens | Tudo dentro do WhatsApp, sem link. | ⚪ Não escolhida. Contra: a interação (passar o mouse, trocar a série) fica só no app, e tabelas grandes e fluxos podem ficar ilegíveis no celular. |
| **B. Texto, imagens e um link para o app** | Como A, mais um link que leva à resposta viva. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: cobre o que o WhatsApp não mostra, sem perder o “como no chat”. Contra: para abrir o link, a pessoa precisa entrar no app. |
| C. Só texto | Gráficos e tabelas só no app. | ⚪ Não escolhida. Contra: perde o visual, que é valor central da promessa (`D-001`). |

**Por que esta:** o link se apoia na `D-095`: como a conversa também existe no app, o link leva a pessoa à resposta viva.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 O link abre a conversa no app e pede o login se a pessoa não estiver entrada; ele **não carrega dado nenhum**, só aponta para a conversa.
- 🔎 O retorno 👍🏻, 👎🏻 ou 🚫 pode ser dado pelo WhatsApp ou pelo app; como isso funciona no WhatsApp é desenho.

**Hipóteses a validar:** 🔎 que a resposta em imagem entregue o conforto visual que a promessa pede. 🔎 *(técnica, vai ao arquiteto na `P-008`, letra (x))* Devolver gráficos e tabelas em imagem pelo WhatsApp.

**Reabrir quando:** a imagem se mostrar ilegível no celular em boa parte das respostas.

### D-095 · A conversa do WhatsApp é a mesma conversa do app: tudo entra no histórico
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** na MF-111:Chat pelo WhatsApp, **tudo o que a pessoa pergunta pelo WhatsApp entra no histórico do Horus** e pode ser **continuado na tela de análise**. Conta na medida de autonomia (`D-004`) e recebe retorno (`D-005`) como qualquer pergunta do app.

**Contexto:** segunda pergunta da definição macro da `P-020`. Complementa a `D-094`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. A mesma conversa do app** | Tudo entra no histórico e pode ser continuado na tela de análise. | ✅ Escolhida pelo dono. Pró: tem uma verdade só, e toda pergunta conta e recebe retorno. Contra: o histórico enche de perguntas soltas. |
| B. Conversa à parte | Fica só no WhatsApp; conta na medida, mas não aparece no app. | ⚪ Não escolhida. Contra: a pessoa não continua a conversa na tela de análise. |
| C. Como no popup | Fica no WhatsApp, e a pessoa escolhe salvar no app (`D-086`). Era a recomendação do PO. | ⚪ Não escolhida. Pró: o histórico só recebe o que a pessoa quer guardar. Contra: um gesto a mais para salvar. |

**Por que esta:** o dono quis uma conversa só, no WhatsApp e no app. A diferença para o popup (`D-086`) é de propósito: lá a pessoa escolhe salvar; aqui tudo entra.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 A conversa que veio do WhatsApp aparece no histórico com a marca de origem, para a pessoa saber de onde veio.
- 🔎 A pessoa apaga uma conversa do WhatsApp pelo app, como apaga qualquer outra.

**Hipóteses a validar:** 🔎 que a pessoa não se incomode com o histórico cheio de perguntas do WhatsApp.

**Reabrir quando:** os dados de uso mostrarem que o histórico ficou inutilizável, e então a opção C volta à mesa.

### D-094 · No chat pelo WhatsApp, a própria pessoa liga o seu número ao perfil e o confirma com um código
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** na MF-111:Chat pelo WhatsApp, **a própria pessoa liga o seu número ao perfil**, no app, e o confirma com um **código que o Horus manda para esse número pelo WhatsApp**.

**Contexto:** primeira pergunta da definição macro da `P-020`. Refina a `D-084`. O WhatsApp só entrega o número de telefone, e o Horus precisa ligá-lo a uma pessoa para valer o que ela pode ver (MF-106:Segurança dos dados por pessoa).

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. A própria pessoa liga o número** | No app, ela informa o número e confirma com um código recebido no WhatsApp. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: a pessoa controla o próprio acesso, e o código prova que o número é dela. Contra: depende de cada pessoa fazer a ligação, e quem troca de número precisa refazer. |
| B. O owner cadastra o número de cada pessoa | A organização informa os números. | ⚪ Não escolhida. Contra: dá trabalho ao owner, e um número digitado errado dá acesso à pessoa errada. |

**Por que esta:** o código confirma que o número é da pessoa, e quem controla o acesso é ela mesma.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 Só quem pode perguntar liga um número: owner, gestor e membro full. O membro leitor não pergunta (`D-069`).
- 🔎 Um número liga-se a uma pessoa só, e a pessoa tem um número só.
- 🔎 Quem sai da organização ou perde o assento deixa de conversar: o número é desligado.

**Hipóteses a validar:** 🔎 *(técnica, vai ao arquiteto na `P-008`, letra (x))* O produto recebe a pergunta do WhatsApp e liga o número à pessoa.

**Reabrir quando:** a ligação pela própria pessoa se mostrar um obstáculo ao uso, ou um cliente exigir que a organização controle os números.

### D-093 · Definição macro da MF-116:Auditoria
Situação: 🟢 decidida (confirmada pelo dono em 01/11/2026; entra na v2.0 pela `D-119`, de 02/11/2026) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** a MF-116:Auditoria fica definida assim. Com ela, a `P-019` se fechou.

- **Nome:** MF-116:Auditoria (proposta do PO; o dono pode renomear).
- **O que é** ✅: o **rastro de quem viu e de quem entregou o quê a quem** (`D-082`).
- **O que o rastro registra** ✅: o que o Horus **entregou** (boards e relatórios publicados, liberações de dados do gestor, o que cada agente ou agendamento enviou, por qual conector e a quem) e **quem abriu** esses boards e relatórios, e quando. **Não registra o conteúdo** das perguntas e das respostas (`D-090`).
- **Quem consulta** ✅: **só o owner da organização**, e ele vê o rastro da organização inteira (`D-091`).
- **Por quanto tempo fica guardado** ✅: **o owner define**, nas preferências da organização, por quantos dias (`D-092`).
- **Como o owner consulta** 🆕: numa tela da organização, filtrando por pessoa, por board ou relatório, por conector e por período.
- **O rastro não se altera** 🆕: nem o owner edita ou apaga um registro; ele só desaparece quando vence o prazo (`D-092`). Sem isso, o rastro não prova nada.
- **Quem ganha** 🆕: o owner da organização, que consegue responder “quem recebeu o quê”; o gestor, cuja responsabilidade pelo que entrega (`D-054`) passa a poder ser comprovada; e o comprador, que ganha prova para compliance e LGPD.
- **Decisão que passa a ser possível** 🆕: deixar o gestor liberar dados e os agentes enviarem por canais externos, porque o owner consegue conferir depois quem fez o quê.
- **Prova de valor** 🆕: o owner Marcos pergunta “quem recebeu o board de vendas de outubro com os dados do Sul?”. A tela mostra que o gestor Pedro o publicou em 03/10, liberando os dados do Sul; que duas pessoas o abriram em 04/10; e que o agente o enviou por e-mail a doze pessoas em 05/10.
- **Retorno para o negócio** 🆕: faz do Horus um produto vendável a empresas com exigência de conformidade, e reduz o risco das liberações do gestor e dos envios dos agentes. Pode virar item de plano (`P-015`).
- **O que não inclui** 🆕: o conteúdo das perguntas e das respostas (`D-090`); a consulta pelo gestor ou pelo owner da instância (`D-091`); alertas automáticos de comportamento suspeito; exportar o rastro para sistemas de fora; bloquear ou desfazer uma entrega (o rastro só registra).
- **Depende de:** a MF-112:Boards e Relatórios (publicar e abrir); a MF-114:Módulo de Agendamentos de Agentes, a MF-115:Agentes ativos e a MF-113:Conectores de Saída (o que sai e por onde); a MF-102:Organizações, pessoas e papéis (owner, gestor e as preferências da organização).

**Contexto:** reúne as `D-082` e as `D-090` a `D-092`. O que veio do dono está marcado com ✅; os campos marcados com 🆕 foram propostos pelo PO e confirmados pelo dono.

**Hipóteses a validar:** a letra (w) da `P-008` (registrar quem abriu e quem entregou o quê sem guardar conteúdo). E 🔎 que os compradores corporativos peçam o rastro antes de liberar dados a outras pessoas e a canais externos, e que as pessoas aceitem que a abertura de boards seja registrada.

**Reabrir quando:** o arquiteto mostrar que o rastro não cabe na regra de telemetria, os gestores pedirem para ver o próprio rastro, ou o jurídico de um cliente exigir mais ou menos do que isso.

### D-092 · O owner define por quantos dias o rastro da auditoria fica guardado
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o **owner da organização** define, nas preferências da organização, **por quantos dias o rastro** da MF-116:Auditoria fica guardado. É o mesmo desenho do prazo de reserva do convite (`D-078`).

**Contexto:** terceira pergunta da definição macro da `P-019`. Complementa a `D-091`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. O owner define o prazo** | Ele escolhe, nas preferências, por quantos dias. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: cada organização se ajusta à sua regra jurídica. Contra: o owner pode escolher um prazo curto demais e perder a prova. |
| B. Prazo fixo do produto | A Maind define um prazo único. | ⚪ Não escolhida. Contra: pode não servir a um cliente que precise guardar por mais tempo. |
| C. Guardado para sempre | O rastro nunca é apagado. | ⚪ Não escolhida. Contra: o custo cresce sem parar, e guardar dados pessoais além do necessário vai contra a LGPD. |

**Por que esta:** cada cliente tem a sua regra jurídica, e o dono já usou esse desenho no prazo do convite.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 O que passa do prazo é apagado de vez, e o prazo vale para o rastro inteiro.
- 🔎 O valor padrão e o menor prazo permitido são assunto de desenho (arquiteto) e comercial, e não foram decididos.

**Reabrir quando:** algum cliente precisar de um prazo que o owner não consiga escolher, ou o jurídico exigir um prazo mínimo.

### D-091 · Só o owner da organização consulta o rastro da auditoria
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** quem consulta o rastro da MF-116:Auditoria é **só o owner da organização**, e ele consulta o rastro da organização inteira.

**Contexto:** segunda pergunta da definição macro da `P-019`. Complementa a `D-090`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Só o owner da organização** | Ele consulta o rastro da organização inteira. | ✅ Escolhida pelo dono. Pró: é simples, e o acesso fica concentrado numa pessoa só. Contra: o gestor, que responde pelo que entrega (`D-054`), não consegue ver o próprio rastro. |
| B. O owner e o gestor | O owner vê tudo; o gestor vê só o das pessoas que gere (`D-046`, `D-049`). Era a recomendação do PO. | ⚪ Não escolhida. Pró: cada um vê o que é da sua responsabilidade. Contra: o gestor passa a ver quem da equipe abriu o quê. |

**Por que esta:** o dono quis o acesso concentrado no owner, o que também evita que o gestor veja quem da equipe dele abriu o quê.

**Leitura do PO** *(confirmada pelo dono em 02/11/2026)*: 🔎 o owner da instância (`D-013`) **não** consulta o rastro das organizações; cada organização guarda o seu e só o owner dela o vê.

**Reabrir quando:** os gestores pedirem para ver o próprio rastro, ou um cliente exigir que o owner da instância o consulte.

### D-090 · O rastro da auditoria registra as entregas e quem as abriu
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o rastro da MF-116:Auditoria registra **o que o Horus entregou** e **quem abriu**: os boards e relatórios publicados, as liberações de dados do gestor (`D-051`, `D-054`), o que cada agente ou agendamento enviou, por qual conector e a quem, e quem abriu esses boards e relatórios, e quando. **Não registra o conteúdo** das perguntas e das respostas.

**Contexto:** primeira pergunta da definição macro da `P-019`. Refina a `D-082`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. As entregas e quem as abriu** | O rastro cobre o que saiu e quem abriu. Era a recomendação do PO. | ✅ Escolhida pelo dono. Pró: cobre o “quem viu e entregou” da `D-082` e comprova a responsabilidade do gestor. Contra: registrar quem abriu o quê é sensível para as pessoas (privacidade e LGPD). |
| B. Só as entregas | Registra o que saiu e para quem, mas não quem abriu. | ⚪ Não escolhida. Contra: não mostra quem de fato viu um board. |
| C. Também o que cada pessoa perguntou e viu | Além de A, guarda o conteúdo das perguntas e respostas. | ⚪ Não escolhida. Contra: quebra a regra de que a telemetria nunca carrega conteúdo de conversa, e é o mais pesado de guardar e de justificar. |

**Por que esta:** a `D-082` pede o rastro de “quem viu e entregou o quê”, e só a opção A cobre as duas partes sem guardar conteúdo.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 O rastro registra **quem fez, o quê (o board, o relatório ou o artefato), para quem, por qual conector e quando**, e não o conteúdo do que foi entregue.
- 🔎 Registrar quem abriu o quê pede um aviso às pessoas de que isso é registrado (assunto sensível, LGPD).

**Hipóteses a validar:** 🔎 *(técnica, vai ao arquiteto na `P-008`, letra (w))* O produto registra quem abriu e quem entregou o quê sem guardar conteúdo de conversa.

**Reabrir quando:** o arquiteto mostrar que o rastro não cabe na regra de telemetria, ou o jurídico de um cliente exigir mais ou menos do que isso.

### D-089 · Definição macro da MF-110:Pergunta rápida
Situação: 🟢 decidida (confirmada pelo dono em 01/11/2026) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** a MF-110:Pergunta rápida fica definida assim. Com ela, a `P-013` se fechou.

- **Nome:** MF-110:Pergunta rápida (proposta do PO; o dono pode renomear).
- **O que é** ✅: um **botão flutuante de chat** que abre um **popup** com a conversa de análise, para a pessoa perguntar sem sair da tela em que está (`D-065`).
- **Independente da tela** ✅: o popup abre a mesma conversa e **não sabe em que tela a pessoa está**; ela escreve a pergunta inteira (`D-085`).
- **Onde a conversa vive** ✅: a conversa **fica no popup**. A pessoa pode **limpar o chat**, e ao limpar o Horus lhe dá a opção de **salvar a conversa** (`D-086`).
- **O que vale na medida** ✅: a pergunta respondida **conta** na medida de autonomia e **pode receber** 👍🏻, 👎🏻 ou 🚫, **salva ou não** (`D-087`).
- **O que o popup oferece** ✅: **tudo o que a conversa de análise oferece**: os modos (dados, web e conversa), os níveis de inferência, a Análise avançada e a escolha do modelo, dentro do que as roles do owner permitem (`D-088`, `D-050`).
- **Quem vê o botão** 🆕: quem pode perguntar, ou seja, o owner, o gestor e o membro full. O **membro leitor não vê o botão** (`D-069`). Vale o que a pessoa já pode fazer na conversa de análise; um interruptor só para o popup, se vier, entra na `P-009`.
- **Em que telas aparece** 🆕: em todas as telas do app, **menos na própria conversa de análise**, onde ele seria repetido.
- **Quem ganha** 🆕: o gestor de área e o executivo, que tiram a dúvida na hora em que ela surge; e o comprador, porque mais perguntas se resolvem sem chamado.
- **Decisão que passa a ser possível** 🆕: tirar uma dúvida de negócio no instante em que ela aparece, sem trocar de tela nem interromper o que a pessoa está fazendo.
- **Prova de valor** 🆕: a gestora Carla, olhando o board de vendas, abre o botão, escreve “por que a filial Centro caiu?” e recebe a resposta sem sair do board. Limpa a conversa sem salvar, e a pergunta conta na medida. Em outra pergunta, ela salva e continua na tela de análise.
- **Retorno para o negócio** 🆕: mais perguntas por pessoa, que movem a medida-norte (`D-004`) e o saving da área de dados.
- **O que não inclui** 🆕: a pergunta que já sabe a tela em que a pessoa está (`D-085`); mais de uma conversa ao mesmo tempo no popup; o botão para o membro leitor; o chat pelo WhatsApp (MF-111) e a investigação guiada (MF-119).
- **Depende de:** a MF-107:Perguntar aos dados em português (a conversa); a MF-108:Respostas visuais; a MF-106:Segurança dos dados por pessoa (o que a pessoa vê continua valendo no popup); a MF-102:Organizações, pessoas e papéis (roles e tipos de assento); a MF-103:Licenças e planos (o leitor não pergunta).

**Contexto:** reúne as `D-065` e as `D-085` a `D-088`. O que veio do dono está marcado com ✅; os campos marcados com 🆕 foram propostos pelo PO e confirmados pelo dono.

**Hipóteses a validar:** a letra (r) da `P-008` (o motor responde de um popup, em qualquer tela, com todos os controles da conversa) e a (y) (contar a pergunta descartada sem guardar o conteúdo). E 🔎 que o gestor pergunte mais, e com mais frequência, quando a pergunta está a um clique da tela em que ele já está.

**Reabrir quando:** a medida de autonomia mostrar que a conversa completa já basta, ou o arquiteto mostrar que o popup não comporta o motor de conversa.

### D-088 · O popup da pergunta rápida oferece tudo o que a conversa de análise oferece
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o popup da MF-110:Pergunta rápida traz **tudo o que a conversa de análise oferece**: os modos (dados, web e conversa), os cinco níveis de inferência, a Análise avançada e a escolha do modelo de IA, dentro do que as roles do owner permitem (`D-050`).

**Contexto:** quarta pergunta da definição macro da `P-013`. Complementa a `D-085`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Tudo o que a conversa oferece** | O popup traz todos os controles da conversa de análise. | ✅ Escolhida pelo dono. Pró: não há diferença entre perguntar no popup e na tela de análise. Contra: o popup fica carregado e a construção é maior. |
| B. Só o essencial | O popup serve para perguntar e receber a resposta, com os padrões da pessoa. Era a recomendação do PO. | ⚪ Não escolhida. Pró: é leve. Contra: quem quer mudar o modo ou o nível precisa ir à tela de análise. |

**Por que esta:** o dono quer que o popup seja a conversa completa, e não uma versão reduzida.

**Fica de fora / adiado:** como encaixar todos esses controles numa janela pequena é desenho, e fica com o arquiteto de soluções (`P-008`, letra (r)).

**Hipóteses a validar:** 🔎 *(técnica, vai ao arquiteto na `P-008`)* O popup comporta todos os controles da conversa de análise em qualquer tela.

**Reabrir quando:** o arquiteto mostrar que os controles não cabem no popup sem prejudicar a pergunta rápida.

### D-087 · A pergunta rápida que a pessoa limpa sem salvar conta na medida de autonomia e recebe retorno como as outras
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** a pergunta respondida no popup da MF-110:Pergunta rápida **conta na medida de autonomia** (`D-004`) e **pode receber 👍🏻, 👎🏻 ou 🚫** (`D-005`), **salva ou não**. Quem limpa a conversa sem salvar perde o conteúdo; fica só a contagem.

**Contexto:** terceira pergunta da definição macro da `P-013`. Complementa a `D-086`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Conta igual** | A pergunta respondida entra na medida e recebe retorno, salva ou não. Era a recomendação do PO. | ✅ Escolhida pelo dono. |
| B. Só conta o que for salvo | A pergunta limpa sem salvar não conta nem recebe retorno. | ⚪ Não escolhida. Contra: subestima a autonomia, porque as perguntas rápidas, que são o objetivo do popup, ficam de fora. |

**Por que esta:** a medida-norte não pode deixar de fora justamente o uso dinâmico que o popup quer criar.

**Leitura do PO** *(confirmada pelo dono com a `D-129`, em 02/11/2026)*: 🔎 quando a pessoa reporta uma resposta (🚫), o Horus guarda aquela resposta para o owner da organização analisar (`D-014`), mesmo que a conversa seja limpa depois.

**Hipóteses a validar:**
- 🔎 *(técnica, vai ao arquiteto na `P-008`)* O produto conta a pergunta respondida sem guardar o conteúdo da conversa descartada, e guarda a resposta reportada até o owner analisá-la.

**Reabrir quando:** a medida de autonomia mostrar que contar as perguntas descartadas distorce o resultado.

### D-086 · A conversa da pergunta rápida fica no popup; a pessoa pode limpá-la e escolher salvar
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** a conversa da MF-110:Pergunta rápida **fica no popup**. Dentro do popup, a pessoa pode **limpar o chat**, e ao limpar o Horus lhe dá a opção de **salvar a conversa**.

**Contexto:** segunda pergunta da definição macro da `P-013`. Complementa a `D-085`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| A. Vira conversa normal | Tudo o que se pergunta no popup entra no histórico e pode ser continuado na tela de análise. Era a recomendação do PO. | ⚪ Não escolhida. Pró: toda pergunta conta e recebe retorno. Contra: o histórico enche de perguntas soltas. |
| B. Fica só no popup e some ao fechar | A pessoa vê a resposta e, ao fechar, a conversa se perde. | ⚪ Não escolhida como estava. Contra: perde a resposta se fechar sem querer. |
| **C. Fica no popup até a pessoa limpar, com a opção de salvar** | Variação da B proposta pelo dono: a conversa não some ao fechar, e salvar é uma escolha na hora de limpar. | ✅ Escolhida pelo dono. |

**Por que esta:** o dono quer o popup leve, sem encher o histórico, mas sem a pessoa perder a resposta por fechar o popup. Salvar vira uma escolha dela.

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 “Fica no popup” quer dizer que a conversa permanece enquanto a pessoa não a limpar, mesmo ao fechar o popup e ao trocar de tela.
- 🔎 A conversa salva vira uma conversa do histórico, aparece na tela de análise e pode ser continuada lá.
- 🔎 O popup tem uma conversa por vez.
- 🔎 Limpar sem salvar apaga a conversa de vez.

**Ponto que a definição macro ainda tem de resolver:** o que a pergunta que não foi salva vale para a medida de autonomia (`D-004`) e para o retorno do usuário (`D-005`).

**Hipóteses a validar:** 🔎 que a opção de salvar baste para a pessoa guardar o que importa sem encher o histórico.

**Reabrir quando:** os dados de uso mostrarem que quase ninguém salva, ou que as pessoas perdem respostas que queriam guardar.

### D-085 · A pergunta rápida é um atalho para a conversa de análise, independente da tela em que a pessoa está
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o popup da MF-110:Pergunta rápida abre a **mesma conversa de análise** e **não sabe em que tela a pessoa está**. A pessoa escreve a pergunta inteira.

**Contexto:** primeira pergunta da definição macro da `P-013`. Refina a `D-065`.

**Opções avaliadas:**

| Opção | Resumo | Resultado |
| --- | --- | --- |
| **A. Atalho para a conversa** | O popup abre o mesmo chat, sem saber a tela. | ✅ Escolhida pelo dono. |
| B. Com a tela | A pergunta já nasce sabendo o que a pessoa vê (board, filtro, gráfico). Era a recomendação do PO. | ⚪ Não escolhida. Pró: “por que essa filial caiu?” sem repetir nada. Contra: só pode aprofundar o que a pessoa já tem permissão de ver (`D-053`). |

**Por que esta:** o dono quis o chat independente da tela. É a opção mais simples e não cria dependência entre o popup e o que cada tela mostra; também evita a tensão com a `D-053`, em que a liberação do gestor vale só dentro do board.

**Fica de fora / adiado:** a pergunta que já nasce sabendo o que a pessoa vê (opção B). Na prova de valor da `D-065`, a Carla passa a escrever a pergunta inteira (“por que a filial Centro caiu?”), em vez de apontar a filial.

**Hipóteses a validar:** 🔎 que as pessoas perguntem mais e com mais frequência mesmo tendo de escrever o contexto.

**Reabrir quando:** a medida de autonomia mostrar que as pessoas desistem da pergunta rápida por terem de explicar o contexto.

### D-084 · Nova MF-111:Chat pelo WhatsApp, para conversar com o Horus pelo WhatsApp vendo o conteúdo como no chat
Situação: 🟢 decidida (a necessidade; o nome e o número são proposta do PO, e os detalhes estão em aberto) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o Horus precisa de uma macro funcionalidade (mf) nova, a **MF-111:Chat pelo WhatsApp**: a pessoa conversa com o Horus **pelo WhatsApp** e vê o conteúdo da resposta **como no chat** do produto. O dono a chamou de “possibilidade”: entra como candidata, e o desenho vem na definição macro.

**Contexto:** o dono acrescentou esta como a 18ª candidata, enquanto se definia a MF-119. Atende ao **problema nº 1 do norte, a pergunta de análise na hora** (`D-001`), e é a leitura mais literal da promessa “informação na palma da mão” e do pressuposto de qualquer dispositivo (`D-002`): a pergunta vai até o aplicativo que a pessoa já tem aberto. Pelo que a busca no código encontrou (01/11/2026), não há nada de WhatsApp no produto de hoje (🔎 a confirmar com o arquiteto). A única saída prevista para o WhatsApp é a de alertas e artefatos pelos conectores (`D-022`, `D-041`), e ela não recebe pergunta.

**Pontos que a definição macro terá de resolver** *(levantados pelo PO, na ordem em que serão perguntados ao dono)*:
1. Quem pode conversar: como o Horus sabe que o número do WhatsApp é de uma pessoa do Horus, e que ela vê só o que o Horus já a deixa ver (a MF-106:Segurança dos dados por pessoa continua valendo).
2. O que a resposta mostra: o gráfico, a tabela e o KPI chegam como imagem (WhatsApp não roda o gráfico vivo). O visual faz parte da promessa (`D-001`), então o que se perde precisa ser dito.
3. O que o WhatsApp faz e o que fica só no app (por exemplo, criar board, mudar o nível de inferência, escolher o modelo de IA).
4. Se é só WhatsApp ou qualquer mensageiro (Teams, Google Chat…), porque os conectores de saída já preveem vários canais (`D-033`).

**Leituras do PO** *(confirmadas pelo dono em 02/11/2026)*:
- 🔎 Quem pergunta pelo WhatsApp usa um assento que pode perguntar: owner, gestor ou membro full. O membro leitor não pergunta (`D-069`).
- 🔎 No modo “tudo dentro” o chat pelo WhatsApp fica bloqueado, porque o WhatsApp é serviço de fora (`D-010`, como os conectores na `D-040`).
- 🔎 Os conectores de saída (MF-113) só transportam e só entregam a usuários do Horus (`D-035`); o chat pelo WhatsApp é uma **via de entrada** e, portanto, outra coisa. Se vira parte da MF-113 ou fica separado, é decisão do dono na definição macro.

**Fica de fora / adiado:** o desenho (quem conversa, o que a resposta mostra, o que fica só no app, só WhatsApp ou vários mensageiros), a versão em que entra e a pontuação. Vira a definição macro da `P-020`.

**Hipóteses a validar:**
- 🔎 Que o gestor pergunte mais, e em mais lugares, quando a pergunta está no WhatsApp que ele já usa.
- 🔎 Que a resposta em imagem e texto entregue o conforto visual que a promessa pede.
- 🔎 *(técnica, vai ao arquiteto na `P-008`)* O produto comporta receber a pergunta do WhatsApp, ligar o número à pessoa e devolver a resposta com gráficos e tabelas em imagem, e quanto custa o canal oficial do WhatsApp (mensagens, janelas de resposta e modelos aprovados pela Meta).

**Prova de valor** *(proposta do PO)*: o gestor Pedro, no carro, manda pelo WhatsApp “como foram as vendas de ontem por região?”. Em segundos, recebe o gráfico e o resumo, e a pergunta não vira chamado à área de dados.

**Reabrir quando:** o arquiteto mostrar que o WhatsApp não comporta a resposta visual que a promessa pede, ou o custo do canal inviabilizar a oferta.

### D-083 · A melhoria do modelo semântico fica com o time de dados por enquanto
Situação: 🟢 decidida · Data: 01/11/2026 · Versão: geral

**Decisão:** o Horus **não** terá, na lista de candidatas à v2.0, o assistente que ajuda a montar e a melhorar o modelo semântico das fontes, nem a lista de perguntas que o Horus não soube responder. Montar e melhorar o modelo semântico continua sendo trabalho do **time de dados**, **por enquanto**.

**Contexto:** ao responder se faltava algo na lista, o dono ouviu três lacunas apontadas pelo PO e incluiu duas (`D-081`, `D-082`). Esta é a terceira, que ele deixou de fora. A lacuna era que o modelo semântico é um documento por fonte e que, se montá-lo depender de pessoas, a autonomia que o comprador paga já nasce dependente. O assistente de modelagem (o chat ajudar a montar o modelo) segue como “previsto e ainda não construído” no [mapa das mfs](04-macro-funcionalidades-de-hoje.md).

**Leitura do PO** *(confirmada pelo dono em 02/11/2026)*: 🔎 “o time de dados” é o da organização contratante, o mesmo que hoje monta dashboards sob encomenda, e o da Maind quando ela implanta a organização.

**Fica de fora / adiado:** o assistente de modelagem e a lista de perguntas sem resposta para o owner. O reporte do usuário (`D-005`, `D-014`) continua indo ao owner da organização, na candidata 2.

**Hipóteses a validar:** 🔎 que o time de dados consiga montar e manter o modelo semântico sem atrasar a implantação de uma organização nova.

**Prova de valor** *(proposta do PO)*: uma organização nova entra no ar sem esperar o modelo semântico além do prazo combinado com o cliente.

**Reabrir quando:** a implantação de organizações novas passar a depender demais de pessoas para montar o modelo, ou a medida de autonomia (candidata 4) mostrar muitas perguntas sem resposta por falha do modelo.

### D-082 · Nova MF-116:Auditoria, o rastro de quem viu e entregou o quê
Situação: 🟢 decidida (a necessidade; o nome e o número são proposta do PO) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o Horus precisa de uma macro funcionalidade (mf) nova, a **MF-116:Auditoria**: um **rastro** de quem viu e de quem entregou o quê a quem.

**Contexto:** lacuna apontada pelo PO e incluída pelo dono como a 17ª candidata. Dois pontos já decididos dependem dela: o gestor entrega dados acima das travas do banco dentro do board e “a responsabilidade é dele” (`D-054`), e os agentes entregam artefatos e alertas por WhatsApp, Teams e e-mail (`D-022`, `D-041`). Sem um registro de quem entregou o quê a quem, essa responsabilidade não tem como ser comprovada, e compradores corporativos pedem isso. Sustenta a **prova da confiança** do norte (`D-001`).

**Fica de fora / adiado:** o desenho (o que se registra, quem consulta, por quanto tempo se guarda), a versão em que entra e a pontuação. Vira a definição macro da `P-019`.

**Hipóteses a validar:**
- 🔎 Que o comprador e o owner peçam o rastro antes de liberar dados a outras pessoas e a canais externos.
- 🔎 *(técnica, vai ao arquiteto na `P-008`)* O produto comporta registrar quem viu e quem entregou o quê sem guardar conteúdo de conversa, porque a telemetria hoje nunca carrega conteúdo (regra do repositório).

**Prova de valor** *(proposta do PO)*: o owner pergunta “quem recebeu o board de vendas de outubro com os dados do Sul?” e o Horus mostra quem publicou, quem abriu e por qual conector o agente enviou.

**Reabrir quando:** o arquiteto mostrar que o rastro não cabe na regra de telemetria, ou o primeiro cliente corporativo dispensar o registro.

### D-081 · Nova MF-119:Investigação guiada, para a pessoa descobrir o porquê de uma mudança passo a passo
Situação: 🟢 decidida (a necessidade; o nome e o número são proposta do PO) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o Horus precisa de uma macro funcionalidade (mf) nova, a **MF-119:Investigação guiada**: a pessoa vê que algo mudou e o Horus a leva, passo a passo, até o porquê.

**Contexto:** o PO apontou que o **problema nº 2 do norte, a investigação** (`D-001`), era o único dos três sem nenhuma candidata. O dono incluiu esta como a 16ª. Hoje a investigação só existe pela conversa (perguntas em sequência, sugestões, “Análise avançada” e os níveis explicativo e de hipótese), sem um caminho guiado de “o que mudou e por quê” ([mapa das mfs](04-macro-funcionalidades-de-hoje.md)). 🔎 A confirmar com o arquiteto.

**Fica de fora / adiado:** o desenho (por onde a pessoa começa, como o Horus a guia, o que fica registrado do caminho percorrido), a versão em que entra e a pontuação. Vira a definição macro da `P-018`.

**Hipóteses a validar:**
- 🔎 Que o gestor chegue ao porquê de uma variação sem abrir chamado à área de dados.
- 🔎 *(técnica, vai ao arquiteto na `P-008`)* O motor de conversa comporta decompor uma variação nas partes que mais a explicam (por loja, produto, período) e guiar a pessoa passo a passo.

**Prova de valor** *(proposta do PO)*: na reunião de resultado, a gestora Carla vê a margem do Sul cair, pede a investigação e, em minutos, o Horus mostra que três lojas e um produto explicam a queda, cada passo com a fonte, sem chamado.

**Reabrir quando:** a conversa de análise já der conta do problema nº 2, segundo a medida de autonomia, ou o arquiteto mostrar que o guia não cabe no motor.

### D-080 · Definição macro da MF-103:Licenças e planos
Situação: 🟢 decidida (confirmada pelo dono em 01/11/2026) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** a MF-103:Licenças e planos fica definida assim. Com ela, a `P-014` se fechou.

- **Nome:** MF-103:Licenças e planos (proposta do PO; o dono pode renomear).
- **O que é:** a **cobrança do Horus por assentos e por plano**. A Maind libera e desativa os assentos de cada organização num **painel de controle**. Vale **só no SaaS**; o arquivo com chave e o on-premises ficaram para depois (`D-066`, `D-067`, `P-016`).
- **Os quatro tipos de assento** ✅: **owner**, **gestor**, **membro full** (pergunta, cria os próprios boards e alertas) e **membro leitor** (só vê boards de outras pessoas e recebe alertas e PDFs). A instalação traz **um assento de owner grátis**; o cliente solicita mais (`D-069`, `D-079`).
- **Quem libera e quem corta** ✅: o **administrador do SaaS**, no painel. **Não existe expiração** no produto: a validade é assunto comercial (`D-068`).
- **Como a pessoa entra** ✅: o **gestor cria o convite** e escolhe o tipo de assento; o **owner aprova**; a aprovação envia o e-mail e **reserva o assento por N dias**, que o **owner define** nas preferências da organização; passado o prazo, o convite expira e o assento volta a ficar livre (`D-071`, `D-078`). **Sem assento livre do tipo, a pessoa não entra** (`D-070`).
- **Como o tipo muda** ✅: a troca segue o mesmo caminho do convite (`D-072`). Quando alguém passa de full a leitor, o que ela criou vai para a área da organização (`D-073`).
- **Como se conta** ✅: quem acumula owner e gestor ocupa **um assento só** (`D-074`).
- **Mais e menos assentos** ✅: o owner **pede mais fora do produto**, por contato comercial (`D-077`). O painel **não reduz** abaixo do que está ocupado; o owner libera antes (`D-076`).
- **O corte** ✅: quando o administrador **desativa os assentos**, as pessoas perdem a permissão e os agendamentos, alertas e agentes da organização **param**; as configurações ficam guardadas (`D-068`, `D-075`).
- **Quem ganha** 🆕: a Maind, que cobra por quem usa e corta quando o cliente não paga; e o owner da organização, que sabe quanto tem, quanto usa e quanto sobra, e decide quem entra.
- **Decisão que passa a ser possível** 🆕: vender o Horus por tamanho e por plano e cortar o acesso de quem não paga, sem depender de uma data dentro do produto.
- **Prova de valor** 🆕: a Maind libera, para a organização da Carla, o assento de owner grátis, 30 assentos de membro full e 100 de membro leitor. O gestor Pedro cria o convite de um analista como membro full; a Carla aprova; o e-mail sai e o assento fica reservado. Quando faltam assentos, a Carla pede mais à Maind. Se a empresa deixa de pagar, o administrador desativa os assentos e nada roda.
- **Retorno para o negócio** 🆕: faz do Horus um produto vendável, com receita por assento e por plano.
- **O que não inclui** 🆕: o arquivo com chave e a data de expiração no produto (`D-067`, `D-068`); o on-premises (`P-016`); os planos, com nomes, preços e o que cada um inclui (`P-015`); um botão ou fila de pedidos de assento dentro do produto (`D-077`); a cobrança e o pagamento em si, que a Maind faz fora do produto; a cobrança por uso do mês (não escolhida na `D-069`).
- **Depende de:** a MF-102:Organizações, pessoas e papéis (papéis, convites e quarentena); a MF-101:Administração da instância (o painel de controle); a MF-114:Módulo de Agendamentos de Agentes e a MF-115:Agentes ativos (que param no corte); a MF-112:Boards e Relatórios (a área da organização); a MF-113:Conectores de Saída (o leitor recebe).

**Contexto:** reúne as `D-066` a `D-079`. O que veio do dono está marcado com ✅; os campos marcados com 🆕 foram propostos pelo PO e confirmados pelo dono.

**Hipóteses a validar:** as letras (s), (t) e (u) da `P-008` (guardar os assentos, ter mais de um owner e os quatro tipos de assento, o gestor convidar com a aprovação do owner). E 🔎 que os clientes aceitem a cobrança por assento e por tipo (`D-066`) e que o assento de owner grátis não prejudique a receita (`D-074`).

**Reabrir quando:** o modelo de cobrança mudar (por exemplo, por consumo), ou surgir o primeiro cliente on-premises (`P-016`).

### D-079 · O membro leitor recebe alertas e PDFs pelos conectores
Situação: 🟢 decidida (as leituras do PO foram confirmadas pelo dono em 02/11/2026) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o **membro leitor** pode ser destinatário de **alertas e PDFs** entregues pelos conectores de saída (`D-035`). Receber não é criar.

**Contexto:** pergunta ao dono com três opções: **A**, o leitor recebe; **B**, o leitor só vê boards dentro do Horus; **C**, o owner liga ou desliga. Exemplo: o diretor da Carla é membro leitor, e toda segunda-feira o gestor Pedro agenda o PDF do board de vendas para o WhatsApp da diretoria. O dono escolheu a opção A.

**Consequências:**
- O leitor da `D-069`, que “só vê boards criados por outros”, passa também a **receber** o que outros geram.
- O custo de gerar o PDF e de rodar o agente fica no assento de quem agendou.
- 🔎 Leituras do PO *(confirmadas pelo dono em 02/11/2026)*:
  - O leitor não cria nem agenda nada. Só recebe.
  - Ele pode ser destinatário por nome ou por grupo (`D-029`).
- ⚠️ Quando o gestor ou o owner entrega dados a outras pessoas por um artefato (`D-059`), isso alcança também quem só lê, com a responsabilidade de quem entregou (`D-054`).

**Fica de fora / adiado:** nada.

**Hipóteses a validar:** nenhuma nova.

**Prova de valor** *(proposta do PO)*: o diretor, como membro leitor, recebe toda segunda o PDF do board de vendas, sem entrar no Horus.

**Reabrir quando:** algum cliente pedir que o leitor não receba artefatos, ou a segurança questionar a entrega a quem só lê.

### D-078 · O owner define, nas preferências da organização, por quantos dias o assento fica reservado para um convite
Situação: 🟢 decidida (as leituras do PO foram confirmadas pelo dono em 02/11/2026) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o **número de dias (N)** da reserva do assento no convite (`D-071`) é definido pelo **owner**, nas **preferências da organização**: um número só para a organização inteira.

**Contexto:** pergunta ao dono com três opções: **A**, número fixo no produto; **B**, o owner define nas preferências da organização; **C**, o gestor escolhe a cada convite. Exemplo: a Carla aprovou o convite de uma diretora que está de licença por dez dias. O dono escolheu a opção B.

**Consequências:**
- Cada empresa ajusta o prazo ao seu ritmo, no mesmo lugar onde o owner já liga e desliga as aprovações (`D-039`) e a publicação pelos gestores (`D-042`).
- 🔎 Leituras do PO *(confirmadas pelo dono em 02/11/2026)*:
  - O produto traz um **valor inicial** e um **teto** para o prazo, para o owner não deixar assentos parados. Os números ficam para o desenho.
  - Mudar o prazo vale para os convites **novos**. Os que já estão com o assento reservado seguem o prazo com que foram aprovados.

**Fica de fora / adiado:** o valor inicial e o teto do prazo (desenho).

**Hipóteses a validar:** nenhuma nova.

**Prova de valor** *(proposta do PO)*: a Carla ajusta o prazo da reserva para 15 dias; o convite que ela aprova depois disso mantém o assento guardado por 15 dias.

**Reabrir quando:** os owners deixarem assentos parados por prazos longos, sinal para um prazo fixo.

### D-077 · O owner pede mais assentos fora do produto, por contato comercial com a Maind
Situação: 🟢 decidida (as leituras do PO foram confirmadas pelo dono em 02/11/2026) · Data: 01/11/2026 · Versão: a pontuar

**Decisão:** o pedido de **mais assentos** se faz **fora do produto**: o owner fala com a Maind por contato comercial, e o administrador do SaaS libera no painel (`D-068`). O produto não tem botão nem fila de pedidos de assentos.

**Contexto:** pergunta ao dono com três opções: **A**, fora do produto; **B**, dentro do produto, com fila no painel; **C**, dentro do produto, só abrindo um e-mail pronto. Exemplo: a Carla, owner, quer aprovar o convite de um analista, mas os 40 assentos de membro full estão ocupados. O dono escolheu a opção A.

**Consequências:**
- Nada a construir para o pedido, e combina com a ideia de que a cobrança é assunto comercial (`D-068`).
- O pedido não deixa rastro no Horus.
- 🔎 Leituras do PO *(confirmadas pelo dono em 02/11/2026)*:
  - Para o convite do gestor não ficar parado sem explicação, o owner vê, no pedido pendente, que **falta assento livre do tipo** pedido (`D-071`).
  - O produto mostra ao owner a contagem dos assentos de cada tipo: quantos tem, quantos usa e quantos estão livres (`D-070`, `D-076`).

**Fica de fora / adiado:** um botão ou fila de pedidos dentro do produto.

**Hipóteses a validar:** nenhuma nova.

**Prova de valor** *(proposta do PO)*: a Carla vê que faltam assentos, pede mais por contato comercial, o administrador libera no painel, e o convite do analista é aprovado.

**Reabrir quando:** o volume de pedidos crescer ao ponto de a Maind precisar de rastro e de fila dentro do produto, ou quando os clientes se perderem no contato comercial.

### D-076 · O painel não deixa reduzir os assentos abaixo do que está ocupado; o owner libera antes
Situação: 🟢 decidida (as leituras do PO foram confirmadas pelo dono em 02/11/2026) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** o administrador do SaaS **não consegue reduzir** os assentos de um tipo para menos do que está **ocupado**. Antes, o owner da organização **libera assentos**, removendo pessoas ou trocando o tipo delas (`D-072`). Só então o administrador reduz.

**Contexto:** pergunta ao dono com três opções: **A**, o painel não deixa reduzir abaixo do ocupado; **B**, reduz e corta os últimos que entraram; **C**, reduz e o owner escolhe quem perde o acesso. Exemplo: a organização da Carla tinha 40 assentos de membro full, todos ocupados, e renovou com 30. O dono escolheu a opção A.

**Consequências:**
- Ninguém perde o acesso por surpresa, e a escolha de quem sai fica com quem conhece a empresa.
- Nunca existe mais gente que assentos, o que combina com a `D-070`.
- 🔎 Leituras do PO *(confirmadas pelo dono em 02/11/2026)*:
  - Os assentos **reservados** para convites pendentes (`D-071`) contam como ocupados na hora de reduzir.
  - Remover uma pessoa leva o que ela criou para a área da organização (`D-044`); trocar o tipo dela para leitor também (`D-073`).
  - O owner enxerga o que precisa liberar: quantos assentos tem de cada tipo, quantos usa e quantos estão livres (`D-070`).
- ⚠️ A empresa pode empacar e não liberar. Nesse caso, a alavanca do administrador é o corte total (`D-075`), que é uma decisão comercial (`D-068`).

**Fica de fora / adiado:** nada.

**Hipóteses a validar:** nenhuma nova.

**Prova de valor** *(proposta do PO)*: a Carla tem 40 assentos de membro full ocupados e renovou com 30; o painel recusa a redução até ela liberar 10; depois que ela libera, o administrador reduz para 30.

**Reabrir quando:** as empresas empacarem com frequência, sinal para outro caminho de redução.

### D-075 · Quando o administrador desativa os assentos de uma organização, os agendamentos, alertas e agentes dela também param
Situação: 🟢 decidida (as leituras do PO foram confirmadas pelo dono em 02/11/2026) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** quando o administrador do SaaS **desativa os assentos** de uma organização (`D-068`), **param junto com as pessoas** os agendamentos, os alertas e os agentes dela. Nada roda nem é enviado enquanto os assentos estiverem desativados. As **configurações ficam guardadas** e voltam quando o administrador reativar.

**Contexto:** pergunta ao dono com três opções: **A**, param junto com as pessoas; **B**, continuam rodando; **C**, o administrador escolhe na hora de desativar. Exemplo: a organização da Carla deixou de pagar; toda segunda-feira às 8h um agente analisa as vendas e manda um alerta à diretoria pelo WhatsApp. O dono escolheu a opção A.

**Consequências:**
- O corte é completo: sem pagamento, o produto para, e a Maind não gasta recurso de IA à toa.
- 🔎 Leituras do PO *(confirmadas pelo dono em 02/11/2026)*:
  - Vale para os dois itens do agendamento (`D-064`): o PDF de um board e o agente.
  - As rodadas que não aconteceram durante a pausa **não são refeitas** quando os assentos voltam; o agendamento segue do próximo horário.
  - Os dados, os boards, as conversas e as configurações ficam guardados.
- ⚠️ Um alerta que a diretoria usa para decidir deixa de chegar sem aviso. É o custo de cortar, e a decisão comercial de cortar é da Maind (`D-068`).

**Fica de fora / adiado:** o que acontece quando o administrador **reduz** os assentos para menos do que as pessoas que já os ocupam (`P-014`).

**Hipóteses a validar:** nenhuma nova. A letra (s) da `P-008` foi ajustada.

**Prova de valor** *(proposta do PO)*: o administrador desativa os assentos de uma organização inadimplente; na segunda seguinte, nenhum agente roda nem nenhum alerta sai. Ao reativar, os agendamentos voltam sem precisar ser refeitos.

**Reabrir quando:** algum cliente crítico precisar manter alertas durante a negociação, sinal para voltar à opção em que o administrador escolhe.

### D-074 · Quem acumula os papéis de owner e de gestor ocupa um assento só, o de owner
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a pessoa que acumula os papéis de **owner** e de **gestor** (`D-048`) ocupa **um assento só**, o de **owner**. O assento é da pessoa, e ela não paga duas vezes.

**Contexto:** pergunta ao dono com duas opções: **A**, um assento só, o de owner; **B**, dois assentos, um de owner e um de gestor. Exemplo: a Carla é owner e, como a equipe é pequena, também gere cinco pessoas. O dono escolheu a opção A.

**Consequências:**
- O assento de owner grátis (`D-069`) cobre os dois papéis. Uma organização de uma pessoa só pode usar o produto inteiro sem pagar.
- 🔎 Leitura do PO *(encerrada em 02/11/2026: com o plano único, o assento grátis alcança tudo da v2.0, `D-115`)*: o alcance real desse assento grátis depende do que cada plano inclui (`P-015`). Se o plano limitar funcionalidades, o assento grátis também fica limitado por ele.
- ⚠️ Para o dono pesar na `P-015`: um owner que acumula o papel de gestor e cria boards (`D-048`) usa o que um gestor e um membro full usam, com um assento só.

**Fica de fora / adiado:** o que cada plano inclui e o alcance do assento grátis (`P-015`).

**Hipóteses a validar:** nenhuma nova.

**Prova de valor** *(proposta do PO)*: a Carla, owner e gestora ao mesmo tempo, ocupa um assento só, e a contagem de assentos do painel mostra uma pessoa, e não duas.

**Reabrir quando:** as organizações de uma pessoa só passarem a usar o produto inteiro de graça e isso pesar na receita.

### D-073 · Quando alguém passa de membro full a leitor, o que ela criou vai para a área da organização
Situação: 🟢 decidida (as leituras do PO foram confirmadas pelo dono em 02/11/2026) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** quando uma pessoa passa de **membro full a membro leitor** (`D-072`), os **boards, alertas e agendamentos que ela criou** vão para a **área da organização**. É a mesma regra de quando o autor sai da organização (`D-044`, `D-045`): o owner **transfere** para qualquer pessoa da organização ou **exclui**, e os agendamentos ficam **pausados** ali.

**Contexto:** pergunta ao dono com três opções: **A**, ficam guardados e pausados em nome da pessoa; **B**, vão para a área da organização; **C**, continuam funcionando. Exemplo: o analista do gestor Pedro criou 3 boards e 2 alertas semanais para a diretoria, e vira leitor. O dono escolheu a opção B.

**Consequências:**
- O leitor não mantém recursos de membro full (alertas e agendamentos) rodando, o que preserva o modelo de assentos.
- Reaproveita uma regra que já existe, e a posse fica sempre clara.
- 🔎 Leituras do PO *(confirmadas pelo dono em 02/11/2026)*:
  - Vale também para os **agentes** que a pessoa criou, além de boards, alertas e agendamentos.
  - Se ela voltar a ser full, **nada volta sozinho**: o owner devolve à mão o que quiser, transferindo.
  - O board conserva o status que tinha (`D-045`). Na área da organização, a pessoa só o vê se a visibilidade do board o permitir.
  - Com que alcance de dados rodam, na área da organização, os agendamentos e agentes que passaram a ser da organização é a hipótese (o) da `P-008`, que já existe.

**Fica de fora / adiado:** o que acontece com as pessoas e com o que elas criaram quando o administrador do SaaS desativa os assentos (`P-014`).

**Hipóteses a validar:** nenhuma nova.

**Prova de valor** *(proposta do PO)*: o analista do Pedro vira leitor; os boards e alertas dele vão para a área da organização, e a Carla, owner, transfere dois boards à gestora Júlia e exclui o resto. Se o analista voltar a ser full, a Carla devolve o que quiser.

**Reabrir quando:** os owners reclamarem do trabalho de devolver o conteúdo quando a pessoa volta a ser full.

### D-072 · A troca do tipo de assento segue o caminho do convite: o gestor pede, o owner aprova, e precisa haver assento livre do tipo novo
Situação: 🟢 decidida (as leituras do PO foram confirmadas pelo dono em 02/11/2026) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** depois que a pessoa entrou, **trocar o tipo do assento dela** segue o mesmo caminho do convite (`D-071`): o **gestor pede**, o **owner aprova**, e precisa existir um **assento livre do tipo novo** (`D-070`).

**Contexto:** pergunta ao dono com três opções: **A**, o mesmo caminho do convite; **B**, só o owner troca; **C**, não troca (novo convite). Exemplo: o analista do gestor Pedro entrou como membro leitor e, dois meses depois, deve passar a membro full. O dono escolheu a opção A.

**Consequências:**
- Uma regra só para a pessoa entrar e para trocar de tipo, e o owner continua controlando o custo.
- 🔎 Leituras do PO *(confirmadas pelo dono em 02/11/2026)*:
  - Aprovada a troca, o assento antigo volta a ficar livre na hora e o novo é ocupado. Não há reserva de N dias, porque a pessoa já está dentro.
  - A regra vale nos dois sentidos: passar de full para leitor também pede a aprovação do owner e um assento de leitor livre.
  - O owner troca o tipo de qualquer pessoa sem pedido, como convida sem aprovação.
  - O pedido de troca entra no mesmo tipo de aprovação do convite, com o mesmo interruptor do owner (`D-039`).
- *(Respondida pela `D-073`.)* Surge uma pergunta nova na `P-014`: o que acontece com os boards, alertas e agendamentos que a pessoa criou como membro full quando ela passa a membro leitor.

**Fica de fora / adiado:** o que acontece com o que a pessoa criou quando passa a leitora (`P-014`).

**Hipóteses a validar:** nenhuma nova. A letra (u) da `P-008` foi ajustada.

**Prova de valor** *(proposta do PO)*: o gestor Pedro pede a troca do analista de leitor para full; a Carla, owner, aprova; o assento de leitor volta a ficar livre, o de full é ocupado, e o analista passa a perguntar e a criar boards.

**Reabrir quando:** o volume de pedidos pesar para o owner, sinal para a aprovação automática.

### D-071 · O gestor cria o convite e escolhe o tipo de assento; o owner aprova; a aprovação envia o e-mail e reserva o assento por N dias
Situação: 🟢 decidida (as leituras do PO foram confirmadas pelo dono em 02/11/2026) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- O **gestor cria o convite** e **escolhe o tipo de assento**, **mesmo que não haja assento livre** daquele tipo.
- O pedido vai para a **aprovação do owner**.
- Ao aprovar, o **e-mail do convite é enviado** e o **assento é reservado por N dias** para esse convite.
- Passados os N dias, o **convite expira** e o assento volta a ficar **disponível**.

**Contexto:** pergunta ao dono: “quem escolhe se o membro é full ou leitor?”. Opções do PO: **A**, só o owner; **B**, o owner e o gestor; **C**, o gestor pede e o owner aprova. O dono foi pela C e acrescentou a reserva do assento.

**Consequências:**
- Responde à pergunta “quem escolhe o tipo”: o gestor escolhe no convite, e o owner aprova.
- **Refina a `D-056` e a `D-047`**: até aqui só o owner emitia convites, e “convite emitido por gestor” estava fora da definição. O convite continua sendo da organização.
- Combina com a `D-070`: a falta de assento não impede o **pedido**, mas a aprovação é o momento em que o assento é reservado.
- 🔎 Leituras do PO *(confirmadas pelo dono em 02/11/2026)*:
  - O gestor que cria o convite fica indicado nele, e a pessoa já entra na carteira dele (`D-047`).
  - O owner também cria convites, sem passar por aprovação, e a reserva funciona igual.
  - Para aprovar, o owner precisa de um assento livre do tipo pedido (`D-070`). Sem ele, solicita mais ao administrador do SaaS antes.
  - O gestor escolhe entre membro full e membro leitor. Assentos de owner e de gestor continuam sendo criados só pelo owner.
  - Quem aceita o convite ocupa o assento do tipo do convite, inclusive na quarentena (quando o owner convida sem indicar gestor). Isso responde à pergunta antiga “qual assento ocupa quem está na quarentena”.
  - O pedido do gestor entra nos tipos de aprovação que o owner liga ou desliga (`D-039`): ele pode deixar a aprovação automática.
  - Se o owner recusa, nada é enviado e nenhum assento é reservado. Se o convite expira, o gestor pede de novo.
- *(Respondida pela `D-078`.)* Sobra uma pergunta na `P-014`: quantos dias vale a reserva (N) e quem define esse número.

**Fica de fora / adiado:** o valor de N; a troca do tipo depois que a pessoa entrou (`P-014`).

**Hipóteses a validar:** 🔎 *(técnica, vai ao arquiteto na `P-008`, letra u)* Hoje o gestor não convida (o papel nasce sem a chave dos convites). O produto comporta o gestor criar o convite, o fluxo de aprovação do owner e a reserva do assento por prazo.

**Prova de valor** *(proposta do PO)*: o gestor Pedro cria o convite de um analista como membro full; a Carla, owner, aprova; o e-mail sai e o assento fica reservado. O analista aceita e ocupa o assento. Se não aceitasse no prazo, o convite expiraria e o assento voltaria a ficar livre.

**Reabrir quando:** os gestores reclamarem da espera pela aprovação, ou o owner virar gargalo, sinal para a aprovação automática do convite.

### D-070 · Quando os assentos de um tipo acabam, a pessoa não entra naquele tipo até o administrador liberar mais
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** se não há assento livre de um tipo, a pessoa **não passa a ocupá-lo**. O owner solicita mais assentos, o administrador do SaaS os libera no painel (`D-068`), e só então a pessoa entra.

**Contexto:** pergunta ao dono com três opções: **A**, bloquear; **B**, deixar entrar e avisar, com a cobrança do excesso depois; **C**, deixar a pessoa em espera. Exemplo: a organização tem 40 assentos de membro full, todos ocupados, e convida o 41º colega. O dono escolheu a opção A.

**Consequências:**
- Responde ao ponto 3 da `D-066`: o que a empresa usa sempre bate com o que contratou e paga, e nunca sobra excesso a cobrar depois.
- 🔎 Leituras do PO *(confirmadas pelo dono em 02/11/2026)*:
  - Vale também para trocar o tipo de uma pessoa que já está dentro (por exemplo, de leitor para full): precisa de assento livre do tipo novo.
  - O owner enxerga, de cada tipo, quantos assentos tem, quantos usa e quantos estão livres.
- *(Respondida pela `D-077`.)* Sobra uma pergunta na `P-014`: como o owner solicita mais assentos (por um pedido dentro do produto ou fora dele, num contato comercial).

**Fica de fora / adiado:** o canal do pedido de mais assentos (`P-014`).

**Hipóteses a validar:** nenhuma nova.

**Prova de valor** *(proposta do PO)*: a Carla tem 40 assentos de membro full ocupados e convida o 41º colega; ele não entra. Ela solicita mais, o administrador libera no painel, e o colega entra.

**Reabrir quando:** os clientes reclamarem de esperar a liberação, o que seria o sinal para voltar à opção de deixar entrar e avisar.

### D-069 · Os assentos têm quatro tipos: owner, gestor, membro full e membro leitor; a instalação traz um assento de owner grátis
Situação: 🟢 decidida (a diretriz; os detalhes seguem em perguntas na `P-014`; o assento de owner grátis é **um por organização**, pela `D-123`, de 02/11/2026, que fechou o `I-013`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- Há **quatro tipos de assento**: **owner**, **gestor**, **membro full** e **membro leitor**.
- A instalação vem com **um assento de owner grátis**. O cliente pode **solicitar mais assentos** quando quiser.
- O **membro full** faz perguntas, cria os próprios boards, cria alertas e o mais que a função do membro permite.
- O **membro leitor** só vê boards criados por outros usuários.

**Contexto:** resposta do dono à pergunta “quem ocupa um assento?”, que tinha as opções de contar toda pessoa com conta, toda pessoa menos a quarentena, ou só quem usou no mês. O dono não escolheu uma: trocou a pergunta por **tipos de assento**.

**Consequências:**
- Responde a pergunta nº 2 da `D-066` no geral: cada pessoa ocupa um assento do tipo da função dela.
- **Refina a `D-066`**: os assentos passam a ser por tipo. **Refina a `D-042`** (quem cria boards): o membro leitor não cria boards.
- 🔎 Leituras do PO *(as duas primeiras confirmadas pelo dono em 02/11/2026; a terceira se encerrou, porque o preço ficou fora dos documentos de produto, `D-116`)*:
  - “Solicitar mais” vale para qualquer tipo, inclusive o de owner (uma organização com mais de um owner). Só o primeiro assento de owner é grátis.
  - O administrador do SaaS libera, no painel, a quantidade de cada tipo (`D-068`).
  - O preço de cada tipo é assunto da `P-015`.
- *(Respondidas pelas `D-070` a `D-074`.)* Sobram detalhes, que viram perguntas da `P-014`: o que acontece quando os assentos de um tipo acabam; qual assento ocupa quem está na quarentena; se quem acumula owner e gestor (`D-048`) ocupa um ou dois assentos; quem escolhe se o membro é full ou leitor, e se dá para trocar; se o leitor recebe alertas e PDFs pelos conectores.

**Fica de fora / adiado:** o preço de cada tipo e o que cada plano inclui (`P-015`).

**Hipóteses a validar:**
- 🔎 Que a divisão entre membro full e membro leitor seja o degrau que o cliente espera.
- 🔎 *(técnica, vai ao arquiteto na `P-008`)* A organização comporta mais de um owner e os quatro tipos de assento.

**Prova de valor** *(proposta do PO)*: a organização começa com o assento de owner grátis; a Maind libera no painel gestores, membros full e membros leitores; a diretoria, como leitora, passa a ver os boards sem poder perguntar nem criar.

**Reabrir quando:** surgir um quinto tipo de pessoa (por exemplo, o convidado externo), ou o preço por tipo pedir outra divisão.

### D-068 · No SaaS, quem desativa os assentos é o administrador do SaaS, e o produto não tem data de expiração
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- No modo SaaS, **desativar os assentos** (seats) é papel do **administrador do SaaS**.
- **Não existe expiração** no produto. A validade da licença e o que fazer com o cliente que não paga são assunto **comercial**, mais do que técnico.

**Contexto:** resposta do dono à pergunta “quando a licença vence e não é renovada, o que acontece com o acesso?”, que tinha as opções de corte no dia, carência avisada e só leitura. Em vez de escolher uma, o dono tirou o vencimento do produto.

**Consequências:**
- **Refina a `D-066` e a `D-067`**: sai a data de expiração (e a “validade” dos assentos). O painel de controle libera e desativa assentos, sem relógio.
- A pergunta nº 1 da `D-066` (o que acontece no vencimento) **deixa de existir**. A carência, o aviso ao owner e o prazo de corte passam a ser escolha comercial da Maind, sem regra no produto.
- A pergunta nº 4 da `D-066` (quem libera os assentos) **está respondida**: o administrador do SaaS.
- 🔎 Leitura do PO *(confirmada pelo dono em 02/11/2026)*: o “administrador do SaaS” é o owner da instância (`D-013`), com os administradores da instância (MF-101:Administração da instância).
- Surge uma pergunta nova para a definição macro: o que acontece com as pessoas, e com o que elas criaram, quando o administrador desativa os assentos de uma organização.

**Fica de fora / adiado:** a política comercial de cobrança, carência e corte (da Maind, fora do produto) e o on-premises (`P-016`).

**Hipóteses a validar:** nenhuma nova. A letra (s) da `P-008` foi ajustada.

**Prova de valor** *(proposta do PO)*: a Maind libera 50 assentos a uma organização; se a empresa deixa de pagar, o administrador do SaaS desativa os assentos no painel e as pessoas perdem a permissão, sem que o produto dependa de nenhuma data.

**Reabrir quando:** o modelo de cobrança pedir renovação automática, ou o on-premises (`P-016`) precisar de uma validade.

### D-067 · A licença é liberada pelo painel de controle, só no modo SaaS; o arquivo com chave e o on-premises ficam para depois
Situação: 🟢 decidida · refinada pela `D-068` (não há data de expiração) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- Esquece-se, por ora, o **arquivo com chave** que a organização importaria.
- A **configuração e a liberação dos assentos** (seats) se fazem por um **painel de controle**.
- Vale **apenas no modo SaaS**. Como ativar assentos numa instalação **on-premises**, na infraestrutura do cliente, fica para depois (`P-016`).

**Contexto:** o dono completou a `D-066` enquanto a pergunta “o que acontece quando a licença vence” estava aberta. A cobrança por usuários e por plano, os assentos com validade e a desabilitação dos usuários sem pagamento da `D-066` continuam de pé.

**Consequências:**
- **Refina a `D-066`**: sai a importação do arquivo; entra o painel de controle. A pergunta nº 4 da `D-066` (quem importa o arquivo e se a conferência é sem internet) vira “quem libera os assentos no painel”; a parte do on-premises vai para a `P-016`.
- Combina com a `D-016` (SaaS primeiro).
- 🔎 Leitura do PO *(confirmada pelo dono em 02/11/2026)*: o painel é o da instância (MF-101:Administração da instância), e quem libera os assentos é o owner da instância, que no SaaS é a Maind (`D-013`), e não o owner da organização.
- ⚠️ Tensão com a `D-017` (a mesma versão em SaaS e on-premises): até a `P-016`, a instalação on-premises fica sem o controle de assentos, e o produto não faz a cobrança ali.

**Fica de fora / adiado:** o on-premises (`P-016`) e a ideia do arquivo com chave.

**Hipóteses a validar:** nenhuma nova. A letra (s) da `P-008` foi ajustada ao painel e ao SaaS.

**Prova de valor** *(proposta do PO)*: a Maind libera, no painel, 50 assentos a uma organização do SaaS; no vencimento sem renovação, o acesso muda como a regra decidir.

**Reabrir quando:** surgir o primeiro cliente on-premises, ou a cobrança do SaaS exigir que a própria organização gerencie a licença.

### D-066 · Nova MF-103:Licenças e planos, para cobrar por usuários e por plano e cortar o acesso quando a licença vence
Situação: 🟢 decidida (a necessidade; o nome e o número são proposta do PO, e os detalhes estão em aberto) · refinada pela `D-067` (o arquivo com chave saiu; vale o painel de controle, só no SaaS) pela `D-068` (não há data de expiração) e pela `D-069` (os assentos têm quatro tipos) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- O Horus será cobrado pela **quantidade de usuários** e pelo **plano** da plataforma. O dono deu como exemplo **Básico, Gold e Diamond**, “algo assim”: os nomes e o número de planos não estão decididos.
- Cada organização poderá **importar um arquivo com uma chave** que libera a **licença**: uma quantidade de **assentos** (seats) com **data de expiração**.
- Quando não houver pagamento das licenças, a **permissão dos usuários é desabilitada**.

**Contexto:** resposta do dono à pergunta “você tem mais alguma candidata além da pergunta rápida?”. Ele acrescentou esta como a 15ª e pediu ajuda para pensar nela. Não atende a um dos três problemas do norte: sustenta o negócio da Maind (o retorno) e faz a cobrança ser cumprida.

**Pontos que a definição macro terá de resolver** *(levantados pelo PO, na ordem em que serão perguntados ao dono)*:
1. O que acontece com o acesso quando a licença vence e não é renovada.
2. Quem ocupa um assento (quem tem conta, quem está ativo, quem é owner, gestor ou membro, quem está na quarentena).
3. O que acontece quando o número de pessoas passa do número de assentos.
4. Quem importa o arquivo (o owner da organização ou o owner da instância, `D-013`) e se o Horus precisa conferir a licença sem internet, no on-premises.
5. O que cada plano inclui: vai para a `P-015`, porque é assunto comercial e pode esperar.

**Leituras do PO** *(encerradas em 02/11/2026: o preço ficou fora dos documentos de produto, `D-116`; a v2.0 tem um plano só, que não limita funcionalidades, `D-115`; e o arquivo com chave saiu, `D-067`)*:
- 🔎 O preço é a conta de assentos por plano.
- 🔎 O plano limita as funcionalidades da organização inteira, como as roles (`D-050`) limitam as da pessoa. Isto depende da `P-015`.
- 🔎 O mesmo arquivo serve ao SaaS e ao on-premises, porque a versão é a mesma (`D-017`).

**Fica de fora / adiado:** nomes, quantidade e preço dos planos e o que cada um inclui (`P-015`); o desenho, a versão em que entra e a pontuação (`P-014`).

**Hipóteses a validar:**
- 🔎 Que os clientes aceitem a cobrança por assento e por plano.
- 🔎 *(técnica, vai ao arquiteto na `P-008`)* O produto comporta guardar a licença da organização, conferir os assentos contra as pessoas e desabilitar os usuários no vencimento.

**Prova de valor** *(proposta do PO)*: a organização importa o arquivo de uma licença com 50 assentos, válida por 12 meses. No vencimento sem renovação, o acesso muda como a regra decidir, e volta ao importar o arquivo novo.

**Reabrir quando:** o modelo de cobrança mudar (por exemplo, por consumo em vez de por assento).

### D-065 · Nova MF-110:Pergunta rápida, um botão flutuante de chat para perguntar sem sair da tela
Situação: 🟢 decidida (a necessidade; o nome e o número são proposta do PO) · refinada pela `D-085` (o popup é um atalho para a conversa, independente da tela) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** o Horus precisa de uma macro funcionalidade (mf) nova, a **MF-110:Pergunta rápida**: um **botão flutuante de chat** que abre um **popup** onde o usuário faz a pergunta, para permitir um uso mais dinâmico das perguntas.

**Contexto:** resposta do dono à pergunta “falta alguma candidata na lista da v2.0?”. Ele acrescentou esta como a 14ª candidata. Atende ao **problema nº 1 do norte, a pergunta de análise na hora** (`D-001`), levando a pergunta até o lugar onde a pessoa já está.

**O que o inventário mostra:** pelo que a busca no código encontrou (31/10/2026), a pergunta só se faz na tela da conversa de análise. Os botões flutuantes que existem hoje são outros (a gaveta do board e o aviso “a resposta continua”). 🔎 A confirmar com o arquiteto de soluções.

**Fica de fora / adiado:** o desenho (em que telas o botão aparece, onde a resposta fica depois de fechar o popup, o que o popup faz e o que fica só na conversa completa), a versão em que entra e a pontuação. Vira a definição macro da `P-013`.

**Hipóteses a validar:**
- 🔎 Que o gestor pergunte mais, e com mais frequência, quando a pergunta está a um clique da tela em que ele já está.
- 🔎 *(técnica, vai ao arquiteto na `P-008`)* O motor de conversa responde de um popup em qualquer tela.

**Prova de valor** *(proposta do PO)*: a gestora Carla, olhando o board de vendas, abre o botão, pergunta por que uma filial caiu e recebe a resposta sem sair do board.

**Reabrir quando:** o arquiteto mostrar que o popup não comporta o motor de conversa, ou a medida de autonomia mostrar que a conversa completa já basta.

### D-064 · O agendamento roda uma de duas coisas, no mesmo nível: o PDF de um board ou um agente
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- O **agente** e o **agendamento** são coisas diferentes.
- Ao configurar um agendamento, o usuário escolhe **o que ele executa**: a **extração de um relatório ou board em PDF**, ou **a execução de um agente**. Os dois estão **no mesmo nível**.
- O resultado, o artefato, vai aos conectores de saída configurados para o agendamento.

**Contexto:** impasse `I-007`. Opções do PO: **A**, o PDF sai por um agente de IA; **B**, por um caminho direto, sem IA; **C**, por um agente pronto de instrução fixa. O dono explicou que o agente e a geração do PDF do board são irmãos: o agendamento escolhe um ou outro. Na prática, é o caminho direto da opção B.

**Consequências:**
- Fecha o `I-007`.
- **Substitui a parte da `D-037`** que dizia “entre o agendamento e o resultado há sempre um agente”. A `D-063` (todo agente usa IA) fica de pé: o PDF de um board não passa por agente.
- A cadeia fica: **Agendamento** → (**PDF de um board** ou **Agente**) → **Artefato** → **Conector** → **Destinos**.
- 🔎 Leitura do PO: um agendamento pode executar mais de um item (vários PDFs, vários agentes) e enviar a mais de um conector, como na `D-035`.
- O nome da MF-114 (“Módulo de Agendamentos de Agentes”) segue o que o dono escolheu na `D-037`, por razão comercial, embora o agendamento agora também rode PDFs de board. O dono pode renomear.
- A regra do board desabilitado (aviso no lugar, `D-044`, `D-045`) segue valendo para o PDF.

**Fica de fora / adiado:** nenhum.

**Hipóteses a validar:** nenhuma por ora.

**Prova de valor** *(proposta do PO)*: a gestora Carla cria um agendamento com dois itens, o PDF do board de vendas e um agente que analisa a semana, e cada resultado sai pelo conector que ela escolheu.

**Reabrir quando:** surgirem outros itens agendáveis, como a exportação de dados em CSV.

### D-063 · Todo agente usa IA
Situação: 🟢 decidida (o conflito com a `D-037` foi resolvido pela `D-064`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** **todos os agentes usam IA**, porque é preciso **interpretar as consultas que devem ser executadas**.

**Contexto:** o dono corrigiu o PO ao ler a proposta da `D-062`, que dizia que nem todo agente usa IA. Substitui a parte da `D-037` que dizia “mesmo quando, por dentro, o agente não é de IA”.

**Consequências:**
- A MF-115:Agentes ativos fica sendo a mf dos agentes de IA. Não precisa mais abranger agentes sem IA. O nível de inferência da `D-024` vale para todos.
- Todo agente consome IA, o que reforça a atenção ao custo (`D-061`).
- ⚠️ **Conflito:** o exemplo do dono na `D-035` e a `D-037` previam um agente sem IA para gerar o PDF de um board, que não precisa interpretar nada. Virou o impasse `I-007`.

**Fica de fora / adiado:** como sai o PDF agendado de um board (`I-007`).

**Hipóteses a validar:** nenhuma por ora.

**Prova de valor** *(proposta do PO)*: toda execução de agente passa pelo modelo que o owner configurou, e o consumo aparece na organização.

**Reabrir quando:** surgirem tarefas repetitivas em que a IA só atrapalha.

### D-062 · Definição macro da MF-115:Agentes ativos
Situação: 🟢 decidida (confirmada pelo dono em 31/10/2026; entra na v2.0 pela `D-122`, de 02/11/2026) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a MF-115:Agentes ativos fica definida assim. Com ela, a `P-007` se fechou.

- **Nome:** MF-115:Agentes ativos (mantido).
- **O que é:** o **trabalhador de IA que o agendamento pode chamar**, ao lado do PDF de um board (`D-064`). Ele extrai e analisa dados e entrega artefatos e alertas pelos conectores de saída. **Todo agente usa IA**, porque precisa interpretar as consultas que devem ser executadas (`D-020`, `D-063`).
- **Como se cria** ✅: com **instruções em texto**, digitadas, coladas ou importadas de um arquivo **.md** (`D-061`). O usuário escolhe o nível de inferência (`D-024`).
- **Como roda** ✅: o **owner configura o modelo** que segue as instruções. A execução é um ciclo controlado pelo modelo: consultas e análise, repetidas até terminar. No fim, o modelo entrega as instruções de renderização para **cada tipo de saída** do agendamento (`D-061`).
- **Só lê** ✅: nunca altera dados nem age nos sistemas da empresa (`D-022`).
- **Quando roda e para quem entrega** ✅: pelo agendamento e pelos conectores, só a usuários do Horus, com a permissão de quem criou o agente (`D-060`, `D-059`).
- **Aprovação** ✅: o owner liga ou desliga a aprovação automática de criar agentes que extraem dados (`D-038`, `D-039`).
- **Quem cria e edita** 🆕: qualquer pessoa cria. As regras dos boards valem: só o autor edita, o owner e o gestor podem desabilitar, e se o autor é removido o agente vai, pausado, para o espaço da organização (`D-043` a `D-045`, `D-060`).
- **Antes de ligar** 🆕: o Horus mostra ao autor o que entendeu das instruções (as consultas e a condição de avisar), e o autor confirma.
- **Rótulo do alerta** 🆕: todo alerta chega rotulado com o nível de inferência usado (`D-024`).
- **Custo de IA** 🆕: o consumo dos agentes aparece no consumo e no custo da organização (MF-105:IA sob controle da organização), e o owner o controla pela escolha do modelo e pela aprovação de criar agentes.
- **Quem ganha** 🆕: o gestor e o executivo, que são avisados e recebem a análise pronta sem perguntar; a área de dados, que deixa de ser acionada para o que se repete.
- **Decisão que passa a ser possível** 🆕: ser avisado quando algo muda, com a análise já feita, sem alguém lembrar de perguntar.
- **Prova de valor** 🆕: a gestora Carla importa um .md com as perguntas da semana; toda segunda o agente consulta, analisa e entrega ao grupo “Vendas Sul” um PDF com gráficos; e, quando as vendas caem mais de 10%, avisa no WhatsApp, rotulado com o nível de inferência.
- **Retorno para o negócio** 🆕: atende ao problema nº 3 do norte, o aviso, e devolve tempo à área de dados.
- **O que não inclui** 🆕: agir sobre os sistemas da empresa (`D-022`); entregar a quem não é usuário do Horus (`D-035`); o relógio (MF-114) e o canal (MF-113); um limite automático de custo por agente ou por organização (a pontuar); o formulário sem IA como forma de criar agente (fica para depois, se o mercado pedir).
- **Depende de:** a MF-105:IA sob controle da organização (o modelo dos agentes e o consumo); a MF-104:Conectar as fontes vivas; a MF-107 e a MF-108 (análise e blocos visuais); a MF-106:Segurança dos dados por pessoa; a MF-114 e a MF-113.

**Contexto:** reúne as `D-020` a `D-024`, `D-037`, `D-038`, `D-039`, `D-059`, `D-060` e `D-061`. O que veio do dono está marcado com ✅; os campos marcados com 🆕 foram propostos pelo PO e confirmados pelo dono.

**Hipóteses a validar:** as dos itens p e q da `P-008` (renderizar gráficos em segundo plano com as bibliotecas do front, e o ciclo controlado pelo modelo). E 🔎 que os contratantes aceitem alertas com especulação sem aval da organização (`D-024`).

**Reabrir quando:** o custo de IA dos agentes surpreender os owners, ou o arquiteto mostrar que a renderização em segundo plano não é viável.

### D-061 · Como o agente é criado e como ele roda
Situação: 🟢 decidida (a diretriz) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- O usuário cria o agente com **instruções em texto**: pode **digitar**, **colar** ou **importar um arquivo .md** com o que deve ser extraído de informação.
- O **owner configura o modelo** de IA responsável por seguir as instruções do agente e convertê-las em análises.
- Como o agente roda em segundo plano, o **resultado de cada execução é sempre um JSON de instruções** do que fazer: **consultas + renderização**, ou **consultas + análise**, com o **modelo controlando o ciclo de forma recursiva**. Quando o modelo termina a análise, ele entrega o **JSON final com as instruções de renderização para cada tipo de saída configurada no agendamento** em execução.

**Contexto:** resposta do dono às duas dúvidas do PO na `P-007`: como o usuário cria o agente (**A**, em português; **B**, formulário; **C**, os dois) e o custo de IA. O dono escolheu uma versão da A, com texto livre e arquivo .md, e respondeu ao custo dizendo que o owner configura o modelo.

**Consequências:**
- Responde à hipótese da `D-023`: o usuário descreve o agente em texto livre. O formulário sem IA (opção B) fica fora desta definição.
- 🔎 Leitura do PO: a escolha do modelo é uma configuração nova do owner na MF-105:IA sob controle da organização, e é a alavanca de custo e de qualidade dos agentes. Um limite automático de custo não foi pedido.
- ⚠️ Dois pontos para o arquiteto: renderizar gráficos em segundo plano com as mesmas bibliotecas do front, “se é que isso é possível” (`P-008`, item p); e o ciclo recursivo controlado pelo modelo, com um JSON final por tipo de saída (`P-008`, item q).

**Fica de fora / adiado:** o limite de custo; como o autor revisa o que o agente entendeu; os tipos de saída além do PDF e do JSON.

**Hipóteses a validar:** as dos itens p e q da `P-008`.

**Prova de valor** *(proposta do PO)*: a gestora Carla importa um .md com as instruções; o agente consulta, analisa e entrega um PDF com gráficos e um JSON, cada um por um conector.

**Reabrir quando:** o custo de IA dos agentes surpreender os owners, ou a renderização em segundo plano não for viável.

### D-060 · Definição macro da MF-114:Módulo de Agendamentos de Agentes
Situação: 🟢 decidida (confirmada pelo dono em 31/10/2026; entra na v2.0 pela `D-122`, de 02/11/2026; o campo “O que é” foi refinado pela `D-064`: o agendamento roda o PDF de um board ou um agente, no mesmo nível) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a MF-114:Módulo de Agendamentos de Agentes fica definida assim. Com ela, a `P-011` se fechou.

- **Nome:** MF-114:Módulo de Agendamentos de Agentes (`D-037`).
- **O que é:** um **agendador único**. Ele decide **quando** um agente roda; o agente gera um ou mais artefatos (PDF, JSON…) e os entrega a um ou mais conectores, para os destinos escolhidos (`D-035`, `D-036`, `D-037`). Serve a boards (MF-112), relatórios e agentes (MF-115).
- **Quem agenda para quem:** cada pessoa agenda para si; para outras pessoas, só o **gestor** (as que ele gere) e o **owner** (qualquer usuário) (`D-059`).
- **Aprovação:** o owner liga ou desliga, tipo por tipo, a aprovação automática de criar agendamento (`D-038`, `D-039`).
- **Board desabilitado:** o agendamento segue ativo, e entra um texto de aviso no lugar do board (`D-044`, `D-045`).
- **Destinos** 🆕: usuários do Horus e grupos, pelo contato que cada um informou em cada conector. O gestor usa só as pessoas que gere e os grupos dele; os grupos da organização são destino dos agendamentos do owner.
- **Com que permissão roda** 🆕: com a de quem criou o agendamento, como o board roda com a do gestor (`D-054`).
- **Usuário removido** 🆕: os agendamentos criados por ele ficam **pausados** no espaço da organização até o owner transferir a propriedade ou excluir. Um usuário removido deixa de ser destino.
- **Quem ganha** 🆕: quem acompanha o negócio sem precisar lembrar de gerar e mandar; o gestor, que leva o PDF ou o alerta à equipe; o owner, que controla.
- **Decisão que passa a ser possível** 🆕: entregar a informação certa na hora certa, sem alguém lembrar de gerar e enviar.
- **Prova de valor** 🆕: a gestora Carla agenda o PDF do board dela para o grupo “Vendas Sul” todo dia 1º, e o João o recebe no WhatsApp, mesmo sem acesso à filial; se a Maria, membro comum, tenta agendar o envio ao João, o Horus não deixa.
- **Retorno para o negócio** 🆕: o acompanhamento recorrente e o aviso (problema nº 3 do norte) chegam sem trabalho manual, e o único “empurrão” de hoje, o relatório por e-mail, vira geral.
- **O que não inclui** 🆕: o que o agente faz e o que ele avalia ao rodar (MF-115); o formato do artefato (MF-112 e o agente); o canal de entrega (MF-113); enviar a quem não é usuário do Horus (`D-035`).
- **Depende de:** a MF-115:Agentes ativos, a MF-113:Conectores de Saída, a MF-112:Boards e Relatórios, a MF-102:Organizações, pessoas e papéis (gestão e grupos) e a MF-106:Segurança dos dados por pessoa.

**Contexto:** reúne as `D-035` a `D-039`, `D-044`, `D-045` e `D-059`. A natureza e as regras vieram do dono; os campos marcados com 🆕 foram propostos pelo PO e confirmados pelo dono, junto com a leitura de que “cada um agenda só para si” é a opção A da dúvida do PO (`D-059`).

**Hipóteses a validar:** a agenda de relatórios de hoje serve de base (`P-008`, item g); e o alcance de dados dos boards da organização e dos agendamentos do owner (`P-008`, item o).

**Reabrir quando:** membros precisarem enviar a colegas, ou o arquiteto mostrar que algum campo não cabe como definido.

### D-059 · Só o gestor e o owner entregam dados a outras pessoas, por board ou por artefato enviado por conector
Situação: 🟢 decidida (a diretriz) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- A regra de que **só o gestor (e o owner) entregam dados a outras pessoas** vale também para o que um **agendamento** envia: cada pessoa agenda para si; para outras pessoas, só o gestor (as que ele gere) e o owner.
- A **restrição de acesso aos dados é ignorada** quando um gestor autoriza alguém sem permissão. Essa autorização se dá de **duas maneiras**: pelo **compartilhamento do board** ou por **artefatos disponibilizados por um conector de saída**.

**Contexto:** resposta do dono à dúvida do PO na `P-011` (a Maria pode mandar o PDF programado ao João?). Opções: **A**, cada um agenda só para si; **B**, qualquer um, com aprovação obrigatória do owner; **C**, qualquer um, sem aprovação obrigatória. O dono respondeu que a regra vale; o PO entendeu como a A, e o dono confirmou em 31/10/2026. Não houve pontuação numérica, por ser regra de quem configura.

**Consequências:**
- **Amplia a `D-053`**: a liberação não fica só na tela do board; vale também no artefato que o gestor envia por conector. Continuam só com a permissão da pessoa: o chat, o SQL e o CSV baixado de um cartão.
- Confirma a leitura do PO de que o PDF do board é o próprio board.
- Responde ao exemplo do dono (board A4 não publicado, PDF enviado a A, B e X): quem agenda para outros é o gestor ou o owner, e o PDF leva o que o gestor vê.
- A responsabilidade é do gestor (`D-054`). 🔎 O registro de liberações (`D-058`) deve cobrir os dois caminhos: o board compartilhado e o artefato enviado por conector.

**Fica de fora / adiado:** com que alcance de dados roda o agendamento do owner, que não é dono de dados (`D-048`).

**Hipóteses a validar:** nenhuma por ora, além da `P-008` (item o).

**Prova de valor** *(proposta do PO)*: a gestora Carla agenda o PDF do board dela para o João, que não tem acesso à filial; o João o recebe e vê os números. Se a Maria tenta agendar o envio ao João, o Horus não deixa.

**Reabrir quando:** membros precisarem enviar a colegas, ou a liberação por artefato causar um incidente.

### D-058 · Definição macro da mf única de boards e relatórios
Situação: 🟢 decidida (confirmada pelo dono em 31/10/2026; entra na v2.0 pela `D-119`, de 02/11/2026) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a mf única que une a MF-006:Acompanhar em boards e a MF-008:Relatórios em PDF agendados fica definida assim. Com ela, a `P-005` se fechou, a mf ganhou o número **MF-112**, e a MF-006 e a MF-008 passam a **substituídas**.

- **Nome:** MF-112:Boards e Relatórios. O dono confirmou a proposta e pode renomear.
- **O que é:** um **editor único**. Todo board é **vivo** na tela e pode ser **impresso em PDF**, de qualquer tamanho; o tamanho é só uma propriedade (`D-018`, `D-057`). Herda o que a MF-006 e a MF-008 já fazem: grade livre, páginas, apresentação em laço, cartões que se recalculam, filtros, temas e o editor de relatórios.
- **Quem cria, vê e publica:** qualquer pessoa cria; o owner e o gestor veem os boards de quem gerem; owner e gestor publicam na organização, e o gestor só se o owner permitir, escolhendo entre Todos, Grupos, Pessoas geridas por mim e Pessoas específicas (`D-042`).
- **Quem edita e desabilita:** só o autor edita; o owner e o gestor podem desabilitar, mas não alterar (`D-043`, `D-044`). O owner não é dono de board; a organização tem um espaço próprio de boards, que o owner edita (`D-048`). Se o autor é removido, os boards dele vão para esse espaço, com o mesmo status (`D-045`).
- **Liberação de dados:** o gestor, dono dos dados, pode liberar a quem abre o board o que ele mesmo vê, inclusive sobre as travas do banco, só dentro do board, e a responsabilidade é dele (`D-051`, `D-053`, `D-054`).
- **Quem ganha:** o gestor e o executivo, que acompanham o negócio num painel vivo e levam a mesma montagem em PDF para a reunião; o owner, que controla quem publica.
- **Decisão que passa a ser possível:** acompanhar o negócio sem pedir um relatório à área de dados, e levar o mesmo conteúdo impresso para quem não abre o Horus.
- **Prova de valor:** a mesma montagem sai como tela viva e como PDF, sem refazer. A gestora Carla monta o board, o publica para “Pessoas geridas por mim”, e o PDF dele chega todo mês à diretoria, por um agendamento.
- **Retorno para o negócio:** o acompanhamento recorrente, que o norte havia adiado (`D-001`), passa a ser entregue, aproveitando o maior volume já construído do produto.
- **O que não inclui:** o agendamento e o envio (MF-114:Módulo de Agendamentos de Agentes e MF-113:Conectores de Saída); a geração automática do artefato (feita por agente, `D-037`); edição por mais de um autor; formatos de saída além de tela viva e PDF (a pontuar); gestor de gestor.
- **Depende de:** a MF-102:Organizações, pessoas e papéis (gestão, grupos e roles, `D-056`); a MF-106:Segurança dos dados por pessoa (o alcance do gestor); a MF-104:Conectar as fontes vivas; a MF-107 e a MF-108, que fazem as análises e os blocos dos cartões; a MF-114 e a MF-113, para o PDF automático.

**Propostas do PO dentro desta definição** *(confirmadas pelo dono)*:
- **Fronteira do board:** a tela, os cartões, o PDF e a imagem do board são **o próprio board** e levam a liberação do gestor. **Ver o SQL, baixar o CSV de um cartão e continuar a pergunta no chat** são **fora do board** e seguem só a permissão da pessoa.
- **Registro de liberações:** o Horus registra, a cada publicação, quem publicou, com qual visibilidade e quando; o owner consulta.
- **Boards públicos da quarentena:** o owner marca quais boards da organização quem está na quarentena pode ver (`D-048`).
- **Leituras anteriores:** o owner tem as mesmas quatro visibilidades do gestor (`D-042`); o gestor desabilita os boards de quem ele gere, e um board excluído se comporta como desabilitado dentro de um agendamento (`D-044`).

**Contexto:** reúne as `D-018`, `D-042` a `D-045`, `D-048`, `D-051`, `D-053`, `D-054` e `D-057`. A natureza e as regras vieram do dono; os campos de ganho, retorno, “o que não inclui” e “depende de” e as propostas acima foram do PO e confirmados pelo dono.

**Hipóteses a validar:** as dos itens a, h, i e n da `P-008`.

**Reabrir quando:** o arquiteto mostrar que o editor de relatórios não comporta o que o board faz, ou algum tamanho de board não virar PDF legível.

### D-057 · O tamanho do board é só uma propriedade: todo board é vivo e pode ser impresso em PDF
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** o **tamanho** do board é **só o tamanho dele**. **Todo board pode ser um board vivo e também ser impresso em PDF, independente do tamanho.**

**Contexto:** resposta do dono à dúvida do PO na `P-005` (o board tem um formato só, ou a mesma montagem sai em vários?). Opções: **A**, um formato por board; **B**, a mesma montagem com adaptação automática; **C**, a mesma montagem com ajuste do autor. O dono corrigiu a premissa: não existe “formato A4” contra “tela”. O A4 do exemplo da `D-035` é só um tamanho de board.

**Consequências:**
- Confirma a promessa da `D-018`: a mesma montagem sai como tela viva e como PDF, sem refazer.
- O PDF é um dos artefatos que um agente gera (`D-035`, `D-037`).

**Fica de fora / adiado:** como um board grande vira PDF (uma página só ou várias); quais outros formatos de saída (imagem, JSON, planilha) entram em cada versão.

**Hipóteses a validar:** 🔎 que todo board, de qualquer tamanho, vire PDF legível. O arquiteto confirma (`P-008`, item n).

**Prova de valor** *(proposta do PO)*: um board de qualquer tamanho abre vivo na tela e sai em PDF sem refazer.

**Reabrir quando:** o arquiteto mostrar que algum tamanho não vira PDF legível.

### D-056 · Definição macro da gestão de pessoas, dos grupos e das roles na MF-102:Organizações, pessoas e papéis
Situação: 🟢 decidida (confirmada pelo dono em 31/10/2026) · refinada pela `D-071` (o gestor também cria convites, com a aprovação do owner) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a gestão de pessoas, os grupos e as roles da MF-102:Organizações, pessoas e papéis ficam definidos assim. Com ela, a `P-012` se fechou. Esta definição completa e, onde houver diferença, vale mais que a `D-032`.

- **Papéis:** owner, gestor e membro. O owner **não é gestor**, mas **vê todos os membros**; pode acumular o papel de gestor (`D-047`, `D-048`).
- **Gestão:** cada membro tem **um gestor**. **Só o owner transfere** membros entre gestores (`D-046`).
- **Entrada:** o **convite é da organização** e pode indicar o gestor. Sem gestor, o membro vai para a **quarentena**: só acessa o perfil e os boards públicos da organização. Dela, o owner ou um gestor o adiciona à carteira (`D-047`, `D-048`). **Só o owner emite convites**, como hoje.
- **Gestor removido:** ao remover um gestor, o owner **indica quem passa a gerir os membros dele**; sem indicação, os membros vão para a quarentena. Os grupos dele deixam de existir.
- **Grupos do gestor:** só gestores os criam, e só com as pessoas que gerem. Servem à visibilidade dentro da hierarquia dele: boards, relatórios e alertas (`D-049`).
- **Grupos da organização:** o owner os cria e edita, com qualquer pessoa. Servem, por exemplo, à Diretoria (`D-055`).
- **Roles:** só o owner as cria, para limitar ou liberar funcionalidades. São a mesma informação, venham do login corporativo ou do cadastro. Com IDP, o owner configura o mapeamento dos campos do JWT (`D-050`, `D-052`).
- **Quem ganha:** o owner, que delega o dia a dia aos gestores sem perder o controle; o gestor, que organiza e enxerga a equipe dele; o membro, que entra já na equipe certa.
- **Prova de valor:** o owner convida a Ana indicando a gestora Carla; a Carla vê o board da Ana, cria o grupo “Vendas Sul” e publica para ele; o owner cria a role “Analista”, atribui à Ana, e cria o grupo da organização “Diretoria” para receber o relatório mensal.
- **Retorno para o negócio:** o owner deixa de ser gargalo do dia a dia, o que permite organizações maiores, sem abrir mão do controle.
- **O que não inclui:** gestor de gestor (hierarquia de vários níveis); gestão preenchida pelo IDP (etapa 2, `D-046`); convite emitido por gestor; a lista de funcionalidades por role (`P-009`); dar acesso a dados pelo grupo ou pela role (isso é da MF-106:Segurança dos dados por pessoa, com a exceção do board, `D-054`).
- **Depende de:** a MF-106:Segurança dos dados por pessoa, pelas claims; a ligação do IDP em cada organização (`D-027`); a mf única de boards e relatórios (`P-005`) e a MF-115:Agentes ativos, que usam os grupos.

**Contexto:** reúne as `D-046` a `D-052` e a `D-055`. A estrutura veio do dono; os campos “Gestor removido”, “Só o owner emite convites”, “Quem ganha”, “Retorno” e “O que não inclui” foram propostos pelo PO e confirmados pelo dono, assim como as leituras da `D-049` (o grupo dinâmico de um gestor vale só sobre os geridos dele; ao ser transferido, o membro sai dos grupos do gestor anterior; na visibilidade “Grupos”, o gestor usa os dele e o owner qualquer um) e a de que **cada membro tem um gestor só**.

**Hipóteses a validar:** as dos itens j, k, l e m da `P-008`.

**Reabrir quando:** o arquiteto mostrar que algum campo não cabe como definido, ou gestores precisarem convidar.

### D-055 · Existe também o grupo da organização, criado pelo owner, com qualquer pessoa
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** além dos grupos dos gestores (`D-049`), existe o **grupo da organização**: o **owner** o cria e edita, com **qualquer pessoa** da organização.

**Contexto:** dúvida do PO dentro da `P-012`: como o grupo que atravessa equipes (a “Diretoria”) recebe relatórios e alertas. Opções: **A**, não existe, e o owner junta grupos e pessoas a cada relatório; **B**, existe o grupo da organização. O dono escolheu a B. Não houve pontuação numérica, por ser regra de quem configura.

**Por que esta:** espelha o board da organização (`D-048`): o owner não tem nada pessoal, mas cuida do que é da empresa.

**Consequências:**
- Refina a `D-049`: passam a existir dois tipos de grupo, o do gestor (visibilidade dentro da hierarquia dele) e o da organização. Fecha a lacuna que a `D-049` abriu.
- 🔎 Leitura do PO: o grupo da organização serve de destino de relatórios e alertas (`D-029`) e de visibilidade dos boards da organização.
- ⚠️ Dois tipos de grupo para explicar ao cliente. Convém nomes distintos na tela.

**Fica de fora / adiado:** os nomes na tela; se o gestor pode usar os grupos da organização ao publicar.

**Hipóteses a validar:** nenhuma por ora.

**Prova de valor** *(proposta do PO)*: o owner cria o grupo “Diretoria” com a Carla e o Paulo e o usa como destino do relatório mensal e do alerta de queda de vendas.

**Reabrir quando:** o cliente confundir os dois tipos de grupo.

### D-054 · Dentro do board, a liberação do gestor vale também sobre as regras da empresa; a responsabilidade é do gestor
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a liberação de dados feita pelo gestor dentro de um board (`D-051`, `D-053`) **passa também por cima das travas que a TI da empresa colocou no banco de dados**. Quem vê o board do gestor o vê **com as mesmas permissões do gestor**: os gráficos e as análises do board geram dados com as permissões dele. Se o gestor deixa alguém ver, **a responsabilidade é do gestor**.

**Contexto:** impasse `I-006`, aberto porque a `D-051` e a `D-026` não cabiam juntas. Opções: **A**, a trava do banco manda; **B**, a liberação do gestor manda; **C**, cada empresa escolhe. O dono escolheu a B. Não houve pontuação numérica, por ser regra de quem configura.

**Consequências:**
- **A `D-026` ganha uma exceção.** O “vale a mais restritiva” continua valendo nas perguntas (chat e qualquer lugar fora do board). Dentro de um board publicado, vale a permissão do gestor. A prova de valor da `D-028` (“ninguém vê no Horus um dado que a empresa já o impede de ver”) passa a ter essa exceção.
- Fecha o `I-006`.
- Os controles que a empresa mantém sobre esse risco: o owner decide se os gestores podem publicar (interruptor da `D-042`), e o owner pode desabilitar qualquer board (`D-043`).
- Na prática, já é assim hoje (segundo o registro de 01/10/2026 e o mapa das mfs): o painel corporativo roda com acesso total e quem abre vê igual, e qualquer pessoa pode baixar o PDF de uma resposta e repassá-lo. O que muda é que quem libera passa a ser o gestor, limitado ao alcance dele (mais restrito que o acesso total de hoje), e a liberação fica dentro do Horus, onde pode ser registrada. O dono lembrou que é o natural, como o gestor compartilhar um PDF que ele criou com mais acesso de dados. O arquiteto confirma como é hoje (`P-008`, item h).
- A TI de um contratante com regras rígidas precisa conhecer a regra. 🔎 Sugestão do PO, para a proposta final da `P-005`: um registro de quem liberou o quê a quem, para a empresa auditar a responsabilidade do gestor.

**Fica de fora / adiado:** o registro (auditoria) das liberações; o alcance de dados dos boards da organização (`D-048`), já que o owner não é dono de dados; a fronteira do board (`D-053`).

**Hipóteses a validar:** como o board executa com a permissão do gestor em fontes com controle no banco. O arquiteto confirma (`P-008`, item h).

**Prova de valor** *(proposta do PO)*: a empresa protegeu os dados no banco e o João está impedido de ver outras filiais. A gestora Carla publica o board com todas, e o João o abre e vê todas. No chat, o João continua só com a filial dele.

**Reabrir quando:** um contratante com regras rígidas recusar a exceção, ou uma liberação do gestor causar um incidente.

### D-053 · A liberação do gestor vale só dentro do board; nas perguntas, cada pessoa fica no que pode ver
Situação: 🟢 decidida (a diretriz; ampliada pela `D-059`: vale também ao artefato que o gestor envia por conector) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- Quando uma pessoa faz perguntas (gera consultas), ela fica **limitada ao que pode ver**.
- O **gestor**, ao criar um board, pode dar a pessoas a permissão de **ver informações a mais naquele board**, e **nunca fora dele**.

**Contexto:** explicação do dono para o conflito entre a `D-051` e a `D-026` (`I-006`). Delimita a `D-051`: a liberação não é uma permissão que a pessoa leva consigo, e sim algo que existe dentro do board.

**Consequências:**
- O “vale a mais restritiva” da `D-026` continua valendo nas perguntas, no chat e em qualquer outro lugar fora do board.
- A liberação é o único ponto em que alguém vê mais do que o seu alcance, e é decisão consciente do gestor, dono dos dados.
- 🔎 Leitura do PO: a saída do board em outro formato (o PDF gerado por um agendamento, `D-035`) conta como o próprio board, e leva a liberação junto.
- Ainda não diz se, **dentro do board**, a liberação vale também sobre as regras da empresa (banco, IDP). Segue no `I-006`.

**Fica de fora / adiado:** a fronteira do board: o que acontece quando alguém baixa o dado de um cartão (CSV, imagem), vê o SQL ou continua a pergunta no chat a partir de um cartão; o registro de quem liberou o quê a quem.

**Hipóteses a validar:** nenhuma por ora.

**Prova de valor** *(proposta do PO)*: o João abre o board do gestor e vê todas as filiais; no chat, ao perguntar pelas mesmas filiais, recebe só a dele.

**Reabrir quando:** a fronteira do board mostrar um caminho por onde o dado liberado vaza para fora dele.

### D-052 · Roles: só o owner cria; são a mesma informação, venham do login corporativo ou do cadastro
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- **Só o owner cria roles** da organização.
- **“Role”** é o nome tanto do que vem do login corporativo quanto do que está no cadastro: **é a mesma informação no Horus**.
- Com o login via IDP, o **owner configura o sincronismo dos campos do JWT com o cadastro do usuário**.

**Contexto:** respostas do dono às leituras e ao alerta do PO na `D-050`.

**Consequências:**
- Fecha o alerta do nome na `D-050`: fica “role”, para os dois usos.
- Liga a `D-050` (roles que limitam funcionalidades), a `D-019` (grupos dinâmicos por claims e papéis), a `D-025` (reaproveitar claims e roles do token) e a `D-027` (IDP ligado em cada organização): o mapeamento do JWT passa a fazer parte da ligação do IDP, configurada pelo owner da organização.
- 🔎 Leitura do PO: “papel” (owner, gestor, membro) segue sendo o degrau hierárquico, à parte das roles.
- 🔎 O arquiteto confirma se o cadastro do usuário já guarda essa informação e se o mapeamento de campos do JWT é viável (`P-008`, item m).

**Fica de fora / adiado:** quem atribui roles à mão; o que vale quando a atribuição manual e o JWT discordam; quais campos do JWT entram no mapeamento.

**Hipóteses a validar:** a do arquiteto, no item m da `P-008`.

**Prova de valor** *(proposta do PO)*: o owner liga o IDP, mapeia um campo do JWT para a role do cadastro, e a Maria já entra com a role “Analista”, sem ninguém atribuí-la à mão.

**Reabrir quando:** o mapeamento do JWT se mostrar complexo demais para o owner configurar sozinho.

### D-051 · Publicar um board entrega a quem o abre o que o autor vê: o gestor, dono dos dados, pode liberar dados
Situação: 🟢 decidida (a diretriz; a liberação vale só dentro do board, pela `D-053`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** quando um gestor publica um board, **quem o abre vê o que o gestor vê**, mesmo que normalmente não visse. O **gestor é o dono dos dados** e **pode liberar dados a pessoas que, na organização, não poderiam vê-los**. Exemplo do dono: o gestor cria um board com todas as filiais; o João só pode ver a filial dele, mas, como o gestor deu acesso, no board compartilhado ele vê mais do que poderia.

**Contexto:** o dono respondeu à leitura do PO na `D-050`, explicando que a liberação é intencional. Responde ao ponto “escopo de dados de quem publica” da `P-005`.

**Consequências:**
- Na prática, **inverte a cautela de 14/10/2026** (o membro não compartilha painel porque quem recebe veria o escopo do autor). Para o gestor, isso passa a ser a função.
- 🔎 Leitura do PO: o gestor só libera o que ele mesmo vê, e o alcance dele limita o do board. Isso responde ao caso do analista com acesso restrito: quem tem pouco acesso só consegue liberar pouco.
- ⚠️ **Tensão com a `D-026`** (“vale a mais restritiva”; prova de valor: “ninguém vê no Horus um dado que a empresa já o impede de ver”). Se o impedimento estiver nas regras da empresa (banco, IDP), a liberação do gestor o contornaria. Resolve-se na `P-005`.

**Fica de fora / adiado:** o alcance de dados de um board da organização (`D-048`); o registro de quem liberou o quê a quem, para auditoria.

**Hipóteses a validar:** como o board executa e com qual alcance. O arquiteto confirma (`P-008`, item h).

**Prova de valor** *(proposta do PO)*: o gestor publica um board com todas as filiais, e o João, que só vê a filial dele, o abre e vê todas.

**Reabrir quando:** um contratante exigir que ninguém veja além do próprio alcance, ou a liberação causar um vazamento percebido.

### D-050 · Grupos ligados aos gestores para a visibilidade; roles do owner para as funcionalidades
Situação: 🟢 decidida (a diretriz) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- Os **grupos** ficam **vinculados aos gestores** e servem para dividir **quem vê o quê dentro da hierarquia de um gestor** (boards, relatórios e alertas).
- Surgem as **roles** (o nome é do dono): o **owner** as usa para **limitar ou não o acesso às funcionalidades** do Horus.

**Contexto:** o dono propôs isso perguntando “que tal?”, depois que o grupo do gestor deixou sem dono a questão dos interruptores de funcionalidade. O PO apoia: separa **quem vê e recebe** (grupos) de **o que pode usar** (roles).

**Por que apoio:** cada conceito faz uma coisa só. A dúvida de quem liga os interruptores de funcionalidade do grupo, que a `D-049` criou, some: quem liga é o owner, nas roles. O código já tem uma matriz de permissões por papel, o que ajuda.

**Consequências:**
- **Substitui a `D-030`** (funcionalidades ativáveis por grupo). O princípio segue, mas o mecanismo passa a ser as roles. Refina a `D-049` e a `D-029`: o grupo é só de visibilidade e destino.
- Reduz a `P-009`: agora é a lista de funcionalidades por role, a combinação quando a pessoa tem mais de uma role e o nome comercial.
- O grupo decide **quem abre** boards, relatórios e alertas dentro da hierarquia do gestor. A segurança por linha de dados segue na MF-106:Segurança dos dados por pessoa, com uma exceção desejada pelo dono: o gestor, dono dos dados, pode liberar dados a quem normalmente não os veria ao publicar um board (`D-051`).
- O nome “role” fica, tanto para o que vem do login corporativo quanto para o do cadastro: é a mesma informação no Horus (`D-052`).
- Só o owner cria roles (confirmado pelo dono, `D-052`). 🔎 Leitura do PO: atribuir roles também é do owner.
- 🔎 O arquiteto confirma se a matriz de permissões por papel comporta roles que o owner configura (`P-008`, item l).
- ⚠️ Segue aberto, na `P-012`: o grupo que atravessa equipes.

**Fica de fora / adiado:** a lista de funcionalidades por role; se a pessoa tem uma role só ou várias; o padrão de uma role nova.

**Hipóteses a validar:** a do arquiteto, no item l da `P-008`.

**Prova de valor** *(proposta do PO)*: o owner cria a role “Analista”, com a Análise avançada e o acesso à web, e a atribui a pessoas de equipes diferentes, sem mexer em nenhum grupo.

**Reabrir quando:** o cliente confundir roles com grupos, ou com os papéis owner, gestor e membro.

### D-049 · Os grupos são criados pelos gestores e só com as pessoas que eles gerem
Situação: 🟢 decidida (a lacuna do grupo que atravessa equipes foi fechada pela `D-055`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- **Só gestores criam grupos** de pessoas.
- O gestor **só inclui em seus grupos as pessoas que ele gere**.

**Contexto:** ao ver o problema do exemplo da “Diretoria Sul” (um grupo com pessoas de gestores diferentes), o dono revisou a regra. Opções que o PO ofereceu na `P-012`: **A**, o owner atribui grupos ao gestor; **B**, qualquer grupo; **C**, só grupos formados por pessoas que ele gere. O dono escolheu outra: o grupo nasce do gestor, com os geridos dele. Em suas palavras, “fica mais sólido”: o grupo e a gestão coincidem.

**Consequências:**
- **Substitui a `D-031`** (só o owner cria e edita grupos) e o campo “Quem gerencia” da `D-032`.
- Fecha a dúvida “quais grupos um gestor gere” da `P-012`: os que ele mesmo cria.
- O owner só cria grupo se acumular o papel de gestor (`D-048`).
- O grupo dinâmico (por claims e papéis, `D-019`) de um gestor vale só sobre as pessoas que ele gere (confirmado pelo dono, `D-056`).
- Quando o owner transfere um membro a outro gestor, o membro sai dos grupos do gestor anterior (confirmado pelo dono, `D-056`).
- Ao publicar com a visibilidade “Grupos”, o gestor usa os grupos dele; o owner, que vê todos os membros, pode usar qualquer um (confirmado pelo dono, `D-056`).
- ⚠️ **Lacuna nova:** o grupo que atravessa equipes (uma “Diretoria” com pessoas de vários gestores) deixa de existir, e a `D-029` usa o grupo como destino de relatórios e alertas. Resolve-se na `P-012`.
- ⚠️ Para a `P-009`: quem liga os interruptores de funcionalidades de um grupo (`D-030`), agora que o grupo é do gestor.

**Fica de fora / adiado:** o grupo que atravessa equipes; quem liga os interruptores de funcionalidades de um grupo.

**Hipóteses a validar:** nenhuma por ora.

**Prova de valor** *(proposta do PO)*: a gestora Carla cria o grupo “Vendas Sul” com quatro pessoas dela; ao tentar incluir uma pessoa de outro gestor, o Horus não deixa.

**Reabrir quando:** gestores precisarem de grupos com pessoas que não gerem, ou o owner precisar de grupos da organização.

### D-048 · Na quarentena só o perfil; a organização tem boards públicos e um espaço próprio de boards, e o owner não é dono de board
Situação: 🟢 decidida (a diretriz) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- Na **quarentena**, o membro **só acessa o perfil dele**. As opções de **conversa e de boards ficam desabilitadas**.
- A organização pode ter **boards públicos**, que **até os membros da quarentena veem**. **O owner define** quais.
- **O owner não é dono de nenhum board**, a não ser que **acumule também o papel de gestor**.
- A organização tem um **espaço de propriedade próprio**, onde os boards ficam **vinculados diretamente a ela**. **Os owners editam os boards da organização.**

**Contexto:** resposta do dono à dúvida da `P-012` sobre o que o membro faz na quarentena. Opções: **A**, usa tudo; **B**, acesso limitado; **C**, não entra. O dono escolheu algo próximo da C, com o perfil e os boards públicos como exceção, e acrescentou a regra de que o owner não é dono de board.

**Consequências:**
- Responde à dúvida da `P-012` sobre a quarentena.
- Refina a `D-043`: o owner continua sem editar o board de uma pessoa, mas edita os boards da organização.
- O board que o owner cria nasce no espaço da organização, já que ele não pode ser dono (confirmado pelo dono em 31/10/2026).
- O espaço da organização é o mesmo para onde vão os boards de autor removido (`D-044`, `D-045`). Logo, o owner passa a poder editá-los, além de transferi-los ou excluí-los (confirmado pelo dono em 31/10/2026).
- Hoje cada pessoa tem **um papel só** (owner, gestor ou membro). Acumular owner e gestor é novo. O arquiteto confirma (`P-008`, item k).
- Um board público para quem está na quarentena segue a regra de hoje do corporativo (roda com acesso total e quem abre vê igual). Quem o torna público é o owner.

**Fica de fora / adiado:** como o owner marca o que a quarentena vê; se o board da organização pode ser desabilitado e agendado como os demais.

**Hipóteses a validar:** a do arquiteto, no item k da `P-008`.

**Prova de valor** *(proposta do PO)*: o João, na quarentena, abre o Horus e vê só o perfil e o board de boas-vindas da organização; as conversas e os demais boards estão desabilitados.

**Reabrir quando:** quem está na quarentena precisar de mais que o perfil e os boards públicos, ou o espaço da organização acumular boards sem uso.

### D-047 · O owner não é gestor, mas vê todos os membros; o convite é da organização e quem fica sem gestor espera na quarentena
Situação: 🟢 decidida (a diretriz) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- O **owner não é um gestor**, mas tem **visibilidade sobre todos os membros** da organização.
- O **convite passa a ser da organização** e **pode indicar o gestor**. Com a indicação, o membro já entra na carteira do gestor certo.
- Sem gestor indicado, o membro vai para uma área de **quarentena**, que guarda os membros ainda não atribuídos a nenhum gestor.
- Da quarentena, **o owner ou um gestor adiciona** o membro “órfão” aos seus geridos.
- **Só o owner transfere membros entre gestores** (segue a segunda parte da `D-046`).

**Contexto:** o dono corrigiu o PO na `D-046` (o owner não é um gestor) e propôs a mudança do convite, perguntando “que tal?”. O PO apoia: separa **entrar na organização** (o convite) de **pertencer a uma equipe** (a gestão), e o convite com gestor indicado cobre o caso comum sem passar pela quarentena.

**Consequências:**
- **Substitui a primeira parte da `D-046`** (quem o owner convida é gerido por ele) e a leitura de que o owner também é um gestor.
- Mexe na MF-102:Organizações, pessoas e papéis: o convite nominal, por link e QR passa a ser da organização, com indicação opcional do gestor. 🔎 O arquiteto confirma se o convite e a planilha de convites aguentam isso (`P-008`, item j).
- 🔎 Leitura do PO: o owner, mesmo não sendo gestor, pode atribuir qualquer membro da quarentena a qualquer gestor.

**Fica de fora / adiado:** o que o membro pode fazer enquanto está na quarentena; se o gestor puxa o membro direto ou com aprovação do owner; quem emite convite (hoje só o owner); o que acontece com os membros de um gestor removido (`P-012`).

**Hipóteses a validar:** a do arquiteto, no item j da `P-008`.

**Prova de valor** *(proposta do PO)*: o owner convida a Ana indicando a gestora Carla, e a Ana cai na carteira da Carla; convida o João sem indicar ninguém, e o João fica na quarentena até a Carla ou o owner o adicionar.

**Reabrir quando:** gestores puxarem membros que não são da área deles, ou a quarentena acumular gente esperando.

### D-046 · Quem o owner convida é gerido por ele, e só o owner transfere membros entre gestores
Situação: 🟢 decidida (a diretriz; a primeira parte foi substituída pela `D-047`, e a segunda segue) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- Os usuários que o **owner convida são geridos por ele**.
- **Só o owner transfere membros entre gestores.**

**Contexto:** resposta do dono à dúvida da `P-012` (de onde vem a carteira de quem cada gestor gere). Opções: **A**, o owner atribui dentro do Horus; **B**, vem do IDP; **C**, dentro do Horus agora e o IDP depois. O dono não escolheu uma das três: deu a regra de como a gestão nasce e muda. Não houve pontuação numérica, por ser regra de quem configura.

**Consequências:**
- 🔎 Leitura do PO: cada usuário tem **um único gestor**. Quem o owner convida nasce gerido pelo owner, e o owner o passa a um gestor quando quiser. Nesse sentido, o owner também é um gestor.
- Combina com o que existe: hoje o gestor não convida (o papel nasce sem a chave dos convites, task 001), então todo usuário nasce gerido pelo owner.
- A gestão vem de dentro do Horus. Preencher a hierarquia pelo IDP não foi decidido e fica fora por ora, como a etapa 2 da `D-025`.
- Refina a `D-042` e a `D-032`: o gestor passa a ter uma carteira de pessoas.
- ⚠️ Falta definir se e como o gestor gere **grupos**, já que a `D-042` fala em “grupos e membros que ele gere” (`P-012`).

**Fica de fora / adiado:** a gestão preenchida pelo IDP; o que acontece com os membros de um gestor que é removido (voltam para o owner?).

**Hipóteses a validar:** nenhuma por ora.

**Prova de valor** *(proposta do PO)*: o owner convida a Ana e o João, e os dois nascem sob o owner; ele passa o João para a gestora Carla, e só a Carla e o owner passam a ver os boards do João.

**Reabrir quando:** owners pedirem a hierarquia vinda do login corporativo, ou a transferência só pelo owner virar gargalo.

### D-045 · No lugar do board desabilitado entra um texto de aviso; o board sem autor mantém o status
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- No lugar da saída de um board desabilitado entra **um texto avisando que o board está desativado**.
- O board que vai para a área da organização **mantém o status que tinha** antes da saída do autor.
- **Só conta como saída quando o usuário é removido** da organização.
- O owner pode transferir a propriedade a **qualquer pessoa da organização**.

**Contexto:** respostas do dono aos três detalhes que o PO deixou na fila ao fechar a `D-044` (o que o destinatário vê, o status na área da organização, para quem se transfere).

**Consequências:**
- Refina a `D-044`: o “não gera nada” passa a ser “gera um texto de aviso no lugar”. O artefato continua sendo gerado e entregue, com o aviso no espaço do board; o agendamento de um board só, desabilitado, entrega o artefato com o aviso (confirmado pelo dono em 31/10/2026).
- Um board publicado continua publicado na área da organização depois da remoção do autor, e quem o abria continua abrindo (confirmado pelo dono em 31/10/2026).
- “Saída” = remoção do usuário da organização. Isso entra na MF-102:Organizações, pessoas e papéis: remover um usuário leva os boards dele para a área da organização.
- ⚠️ Ponto novo para a `P-011`: o que acontece com os agendamentos criados pelo usuário removido.

**Fica de fora / adiado:** o texto exato do aviso; os agendamentos, os agentes e os dados de contato do usuário removido.

**Hipóteses a validar:** nenhuma por ora.

**Prova de valor** *(proposta do PO)*: o PDF semanal chega com a página do board desabilitado trocada por um aviso, e as demais páginas normais.

**Reabrir quando:** os destinatários acharem o aviso confuso, ou um board publicado sem ninguém responsável causar problema.

### D-044 · Desabilitar um board: quem pode, o efeito nos agendamentos e o que fazer quando o autor sai
Situação: 🟢 decidida (refinada pela `D-045`: no lugar da saída entra um aviso) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- **O gestor também pode desabilitar** um board, e não só o owner.
- **O agendamento continua ativo, mas não gera nada** enquanto o board estiver desabilitado. Num agendamento que gera mais de uma saída, baseado em boards diversos, **só os boards ativos geram saída**.
- **Quando o autor sai da empresa**, os boards dele vão para uma **área de propriedade da organização**. Nela, o owner pode **transferir a propriedade** ou **excluir permanentemente** o board.

**Contexto:** o dono respondeu aos três pontos que o PO deixou abertos na `D-043` (quem desabilita, efeito nos agendamentos, board sem autor).

**Consequências:**
- Fecha os três pontos da `D-043`. A exclusão permanente passa a existir só para o board sem autor; o owner não exclui board de quem está na empresa (`D-043`).
- A regra do agendamento vale para a MF-114:Módulo de Agendamentos de Agentes (`P-011`).
- 🔎 Leitura do PO: o gestor desabilita os boards de quem ele gere (o mesmo alcance de abrir, `D-042`).
- 🔎 Leitura do PO: um board excluído se comporta como desabilitado dentro de um agendamento.

**Fica de fora / adiado:** o que o destinatário e o autor veem quando uma saída é pulada por um board desabilitado (`P-011`); se o board na área da organização continua publicado ou fica desabilitado; para quem o owner pode transferir a propriedade.

**Hipóteses a validar:** nenhuma por ora.

**Prova de valor** *(proposta do PO)*: o gestor desabilita um board que alimentava um agendamento com dois boards, e o agendamento entrega só a saída do board que continua ativo.

**Reabrir quando:** destinatários reclamarem de ficar sem a saída sem saber o motivo, ou a área da organização acumular boards sem destino.

### D-043 · Só o autor edita um board; o owner pode desabilitá-lo, mas não alterá-lo
Situação: 🟢 decidida (os três pontos deixados em aberto foram fechados pela `D-044`; o owner edita os boards da organização, pela `D-048`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** **só o autor do board (quem o criou) pode editá-lo.** O owner da organização **não pode alterar** o board, mas **pode desabilitá-lo**. Assim, o acesso do owner e do gestor aos boards de quem gerem (`D-042`) é de **abrir**, e não de editar.

**Contexto:** o dono corrigiu a leitura do PO na `D-042` (“ter acesso” = abrir; editar não foi dito). Aqui se usa “autor” para o que o dono chamou de “dono do board”, a fim de não confundir com o owner da organização.

**Consequências:**
- 🔄 **Reverte a regra de 18/09/2026**, em que o painel corporativo é da organização e só o owner o edita (o criador vira procedência, e não posse). Agora quem edita é sempre o autor, mesmo com o board publicado.
- 🔎 Leitura do PO: “desabilitar” é tirar o board do ar, de forma reversível: quem o abria deixa de vê-lo, e o conteúdo fica guardado com o autor. Não é apagar.
- ⚠️ Surge o caso do **autor que sai da empresa**: o board fica sem quem o edite, e o owner só pode desabilitá-lo. Ponto para a `P-005`.
- Refina a `D-042`.

**Fica de fora / adiado:** se o gestor também pode desabilitar; o efeito de desabilitar sobre os agendamentos do board; o board que fica sem autor.

**Hipóteses a validar:** o que muda no código ao tirar do owner a edição do corporativo e criar o “desabilitar”. O arquiteto confirma (`P-008`, item i).

**Prova de valor** *(proposta do PO)*: o owner abre um board publicado e não consegue editá-lo, mas consegue desabilitá-lo, e o autor continua sendo o único a editar.

**Reabrir quando:** boards sem autor se acumularem, ou owners precisarem corrigir boards de outras pessoas.

### D-042 · Quem cria, quem vê e quem publica boards e relatórios
Situação: 🟢 decidida (a diretriz; o acesso do owner e do gestor é de abrir, pela `D-043`) · refinada pela `D-069` (o membro leitor não cria boards) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- **Qualquer pessoa cria** um board ou um relatório.
- **O owner e o gestor têm acesso a todos os boards** dos grupos e dos membros que gerem.
- **A publicação na organização é feita pelo owner e pelos gestores.** O gestor escolhe a visibilidade entre quatro: **Todos**, **Grupos**, **Pessoas geridas por mim** e **Pessoas específicas**.
- **O owner configura, nas preferências da organização, se permite que os gestores publiquem** na organização. É um interruptor.

**Contexto:** resposta do dono à dúvida da `P-005` “quem pode publicar um board”. Opções: **A**, só o owner; **B**, o owner e o gestor; **C**, qualquer pessoa pede e o owner aprova. O dono escolheu uma versão ampliada da B, com interruptor do owner, e acrescentou a criação livre e o acesso do owner e do gestor aos boards de quem gerem.

**Consequências:**
- 🔄 **Reverte, para o gestor, a regra de 18/09/2026**, em que só o owner promove um painel a corporativo (hoje o gestor também não promove, segundo `BoardEndpoints.cs`). A regra de 14/10/2026 de que o **membro** não compartilha painel continua.
- Surge o conceito de **gestão**: quem cada gestor gere. Hoje o gestor é só um degrau de papel (task 001, 22/09/2026), sem carteira de pessoas. Virou a `P-012`.
- 🔎 Leitura do PO: “ter acesso” aos boards de quem o gestor gere é poder abri-los. Editar ou apagar não foi dito.
- 🔎 Leitura do PO: o owner tem as mesmas quatro visibilidades.
- ⚠️ Segue aberto o ponto de segurança: o painel corporativo roda com acesso total (registro de 01/10/2026). Quando o gestor publica, o que quem abre vê? Resolve-se na `P-005`.
- O interruptor do owner se soma a outros interruptores nas preferências da organização (`D-039`).

**Fica de fora / adiado:** o padrão do interruptor ao criar uma organização; se “Pessoas específicas” aceita qualquer pessoa ou só as geridas; o escopo de dados de quem publica.

**Hipóteses a validar:** a do registro de 01/10/2026, com o arquiteto de soluções (`P-008`, item h).

**Prova de valor** *(proposta do PO)*: o owner permite que gestores publiquem, a gestora publica um board para “Pessoas geridas por mim” e só essas pessoas o veem; o owner desliga a permissão e ela deixa de poder publicar.

**Reabrir quando:** o ponto de segurança mostrar que a publicação por gestor expõe dados que o gestor não pode ver.

### D-041 · Definição macro da MF-113:Conectores de Saída
Situação: 🟢 decidida (confirmada pelo dono em 31/10/2026; entra na v2.0 pela `D-122`, de 02/11/2026; os conectores da v2.0 são o e-mail e o WhatsApp, pela `D-124`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a MF-113:Conectores de Saída fica definida assim. Com ela, a `P-010` se fechou.

- **Nome:** MF-113:Conectores de Saída (mantido).
- **O que é:** os canais que **só transportam** o que o Horus produz (e-mail, WhatsApp, Teams, Google Chat e outros) e **só entregam a usuários do Horus** (`D-035`). O formato do que sai é o artefato, outra coisa.
- **Quem ganha:** o owner da organização, que escolhe por onde a informação da empresa sai; os usuários, que recebem o resultado no canal onde já olham; o contratante com regras rígidas de segurança, que controla o que sai.
- **Decisão que passa a ser possível:** levar o que o Horus produz (alertas, relatórios exportados…) até a pessoa, sem ela precisar abrir o Horus, com a empresa no controle dos canais.
- **Como se controla:** só o owner da organização liga os conectores (`D-034`); o usuário informa o próprio contato em cada canal, e o owner aprova ou deixa automático, com um interruptor por tipo (`D-038`, `D-039`); no modo “tudo dentro”, os conectores ficam bloqueados até o owner da instância liberar cada tipo (`D-040`).
- **Prova de valor:** o owner liga o conector do Teams uma vez, um agendamento envia o PDF de um board, e o usuário o recebe no Teams. Nenhum conector funciona sem o owner ligar, e no “tudo dentro” nenhum conector que leve informação para fora funciona até a instância liberar.
- **Retorno para o negócio:** a informação chega sem ninguém ir buscá-la (o aviso, problema nº 3 do norte), e o contratante com regras de segurança aceita o produto porque controla o que sai.
- **O que não inclui:** o formato e o conteúdo do que sai (o artefato, feito pelo agente, `D-035`, `D-037`); o agendamento (MF-114:Módulo de Agendamentos de Agentes); entregar a quem não é usuário do Horus (`D-035`); agir sobre os sistemas da empresa (`D-022`); quem pode usar cada conector, que é candidato a interruptor por grupo (`P-009`); a lista de conectores que entram em cada versão (a pontuar).
- **Depende de:** a MF-114:Módulo de Agendamentos de Agentes e a MF-115:Agentes ativos, que chamam os conectores; a MF-102:Organizações, pessoas e papéis, para o perfil onde o usuário informa o contato e para o papel de owner; a MF-101:Administração da instância, onde o owner da instância libera os tipos no modo “tudo dentro”.

**Contexto:** reúne as `D-033` a `D-040`. A natureza, o controle e os interruptores vieram do dono; os campos “quem ganha”, “retorno”, “o que não inclui” e “depende de” foram propostos pelo PO e confirmados pelo dono. A leitura de que o **usuário informa o próprio contato** (`D-038`) foi confirmada junto.

**Hipóteses a validar:** a saída por e-mail de hoje serve de ponto de partida (`P-008`, item f).

**Reabrir quando:** o arquiteto mostrar que algum campo não cabe como definido, ou um contratante exigir conectores diferentes por organização.

### D-040 · No modo “tudo dentro”, os conectores de saída ficam bloqueados até a instância liberar
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** no modo **“tudo dentro”** (`D-010`), os conectores de saída que levam informação para fora **ficam bloqueados por padrão**, e o **owner da instância libera cada tipo de conector**. O owner da organização liga os conectores (`D-034`) só dentro do que a instância liberou. No modo “com serviços externos autorizados”, que é o padrão da `D-010`, não há bloqueio extra.

**Contexto:** dúvida do PO dentro da `P-010`. Opções: **A**, bloqueio total, sem exceção; **B**, o modo não muda nada; **C**, bloqueado por padrão e a instância libera. O dono escolheu a C. Não houve pontuação numérica, por ser regra de quem configura.

**Por que esta:** cumpre o “nada sai” por padrão e deixa o contratante autorizar o que quiser (`D-010`), com os dois níveis de owner da `D-013`.

**Consequências:**
- Responde em parte à hipótese da `D-010` (“o que, em cada modo, o contratante autoriza a sair”): para os conectores, o contratante autoriza por tipo.
- 🔎 Hipótese do PO: a configuração mora na MF-101:Administração da instância.

**Fica de fora / adiado:** quais tipos o produto já trata como internos (por exemplo, o e-mail por servidor do próprio contratante) e se algum vem liberado de fábrica.

**Hipóteses a validar:** que o contratante com exigência de “tudo dentro” libere poucos tipos.

**Prova de valor:** no “tudo dentro”, o owner da organização não consegue ligar o conector do WhatsApp enquanto o owner da instância não o libera.

**Reabrir quando:** contratantes pedirem a liberação por organização, e não por instância.

### D-039 · A aprovação do owner é um interruptor por tipo
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** cada tipo de coisa que exige aprovação tem **o seu interruptor**. Os tipos já conhecidos são a **criação de agendamento** (MF-114:Módulo de Agendamentos de Agentes) e o **dado de contato** do usuário (MF-113:Conectores de Saída). Outros tipos entram se a definição apontar, como a criação de agentes que extraem dados (`P-007`).

**Contexto:** dúvida do PO dentro da `P-010`, depois da `D-038`. Opções: **A**, um interruptor só; **B**, um por tipo; **C**, um por grupo (`D-030`). O dono escolheu a B. Não houve pontuação numérica, por ser regra de quem configura.

**Por que esta:** o owner pode confiar nos contatos que os usuários informam e, ao mesmo tempo, querer revisar cada agendamento. Cada mf cuida do seu interruptor.

**Fica de fora / adiado:** a lista final de tipos, o padrão de cada interruptor ao criar uma organização, e o interruptor por grupo, que a `P-009` pode vir a tratar.

**Hipóteses a validar:** que a lista de tipos fique curta o bastante para o owner entender.

**Prova de valor:** o owner deixa os contatos em aprovação automática e exige aprovação para os agendamentos, e cada um se comporta como configurado.

**Reabrir quando:** a lista de tipos crescer a ponto de a configuração virar um labirinto.

### D-038 · O owner da organização liga ou desliga a aprovação automática de agendamentos e de dados de contato
Situação: 🟢 decidida (a diretriz; o interruptor é por tipo, pela `D-039`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** o owner da organização pode configurar se a criação de agendamentos e os dados de contato dos usuários são **aprovados automaticamente** ou **esperam a aprovação dele**. Haverá uma funcionalidade para o owner **ligar ou desligar essa aprovação automática** em **qualquer forma de extração de dados e em tudo o que se relaciona a isso**.

**Contexto:** resposta do dono à dúvida da `P-010` sobre quem informa o contato de cada usuário num canal. Ele não escolheu A, B ou C: acrescentou a regra de aprovação.

**Consequências:**
- 🔎 Leitura do PO, confirmada na definição da `P-010` (`D-041`): a resposta pressupõe que o **usuário informa o próprio contato** (a opção A da dúvida), e o owner aprova ou deixa automático.
- 🔎 Leitura do PO: “aprovação automática ou não” é um interruptor de dois estados. Ligada, o que o usuário cria vale na hora. Desligada, fica esperando o owner.
- Como todo trabalho entre o agendamento e o artefato é feito por um agente (`D-037`), “qualquer forma de extração” alcança também a criação de agentes que extraem dados (`P-007`).
- Segue o que o owner já controla (`D-027`, `D-031`, `D-034`).

**Fica de fora / adiado:** a lista exata do que exige aprovação; se o interruptor é geral, por tipo ou por grupo; o padrão ao criar uma organização; o que o usuário vê enquanto espera.

**Hipóteses a validar:** que o owner dê conta de aprovar sem virar gargalo, a mesma das `D-031` e `D-034`.

**Prova de valor** *(proposta do PO)*: com a aprovação ligada, um membro cria um agendamento e ele só roda depois que o owner aprova; com a aprovação automática, roda na hora.

**Reabrir quando:** owners relatarem uma fila de aprovações parada.

### D-037 · MF-114:Módulo de Agendamentos de Agentes: entre o agendamento e o artefato há sempre um agente
Situação: 🟢 decidida (a parte “mesmo quando não é de IA” foi substituída pela `D-063`, e a de “sempre um agente”, pela `D-064`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- A MF-114 se chama **Módulo de Agendamentos de Agentes**. A escolha é de linguagem comercial.
- **Entre o agendamento e o resultado há sempre um agente.** O agendamento chama o agente, o agente gera o artefato e o entrega ao conector. Vale **mesmo quando, por dentro, o agente não é de IA** (por exemplo, o que só gera o PDF de um board).
- A cadeia fica: **Agendamento** (MF-114) → **Agente** (MF-115) → **Artefato** (PDF, JSON…) → **Conector** (MF-113) → **Destinos**.

**Contexto:** o dono renomeou a MF-114, que o PO havia chamado de “Agendamentos”, e explicou a razão: do ponto de vista comercial, “agente” é a palavra que o cliente vai usar. Refina a `D-035` (no exemplo do board A4, o agendamento chama um agente que gera o PDF) e a `D-036` (o nome).

**Consequências:**
- 🔎 Hipótese do PO: “agente” passa a ser o nome comercial de qualquer trabalhador configurado que produz um artefato. Uns usam IA (extrair, analisar, avisar: `D-020`, `D-023`, `D-024`) e outros não (gerar o PDF de um board). O nível de inferência livre da `D-024` vale só para os que usam IA.
- 🔎 Isso alarga a MF-115:Agentes ativos, que passa a abranger também os agentes que não usam IA. O alcance e o nome se fecham na `P-007`. A divisão de papéis: a MF-115 define o que o agente faz, a MF-114 define quando ele roda, e a MF-113 define por onde o resultado sai.

**Fica de fora / adiado:** os tipos de agente e onde mora o agente que só gera o PDF de um board (`P-007` e `P-005`).

**Hipóteses a validar:** 🔎 que o cliente aceite chamar de “agente” o que não usa IA, sem esperar inteligência onde ela não existe. Validar com clientes.

**Prova de valor** *(proposta do PO)*: o cliente descreve o agendamento do PDF de um board como “o meu agente de relatório”, sem estranhar.

**Reabrir quando:** clientes confundirem o “agente” que só gera PDF com um agente de IA, ou a venda prometer inteligência que o agente não tem.

### D-036 · Nova MF-114:Módulo de Agendamentos de Agentes, um agendador só para gerar artefatos e enviá-los
Situação: 🟢 decidida (a necessidade) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** o Horus terá uma macro funcionalidade (mf) nova, a **MF-114:Módulo de Agendamentos de Agentes**: **um agendador único**, que decide **quando** gerar um ou mais artefatos e **por quais conectores e para quais destinos** enviá-los. Serve a boards, relatórios e agentes. O PO a chamou de “Agendamentos”, nome provisório; o dono deu o nome definitivo na `D-037`.

**Contexto:** impasse `I-005`, aberto pela `D-035`. Opções: **A**, numa mf nova só de agendamentos; **B**, na mf única de boards e relatórios; **C**, na MF-115:Agentes ativos. O dono escolheu a A. Não houve pontuação numérica, por ser decisão de organização do mapa das mfs.

**Por que esta:** o agendamento é uma peça própria entre o artefato e o conector, como no exemplo do dono (`D-035`). Um agendador só evita dois agendadores no produto.

**Consequências:**
- 🔎 Hipótese do PO: a mf única de boards e relatórios (`D-018`) e a MF-115:Agentes ativos usam a MF-114 para agendar, em vez de ter cada uma o seu. O “agendamento de extração” da `D-020` e a agenda dos relatórios de hoje (MF-008:Relatórios em PDF agendados) iriam para ela. Fecha-se nas `P-005`, `P-007` e `P-011`.
- Abre a `P-011`, a definição macro da MF-114:Módulo de Agendamentos de Agentes.
- A lista de candidatas à v2.0 ganha a de nº 13, “Agendamentos” ([inventário](03-inventario-de-lacunas.md)).

**Fica de fora / adiado:** o que o agendamento pode agendar, quem cria e para quem (`P-011`).

**Hipóteses a validar:** 🔎 que a agenda que o relatório em PDF já tem hoje sirva de base para o agendador único. O arquiteto confirma (`P-008`).

**Prova de valor** *(proposta do PO)*: um agendamento gera o PDF de um board e o JSON de um agente e envia cada um por um conector diferente.

**Reabrir quando:** o arquiteto mostrar que um agendador só não serve a boards e agentes ao mesmo tempo.

### D-035 · Os conectores de saída só transportam; o formato (artefato) é outra coisa; e só entregam a usuários do Horus
Situação: 🟢 decidida (a diretriz) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:**
- Os conectores de saída da MF-113:Conectores de Saída são **só transporte**: levam o que lhes entregam. O **formato** em que o dado sai (PDF, JSON…) é outra coisa, o **artefato**, e não é tarefa do conector.
- O processo é uma cadeia de partes ligadas por conectores. Exemplo do dono: criar um board em formato A4, sem publicá-lo; criar um **agendamento** que gera um PDF dele e o envia pelo conector do WhatsApp aos destinos A, B ou X.
- Um agendamento pode **gerar mais de um artefato** e **enviar a mais de um conector**.
- O conector de saída **só envia a quem é usuário do Horus**.

**Contexto:** o dono corrigiu o PO na `P-010`. A dúvida “quem decide o que pode sair por um conector” tratava o conector como quem carrega o conteúdo, e foi retirada. Esta decisão refina a `D-033`: a mf continua, mas só com o transporte.

**Consequências:**
- O ponto “o que pode sair” deixa de ser do conector. O conteúdo é do artefato, e o agendamento decide o que gerar.
- Surgem duas partes novas no processo, o **artefato** e o **agendamento**. Onde elas moram virou o impasse `I-005`.
- A regra “só usuários do Horus” ajuda a segurança por pessoa: o Horus sabe quem recebe. 🔎 Seguem abertos, para a `P-010`: o artefato respeita o que cada destinatário pode ver? (um PDF gerado de um board pessoal e enviado a A, B e X toca na regra de que o membro não compartilha painel, registro de 14/10/2026); como o Horus acha cada usuário em cada canal (o número do WhatsApp, a conta do Teams) e quem informa isso.
- 🔎 Hipótese do PO: os e-mails do sistema (convite, recuperação de senha) ficam fora dos conectores. Corrige a hipótese da `D-033`, que os incluía.
- 🔎 Hipótese do PO: os destinos A, B e X podem ser usuários ou grupos (`D-029`).

**Fica de fora / adiado:** a lista de formatos de artefato (PDF, JSON…), a lista de conectores e onde mora o agendamento (`I-005`).

**Hipóteses a validar:** as dos itens acima. O arquiteto confirma para quem o relatório agendado vai hoje (`P-008`).

**Prova de valor** *(proposta do PO)*: o dono cria um board A4 sem publicar, agenda um PDF e o recebe no WhatsApp; o mesmo agendamento envia também um JSON por e-mail.

**Reabrir quando:** surgir a necessidade de enviar a quem não é usuário do Horus, como um cliente externo.

### D-034 · Só o owner da organização liga os conectores de saída
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** **ligar e autorizar os conectores de saída da MF-113:Conectores de Saída é tarefa só do owner da organização.** Gestores e membros usam os conectores ligados, mas não os ligam.

**Contexto:** dúvida do PO dentro da `P-010`. Opções: **A**, só o owner da organização; **B**, o owner e cada usuário (conectores da empresa e pessoais); **C**, só o owner da instância. O dono escolheu a A. Não houve pontuação numérica, por ser regra de quem configura.

**Por que esta:** a empresa decide por onde a informação dela sai, e um alerta com dado sensível não vai parar num canal pessoal. Combina com o que o owner da organização já faz (`D-027`, `D-031`).

**Fica de fora / adiado:** o usuário levar o próprio canal (como o WhatsApp dele); abre-se mão dessa autonomia, e o owner vira passagem obrigatória. 🔎 Surgiu um ponto novo para a `P-010`: **quem pode usar** cada conector depois de ligado (todos, ou só certos grupos, como na `D-030`).

**Hipóteses a validar:** que o owner dá conta de ligar os conectores sem virar gargalo.

**Prova de valor:** nenhuma informação sai por um canal que o owner da organização não ligou.

**Reabrir quando:** owners relatarem o gargalo, ou um contratante exigir que o usuário leve o próprio canal.

### D-033 · Nova MF-113:Conectores de Saída, por onde o Horus entrega o que produz
Situação: 🟢 decidida (a necessidade; refinada pela `D-035`: os conectores só transportam) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** o Horus precisa de uma macro funcionalidade (mf) nova, a **MF-113:Conectores de Saída**, que define os **conectores de saída de informação**, isto é, os canais por onde o Horus entrega o que produz. Exemplos do dono: **alertas** e **exportação de relatórios**; a lista fica aberta (“etc.”).

**Contexto:** o dono pediu a mf antes de abrirmos a próxima definição. Até aqui os canais de saída (e-mail, WhatsApp, Teams, Google Chat…) apareciam só como parte da MF-115:Agentes ativos (`D-020`, `D-022`). Agora são uma mf própria, que outras mfs usam.

**Consequências:**
- 🔎 Hipótese do PO: a MF-115:Agentes ativos (alertas) e a mf única de boards e relatórios (`D-018`, exportação) passam a usar os conectores de saída, em vez de cada uma ter os seus.
- Os pontos que a `D-022` deixou abertos sobre os canais (quem autoriza cada canal, o que o alerta pode conter, o encaixe com o modo “tudo dentro” da `D-010` e com a segurança por pessoa) passam da `P-007` para a definição desta mf (`P-010`). A `D-022` não muda.
- A lista de candidatas à v2.0 ganha a de nº 12, “Conectores de saída” ([inventário](03-inventario-de-lacunas.md)).

**Fica de fora / adiado:** quais conectores existem, quais entram na v2.0, quem configura e autoriza cada um e o que pode sair por eles. Tudo isso é a definição macro (`P-010`).

**Hipóteses a validar:** 🔎 que hoje a única saída seja o e-mail (relatório agendado, convites e recuperação de senha, dentro da MF-008 e da MF-101) e que ela sirva de ponto de partida. O arquiteto confirma (`P-008`).

**Prova de valor** *(proposta do PO)*: o owner da organização liga um conector uma vez e o usa tanto para um alerta quanto para um relatório exportado.

**Reabrir quando:** surgir uma saída que não caiba como conector, por exemplo uma que aja sobre os sistemas da empresa, o que a `D-022` não permite.

### D-032 · Definição macro dos grupos de pessoas (MF-102:Organizações, pessoas e papéis)
Situação: 🟢 decidida (confirmada pelo dono em 31/10/2026; o campo “Quem gerencia” foi substituído pela `D-049`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a melhoria dos grupos de pessoas na MF-102:Organizações, pessoas e papéis fica definida assim. Com ela, a `P-006` se fechou.

- **Nome:** MF-102:Organizações, pessoas e papéis (mantido). Os grupos entram como parte dela, e não como mf nova.
- **Quem ganha:** o owner da organização, que dá acesso, relatórios e permissões a muita gente de uma vez, em vez de pessoa por pessoa; as pessoas, que passam a receber o que lhes cabe sem pedir.
- **Decisão que passa a ser possível:** organizar a empresa em grupos (uma diretoria, uma região, um time de análise) e decidir, uma vez só, o que cada grupo abre, recebe e pode usar (`D-029`, `D-030`). No grupo dinâmico, quem entra na empresa com a claim ou o papel certo já cai no grupo sozinho (`D-019`).
- **Prova de valor:** o owner cria um grupo uma vez e o usa para dar acesso a um board, enviar um relatório e receber um alerta. Quando alguém passa a ter a claim do grupo dinâmico, o acesso chega sem o owner mexer (`D-029`).
- **Retorno para o negócio:** menos trabalho de administração por organização e implantação mais rápida; é a base de outras mfs (acesso a boards e relatórios, destino dos alertas dos agentes).
- **Quem gerencia:** só o owner da organização cria e edita grupos (`D-031`).
- **O que não inclui:** dar acesso a dados (o que cada pessoa vê dos dados continua sendo da MF-106:Segurança dos dados por pessoa); a lista de funcionalidades ativáveis por grupo e como elas se combinam (`P-009`); grupos que atravessam organizações (cada grupo vale dentro de uma organização, `D-008`).
- **Depende de:** as claims do vínculo da pessoa (MF-106:Segurança dos dados por pessoa) e os papéis (owner, gestor, membro), para os grupos dinâmicos; da mf única de boards e relatórios (`P-005`) e da MF-115:Agentes ativos (`P-007`), que usam os grupos.

**Contexto:** reúne as `D-019`, `D-029`, `D-030` e `D-031`. Os usos e a forma de montar vieram do dono; quem gerencia foi dúvida do PO; os campos “quem ganha”, “retorno”, “o que não inclui” e “depende de” foram propostos pelo PO e confirmados pelo dono.

**Hipóteses a validar:** a do item “Consequências” da `D-029`, com o arquiteto de soluções (`P-008`).

**Reabrir quando:** um uso novo de grupo exigir regra diferente das já definidas, ou o arquiteto mostrar que algum campo não cabe como definido.

### D-031 · Só o owner da organização cria e edita grupos de pessoas
Situação: ⚪ substituída por `D-049` · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** **criar e editar grupos de pessoas é tarefa só do owner da organização.** Gestores e membros usam os grupos, mas não os montam.

**Contexto:** dúvida do PO dentro da `P-006`. Opções: **A**, só o owner da organização; **B**, o owner e o gestor. O dono escolheu a A. Não houve pontuação numérica, por ser regra de quem configura.

**Por que esta:** o grupo mexe em acesso a boards, relatórios e funcionalidades, que é decisão sensível. Combina com o que o owner da organização já faz (`D-013`, `D-027`) e com a regra de que o membro não compartilha painel (registro de 14/10/2026).

**Fica de fora / adiado:** o gestor montar o grupo da própria equipe. Abre-se mão da autonomia do gestor.

**Hipóteses a validar:** que o owner dá conta de manter os grupos sem virar gargalo.

**Prova de valor:** nenhum grupo existe sem que o owner da organização o tenha criado.

**Reabrir quando:** owners de organizações grandes relatarem que viraram gargalo (grupos parados esperando o owner).

### D-030 · Funcionalidades do Horus poderão ser ativadas ou desativadas por grupo
Situação: ⚪ substituída por `D-050` (o princípio segue, pelo mecanismo das roles) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** em geral, será possível **ativar ou desativar funcionalidades do Horus por grupo de pessoas**. Exemplos do dono: o grupo pode usar o acesso à web ou a Análise avançada no chat? Pode escolher o modelo de IA na conversa? A lista completa fica para depois (`P-009`).

**Contexto:** o dono acrescentou isto à definição dos grupos (`D-029`). Além de acesso a boards, relatórios e alertas, o grupo passa a controlar o que a pessoa pode usar no Horus.

**Fica de fora / adiado:** quais funcionalidades entram na lista e como os interruptores se combinam quando a pessoa está em mais de um grupo.

**Pontos a resolver na definição** *(levantados pelo PO)*:
- A relação com o nível de inferência autorizado pela organização (`D-001`) e com o nível livre dos agentes (`D-024`).
- A relação com a configuração de IA da organização (MF-105:IA sob controle da organização), que hoje define o modelo de cada função.

**Hipóteses a validar:** nenhuma por ora.

**Prova de valor** *(proposta do PO)*: o owner da organização libera a Análise avançada só para o grupo de analistas, sem mexer pessoa por pessoa.

**Reabrir quando:** a lista de funcionalidades mostrar que algum interruptor não faz sentido por grupo.

### D-029 · Os grupos de pessoas servem a vários usos, e não só aos alertas
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** os grupos de pessoas da `D-019` (estáticos e dinâmicos, por claims e/ou papéis) são **um recurso geral da MF-102:Organizações, pessoas e papéis**. Servem, entre outros usos, para:
- configurar a **permissão de acesso a boards**;
- definir quem **recebe relatórios**;
- ser o **grupo de destino dos alertas** dos agentes (MF-115:Agentes ativos).

A lista de usos fica aberta (“etc.”, nas palavras do dono): outros usos podem entrar depois.

**Contexto:** o dono corrigiu o PO, que havia tratado os alertas como o uso principal dos grupos. Esta decisão responde à hipótese da `D-019` (“que o mesmo grupo sirva a acesso e a compartilhamento, e não só a alertas”): sim.

**Por que esta:** um grupo definido uma vez evita repetir a lista de pessoas em cada board, relatório e agente.

**Consequências:**
- A definição macro dos grupos (`P-006`) é a base de outras mfs: o acesso aos boards e relatórios (a mf única da `D-018`) e os destinatários dos agentes.
- 🔎 Segundo o registro de 14/10/2026, o board corporativo já tem “Quem abre”, por regra de claims e pessoas avulsas, e o membro não compartilha painel. Os grupos tendem a generalizar essa regra, e quem configura é o owner da organização, e não cada membro. O arquiteto confirma (`P-008`).

**Hipóteses a validar:** a do item acima.

**Prova de valor:** o owner da organização cria um grupo uma vez e o usa para dar acesso a um board, enviar um relatório e receber um alerta.

**Reabrir quando:** um uso novo de grupo exigir regra diferente das já definidas.

### D-028 · Definição macro da MF-106:Segurança dos dados por pessoa
Situação: 🟢 decidida (confirmada pelo dono em 31/10/2026) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a MF-106:Segurança dos dados por pessoa fica definida assim. Com ela, a `P-004` se fechou.

- **Nome:** MF-106:Segurança dos dados por pessoa (mantido).
- **Quem ganha:** o owner da organização, que configura o acesso sem depender de ninguém; a TI e a segurança do contratante, que não recriam o que já têm; o gestor e o executivo, que perguntam sem receio de ver ou mostrar o que não podem.
- **Decisão que passa a ser possível:** abrir o Horus a mais gente, inclusive a áreas com dados sensíveis (financeiro, pessoas), porque cada um vê só o que lhe cabe.
- **Prova de valor:** na etapa 1, o owner de uma organização sem controle próprio configura o acesso e cada pessoa vê só o que lhe cabe. Na etapa 2, um contratante com controle próprio liga o Horus sem recriar as regras. Nos dois casos, ninguém vê no Horus um dado que a empresa já o impede de ver (`D-026`).
- **Retorno para o negócio:** a confiança destrava a contratação por empresas com regras de acesso, e a implantação tem menos atrito, porque o contratante não refaz as regras.
- **O que não inclui:** criar ou alterar regras de acesso no banco ou no IDP da empresa (`D-022`); criar ou gerenciar usuários no IDP; substituir a segurança do banco (o Horus soma-se a ela, `D-026`).
- **Depende de:** um IDP da empresa que entregue claims e papéis no token (etapa 2); fontes de dados com controle de acesso próprio (etapa 2); a MF-102:Organizações, pessoas e papéis, para os grupos dinâmicos por claims (`D-019`).

**Contexto:** reúne as `D-025`, `D-026` e `D-027`. Os campos “decisão possível”, “retorno”, “o que não inclui” e “depende de” foram propostos pelo PO e confirmados pelo dono; o restante veio do dono.

**Hipóteses a validar:** as da `D-025` e da `D-026`, com o arquiteto de soluções (`P-008`).

**Reabrir quando:** o arquiteto mostrar que alguma etapa não cabe como definida.

### D-027 · O IDP da empresa se liga em cada organização, pelo owner da organização
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a ligação do Horus com o IDP da empresa (o login corporativo) é feita **em cada organização, pelo owner da organização**, e não uma vez por instância.

**Contexto:** dúvida do PO dentro da `P-004`. Opções: **A**, em cada organização; **B**, uma vez na instância. O dono escolheu a A. Não houve pontuação numérica, por ser regra de quem configura.

**Por que esta:** uma organização pode ser um cliente com IDP próprio (`D-008`), e a A também serve a setores da mesma empresa.

**Consequências:** complementa a `D-013`: o owner da organização passa a ligar também o IDP. Numa empresa com vários setores no mesmo IDP, cada organização repete a ligação.

**Hipóteses a validar:** 🔎 que repetir a ligação em cada setor não incomode quem contrata.

**Prova de valor:** um contratante com várias organizações, cada uma com seu IDP, entra com o login da própria empresa.

**Reabrir quando:** contratantes com muitos setores no mesmo IDP reclamarem de repetir a ligação.

### D-026 · As regras da empresa e as do Horus valem juntas, e vale a mais restritiva
Situação: 🟢 decidida (com uma exceção: dentro de um board publicado vale a permissão do gestor, pela `D-054`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** numa mesma fonte de dados, a segurança corporativa (controles de acesso das tecnologias de dados e claims e papéis do IDP) e as regras do documento semântico de segurança do Horus **podem valer ao mesmo tempo**. Quando as duas se aplicarem, **vale a mais restritiva**.

**Contexto:** dúvida do PO aberta dentro da `P-004`, sobre como as duas etapas da `D-025` convivem. Opções: **A**, as duas valem juntas e vale a mais restritiva; **B**, cada fonte usa só uma. O dono escolheu a A. Não houve pontuação numérica, por ser regra de produto sobre confiança.

**Por que esta:** o Horus nunca dá mais acesso do que a empresa deu, e ainda pode restringir mais.

**Consequências:**
- O owner da organização pode restringir, dentro do Horus, uma fonte que já tem controle corporativo.
- Passa a haver duas fontes de regra: o produto terá de explicar a quem pergunta por que um dado não aparece (assunto da definição da MF-106:Segurança dos dados por pessoa).

**Hipóteses a validar:** 🔎 que “vale a mais restritiva” seja simples de calcular e de explicar quando as regras divergem. Quem confirma é o arquiteto de soluções (`P-008`).

**Prova de valor** *(proposta do PO)*: ninguém vê, no Horus, um dado que a empresa já o impede de ver, e o owner da organização consegue esconder mais do que a empresa esconde.

**Reabrir quando:** explicar por que um dado não aparece se mostrar confuso para quem usa.

### D-025 · A MF-106:Segurança dos dados por pessoa será redesenhada em duas etapas
Situação: 🟢 decidida (a direção) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a MF-106:Segurança dos dados por pessoa passa a ter duas etapas, nesta ordem:
1. **Acesso configurado dentro do Horus (o básico).** O usuário define, no próprio Horus, quem acessa quais dados, usando o documento semântico de segurança que o Horus já tem. Serve às empresas que não têm controle de acesso próprio.
2. **Segurança corporativa integrada.** O Horus passa a usar o que a empresa já definiu, em duas frentes:
   - os **controles de acesso a dados das próprias tecnologias de dados** da empresa;
   - a **autenticação integrada ao IDP** da empresa (o sistema de login corporativo), reaproveitando as **claims e os papéis (roles)** do token que ele gera para definir os acessos no Horus.

**Contexto:** o dono abriu a `P-004` com esta direção. O objetivo é o Horus respeitar os controles de acesso que o contratante já tem, em vez de obrigá-lo a recriar tudo.

**Por que esta:** a etapa 1 atende quem não tem controle próprio; a etapa 2 evita retrabalho a quem tem. O básico vem primeiro.

**Fica de fora / adiado:** como as duas formas convivem na mesma fonte de dados, o que já está construído de cada etapa (`P-008`) e a versão em que cada uma entra (a pontuar com a `D-015`).

**Hipóteses a validar:** 🔎 que o documento semântico de segurança, como está, já baste para a etapa 1. Quem confirma é o arquiteto de soluções (`P-008`).

**Prova de valor** *(proposta do PO, confirmada com a `D-028`)*: na etapa 1, o owner de uma organização sem controle próprio configura o acesso e cada pessoa vê só o que lhe cabe. Na etapa 2, um contratante com controle próprio liga o Horus sem recriar as regras.

**Reabrir quando:** a etapa 1 mostrar que o documento semântico de segurança não basta, ou um contratante exigir a etapa 2 antes.

### D-024 · O usuário define livremente o nível de inferência do agente
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** o **usuário que cria o agente** ativo define o nível de inferência dele (descritivo, explicativo, comparativo, hipótese ou especulativo), sem ficar preso ao nível que a organização autorizou para o chat.

**Contexto:** impasse `I-004`, aberto pela `D-023`. Opções: **A**, o nível da organização é o teto do agente (recomendada pelo PO); **B**, o usuário define o nível do agente livremente. O dono escolheu a B. Não houve pontuação numérica, porque a A era a única que respeitava a `D-001` e a decisão era do dono.

**Por que esta:** dá ao usuário a autonomia que é o propósito do norte também nos agentes.

**Consequências:**
- É uma **exceção** à regra da `D-001` de que os níveis de inferência são autorizados pela organização. Vale só para os agentes; o chat segue com o nível da organização. O [norte](02-norte-do-produto.md) foi ajustado.
- A regra do norte de que a resposta acima do descritivo diz que é hipótese ou especulação continua valendo para os alertas.
- O owner da organização não limita o nível dos agentes.

**Hipóteses a validar:** 🔎 que o risco de um alerta chegar com especulação sem aval da organização seja aceito pelos contratantes.

**Prova de valor:** o gestor configura o agente no nível que precisa, e o alerta chega rotulado com o nível usado.

**Reabrir quando:** um contratante exigir que a organização limite o nível dos agentes, ou um alerta especulativo causar uma decisão errada.

### D-023 · O agente interpreta os dados como o usuário o configurar
Situação: 🟢 decidida (a diretriz) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** o agente ativo (`D-020`) criado pelo usuário **interpreta os dados conforme o usuário o configurar**. É o usuário quem define como o agente lê o que extraiu antes de decidir o que avisar.

**Contexto:** o dono acrescentou isto ao escolher a opção A do `I-003`. Complementa a `D-020`.

**Fica de fora / adiado:** o que o usuário pode configurar e até onde (virou o impasse `I-004`, sobre o teto de inferência) e o desenho da tela.

**Hipóteses a validar:** 🔎 que o usuário prefira descrever a interpretação em português, em vez de escolher opções de uma lista.

**Prova de valor:** dois agentes sobre os mesmos dados avisam coisas diferentes, cada um conforme o jeito que o usuário o configurou.

**Reabrir quando:** o `I-004` mudar o que o usuário pode configurar.

### D-022 · O “só lê” vale para as fontes de dados; o Horus pode enviar alertas por canais de saída
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: geral

**Decisão:** o limite “só lê” da `D-001` passa a valer para as **fontes de dados**: o Horus nunca altera dados nem executa ações nos sistemas da empresa. O Horus **pode enviar alertas** por canais de saída (e-mail, WhatsApp, Teams, Google Chat e outros).

**Contexto:** impasse `I-003`, aberto porque o agente ativo (`D-020`) envia alertas a canais externos. Opções: **A**, o limite vale para as fontes; **B**, “só lê” estrito, com o agente avisando só dentro do Horus. O dono escolheu a A. Não houve pontuação numérica, porque a B nega o pedido do dono e sobrava uma única opção viável.

**Por que esta:** libera o problema nº 3 do norte, o aviso, e mantém a garantia que o cliente mais quer: os bancos dele ficam intocados.

**Consequências:**
- Refina a `D-001`: enviar um alerta é saída de informação, e não ação sobre os sistemas da empresa. O [norte](02-norte-do-produto.md) foi ajustado.
- Seguem abertos, e vão para o desenho dos agentes (`P-007`): quem autoriza cada canal, o que o alerta pode conter, o encaixe com o modo “tudo dentro” (`D-010`) e com a segurança por pessoa (MF-106:Segurança dos dados por pessoa).

**Hipóteses a validar:** nenhuma.

**Prova de valor:** o contratante liga o Horus aos canais dele sem receio de que algo mude nos sistemas.

**Reabrir quando:** um contratante exigir “só lê” estrito, inclusive nos canais de saída.

### D-021 · As mfs que o dono não mencionou entram na v2.0 como base herdada
Situação: 🟢 decidida · Data: 31/10/2026 · Versão: geral

**Decisão:** as oito mfs a seguir, do [mapa](04-macro-funcionalidades-de-hoje.md), seguem como **base herdada**: não passam pela pontuação.
- MF-107:Perguntar aos dados em português
- MF-108:Respostas visuais
- MF-104:Conectar as fontes vivas
- MF-109:A web como fonte
- MF-117:Home da organização
- MF-105:IA sob controle da organização
- MF-101:Administração da instância
- MF-118:Bases de demonstração

Só disputam vaga na v2.0 as **candidatas** (hoje, as onze do [inventário](03-inventario-de-lacunas.md), das quais a 10 e a 11 vêm do redesenho da MF-106:Segurança dos dados por pessoa, `D-025`) e o redesenho da MF-106:Segurança dos dados por pessoa, quando for definido (`P-004`).

**Contexto:** impasse `I-002`, aberto pelo mapa das mfs de hoje. Opções: **A**, base herdada; **B**, pontuar tudo junto. O dono escolheu a A. Não houve pontuação numérica, porque a pergunta definia o que entra na pontuação.

**Por que esta:** respeita a `D-003` (o produto de hoje é ponto de partida) e evita pontuar o que já está pronto, onde a nota de tempo até o valor ficaria distorcida.

**Consequências:**
- As lacunas dessas mfs (web completa, retorno do usuário, marca, infraestrutura do contratante) continuam entrando pelas candidatas 1 a 6.
- As mfs a redesenhar ou criar (MF-106:Segurança dos dados por pessoa, MF-006:Acompanhar em boards, MF-008:Relatórios em PDF agendados, MF-102:Organizações, pessoas e papéis e MF-115:Agentes ativos) têm direção própria nas `D-018` a `D-020` e na `P-004`.

**Hipóteses a validar:** nenhuma.

**Prova de valor:** a pontuação da v2.0 compara só o que é novo ou redesenhado.

**Reabrir quando:** o arquiteto de soluções mostrar que uma mf herdada atrapalha o norte.

### D-020 · Nova MF-115:Agentes ativos, que extraem, analisam e avisam
Situação: 🟢 decidida (a necessidade; o agendamento foi para a MF-114 pela `D-036`, e os conectores de saída para a MF-113 pela `D-033`) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** o Horus precisa de uma macro funcionalidade (mf) nova, a **MF-115:Agentes ativos**, de extração e análise de dados. A pessoa cria **agendamentos** de extração, e o agente **emite alertas** para **N conectores de saída** (e-mail, WhatsApp, Teams, Google Chat e outros).

**Contexto:** pedido do dono ao ler o [mapa das mfs de hoje](04-macro-funcionalidades-de-hoje.md). Atende ao **problema nº 3 do norte, o aviso** (`D-001`), que o produto de hoje não cobre. A única saída ativa que existe é o relatório agendado por e-mail (MF-008:Relatórios em PDF agendados).

**Tensões que o desenho terá de resolver:**
- O norte diz que o Horus **só lê** (`D-001`); enviar um alerta a um canal externo é uma saída. Virou o impasse `I-003` no backlog.
- O modo “tudo dentro” (`D-010`): canais como o WhatsApp levam informação para fora da infraestrutura do contratante.
- A segurança por pessoa (MF-106:Segurança dos dados por pessoa): um alerta num canal compartilhado chega igual a todos. Liga-se à MF-106, a redesenhar, e aos grupos (`D-019`).

**Fica de fora / adiado:** a versão em que entra (a pontuar com os pesos da `D-015`), o que o agente faz e quais conectores vêm primeiro.

**Hipóteses a validar:** 🔎 que o aviso é o que mais falta ao gestor depois da pergunta de análise na hora (o norte já o põe em terceiro lugar).

**Prova de valor:** a pessoa fica sabendo de uma mudança relevante por um alerta, sem ter perguntado.

**Reabrir quando:** a pontuação da v2.0 mostrar que o aviso não cabe na primeira versão, ou o impasse do “só lê” mudar o desenho.

### D-019 · A MF-102:Organizações, pessoas e papéis ganha grupos de pessoas, estáticos e dinâmicos
Situação: 🟢 decidida (a necessidade) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a MF-102:Organizações, pessoas e papéis precisa permitir **grupos de pessoas**. Um grupo **estático** tem a lista escolhida à mão. Um grupo **dinâmico** tem a lista definida por uma regra baseada em **claims** e/ou **papéis**, e muda sozinho quando a pessoa muda.

**Contexto:** hoje a pessoa tem um papel (owner, gestor ou membro) e claims de acesso (MF-106:Segurança dos dados por pessoa), mas não existe agrupar pessoas. Os grupos devem servir, ao menos, de destinatários dos alertas dos agentes (`D-020`).

**Fica de fora / adiado:** para que mais os grupos servem (acesso, compartilhamento, destinatário), a versão e o desenho.

**Hipóteses a validar:** 🔎 que o mesmo grupo sirva a acesso e a compartilhamento, e não só a alertas.

**Prova de valor:** o owner da organização cria um grupo dinâmico uma vez, e a lista se mantém sozinha quando as pessoas mudam.

**Reabrir quando:** o redesenho da MF-106:Segurança dos dados por pessoa mudar o que é claim e o que é papel.

### D-018 · MF-006:Acompanhar em boards e MF-008:Relatórios em PDF agendados serão repensadas como uma mf só
Situação: 🟢 decidida (a direção) · Data: 31/10/2026 · Versão: a pontuar

**Decisão:** a MF-006:Acompanhar em boards e a MF-008:Relatórios em PDF agendados serão **repensadas juntas**. O editor de relatórios poderá desenhar também os boards, e boards e relatórios passam a ser **uma coisa só, com formatos de saída diferentes** (por exemplo, tela viva e PDF).

**Contexto:** hoje são dois editores e duas telas. O norte havia deixado o acompanhamento recorrente para “quando decidirmos a funcionalidade de Board” (`D-001`); isso passa a ser tratado nesta mf única.

**Fica de fora / adiado:** o desenho da mf única (o que cada formato de saída oferece) e a versão em que entra.

**Hipóteses a validar:** 🔎 que o editor de relatórios aguente o que o board faz hoje (cartões que se recalculam, apresentação em laço, filtros por pessoa). Quem confirma é o arquiteto de soluções.

**Prova de valor:** a mesma montagem sai como tela viva e como PDF, sem refazer.

**Reabrir quando:** o arquiteto mostrar que o editor de relatórios não comporta o que o board faz.

### D-017 · A versão é a mesma em SaaS e on-premises; a diferença está na instância
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** o Horus tem **uma versão só**, igual em SaaS e on-premises. A diferença está na **instância**: onde ela roda, quem a opera e como é configurada.

**Contexto:** o dono corrigiu a `D-016`, que tratava a forma de entrega como escolha de versão. Os dois modos já existiam na `D-007`; faltava dizer que eles não dividem as versões.

**Por que esta:** manter uma só versão evita um produto para cada forma de entrega, com funcionalidades diferentes, correções duplicadas e dois caminhos de atualização.

**Consequências:**
- Nenhuma macro funcionalidade é “só SaaS” ou “só on-premises”.
- A forma de entrega **não entra** na composição das versões.
- O que a instância on-premises exige (a fonte alcançar a rede interna do contratante, a IA dentro da infraestrutura) deixa de ser “escolha de v2.0” e passa a ser **capacidade do produto** para que a mesma versão rode em qualquer instância. Entra no inventário como lacuna.

**Fica de fora / adiado:** como a instância é instalada, atualizada e operada — assunto do arquiteto de soluções.

**Hipóteses a validar:** nenhuma.

**Prova de valor:** a mesma versão sobe nas duas instâncias, e o usuário faz o mesmo nas duas.

**Reabrir quando:** surgir uma funcionalidade que só faça sentido em uma das formas.

### D-016 · Forma de entrega da v2.0: SaaS primeiro
Situação: ⚪ substituída por `D-017` (o dono esclareceu que a forma de entrega não divide as versões) · Data: 30/10/2026 · Versão: v2.0

**Decisão (proposta):** a v2.0 chega aos contratantes em **SaaS**, na infraestrutura da Maind. A entrega **on-premises** fica para a versão seguinte.

**Contexto:** primeira bifurcação da composição da v2.0, aberta pelas lacunas 14 a 16 do inventário. Objetivo da v2.0: levar a **pergunta de análise na hora** (problema nº 1) à empresa que usa o Horus por dentro (`D-009`). Pontuada com os pesos da `D-015`.

**Opções avaliadas** (nota de 0 a 100):

| Opção | Nota |
| --- | --- |
| 🏆 SaaS primeiro, on-premises depois | **80** |
| 🥈 SaaS e on-premises juntos | 73 |
| 🥉 On-premises primeiro | 54 |

Detalhe dos critérios, dos prós e dos contras na conversa de 30/10/2026.

**Por que esta:** ganha no tempo até o valor e no aprendizado: o produto já roda em servidor da Maind (roteiro de publicação existente) e começa a ensinar com clientes reais mais cedo.

**Fica de fora / adiado:** a entrega on-premises, o modo “tudo dentro” da IA (`D-010`) e a fonte alcançando a rede interna do contratante.

**Hipóteses a validar:** que há clientes dispostos a começar em SaaS; o esforço real de instalar on-premises, ainda não medido.

**Prova de valor:** empresas usando em SaaS, com as perguntas de análise respondidas, antes de qualquer instalação on-premises.

**Reabrir quando:** um primeiro cliente-âncora exigir os dados dentro da própria infraestrutura desde o início.

### D-015 · Pesos da pontuação entre caminhos
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** toda escolha entre caminhos é pontuada com seis critérios: **aderência à missão 25**, **tempo até o valor 25**, **confiança e governança 20**, **retorno para o negócio 15**, **aprendizado e reversibilidade 5** e **alavancagem 10** (soma 100).

**Contexto:** a primeira proposta tinha confiança 15 e aprendizado 10. À luz do norte, onde um número errado diante do CEO é pior que nenhum, a confiança sobe cinco pontos e o aprendizado cede cinco.

**Por que esta:** a confiança é a prova da promessa; o tempo até o valor segue em 25 porque a regra do dono é priorizar o que traz valor mais rápido; o aprendizado pesa menos porque a diretriz é entregar a opção definitiva.

**Fica de fora / adiado:** nenhum critério novo por ora.

**Hipóteses a validar:** nenhuma.

**Prova de valor:** as escolhas entre caminhos passam a vir com nota, ranking e motivo, e a comparação entre elas é consistente.

**Reabrir quando:** uma pontuação der um resultado que o dono sinta ser errado, sinal de que o peso de algum critério não reflete o que importa.

### D-014 · Os reportes vão para o owner da organização
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** quem recebe os reportes (`D-005`) é o **owner da organização** (ou área) em que a resposta foi dada.

**Contexto:** a `D-005` diz que o time de gestores da ferramenta analisa uma possível falha no modelo semântico ou nos dados. Com os dois níveis de owner (`D-013`), faltava dizer quem é esse time. Alternativas: o owner da organização, o owner da instância, ou depender do motivo.

**Por que esta:** o modelo semântico e os dados pertencem à organização. Quem os mantém é quem sabe corrigi-los, e o owner da instância não conheceria o assunto de cada setor.

**Fica de fora / adiado:** reportes de falha geral do produto e o encaminhamento ao owner da instância. Só entram se surgir um motivo de reporte que não seja do modelo semântico nem dos dados.

**Hipóteses a validar:** o que o owner da organização faz com cada reporte e em quanto tempo responde; se uma organização pode delegar a análise a outras pessoas.

**Prova de valor:** todo reporte chega ao owner da organização certa e leva a uma correção ou a uma resposta.

**Reabrir quando:** surgir um motivo de reporte que não seja da organização.

### D-013 · Dois níveis de owner: o da instância e o da organização
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** existem **dois tipos de owner**.
- **Owner da instância:** configura a **marca da instância** (logo, nome e e-mail, conforme a `D-011`) e o que vale para todas as organizações.
- **Owner da organização (ou área):** **convida pessoas**, configura **preferências** e cuida do que pertence à própria organização.

**Contexto:** informado pelo dono ao discutir quem recebe os reportes (`D-005`). O produto de hoje já faz essa separação: a área “Administração” (identidade, desempenho, segurança, homologações e administradores) vale para todas as organizações, e a área “Organização” (informações, bases, modelos, funcionalidades de IA, gráficos, membros e segurança de acesso) vale para cada uma.

**Por que esta:** casa com as várias organizações por instalação (`D-008`) e com a marca branca (`D-011`): quem cuida da marca e das regras gerais não é quem convida pessoas e cuida do modelo semântico de um setor.

**Fica de fora / adiado:** a divisão exata de cada configuração entre os dois níveis e o que cada um pode delegar — assunto do arquiteto de soluções e das regras de acesso.

**Hipóteses a validar:** se a divisão de hoje entre “Administração” e “Organização” serve para o Horus que estamos desenhando.

**Prova de valor:** cada configuração tem um dono claro; o owner de uma organização nunca altera a marca da instância, nem o da instância convida pessoas por ele.

**Reabrir quando:** surgir um caso que exija um terceiro nível de responsabilidade.

### D-012 · A frase da promessa mora na comunicação da Maind
Situação: 🟢 decidida (confirmada pelo dono em 30/10/2026) · Data: 30/10/2026 · Versão: geral

**Decisão:** a frase da promessa (“Informação na palma da mão”, hoje nome de trabalho) vive na **comunicação comercial da Maind**, voltada a quem contrata. Dentro do produto, cada contratante usa a sua marca (`D-011`).

**Contexto:** impasse aberto pela marca branca. O dono definiu que a personalização é só de logo, e-mail e nome, e que as páginas institucional e de propaganda ficam apartadas do produto (`D-011`). A frase de promessa é conteúdo de propaganda.

**Opções avaliadas:** na comunicação da Maind (recomendada), no produto de forma trocável, fixa em toda instalação.

**Por que esta:** o usuário final não vê a Maind; embutir a nossa frase no produto contraria a marca branca. A frase continua a convencer o comprador, que é quem a lê.

**Hipóteses a validar:** a redação final da frase, que fica para o documento de posicionamento.

**Prova de valor:** nenhuma tela do produto exibe a frase da Maind.

**Reabrir quando:** o contratante pedir para ter uma frase de apresentação dentro do produto.

### D-011 · Escopo do white label: logo, e-mail e nome
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: v2.0

**Decisão:** na primeira entrega com marca branca, o contratante configura apenas o **logo** da empresa, o **e-mail** e o **nome**. O **tema** (visual) fica para uma **versão futura**, ainda a ordenar. As páginas **institucional e de propaganda ficam apartadas** do produto.

**Contexto:** informado pelo dono ao discutir onde mora a frase da promessa.

**Por que esta:** entrega a marca do contratante com pouco trabalho, e mantém a comunicação comercial fora do produto.

**Fica de fora / adiado:** o tema e qualquer personalização além de logo, e-mail e nome.

**Hipóteses a validar:** o que “e-mail” cobre exatamente (por exemplo, o remetente das mensagens do produto).

**Prova de valor:** o contratante vê a própria marca no produto, e o usuário final não encontra a marca da Maind.

**Reabrir quando:** clientes exigirem personalizar mais do que logo, e-mail e nome já na primeira entrega.

### D-010 · IA e web: o contratante escolhe, com serviços externos autorizados como padrão
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** o Horus oferece **dois modos** para a IA e a pesquisa web: **“com serviços externos autorizados”** e **“tudo dentro”** da infraestrutura do contratante. O **padrão** é “com serviços externos autorizados”, e cada contratante liga o que quiser.

**Contexto:** impasse aberto pela entrega on-premises (`D-007`): quem instala na própria infraestrutura costuma ter exigências de segurança diferentes, e o norte promete a web como fonte viva e a confiança como prova. Alternativas: sempre sair com autorização, nada sair, o contratante escolher, ou sair só a web.

**Por que esta:** mantém as duas promessas do norte sem forçar todos ao mesmo modelo. Quem aceita serviços externos ganha tudo o que o norte descreve; quem exige que nada saia tem um modo próprio.

**Fica de fora / adiado:** em que versão entra o modo “tudo dentro” e o que ele deixa de oferecer (por exemplo, a pesquisa web). Será ordenado na composição das versões, pelo tempo até o valor.

**Hipóteses a validar:** a parcela dos contratantes que exigirá “tudo dentro”; o que, em cada modo, o contratante autoriza a sair (a pergunta de análise, os resultados, nenhum dado dos bancos).

**Prova de valor:** o contratante liga e desliga o que sai da infraestrutura, e o Horus respeita essa escolha em toda resposta.

**Reabrir quando:** a maioria dos contratantes exigir “tudo dentro” ou nenhum o fizer.

### D-009 · O primeiro contratante é a empresa que usa por dentro
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: v2.0

**Decisão:** o primeiro contratante a conquistar é a **empresa que usa o Horus por dentro**, para os próprios setores e gestores. Cada setor é uma organização na instalação. A revenda (consultoria, software house ou integrador que oferece o Horus aos seus clientes) fica como **segundo passo**.

**Contexto:** impasse aberto ao registrar a marca branca e as várias organizações (`D-007`, `D-008`). Alternativas: a empresa que usa por dentro, a que revende, ou as duas com o mesmo peso.

**Por que esta:** o norte, o momento-âncora (o gestor respondendo ao CEO) e as medidas de sucesso foram desenhados para quem usa por dentro. Quando a empresa final provar o valor, a revenda tende a surgir como consequência.

**Fica de fora / adiado:** o canal de revenda: marca de cada cliente, isolamento forte entre clientes, preço para revendedor. Voltam a ser decididos quando a revenda entrar em pauta.

**Hipóteses a validar:** que a revenda vem depois da prova de valor na empresa final.

**Prova de valor:** empresas contratando para os próprios setores e usando de forma recorrente.

**Reabrir quando:** um revendedor aparecer com demanda concreta antes da prova de valor na empresa final.

### D-008 · Uma instalação do Horus comporta várias organizações
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** cada instalação (instância) do Horus permite ter **várias organizações**. Uma organização pode representar um **cliente** (em cenários B2B) ou um **setor** dentro de uma empresa, entre outros usos.

**Contexto:** informado pelo dono ao revisar o norte, como característica da plataforma.

**Por que esta:** uma mesma instalação atende estruturas diferentes, de uma empresa com vários setores a quem serve vários clientes, sem precisar de uma instalação por cada um.

**Fica de fora / adiado:** como as organizações se isolam, quem as administra e como se compartilha entre elas — é assunto do arquiteto de soluções, apoiado nas regras de acesso e segurança.

**Hipóteses a validar:** os usos além de “cliente” e “setor”.

**Prova de valor:** uma só instalação atende, ao mesmo tempo, organizações com estruturas diferentes sem misturar os dados de uma com os de outra.

**Reabrir quando:** surgir um uso de organização que o modelo não comporte.

### D-007 · Horus é plataforma white label, em duas formas de entrega
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** o Horus é uma **plataforma white label** (pode levar a marca de quem a contrata) e é entregue de duas formas: **on-premises**, na infraestrutura do contratante, ou **SaaS**, contratada na infraestrutura da Maind.

**Contexto:** informado pelo dono ao revisar o norte; muda a pergunta de quem é o cliente, de quem é a marca e de onde ficam os dados.

**Por que esta:** atende quem exige os dados dentro da própria infraestrutura e quem prefere contratar pronto, com a mesma plataforma.

**Fica de fora / adiado:** como implantar, atualizar e operar cada forma de entrega (assunto do arquiteto de soluções); preço de cada modelo (tema 18 da visão de produto).

**Hipóteses a validar:** a parcela de clientes que prefere cada forma; o que a marca branca precisa permitir personalizar.

**Prova de valor:** o mesmo produto roda nas duas formas, com a marca do contratante, sem diferença no que o usuário consegue fazer.

**Reabrir quando:** uma das formas de entrega se mostrar inviável ou sem demanda.

### D-006 · Toda informação da web mostra a fonte e a data
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** toda informação que o Horus traz da web aparece com o **link da fonte** e a **data de publicação**. Quando não for possível identificar a data, o Horus **avisa expressamente** que não foi possível identificar a data da informação obtida na web.

**Contexto:** impasse aberto na `D-001`: como o Horus indica a qualidade e a atualidade do que vem de fora. Alternativas: fonte e data sempre, selo de confiança, aviso só quando frágil, lista de fontes aprovadas.

**Por que esta:** é simples e cumpre a prova do norte. O gestor sabe o que é dado da empresa e o que veio de fora, e confere a origem antes de mostrar ao CEO. Avisar quando a data falta evita que uma informação antiga passe por atual sem ninguém perceber.

**Fica de fora / adiado:** classificação da origem em selos (oficial, imprensa, outras) e lista de fontes aprovadas pela organização; podem voltar como refinamentos.

**Hipóteses a validar:** nenhuma.

**Prova de valor:** nenhuma informação da web aparece sem fonte, e nenhuma aparece sem data ou sem o aviso de que a data não foi identificada.

**Reabrir quando:** clientes pedirem controle sobre as fontes usadas, ou a qualidade das fontes se mostrar um problema recorrente.

### D-005 · Retorno do usuário sobre cada resposta
Situação: 🟢 decidida (confirmada pelo dono em 30/10/2026) · Data: 30/10/2026 · Versão: geral

**Decisão:** o usuário pode avaliar cada resposta do Horus com três sinais: **👍🏻 Gostei**, **👎🏻 Não gostei** e **🚫 Reportar**. Ao **reportar**, o usuário **escolhe o que está reportando**, para que o **time de gestores da ferramenta** analise uma possível falha no **modelo semântico** ou nos **dados**.

**Contexto:** a `D-004` deixa a satisfação de fora da definição de pergunta de análise respondida. O retorno do usuário passa a ser o canal próprio para medir a qualidade percebida.

**Por que esta:** separa duas coisas que se confundem. Cobertura é o Horus ter conseguido responder (`D-004`); qualidade é a pessoa achar a resposta boa. Sem a segunda, uma resposta ruim contaria como sucesso sem ninguém perceber.

**Fica de fora / adiado:** formato, posição e comportamento dos botões, que são assunto do arquiteto de soluções.

**Hipóteses a validar:** quais opções de motivo o usuário vê ao reportar (além de modelo semântico e dados); o que o time faz com os reportes e em quanto tempo responde.

**Prova de valor:** parcela das respostas que recebem avaliação, proporção entre 👍🏻 e 👎🏻 e reportes tratados.

**Reabrir quando:** poucas pessoas avaliarem, ou os sinais não ajudarem a melhorar as respostas.

### D-004 · O que é uma pergunta de análise respondida
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** uma pergunta de análise é **respondida** quando o Horus consegue responder, com gráfico, com texto ou com os dois, **independentemente da satisfação do usuário**.

**Contexto:** impasse aberto na `D-001`, que sustenta a medida principal do norte (perguntas de análise respondidas sem chamado). Alternativas: sem sinal de desistência, confirmação explícita, uso do resultado e ausência de chamado.

**Opções avaliadas:** o dono escolheu uma variação da primeira alternativa: em vez de observar o comportamento do usuário, a definição olha **o que o Horus entregou**.

**Por que esta:** mede a cobertura (o Horus consegue?) sem depender de clique, de opinião nem de integração com outro sistema. A qualidade é medida à parte: pelo retorno do usuário (`D-005`) e, de fora do produto, pelos chamados que ainda chegam à área de dados.

**Consequência a ter em mente:** uma resposta errada ainda conta como respondida; por isso a qualidade tem medidas próprias. Se o Horus diz que não consegue responder, a pergunta de análise não conta como respondida.

**Fica de fora / adiado:** satisfação do usuário (vai para a `D-005`).

**Hipóteses a validar:** nenhuma.

**Prova de valor:** a parcela das perguntas de análise que o Horus consegue responder, acompanhada da queda de chamados à área de dados.

**Reabrir quando:** a taxa de respondidas subir sem os chamados caírem, sinal de que respostas ruins estão contando como sucesso.

### D-003 · O norte guia o produto; o produto de hoje é ponto de partida
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** quando o norte e o produto atual divergirem, a divergência é uma **lacuna a fechar**, e não um motivo para encolher o norte. O produto de hoje serve para inventariar o que já existe e medir a distância até o norte.

**Contexto:** ao registrar a `D-001`, a skill apontou que a pesquisa web, hoje restrita pelos níveis de inferência, destoa do norte e tratou a divergência como uma escolha entre mudar o produto ou ajustar o norte. O dono corrigiu: o objetivo de documentar o norte é justamente dar um passo atrás para estruturar o crescimento do Horus.

**Por que esta:** se o produto de hoje limitasse o norte, o resultado seria uma descrição do que já existe, sem crescimento planejado. É como projetar a casa antes de olhar o terreno: o terreno informa os desvios, mas a planta é que decide o que se constrói.

**Fica de fora / adiado:** quando e como fechar cada lacuna — é assunto da priorização por versão e do arquiteto de soluções. Mudar um gesto ou o visual de algo que já existe continua sendo decisão do dono, caso a caso.

**Hipóteses a validar:** nenhuma.

**Prova de valor:** cada lacuna entre o norte e o produto aparece registrada, com destino claro (versão em que será fechada ou motivo de adiamento).

**Reabrir quando:** o norte for revisado (nova decisão que substitua a `D-001`).

### D-002 · Acesso em qualquer dispositivo é pressuposto
Situação: 🟢 decidida · Data: 30/10/2026 · Versão: geral

**Decisão:** o usuário acessa o dado no computador, no celular e no tablet, e a responsividade é **pressuposto de todas as versões**, não uma funcionalidade a priorizar.

**Contexto:** na `D-001`, “palma da mão” deixou em aberto se o uso no celular entrava na primeira versão. O dono esclareceu que o comportamento por dispositivo está num nível abaixo do produto; para o executivo do produto, basta que o dado esteja ao alcance em qualquer tela.

**Por que esta:** a promessa fala em ter a informação à mão, e o momento-âncora acontece numa reunião, onde o dispositivo pode ser qualquer um. Tratar como pressuposto evita discutir “celular sim ou não” a cada versão.

**Fica de fora / adiado:** como cada tela se comporta em cada dispositivo — é assunto do arquiteto de soluções.

**Hipóteses a validar:** nenhuma nova. Resolve a hipótese “uso no celular” listada na `D-001`.

**Prova de valor:** a pessoa consegue fazer a pergunta e entender a resposta nos três tipos de dispositivo, sem perder clareza do visual.

**Reabrir quando:** algum dispositivo se mostrar inviável para a clareza do visual ou para a segurança.

### D-001 · Norte do produto: autonomia, para o gestor e o executivo
Situação: 🟢 decidida (o limite “só lê” foi refinado pela `D-022`, e o nível de inferência dos agentes é livre, pela `D-024`) · Data: 30/10/2026 · Versão: geral

**Decisão:** o Horus existe para dar **autonomia** a quem decide, atendendo primeiro o gestor de área e o executivo, com a pergunta na hora como primeiro problema e “informação na palma da mão” (nome provisório) como promessa. O texto completo está em [02-norte-do-produto.md](02-norte-do-produto.md).

**Contexto:** ponto de partida da visão de produto (temas 1 a 5 da lista inicial). Não havia missão nem objetivos escritos; a skill precisava de um norte para pontuar as escolhas seguintes. Decisão tomada em entrevista, um bloco por vez, com recomendação em cada pergunta e confirmação do dono (sem pontuação numérica, porque ainda não havia norte contra o qual pontuar).

**Opções avaliadas** (a escolhida em negrito):

| Bloco | Escolha | Alternativas |
| --- | --- | --- |
| Propósito | **Autonomia** | Confiança, produtividade da área de dados, antecipação |
| Público inicial | **Gestor de área e executivo** | Analista de negócio, pessoa da área de dados |
| Problema primeiro | **A pergunta na hora, depois a investigação, depois o aviso** | A pergunta recorrente (adiada para o Board) |
| Promessa | **Informação na palma da mão**, com a confiança como prova | Sem ponto cego, sem complicação, sem medo |
| Sucesso | **Perguntas respondidas sem chamado** (norte) e **saving da área de dados** (comprador) | Tempo até a resposta, uso recorrente |
| Limites | **Só lê** e **não arruma os dados** | Não ser construtor de dashboards sofisticados (rejeitado: o visual é valor central) |

**Por que esta:** a autonomia é o que o usuário sente e o comprador paga; a confiança entra como condição, não como razão de existir. O dono acrescentou que a web é fonte viva ao lado dos bancos, e que o visual da resposta é parte do valor.

**Fica de fora / adiado:** acompanhamento recorrente (decidido junto com a funcionalidade de Board); uso no celular (ponto em aberto).

**Hipóteses a validar:** uso no celular na v2.0; ponto de partida de chamados da área de dados; definição de “pergunta respondida”; qualidade e data da informação da web; a web nos níveis baixos de inferência (hoje só traz fatos a partir do nível 4).

**Prova de valor:** a porcentagem de perguntas respondidas sem chamado e as horas de chamados que a área de dados deixou de atender.

**Reabrir quando:** a validação com clientes mostrar que o primeiro público não é o gestor, ou que a promessa não se sustenta na reunião ao vivo.
