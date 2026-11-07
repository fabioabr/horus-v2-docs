# Backlog estratégico do Horus

Registro das decisões de produto: o que o Horus entrega, para quem e em que ordem. Mantido pela skill `product-owner-horus`.

Aqui entram decisões de **valor** (visão, público, macro funcionalidades, versões, preço, cortes). Tarefas e escolhas de **como construir** pertencem ao arquiteto de soluções e não são registradas neste arquivo.

Última atualização: 07/11/2026.

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
- **A numeração das mfs foi refeita duas vezes.** Em 01/11/2026 (`D-100` a `D-102`), em ordem de leitura, de `MF-01` a `MF-19`. Em 02/11/2026 (`D-137` a `D-139`), pela entrega em que a mf entra e pela importância para a fundação do novo Horus: **de `MF-101` a `MF-119`**. A regra de número fixo vale a partir desta última, a `MF-120` foi dada à faixa de avisos e números (`D-152`, nome provisório), a `MF-121`, ao middleware (`D-196`; hoje `MF-121:Middleware da organização`, `D-270`), a `MF-122`, aos conectores de chat corporativo, e a `MF-123`, ao AWS Athena (`D-198`, nomes provisórios), e a próxima mf nova é a `MF-124`. Os números anteriores (os de dois dígitos e os de três que começam com zero, `MF-001` a `MF-021`) só valem na tabela de conversão do mapa. Em todas as decisões, as citações de mf foram trocadas pelos números novos, e o conteúdo das decisões não mudou; as decisões das próprias renumerações (`D-100` a `D-102` e `D-137` a `D-139`) mantêm os números da época. A `MF-006` e a `MF-008`, substituídas, não ganharam número novo e aparecem com o número mais antigo.
- **Os números `D-138` e `D-139` foram usados duas vezes** (achado na revisão de 05/11/2026): outra sessão registrou as decisões do MVP da v1.xx (`D-138`, "A v1.xx fecha como MVP no HML…", e `D-139`, "No MVP da v1.xx, as seis peças pela metade saem todas da tela") quando a renumeração das mfs já tinha as suas (`D-138`, "O número novo das mfs tem três dígitos…", e `D-139`, "Tabela de conversão das mfs…"). Nenhuma foi renumerada, para não quebrar as citações: cite sempre `D-138 (MVP)`, `D-139 (MVP)`, `D-138 (numeração)` ou `D-139 (conversão)`. Do `D-140` em diante os números são únicos.

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
| `P-022` | 🕓 Pendência | Definir o **preço em reais** do plano único, por tipo de assento (*com a `D-267`, a Maind paga a chave de IA que dá à organização: o preço precisa dizer se essa IA dada entra no preço do assento*). Precisa da visão de mercado, que segue em aberto para o PO, e do primeiro cliente | `D-116` | Dono e comercial da Maind, com a visão de mercado (o PO pode pesquisar o mercado se o dono pedir, opção C da `D-116`). **Pode esperar:** o preço fica fora dos documentos de produto e não trava a v2.0 | 02/11/2026 |
| `P-028` | 🕓 Pendência | **Sincronizar a arquitetura e o portal com as decisões `D-146` a `D-240`** *(a parte do PO, o inventário `04`, `05`, `06` e `07` e as páginas de leitura, ficou pronta em 05/11/2026, até a `D-240`; a arquitetura também precisa acompanhar o que mudou da `D-204` à `D-240`: sem transferência e sem área que recebe o que sai, `D-206` a `D-211`; a IA da organização ou da instância, `D-216` e `D-217`; a web como interruptor, `D-215`; o PDF de uma página só, `D-229`; o grupo dinâmico por tipo de assento, `D-235`; a planilha de convites só do owner, `D-236`; e, de 06/11/2026, a exportação da conversa e o registro dela no rastro, `D-249` a `D-252`, e o login da empresa, `D-253` a `D-257`, que fecham o `A-20` e o `A-25` do documento 14)*: o documento 01 (a seção 4 lista 19 mfs, põe a marca completa e o interruptor na `MF-101` e tem o marco de marca), o 04, o 05 e o 14, a nota de "backlog congelado" dos documentos 01 e 14 e do README da arquitetura (os itens `A-02`, `A-21` e `A-29` do 14 viraram `I-015`, `P-025` e `P-026`); e o portal, cujo `montar_fontes.py` está fixo em 19 mfs e lê a lista da seção 4 do documento 01 | `D-146` a `D-240` | Arquiteto de soluções (arquitetura) e PO (o portal, depois do 01) | 05/11/2026 |
| `P-029` | 🕓 Pendência | **Numerar os 24 itens restantes do documento 14** (`A-nn` sem número), que o backlog congelado não pôde receber. *Em 06/11/2026, o `A-20` e o `A-25` foram resolvidos com o dono (`I-070` a `I-074`, `D-253` a `D-257`); restam sem número, do dono, o `A-05`, o `A-06` e o `A-15`, e, do PO, o `A-07`, o `A-12`, o `A-26` e o `A-27`.* Os impasses `A-03`, `A-04` e `A-11` já ganharam número em 05/11/2026 (`I-016`, `I-017` e `I-018`); na revisão das mfs da v2.0, também em 05/11/2026, os itens `A-08`, `A-10`, `A-13`, `A-14`, `A-16`, `A-17`, `A-18`, `A-19`, `A-22`, `A-23`, `A-24` e `A-30` viraram impasses (`I-030` a `I-043`) | Documento 14 (arquitetura), seção 4 | PO | 05/11/2026 |
| `P-032` | 🕓 Pendência | **Para o arquiteto de soluções:** como a conta de IA da Maind chega às organizações do SaaS (hoje a v1.xx tem a conexão de IA de cada organização) e o que acontece com a conexão que uma organização já cadastra. *O lado do produto está decidido: a IA é sempre da organização, configurada no front do middleware, pela organização ou pelo time da Maind; a Maind pode dar uma chave que ela paga; não há mais conexão da instância (`D-264` a `D-267`). Fica para o arquiteto como a chave dada chega à configuração da organização e o que acontece com a conexão que a organização já cadastra* | `D-159`, `D-216`, `D-264` a `D-267` | Arquiteto de soluções | 05/11/2026 |
| `P-033` | 🕓 Pendência | **Para o arquiteto de soluções:** dimensionar o AWS Athena na v2.1: o conector, o dialeto, a segurança por pessoa (que hoje só cobre o SQL Server) e o que isso pede do resto da v2.1 | `D-161` | Arquiteto de soluções | 05/11/2026 |
| `P-034` | 🕓 Pendência | **Para o arquiteto de soluções:** conferir o que é a "fonte de páginas web" da v1.xx (a conexão do tipo `web`, que o chat lê no lugar de planejar uma consulta), se a `ARQ-027` a cobre, e decidir se o tipo de fonte `web` some ou continua | `D-162` | Arquiteto de soluções | 05/11/2026 |
| `P-035` | 🕓 Pendência | **Para o arquiteto de soluções:** como o motor calcula o board público em nome do owner que o publicou (`D-164`). *Com a `D-209`, o board some junto com o owner que sai: deixou de ser dúvida o que acontece nesse caso* | `D-164`, `D-048` | Arquiteto de soluções | 05/11/2026 |
| `P-036` | 🕓 Pendência | **Para o arquiteto de soluções:** como a faixa calcula os cards de número com o acesso de cada pessoa sem pesar na abertura da tela (reaproveitar o cálculo por escopo, o ritmo de atualização) | `D-167` | Arquiteto de soluções | 05/11/2026 |
| `P-037` | 🕓 Pendência | **Para o arquiteto de soluções:** o arquivo de licença do on-premises: o formato, a assinatura, a importação e a conferência sem internet, e o que fazer com um arquivo adulterado (`D-175`) | `D-175`, `P-016` | Arquiteto de soluções | 05/11/2026 |
| `P-038` | 🕓 Pendência | **Para o arquiteto de soluções:** como o Teams e o Google Chat se integram como conectores de saída (a forma de integrar, a autenticação, a aprovação da TI do cliente e o que cada um entrega: texto, imagem e link) (`D-182`) | `D-182`, `D-124`, `ARQ-046` | Arquiteto de soluções | 05/11/2026 |
| `P-039` | 🕓 Pendência | **Para o arquiteto de soluções:** o provedor de IA compatível com o protocolo da OpenAI que o contratante aponta no modo "tudo dentro": a conexão, a guarda de rede (o modelo mora na rede interna), os modelos que o Horus prova e a qualidade mínima de resposta (`D-185`) | `D-185`, `ARQ-051` | Arquiteto de soluções | 05/11/2026 |
| `P-040` | 🕓 Pendência | **Para o arquiteto de soluções:** a viabilidade do middleware na casa do contratante (`D-188`): quais partes do motor de análise rodam nele, como ele se conecta ao Horus sem abrir porta no cliente, como se atualiza e o que acontece com as decisões `D-175`, `D-176`, `D-185` a `D-187`, a `ARQ-060` e a `ARQ-074`. Parte do impasse `I-020`. *Em 07/11/2026, o dono confirmou o lado do produto: o ciclo da análise (o modelo de IA e as consultas) roda dentro do middleware, e ao Horus chega só a pergunta e a resposta pronta (`D-189`, `D-196`). O rascunho dele traz ainda uma base de configuração e um aplicativo de setup na casa do cliente, decididos nas `D-258` a `D-269` (o desenho técnico segue na `P-048`)* | `D-188`, `I-020`, `ARQ-052` (opção 3) | Arquiteto de soluções | 05/11/2026 |
| `P-042` | 🕓 Pendência | **Para o arquiteto de soluções:** a imagem do middleware (`D-195`): **o protocolo (servidor MCP, API REST ou gRPC, de preferência gRPC, `D-196`)**, o endereço público, o par de chaves cadastrado no Horus por organização, a rotação das chaves, o bloqueio por IP e porta, a atualização da imagem pelo cliente e o que o Horus faz quando o middleware está fora do ar. Parte da `P-040` | `D-195`, `P-040` | Arquiteto de soluções | 05/11/2026 |
| `P-044` | 🕓 Pendência | **Para o arquiteto de soluções:** conferir se apagar tudo de quem é excluído (`D-210`) convive com a guarda técnica do registro de acesso (seis meses, `ARQ-035`) e com as cópias de segurança; e o que a Auditoria, o aviso de abertura e a medida de autonomia precisam mudar. *O lado jurídico passou ao setup de cada cliente (`D-247`)* | `D-209`, `D-210`, `ARQ-035`, `D-247` | Arquiteto de soluções | 05/11/2026 |
| `P-046` | 🕓 Pendência | **Definir os componentes da faixa de avisos e números:** o catálogo (KPIs, ícones etc.), as regras de cada um (inclusive a hora de fim e a retirada à mão do aviso do owner da organização) e o gesto e o visual da faixa. O dono disse que "ainda vamos definir" (`D-213`) | `D-213`, `D-212`, `D-174` | Dono, com o PO e o arquiteto de soluções | 05/11/2026 |
| `P-047` | 🕓 Pendência | **Para o arquiteto de soluções:** a viabilidade e o desenho da exportação da conversa em PDF ou HTML na `MF-107` da v2.0 (`D-250`): o que o arquivo leva (as respostas, os gráficos e as tabelas, as fontes), se reaproveita o desenho único dos gráficos e a geração de PDF do board, o registro da exportação no rastro da Auditoria (`D-252`) e o que isso pede do resto da v2.0. O código da v1.xx só baixa o CSV e a imagem de um bloco; o PDF só existe no board | `D-250`, `D-249` | Arquiteto de soluções | 06/11/2026 |
| `P-048` | 🕓 Pendência | **Para o arquiteto de soluções:** o fluxo do dono (`D-258`): como o SaaS e o middleware sobem em infraestruturas separadas e como isso convive com o chart único e a `ARQ-060`; o formato, a rotação e a revogação do certificado, a chave de instalação, o handshake e a troca dos arquivos assinados; o endereço da organização com token (o que ele carrega e como não vaza em registro e histórico) e o que vai na sessão (só o necessário para encaminhar, sem endereço nem porta da infraestrutura); quem emite a sessão; o que a pessoa vê e o que o Horus faz com o middleware fora do ar, já que o login da organização cai junto; a atualização do middleware; a criação automática de um middleware para cada organização nova (`D-259`); o que o SaaS guarda de cada pessoa (`D-261`), se ele só repassa o e-mail do convite sem guardá-lo (`D-262`) e como mostra o nome dela sem guardá-lo (a Home da organização, o rastro da Auditoria, a medida de autonomia); a revisão da `ARQ-097`, cuja dimensão de pessoas do banco de log não pode guardar o nome (`D-274`); onde roda a pergunta do administrador sobre a história da instância (`D-276`), que lê o banco de log e não passa por middleware; e o que muda na `P-040` e na `P-042` | `D-258`, `P-040`, `P-042`, `ARQ-060` | Arquiteto de soluções | 07/11/2026 |

### Fechados

| Nº | O que era | Como fechou | Em |
| --- | --- | --- | --- |
| `I-093` | O painel de uso e custo da instância mostra o consumo de IA das chaves que a Maind dá, por organização (e só dessas)? | O dono escolheu, com a opção recomendada, que **sim**, só das chaves que a Maind dá (`D-279`) | 07/11/2026 |
| `I-092` | Excluir uma organização apaga também o middleware dela e tudo o que há nele (pessoas e configuração), além do uso (`D-149`)? | O dono escolheu, com a opção recomendada, que **sim**: apaga tudo o que há dela no middleware (`D-278`) | 07/11/2026 |
| `I-091` | A organização só passa a ativa depois de o middleware estar ligado (handshake confirmado) e os bancos e a IA configurados, ou a Maind a marca como ativa quando quiser (`D-148`)? | O dono escolheu a opção B, contra a recomendação do PO (a A): **só depois de o middleware estar ligado e de os bancos e a IA estarem configurados** (`D-277`) | 07/11/2026 |
| `I-090` | O administrador da instância ainda pergunta ao próprio Horus sobre a história da instância (`D-158`), já que não há mais conexão de IA da instância (`D-266`)? | O dono escolheu a opção B, contra a recomendação do PO (a A): **sim, com uma chave de IA que a Maind cadastra só para isso** (`D-276`) | 07/11/2026 |
| `I-089` | O painel da instância mostra o estado do middleware de cada organização (no ar ou fora, versão)? | O dono escolheu, com a opção recomendada, que **sim**: o painel mostra o estado e a versão (`D-275`) | 07/11/2026 |
| `I-088` | A Maind continua vendo, no relatório da organização, o nome de quem ocupa cada assento (`D-157`), agora que as pessoas ficam no middleware, fora do SaaS (`D-261`)? | O dono escolheu, com a opção recomendada, que **não**: a Maind vê só a história dos assentos em números, sem o nome (`D-274`) | 07/11/2026 |
| `I-095` | Na hospedagem da Maind, quem configura os bancos e a IA de cada organização: o owner da organização, com o usuário que a Maind cria, ou o time da Maind, por ele, como suporte? | O dono escolheu, com a opção recomendada, que **é o owner da organização**, em qualquer hospedagem; o time da Maind só dá suporte (`D-273`) | 07/11/2026 |
| `I-094` | O middleware passa a ser multi-organização em qualquer hospedagem (o da Maind atende as organizações do SaaS, e o do cliente, as organizações dele), o que substitui a `D-259` (um middleware por organização)? | O dono escolheu, com a opção recomendada, que **sim: o middleware é multi-organização em qualquer hospedagem** (`D-272`); a `D-259` sai | 07/11/2026 |
| `I-087` | Na hospedagem da Maind, quem do time da Maind configura os bancos e a IA de cada organização no front do middleware: o administrador da instância ou um papel de suporte à parte? | O dono respondeu fora das opções: **o middleware é o mesmo em qualquer hospedagem, a diferença é só o local físico, e o owner da organização acessa o front do middleware também na Maind, com um usuário que a Maind cria** (`D-271`). Abriu o `I-094` e o `I-095` | 07/11/2026 |
| `I-080` | O owner adicional ligado ao login da empresa (no máximo mais dois, no fluxo do dono) ocupa um assento de owner pago, ou é à parte? | O dono escolheu, com a opção recomendada, que **cada owner adicional ocupa um assento de owner contratado**; só o primeiro é grátis (`D-269`) | 07/11/2026 |
| `I-086` | Quem é avisado quando a IA de uma organização para (chave recusada, falta de crédito), agora que não há conexão da instância e o time da Maind configura na hospedagem dela? | O dono escolheu, com a opção recomendada, que **o owner da organização é sempre avisado e, se a chave é da Maind, o time da Maind também** (`D-268`) | 07/11/2026 |
| `I-084` | Uma chave de provedor de IA que a Maind dá à organização, em qualquer hospedagem: quem paga e quem vê o consumo? | O dono escolheu a opção B, contra a recomendação do PO (a A): **a Maind paga, e o owner da organização também vê o consumo e o custo** (`D-267`) | 07/11/2026 |
| `I-085` | A conexão da instância (a IA que a Maind cadastra no nível da instância e disponibiliza às organizações) deixa de existir, já que a IA é configurada por organização, no front do middleware? | O dono escolheu, com a opção recomendada, que **deixa de existir**: a IA é sempre da organização, configurada no middleware (`D-266`). Abriu o `I-086` | 07/11/2026 |
| `I-083` | Com o middleware hospedado pela Maind, a IA segue como na `D-216` (a Maind cadastra a conexão da instância e a disponibiliza à organização), ou a organização configura a dela também nesse caso? | O dono respondeu fora das opções: **em qualquer hospedagem, os bancos e a IA são configurados no front do middleware; quem configura é a organização, ou o time da Maind, em suporte técnico, na hospedagem da Maind** (`D-265`). Abriu o `I-085` | 07/11/2026 |
| `I-078` | A organização que usa o middleware pode usar a conexão de IA da instância (a Maind paga), ou usa só a própria? | O dono respondeu fora das opções: **com o middleware fora da Maind, a organização configura a IA dela, e a Maind pode lhe dar uma chave de provedor** (`D-264`). Abriu o `I-083` e o `I-084` | 07/11/2026 |
| `I-081` | A segurança dos dados por pessoa (`MF-106`, v2.1) continua na v2.1, agora que o middleware está em toda organização na v2.0 e a `MF-121` sobe para a v2.0? | O dono escolheu, com a opção recomendada, que **continua na v2.1**; a `MF-121` deixa de depender da `MF-106`, e a `MF-106` passa a depender da `MF-121` (`D-263`) | 07/11/2026 |
| `I-082` | O gestor também usa o front do middleware (para criar convites e pedir a troca do tipo de assento), ou só o owner o usa e o gestor pede pelo Horus? | O dono escolheu a opção B, contra a recomendação do PO (a A): **só o owner usa o front do middleware; o gestor cria o convite e pede a troca pelo Horus** (`D-262`) | 07/11/2026 |
| `I-076` | Das funções de pessoas da `MF-102` (convite, aprovação, gestor, quarentena, grupos, planilha, troca do tipo de assento), quais passam a viver no setup do middleware e quais ficam no Horus? | O dono respondeu fora das opções, na linha da B: **o owner da organização usa o front do middleware para gerir as pessoas, que ficam isoladas fora do SaaS**, por separação de responsabilidade e segurança (`D-261`). Abriu o `I-082` | 07/11/2026 |
| `I-079` | Com o middleware em toda organização (`D-258`), a v2.0 ganha uma mf nova (`MF-124`) e a `MF-121` fica só com a hospedagem na casa do cliente, na v2.1, ou a `MF-121` sobe inteira para a v2.0? | O dono escolheu a opção B, contra a recomendação do PO (a A): **a `MF-121` sobe inteira para a v2.0**, sem mf nova (`D-260`). Abriu o `I-081` | 07/11/2026 |
| `I-077` | Na hospedagem da Maind, o middleware é um só para todas as organizações do SaaS ou um por organização? | O dono escolheu a opção B, contra a recomendação do PO (a A): **um middleware para cada organização**, também na hospedagem da Maind (`D-259`) | 07/11/2026 |
| `I-075` | O desenho da infraestrutura separada que o dono rascunhou (o middleware, a base de configuração e o aplicativo de setup) vale para toda organização desde a v2.0, ou é o interior da `MF-121` (v2.1, onda 2)? | O dono escolheu a opção B, contra a recomendação do PO (a A): **toda organização, desde a v2.0** (`D-258`). Abriu o `I-076` a `I-080` e a `P-048` | 07/11/2026 |
| `I-074` | O que o Horus faz com uma fonte cuja tecnologia não aceita a identidade da pessoa, com o login da empresa ligado? (segunda parte do `A-25` do documento 14) | O dono escolheu, com a opção recomendada, que **a fonte fica só com a regra do Horus, e o owner é avisado** (`D-257`); o `A-25` está fechado | 06/11/2026 |
| `I-073` | O que a pessoa lê quando a resposta sai limitada e a regra que limitou é a da empresa, que o banco não explica? (primeira parte do `A-25` do documento 14) | O dono escolheu, com a opção recomendada, que **o aviso diz qual regra do Horus limitou e que as regras da empresa também valem** (`D-256`) | 06/11/2026 |
| `I-072` | Quem sai da empresa continua entrando no Horus até a sessão de 30 dias acabar? (item 3 do `A-20` do documento 14) | O dono escolheu, com a opção recomendada, que **a sessão nascida pelo login da empresa se confirma com ele a cada 8 horas** (`D-255`); o `A-20` está fechado | 06/11/2026 |
| `I-071` | Quando a role do cadastro do Horus e a do login da empresa discordam, qual vale? (item 2 do `A-20` do documento 14) | O dono escolheu, com a opção recomendada, que **vale a do login da empresa**, e quem chega sem valor mapeado cai na role padrão (`D-254`) | 06/11/2026 |
| `I-070` | Quem chega pelo login da empresa sem convite entra no Horus? (item 1 do `A-20` do documento 14) | O dono escolheu, com a opção recomendada, que **não entra: o login só autentica, e só entra quem foi convidado** (`D-253`) | 06/11/2026 |
| `I-069` | A exportação da conversa fica registrada no rastro da Auditoria (`MF-116`)? | O dono escolheu, contra a recomendação do PO, que **só a exportação da conversa fica no rastro**; os downloads de CSV, imagem e PDF continuam fora (`D-252`) | 06/11/2026 |
| `I-068` | A exportação da conversa é um dos botões das roles (a `D-110` lista nove), ou quem pode exportá-la? | O dono escolheu, com a opção recomendada, que **a exportação fica no botão "Baixar" que já existe**, sem botão novo (`D-251`) | 06/11/2026 |
| `I-067` | Em que mf e em que versão entra a exportação da conversa em PDF ou HTML, já que o dono a chamou de recurso nativo da conversa (`MF-107`, v2.0) | O dono escolheu, contra a recomendação do PO (a `MF-119`, v2.1), a **`MF-107`, na v2.0** (`D-250`) | 06/11/2026 |
| `I-066` | Como uma pessoa mostra uma investigação guiada a outras pessoas, se a `D-179` diz que ela "compartilha a conversa" e o dono decidiu em 14/10/2026 (v1.xx) que a conversa nunca é compartilhada | O dono respondeu fora das opções: **exportar a conversa em PDF ou HTML**, recurso nativo dela, "em um primeiro momento talvez"; a conversa continua sem compartilhamento (`D-249`). Onde e quando a exportação entra ficou no `I-067` | 06/11/2026 |
| `P-045` | O jurídico da Maind confirmar que o owner ler as conversas de todos, sem aviso especial à pessoa (`D-223`), é aceitável diante da proteção de dados pessoais, e se o aviso de privacidade da instância precisa dizer isso | O dono manteve a regra e pediu que a documentação e o setup indiquem ao cliente consultar o jurídico dele (`D-247`); o aviso de privacidade da instância segue com a `A-16` do documento 14 | 06/11/2026 |
| `I-065` | Onde ficam os boards de exemplo das bases de demonstração | O dono escolheu, com a opção recomendada, que ficam no espaço da organização, publicados (`D-245`) | 05/11/2026 |
| `I-064` | O que a pessoa vê enquanto o agendamento ou o agente espera o sim do owner | O dono escolheu, com a opção recomendada, que o item aparece marcado "aguardando aprovação do owner" e depois "ativo" ou "recusado" (`D-244`) | 05/11/2026 |
| `I-063` | O que a tela mostra quando a pesquisa na web não traz fato nenhum | O dono escolheu, com a opção recomendada, que a resposta sai com os dados da empresa e um aviso curto (`D-243`) | 05/11/2026 |
| `I-062` | O cartão do board que usa um fato da web: guarda os fatos ou pesquisa de novo a cada atualização? | O dono escolheu, com a opção recomendada, que o cartão guarda os fatos da resposta, com a data à vista, e não pesquisa de novo (`D-242`) | 05/11/2026 |
| `I-061` | O que o owner da organização vê do consumo de IA: da conexão própria e da conexão da instância | O dono escolheu, com a opção recomendada, que o owner vê consumo e custo só da conexão que a organização paga (`D-241`) | 05/11/2026 |
| `I-057` | Quem fica sabendo quando um serviço da organização, que não é a IA, para (`A-22` do documento 14) | O dono escolheu, com a opção recomendada, que é avisado o dono do serviço, como na IA (`D-240`) | 05/11/2026 |
| `I-060` | A Home da organização mostra a divisão das perguntas respondidas por canal (a conversa de análise, a Pergunta rápida e o WhatsApp)? | O dono escolheu, com a opção recomendada, que a Home mostra a divisão por canal (`D-239`) | 05/11/2026 |
| `I-047` | Quem mais vê a medida de autonomia (o gestor da própria equipe, o comprador) e se a Home mostra a divisão por canal (conversa, Pergunta rápida, WhatsApp) | Primeira parte respondida pelo dono, com a opção recomendada: o gestor vê a medida da própria equipe (`D-238`). A divisão por canal virou o `I-060` | 05/11/2026 |
| `I-046` | O tema dos gráficos por organização fica na v2.0, já que o tema do contratante está sem versão? | O dono escolheu, com a opção recomendada, que o tema dos gráficos por organização fica como na v1.xx (`D-237`) | 05/11/2026 |
| `I-059` | A planilha de convites em lote: quem a usa, se cada linha traz o tipo de assento e o gestor, e se o lote passa pela aprovação e pela reserva do assento | O dono escolheu, com a opção recomendada, que a planilha é só do owner, cada linha traz o tipo de assento e o gestor, o lote reserva os assentos e a linha sem vaga fica de fora (`D-236`) | 05/11/2026 |
| `I-045` | Os grupos dinâmicos aceitam o tipo de assento como regra; e a planilha de convites em lote: quem a usa e se cada linha traz o tipo de assento e o gestor | Primeira metade respondida pelo dono, com a opção recomendada: o tipo de assento vira regra de grupo dinâmico (`D-235`). A planilha de convites virou o `I-059` | 05/11/2026 |
| `I-044` | Um teto automático de custo, por agente ou por organização, entra na v2.0 (`D-216`)? | O dono escolheu, com a opção recomendada, que não entra: ficam os tetos técnicos por execução e o aviso de custo (`D-234`) | 05/11/2026 |
| `I-058` | A DRE de usina segue na vitrine da v2.0, sendo que só duas organizações de exemplo chegam à v2.0? | O dono escolheu, com a opção recomendada, que a DRE de usina sai e ficam a rede de lojas e a frota (`D-233`) | 05/11/2026 |
| `I-043` | Os cenários e os boards de exemplo das bases de demonstração, e se a DRE de usina segue na vitrine da v2.0 (`A-14` do documento 14) | Primeira parte respondida pelo dono, com a opção recomendada: um cenário para cada prova de valor da v2.0 (`D-232`). A DRE de usina virou o `I-058` | 05/11/2026 |
| `I-042` | O aviso de abertura do rastro da Auditoria: onde fica o documento, se há texto padrão, se o primeiro acesso pede ciência (`A-30` do documento 14) | O dono escolheu, com a opção recomendada, o texto padrão do Horus, que o owner pode trocar, sem pedir ciência no primeiro acesso (`D-231`) | 05/11/2026 |
| `I-056` | Como o autor aprova o cartão que descreve em texto (`A-23`, item 2, do documento 14) | O dono escolheu, com a opção recomendada, que o autor vê o resultado antes de salvar e salvar é a aprovação, sem estado à parte (`D-230`) | 05/11/2026 |
| `I-041` | O board maior que a folha vira PDF reduzido ou em várias folhas, e como o autor aprova o cartão que descreve em texto (`A-23` do documento 14) | Primeira metade respondida pelo dono, com uma sugestão dele: o PDF tem uma página só, do tamanho do board (`D-229`). A segunda metade virou o `I-056` | 05/11/2026 |
| `I-039` | O padrão de nascimento da organização: os interruptores de aprovação (conectores, publicação do gestor) e a role padrão com o botão do WhatsApp nascem ligados? | O dono escolheu, com a opção recomendada, que todos nascem liberados e o owner restringe (`D-228`) | 05/11/2026 |
| `I-055` | O artefato que não cabe no canal (um PDF maior que o anexo do e-mail, um alerta maior que a mensagem do WhatsApp) | O dono escolheu, com a opção recomendada, não entregar naquele canal e avisar o autor, sem cortar nem alterar o artefato (`D-227`) | 05/11/2026 |
| `I-038` | Quando uma execução de agente ou de agendamento falha ou passa do teto, e quando o artefato não cabe no canal: o que recebem o autor e os destinatários (`A-10` e `A-19` do documento 14) | Primeira metade respondida pelo dono, com a opção recomendada: só o autor recebe o aviso de falha, e os destinatários não recebem nada (`D-226`). A segunda metade virou o `I-055` | 05/11/2026 |
| `I-037` | O que recebe quem escreve no WhatsApp sem número ligado, sem o botão da role ou como membro bronze (`A-18` do documento 14) | O dono escolheu, com a opção recomendada, uma resposta fixa, sem dado, que aponta para o app (`D-225`) | 05/11/2026 |
| `I-036` | O número de WhatsApp: um só por pessoa em cada organização, para a conversa e para os avisos, e como fica quem está em duas organizações no número da Maind (`A-17` do documento 14) | O dono escolheu, com a opção recomendada, que o telefone fica ligado a uma organização por vez, com aviso à pessoa; o número é um só para a conversa e os avisos (`D-224`) | 05/11/2026 |
| `I-035` | O owner da organização continua lendo as conversas de todos, e a pessoa é avisada? (`A-16`, item 2, do documento 14) | O dono escolheu que o owner continua lendo, sem aviso especial à pessoa, contra a recomendação do PO (`D-223`). Abriu a `P-045` | 05/11/2026 |
| `I-034` | O que conta como pergunta de análise respondida na medida de autonomia (`A-08` do documento 14) | O dono escolheu, com a opção recomendada, contar só a resposta que trouxe dado ou web, e não a consulta vazia, a falha nem a conversa sem fonte (`D-222`) | 05/11/2026 |
| `I-033` | Fixar uma resposta num board: é um botão da role ou segue o tipo de assento (`A-24` do documento 14) | O dono respondeu fora das opções: só o dono do board fixa uma resposta nele, e não é um botão das roles (`D-221`) | 05/11/2026 |
| `I-032` | O teto de inferência: o "teto da organização" de que as roles falam, ou o teto de cada fonte de dados, como hoje (`A-13` do documento 14) | O dono escolheu, com a opção recomendada, o teto de cada fonte, e a role só pode baixá-lo (`D-220`) | 05/11/2026 |
| `I-031` | Quem escreve o modelo semântico de uma organização (o "time de dados") e com qual assento | O dono escolheu, com a opção recomendada, que o modelo é escrito fora do Horus e o owner da organização o carrega (`D-219`) | 05/11/2026 |
| `I-030` | Quem é avisado quando a IA da organização para (chave recusada ou falta de crédito) | O dono escolheu, com a opção recomendada, que é avisado o dono da conexão: o owner da organização, se a conexão é dela, ou o administrador da instância, se é da instância (`D-218`) | 05/11/2026 |
| `I-054` | Quando uma organização é criada, ela já nasce com a conexão de IA da instância disponível, ou fica sem IA até o administrador disponibilizar uma? | O dono escolheu, com a opção recomendada, que a organização nasce sem IA e o administrador da instância disponibiliza uma conexão ao criá-la (`D-217`) | 05/11/2026 |
| `I-029` | A Maind limita os modelos de IA que cada organização pode aceitar, agora que a Maind paga a IA? | O dono corrigiu a premissa: há conexão da organização (ela paga) e conexão da instância (a Maind paga), disponibilizada a uma ou mais organizações e sem edição no nível da organização (`D-216`) | 05/11/2026 |
| `I-028` | O modo web depois de a web virar pesquisa do modelo (`D-162`): o botão da role passa a ser "pesquisar na web", valendo nos outros modos? | O dono escolheu, com a opção recomendada, que a web vira um interruptor ao lado dos dados e que os modos passam a ser dois: dados e conversa (`D-215`) | 05/11/2026 |
| `I-027` | O que a visão de cobrança do owner da organização mostra na v2.0 | O dono escolheu, com a opção recomendada, só a contagem de assentos por tipo: tem, usa e livres (`D-214`) | 05/11/2026 |
| `I-026` | O aviso do owner da organização na faixa: texto livre, com hora de fim opcional e retirada à mão, como o da instância? | O dono respondeu fora das opções: a faixa é um contêiner de componentes, o aviso é o componente de texto livre, e os outros (KPIs, ícones) serão definidos depois (`D-213`) | 05/11/2026 |
| `I-025` | Os "números do negócio" da faixa: o owner escolhe a métrica e o período do modelo semântico, ou os cards são fixos do produto? | O dono escolheu, com a opção recomendada, que o owner aponta o card para uma métrica do modelo semântico e escolhe o período (`D-212`) | 05/11/2026 |
| `I-053` | O total de perguntas respondidas da organização, quando uma pessoa é excluída: a parte dela some ou o total segue como número sem dono? | O dono escolheu, com a opção recomendada, que o total e a série mensal seguem como número sem dono (`D-211`) | 05/11/2026 |
| `I-052` | O que a organização guarda de quem sai (o rastro da Auditoria, os reportes pendentes e a contagem da medida de autonomia) | O dono escolheu apagar tudo junto com a pessoa, contra a recomendação do PO (`D-210`). Abriu o `I-053` e a `P-044` | 05/11/2026 |
| `I-050` | A transferência do que a pessoa criou, que saiu da v2.0: ela volta na v2.1 como mf própria ou fica sem versão? | O dono respondeu fora das opções: não há transferência, nem na v2.1; quem é excluído perde em definitivo e quem é rebaixado só desabilita (`D-209`) | 05/11/2026 |
| `I-040` | O board público quando o owner da organização que o publicou sai da organização | Sem objeto: o que a pessoa criou se perde na saída, e o board público some com o owner que o publicou (`D-206`, `D-209`) | 05/11/2026 |
| `I-049` | Quem volta a ser ouro depois de ter passado a prata ou a bronze: o que ficou desabilitado volta a funcionar? | O dono escolheu, com a opção recomendada, que ela reativa um a um e nada volta sozinho (`D-208`) | 05/11/2026 |
| `I-051` | Quem passa de ouro a prata ou a bronze e continua na organização: perde o que criou ou o que criou fica guardado? | O dono respondeu fora das opções: o que criou fica vinculado a ela, desabilitado, sem uso, e só pode ser excluído (`D-207`) | 05/11/2026 |
| `I-048` | Quando o novo dono de um agendamento é um gestor, o que acontece com os destinatários fora da carteira dele | O dono respondeu que, na v2.0, quem sai da organização perde o que criou e não há transferência (`D-206`): sem objeto | 05/11/2026 |
| `I-024` | Para quem o owner da organização pode transferir o que ficou na área da organização, já que a prata e o bronze não criam (`D-203`) e só o gestor e o owner entregam a outras pessoas (`D-059`) | O dono escolheu que só se transfere a outro owner ou a um gestor, contra a recomendação do PO (`D-205`). Abriu o `I-048` e o `I-049` | 05/11/2026 |
| `I-023` | A `MF-120:Faixa de avisos e números` era dada como a mais fácil de cortar, mas o aviso da instância vai só pela faixa e a `MF-101` depende dela | O dono escolheu que a `MF-120` sai da lista de cortes e fica na v2.0 como parte indispensável (`D-204`) | 05/11/2026 |
| `P-043` | Completar a definição macro da `MF-122:Conectores de chat corporativo` e da `MF-123:Fonte AWS Athena` | O dono confirmou a definição proposta pelo PO (`D-201`) | 05/11/2026 |
| `I-022` | O que o membro prata pode fazer além de perguntar e o que acontece com o que o ouro criou ao mudar de faixa | O dono escolheu que a prata pergunta (app, Pergunta rápida e WhatsApp), investiga e recebe alertas e PDFs, e não cria nada: criar é do ouro; e que quem passa de ouro a prata ou a bronze deixa o que criou na área da organização (`D-203`) | 05/11/2026 |
| `I-021` | Aplicar a regra "uma mf não se divide em duas versões" (`D-197`) às partes que ainda estavam na v2.1 | O dono escolheu que o Teams e o Google Chat viram a `MF-122` e o Athena a `MF-123` (`D-198`), e que o interruptor geral e as demais peças da segurança por pessoa passam à `MF-106` (`D-199`). As partes da casa do contratante seguem sem versão (`D-188`) | 05/11/2026 |
| `P-018` | Definição macro da `MF-119:Investigação guiada` | O dono respondeu as três dúvidas de desenho (`D-177` a `D-179`) e confirmou a definição completa (`D-180`) | 05/11/2026 |
| `P-016` | Como ativar os assentos numa instalação on-premises | O dono escolheu um arquivo de licença com chave, sem internet (`D-175`), com um teto por tipo de assento para a instância inteira, que o administrador do cliente reparte entre as organizações (`D-176`) | 05/11/2026 |
| `P-027` | Definição macro da `MF-120:Faixa de avisos e números` (nova, nome provisório) | O dono respondeu as sete dúvidas de desenho (`D-167` a `D-173`) e confirmou a definição completa (`D-174`) | 05/11/2026 |
| `P-031` | Em que formato o administrador baixa o relatório da organização | O dono escolheu a planilha e o PDF (`D-166`) | 05/11/2026 |
| `P-030` | Quando o aviso da instância sai da faixa | O dono escolheu os dois: hora de fim opcional e retirar à mão a qualquer momento (`D-165`) | 05/11/2026 |
| `P-041` | O "controle de criação de instâncias mais eficiente" (`D-192`) | O dono respondeu que era uma confusão dele: a configuração fica na organização (`D-193`, `D-195`), e o SaaS é uma instância só. Sem objeto | 05/11/2026 |
| `I-020` | Como o Horus chega à infraestrutura do contratante | O dono propôs, e o impasse se fechou com: o Horus fica sempre no SaaS da Maind, e a casa do contratante é atendida por um **middleware** (`D-188`), um servidor MCP em imagem de container da Maind (`D-190`, `D-195`); só a pergunta e a resposta pronta saem, e o owner da organização pode permitir mais (`D-189`, `D-193`); as permissões e a conexão são da organização (`D-195`); a instalação completa só volta se um cliente exigir | 05/11/2026 |
| `I-019` | O que os boards públicos mostram à quarentena | O dono escolheu que o board público calcula os dados com o acesso do owner que o tornou público, e que o owner responde pelo que publica (`D-164`) | 05/11/2026 |
| `I-018` | Com que alcance de dados roda o espaço da organização (`A-11` do documento 14) | O dono escolheu que os boards do espaço da organização usam o acesso de quem os abre (`D-163`). A leitura do PO sobre os agendamentos e os agentes foi confirmada pelo dono em 05/11/2026 (`D-163.1`); o efeito sobre os boards públicos da quarentena virou o `I-019` | 05/11/2026 |
| `I-017` | As duas fontes que o MVP tira da tela (`A-04` do documento 14): a fonte de páginas web e o AWS Athena | O dono decidiu que o Athena entra, terminado, na v2.1 (`D-161`) e que a web como fonte entra na v2.0, como o modelo poder sair à web quando autorizado (`D-162`) | 05/11/2026 |
| `I-016` | De quem é cada custo no SaaS (`A-03` do documento 14): a IA e o WhatsApp | O dono escolheu que a Maind paga a IA de todas as organizações e a embute no preço do assento (`D-159`), e que a organização que usa o número da Maind no WhatsApp paga as mensagens que gerar (`D-160`) | 05/11/2026 |
| `P-026` | O painel de controle do owner da instância, com o uso (`A-29`): o que mostra, o aviso de custo e se é mf nova | O dono respondeu com a ideia dos cards configuráveis em duas categorias (`D-152`). Os números e o aviso de custo ficam na MF-101 como Instance Cards prontos, por leitura do PO (`D-153`, proposta); o que falta (quais números o owner pode mostrar e onde) passou para a `P-027` | 05/11/2026 |
| `P-025` | Como a instância fala com todas as pessoas quando ela para (`A-21`) | O dono decidiu o aviso da instância na v2.0, em faixa contínua e só pela faixa (`D-151`), e ampliou a faixa na `MF-120` (`D-152`); a página de manutenção e o corte da página de estado seguem como proposta (`D-154`) | 05/11/2026 |
| `I-015` | Quem cria organizações no SaaS (`A-02`) | O dono escolheu a opção A: só o administrador da instância (`D-146`) | 05/11/2026 |
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

### D-280 · Definição macro revisada da MF-101:Administração da instância, com o middleware
Situação: 🟢 decidida (proposta do PO, confirmada pelo dono em 07/11/2026) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** a `MF-101:Administração da instância` fica redefinida assim, reunindo o que o dono decidiu em 07/11/2026 (`D-258` a `D-279`). Esta entrada **substitui a `D-202`**.
- **O que é:** o painel de quem opera o SaaS, um **funcionário da Maind** (o administrador da instância, `D-147`), que **entra por usuário e senha** (`D-258`). Nele, a Maind:
  - **cria as organizações** (`D-146`): a criação **liga a organização ao middleware** (o certificado e a chave de instalação, `D-258`) e **cria o usuário do owner** no front do middleware (`D-271`); a organização nasce em configuração e **só passa a ativa** com o middleware ligado e os bancos e a IA configurados pelo owner (`D-277`, `D-273`);
  - **libera, reduz e corta os assentos** (`D-080`), que vão ao middleware (`D-258`); **corta** a organização inteira ao inativá-la (`D-148`);
  - **vê o estado e a versão do middleware** de cada organização (`D-275`);
  - **vê o uso e o custo**, inclusive o consumo de IA **das chaves que a Maind dá**, e **baixa o relatório** em planilha e PDF, com a história dos assentos **em números, sem o nome de quem os ocupou** (`D-149`, `D-153`, `D-274`, `D-279`);
  - **publica o aviso da instância** (`D-151`), cuida do **e-mail do produto** (`D-155`) e da **marca da Maind** (`D-200`);
  - **pergunta ao próprio Horus** sobre a história da instância, com uma chave de IA da instância usada só para isso (`D-158`, `D-276`);
  - **exclui a organização**, o que apaga também tudo o que há dela no middleware (`D-278`).
- **Quem ganha:** o **administrador da instância** (a Maind), que opera o SaaS sem planilha nem chamado; de forma indireta, o **owner da organização**, que recebe o middleware, os assentos e os avisos.
- **Decisão que passa a ser possível:** abrir uma organização nova e ligá-la ao seu middleware, saber se ele está no ar, liberar ou cortar assentos, ver quanto cada organização usa e custa, e avisar todo mundo de uma manutenção, tudo num lugar só.
- **Prova de valor:** a Maind cria uma organização, vê o middleware ligado, o owner configura o banco e a IA e a organização vira ativa; a Maind libera os assentos, acompanha o uso e o custo, baixa o relatório e publica um aviso que aparece na faixa de todas as pessoas.
- **Retorno para o negócio:** controle da receita e do custo por organização e menos suporte para operar o SaaS, com um middleware só para as organizações do SaaS (`D-272`).
- **O que não inclui:** o nome de quem ocupa o assento (`D-274`); ver as conexões e as credenciais das organizações, que o owner configura (`D-273`); a conexão de IA para as organizações, que não existe mais (`D-266`); a marca completa do contratante, sem versão (`D-200`); o interruptor geral da segurança, que é da `MF-106` (`D-199`); a página pública do estado da instância (`D-154`); o preço (`P-022`).
- **Depende de:** `MF-102:Organizações, pessoas e papéis`; `MF-103:Licenças e planos`; `MF-120:Faixa de avisos e números` (onde o aviso aparece); `MF-121:Middleware da organização` (a criação liga a organização a ele).
- **Valor:** **essencial** para operar o SaaS: sem ela a Maind não cria organizações, não as liga ao middleware nem libera assentos.
**Contexto:** o dono pediu, em 07/11/2026, que a `MF-101` fosse reescrita considerando a estrutura nova. A `D-202`, de 05/11/2026, excluía o middleware e supunha que o administrador não precisa ver as conexões das organizações.
**Opções avaliadas:** definição direta, sem pontuação: reúne decisões já tomadas.
**Por que esta:** põe num lugar só o que a `MF-101` é depois do middleware. Não decide nada novo de valor.
**Hipóteses a validar:** 🔎 que o isolamento por certificado baste entre as organizações do SaaS (`D-272`); 🔎 que o owner consiga configurar sozinho o banco e a IA (`D-273`); 🔎 que a cobrança se confira só com contagens, sem nome (`D-274`).
**Reabrir quando:** o suporte da Maind pedir ver mais, ou o dono quiser mudar o que a mf inclui.

### D-279 · O painel de uso e custo da instância mostra o consumo de IA só das chaves que a Maind dá
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-093`. O painel de uso e custo da instância (`MF-101`) mostra, por organização, o **consumo e o custo de IA das chaves que a Maind dá** (`D-264`, `D-267`), e o **aviso de custo** (`D-153`) alcança só isso. O consumo da chave que a própria organização paga **não aparece no painel da Maind**: é da organização (`D-267`).
**Contexto:** sem a conexão da instância (`D-266`), o que sobrou de custo de IA para a Maind são as chaves que ela dá, e as páginas da `MF-101` e da `MF-105` deixavam em aberto o que o aviso de custo ainda alcança.
**Opções avaliadas** (sem pontuação): **A. só das chaves que a Maind dá (recomendação do PO, escolhida pelo dono)** · B. o painel não traz custo de IA.
**Por que esta:** a Maind paga essas chaves e precisa ver quanto cada organização consome. Abre-se mão de: ⚠️ a Maind não vê o consumo de IA das organizações que trazem a própria chave.
**Afeta:** `D-153` (o aviso de custo e os Instance Cards), `D-267`, `MF-101`, `MF-105`.
**Reabrir quando:** a Maind precisar ver todo o consumo de IA, inclusive o das chaves das organizações.

### D-278 · Excluir uma organização apaga também tudo o que há dela no middleware
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-092`. Excluir uma organização apaga, além do uso no SaaS (`D-149`), **tudo o que há dela no middleware**: as pessoas, os bancos e a IA configurados e a configuração. Como o middleware é compartilhado (`D-272`), a exclusão apaga **só o que é daquela organização**. **Completa a `D-149`.**
**Contexto:** com as pessoas, os bancos e a IA no middleware (`D-258`, `D-261`, `D-265`), excluir só o uso deixaria dado pessoal e credenciais de uma organização que não existe mais.
**Opções avaliadas** (sem pontuação): **A. apaga tudo, também no middleware (recomendação do PO, escolhida pelo dono)** · B. o que está no middleware fica.
**Por que esta:** é coerente com "quem é excluído perde tudo" (`D-209`, `D-210`) e não deixa dado pessoal para trás. Abre-se mão de: ⚠️ uma exclusão por engano leva também a configuração, sem volta; ⚠️ a guarda técnica do registro de acesso e as cópias de segurança (`P-044`) passam a valer também para o middleware.
**Afeta:** `D-149`, `D-209`, `D-210`, `P-044`, `MF-101`, `MF-102`.
**Reabrir quando:** uma exclusão por engano custar um cliente.

### D-277 · A organização só passa a ativa depois de o middleware ligado e dos bancos e da IA configurados
Situação: 🟢 decidida (resposta do dono em 07/11/2026, contra a recomendação do PO, que era a opção A) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-091`. Uma organização **nasce em configuração e só passa a ativa depois de três condições**: o **middleware ligado** (o handshake com o SaaS confirmado, `D-258`), ao menos **um banco configurado** e a **IA configurada**, pelo owner (`D-273`). **Altera em parte a `D-148`**, em que a Maind a marcava como ativa quando a dava por pronta. 🔎 Leitura do PO, a confirmar com o dono: cumpridas as condições, a Maind a marca como ativa (a trava é automática; o ato segue sendo dela).
**Contexto:** com o middleware em toda organização, uma organização pode nascer sem conseguir responder. O PO recomendava manter a ativação como a `D-148`, com o estado do middleware à vista (`D-275`).
**Opções avaliadas** (sem pontuação): A. a Maind a marca como ativa quando quiser (`D-148`; recomendação do PO) · **B. só depois das condições (escolhida pelo dono)**.
**Por que esta:** não se ativa uma organização que não consegue responder. Abre-se mão de: ⚠️ a ativação depende de o owner configurar o banco e a IA; ⚠️ a Maind não ativa por conta própria uma organização incompleta, e as organizações de exemplo também precisam cumprir as condições.
**Afeta:** `D-148`, `MF-101`, `MF-118`, `MF-121`.
**Reabrir quando:** a trava atrapalhar a entrada de um cliente.

### D-276 · A pergunta do administrador sobre a história da instância continua, com uma chave de IA que a Maind cadastra só para isso
Situação: 🟢 decidida (resposta do dono em 07/11/2026, contra a recomendação do PO, que era a opção A) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-090`. O administrador da instância **continua perguntando ao próprio Horus sobre a história da instância** (`D-158`). Para isso, a Maind **cadastra uma chave de IA no nível da instância, usada só para essa pergunta**, e paga por ela. A decisão **não traz de volta a conexão da instância para as organizações** (`D-266`): nenhuma organização usa essa chave.
**Contexto:** a `D-158` supunha a IA da instância, que a `D-266` extinguiu. O PO recomendava tirar a pergunta da v2.0; o dono preferiu mantê-la.
**Opções avaliadas** (sem pontuação): A. a pergunta sai da v2.0, sem versão (recomendação do PO) · **B. continua, com uma chave só para isso (escolhida pelo dono)**.
**Por que esta:** a Maind mantém a pergunta em português sobre a história da instância. Abre-se mão de: ⚠️ volta um cadastro de IA no painel da instância, de alcance estreito; ⚠️ a pergunta lê a história guardada no SaaS (o banco de log) e não passa por middleware de organização nenhum; como ela roda é do arquiteto (`P-048`).
**Afeta:** `D-158` (volta a valer), `D-266` (segue: nenhuma organização usa a chave da instância), `MF-101`, `P-048`, a arquitetura geral (o administrador e o banco de log).
**Hipóteses a validar:** 🔎 que a Maind use a pergunta o bastante para valer o custo da chave.
**Reabrir quando:** a Maind não usar a pergunta, ou o custo pesar.

### D-275 · O painel da instância mostra o estado e a versão do middleware de cada organização
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-089`. O painel da instância (`MF-101`) mostra, para cada organização, o **estado do middleware dela** (no ar ou fora) e a **versão** que ele informa: o da Maind, que atende as organizações do SaaS, e, nas organizações que usam o da casa do cliente, o desse cliente, enquanto o SaaS o alcança (`D-272`). **Quem é avisado quando ele para** segue a `D-240`: o dono do serviço (a Maind, no middleware dela; o cliente, no dele).
**Contexto:** o login e os dados de toda organização passam pelo middleware (`D-258`, `D-261`), e a Maind opera o dela. Sem o estado à vista, a Maind descobriria a queda por fora do produto.
**Opções avaliadas** (sem pontuação): **A. mostra o estado e a versão (recomendação do PO, escolhida pelo dono)** · B. fora do painel, na observabilidade da infraestrutura.
**Por que esta:** a peça mais crítica do SaaS fica à vista de quem opera. Abre-se mão de: ⚠️ o painel deixa de ser só assentos, uso e custo; o que o SaaS consegue saber do middleware do cliente depende de como ele o alcança (`P-042`, `P-048`).
**Afeta:** `MF-101`, `D-240`, `P-040`, `P-042`, `P-048`.
**Reabrir quando:** o estado do middleware do cliente não puder ser medido de fora.

### D-274 · O relatório da organização mostra a história dos assentos sem o nome de quem os ocupou
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-088`. O relatório da organização (`D-149`) mostra a **história dos assentos em números** (as ocupações, as reservas por convite, as devoluções, os cortes e as reativações, mês a mês), **sem o nome de quem os ocupou**: a Maind não vê o nome de quem ocupa cada assento. **Substitui em parte a `D-157`**, que mostrava o nome, e resolve o conflito dela com a `D-261` e a `ARQ-097` (o banco de log não guarda o nome da pessoa).
**Contexto:** as pessoas ficam isoladas no middleware, fora do SaaS (`D-261`), e a `D-157` fazia a Maind ver o nome de quem ocupa cada assento. Era a opção B da `D-157`, que o PO recomendara e o dono preferira não seguir em 05/11/2026.
**Opções avaliadas** (sem pontuação): **A. sem nome (recomendação do PO, escolhida pelo dono)** · B. com o nome, informado pelo middleware ao SaaS (`D-157`).
**Por que esta:** é coerente com as pessoas fora do SaaS, e o indicador "na implantação" sobre a Maind ver o nome (`D-247`) deixa de existir. Abre-se mão de: ⚠️ a Maind não confere mais a cobrança assento a assento com nome, e o suporte não responde "quem ocupava o assento".
**Afeta:** `D-157`, `D-247` (o indicador da `MF-101`), `ARQ-097` (a dimensão de pessoas do banco de log, do arquiteto, `P-048`), `MF-101`, a arquitetura geral (o diagrama de dados e história).
**Hipóteses a validar:** 🔎 que a cobrança se confira só com contagens.
**Reabrir quando:** a Maind não conseguir conferir a cobrança, ou um cliente contestar um assento.

### D-273 · Em qualquer hospedagem, quem configura os bancos e a IA é o owner da organização; o time da Maind só dá suporte
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-095`. Os bancos e a IA são configurados **pelo owner da organização, no front do middleware, em qualquer hospedagem** (na Maind, com o usuário que a Maind cria, `D-271`). O **time da Maind dá suporte técnico, antes e depois da venda, mas não configura por ele**. A chave de IA que a Maind dá (`D-264`) é cadastrada pelo owner. **Substitui em parte a `D-265`**, que punha o time da Maind como quem configura na hospedagem da Maind.
**Contexto:** a `D-271` disse que o owner acessa o front do middleware também na Maind. O PO perguntou, então, quem configura: o owner ou o time da Maind, por ele.
**Opções avaliadas** (sem pontuação): **A. o owner da organização (recomendação do PO, escolhida pelo dono)** · B. o time da Maind, por ele (`D-265`).
**Por que esta:** o front e a responsabilidade são os mesmos nas duas hospedagens, e o time da Maind deixa de conhecer, por rotina, as credenciais dos bancos de cada cliente. Abre-se mão de: ⚠️ o owner da organização precisa saber configurar um banco e uma IA, com o apoio da Maind; ⚠️ quem opera o middleware da Maind segue podendo, tecnicamente, alcançar as credenciais (a promessa "a Maind não vê", `D-189`, só vale com o middleware na casa do cliente).
**Afeta:** `D-265`, `D-264`, `D-268` (o aviso ao time da Maind segue), `MF-101`, `MF-104`, `MF-105`, `MF-121`, a arquitetura geral (o nó "Time da Maind").
**Hipóteses a validar:** 🔎 que o owner consiga configurar sozinho, com a documentação e o suporte.
**Reabrir quando:** os owners não conseguirem configurar sozinhos e o suporte virar o caminho de sempre.

### D-272 · O middleware é multi-organização em qualquer hospedagem; a D-259 sai
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-094`. Em qualquer hospedagem, o **middleware atende várias organizações**: o da **Maind** atende **todas as organizações do SaaS**, cada uma isolada pelo seu certificado (`D-258`), e o do **cliente** atende as **organizações dele** (`D-008`). A diferença entre as hospedagens é só o local físico. **Substitui a `D-259`** (um middleware por organização); na hospedagem da Maind a frota volta a ser única (o retorno da `D-196`).
**Contexto:** ao reescrever a `MF-101`, o dono disse que o middleware será multi-organização em qualquer hospedagem, o que contradizia a `D-259`, decidida no mesmo dia. O passo 4 do fluxo da `D-258` (importar o certificado "replica a org no middleware") já supunha isso.
**Opções avaliadas** (sem pontuação): **A. multi-organização (recomendação do PO, escolhida pelo dono)** · B. um por organização (`D-259`).
**Por que esta:** uma frota só, e criar uma organização não exige subir um middleware novo. Abre-se mão de: ⚠️ um ponto único na hospedagem da Maind: se o middleware for invadido, expõe as credenciais e as regras de todas as organizações do SaaS; quem exigir mais isolamento usa o middleware na casa dele.
**Afeta:** `D-259` (substituída), `D-258` (passo 1: sobe um só), `D-196` (volta o retorno "uma frota só"), `D-265`, `P-048` (a "criação automática de um middleware por organização" vira "adicionar a organização ao middleware"), o documento 01, os diagramas da arquitetura geral (execução, infraestrutura separada, criar organização, segurança, implantação) e as páginas da `MF-101` e da `MF-121`.
**Hipóteses a validar:** 🔎 que o isolamento por certificado baste entre as organizações do SaaS; 🔎 que a Maind opere um middleware só sem ele virar ponto único de falha.
**Reabrir quando:** um cliente do SaaS exigir um middleware só dele, ou houver um incidente de isolamento.

### D-271 · O owner da organização acessa o front do middleware também na hospedagem da Maind; a Maind cria o usuário dele
Situação: 🟢 decidida (resposta do dono em 07/11/2026, fora das opções) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-087`. A diferença entre o middleware hospedado pela Maind e o da casa do cliente é **só o local físico da implantação**: o front do middleware é o mesmo, e **o owner da organização o acessa nas duas hospedagens**. Na hospedagem da Maind, **a Maind cria o usuário** com que o owner entra no front do middleware.
**Contexto:** a reescrita da `MF-101` (pedido do dono, 07/11/2026) levou o PO a perguntar quem do time da Maind configura os bancos e a IA na hospedagem da Maind: o administrador da instância ou um papel de suporte à parte. O dono respondeu fora das opções: o owner da organização tem acesso ao front, como no cliente, e o middleware será multi-organização em qualquer hospedagem (o que muda a `D-259`: `I-094`).
**Por que esta:** uma peça só e a mesma experiência nas duas hospedagens, sem um segundo papel na Maind.
**Fica de fora / adiado:** se, na hospedagem da Maind, é o owner ou o time da Maind quem configura os bancos e a IA (`I-095`, que revê a `D-265`); se o middleware atende várias organizações (`I-094`).
**Afeta:** `D-265`, `D-259`, `D-193`, `D-202`, `MF-101`, `MF-121`.
**Reabrir quando:** o owner não conseguir configurar sozinho e o suporte da Maind virar o caminho de sempre.

### D-270 · A MF-121 passa a se chamar "Middleware da organização"
Situação: 🟢 decidida (resposta do dono em 07/11/2026, contra a recomendação do PO, que era "Dados e pessoas sob a guarda da organização") · Data: 07/11/2026 · Versão: v2.0

**Decisão:** a `MF-121` passa a se chamar **`MF-121:Middleware da organização`**. O nome deixa de ser provisório, e o número não muda. O nome antigo, "Middleware na casa do contratante", vale só nas decisões antigas (`D-188`, `D-195`, `D-196`), que seguem como estão.
**Contexto:** a `D-260` pôs a `MF-121` na v2.0 e fez dela o middleware de toda organização, na Maind ou na casa do cliente. O nome antigo, provisório, descrevia só a casa do contratante.
**Opções avaliadas** (sem pontuação): A. "Dados e pessoas sob a guarda da organização" (recomendação do PO: diz o resultado para o cliente) · **B. "Middleware da organização" (escolhida pelo dono)**.
**Por que esta:** o nome é curto e usa a palavra que o time e o dono já usam. Abre-se mão de: ⚠️ o nome diz o mecanismo, e não o resultado; as páginas de leitura explicam o termo na primeira vez.
**Afeta:** os documentos `04` a `07`, as páginas de leitura da `MF-121`, o site das mfs.
**Reabrir quando:** os clientes não entenderem o nome.

### D-269 · Os owners adicionais, no máximo mais dois, ocupam assento de owner contratado; só o primeiro é grátis
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-080`. A organização pode ter **no máximo mais dois owners além do primeiro** (fluxo do dono, `D-258`), e **cada owner adicional ocupa um assento de owner contratado**, contado e cobrado como qualquer assento (`D-067`, `D-194`). Só o primeiro owner é grátis (`D-069`, `D-123`). O limite de mais dois é um teto do que a organização pode contratar. Os owners ligados ao login da empresa chegam na v2.1 (`D-118`, `D-184`).
**Contexto:** a `D-069` e a `D-123` dão um assento de owner grátis por organização, e o cliente pode pedir mais assentos. No fluxo do dono, o primeiro owner cadastra até dois outros.
**Opções avaliadas** (sem pontuação): **A. ocupam assento de owner contratado (recomendação do PO, escolhida pelo dono)** · B. não contam como assento.
**Por que esta:** a cobrança por assento desde o primeiro cliente (`D-107`) vale também para os owners. Abre-se mão de: ⚠️ o cliente paga por até dois owners a mais.
**Afeta:** `D-069`, `D-123`, `D-194`, `MF-103`, `P-022` (o preço por tipo de assento).
**Reabrir quando:** os clientes recusarem pagar por owners adicionais.

### D-268 · Quando a IA da organização para, é avisado o owner da organização e, se a chave é da Maind, também o time da Maind
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-086`. Quando a IA de uma organização para (chave recusada ou falta de crédito), **o owner da organização é sempre avisado**; quando a chave é a que a Maind dá (`D-264`), **o time da Maind também é avisado**, para repor o crédito. **Substitui em parte** a `D-218` ("é avisado o dono da conexão": o owner da organização ou o administrador da instância), que supunha a conexão da instância.
**Contexto:** com o fim da conexão da instância (`D-266`) e a IA configurada no middleware (`D-265`), "o dono da conexão" deixou de ser o administrador da instância.
**Opções avaliadas** (sem pontuação): **A. o owner da organização e, se a chave é da Maind, o time da Maind (recomendação do PO, escolhida pelo dono)** · B. só o owner da organização.
**Por que esta:** quem sente a falta da IA sempre sabe, e a Maind não depende de o owner avisá-la. Abre-se mão de: ⚠️ o time da Maind passa a receber o aviso de cada organização que usa chave dela; como o aviso chega a ele é do arquiteto (`P-048`).
**Afeta:** `D-218`, `D-240` (o aviso quando outro serviço para segue com o dono do serviço), `MF-101`.
**Reabrir quando:** o volume de avisos ao time da Maind virar ruído.

### D-267 · A chave de IA que a Maind dá é paga pela Maind, e o owner da organização vê o consumo e o custo de toda a IA dela
Situação: 🟢 decidida (resposta do dono em 07/11/2026, contra a recomendação do PO, que era a opção A) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-084`. Quando a Maind **dá uma chave de provedor de IA** à organização (`D-264`), **quem paga é a Maind**. O **owner da organização vê o consumo e o custo de toda a IA da organização**, tanto da chave que a organização paga quanto da que a Maind dá. Onde essa tela mora (o Horus ou o front do middleware) é do arquiteto (`P-048`).
**Substitui em parte:** a `D-241` ("o owner vê o consumo e o custo só da conexão que a organização paga"): agora ele vê também o da chave que a Maind dá.
**Contexto:** com o fim da conexão da instância (`D-266`), a chave que a Maind dá passou a morar na configuração da organização, e o PO perguntou quem a paga e quem vê o consumo dela.
**Opções avaliadas** (sem pontuação): A. a Maind paga e é a única a ver o consumo (recomendação do PO) · **B. a Maind paga, e o owner da organização também vê o consumo (escolhida pelo dono)**.
**Por que esta:** o owner controla o gasto de toda a IA da organização, e não só de parte dela. Abre-se mão de: ⚠️ o custo que a Maind paga fica à vista do cliente.
**Afeta:** `D-241` (o consumo), `D-153` (o aviso de custo da administração), `MF-105`, `P-022` (o preço: a IA dada pela Maind entra ou não na conta).
**Reabrir quando:** a visibilidade do custo da Maind para o cliente virar um problema comercial.

### D-266 · A conexão da instância deixa de existir: a IA é sempre da organização, configurada no middleware
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada; a `D-276` abre uma exceção estreita: uma chave de IA da instância só para a pergunta do administrador sobre a história da instância) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-085`. **Não há mais conexão de IA no nível da instância.** Cada organização tem a sua configuração de IA no front do middleware (`D-265`). Quando a Maind paga, o time dela coloca a chave da Maind nessa configuração (`D-264`); quem paga e quem vê o consumo é o `I-084`. Some o cadastro de IA do painel da instância (`MF-101`) e o passo de "disponibilizar uma conexão" ao criar a organização.
**Substitui em parte:** a `D-216` (as duas origens de IA: sobra só a da organização) e a `D-217` (a organização nasce sem IA e o administrador da instância disponibiliza uma conexão: agora a IA é configurada no middleware, pela própria organização ou pelo time da Maind).
**Contexto:** a `D-265` pôs a configuração da IA no front do middleware, organização por organização. O PO perguntou se a conexão da instância sobrevivia, e o dono escolheu que deixa de existir.
**Opções avaliadas** (sem pontuação): **A. deixa de existir (recomendação do PO, escolhida pelo dono)** · B. continua para as organizações hospedadas pela Maind.
**Por que esta:** há um lugar só para configurar a IA. Abre-se mão de: ⚠️ o controle central de qual modelo cada organização usa e de quanto se gasta, que a conexão da instância dava à Maind; ⚠️ a Maind configura uma organização por vez.
**Afeta:** `D-218` (quem é avisado quando a IA para: `I-086`), `D-241` (o consumo: `I-084`), `D-216`, `D-217`, `MF-101`, `MF-105`.
**Reabrir quando:** a Maind precisar de um controle central do modelo e do gasto.

### D-265 · Os bancos e a IA são sempre configurados no front do middleware; quem configura é a organização ou, na hospedagem da Maind, o time da Maind
Situação: ⚪ substituída em parte pela `D-273` (em qualquer hospedagem, quem configura é o owner da organização; o time da Maind só dá suporte) · antes: 🟢 decidida (resposta do dono em 07/11/2026, fora das opções) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-083`. **Em qualquer hospedagem, a configuração dos bancos (as fontes de dados) e da IA é feita no front do middleware**, e não no Horus. **Quem configura depende de onde o middleware está:** com o middleware **fora da Maind**, é a organização (`D-264`); com o middleware **hospedado pela Maind** ("full SaaS"), é o **time da Maind**, como suporte técnico de pré e de pós-venda.
**Contexto:** o PO perguntou se, com o middleware hospedado pela Maind, a IA seguia como na `D-216` (a Maind cadastra a conexão da instância e a disponibiliza). O dono respondeu fora das opções: a regra é uma só, e o que muda é quem a executa.
**Por que esta:** uma regra só para qualquer hospedagem, e as credenciais dos bancos e da IA ficam fora do SaaS (`D-258`). Abre-se mão de: ⚠️ na hospedagem da Maind, o time de suporte da Maind passa a configurar, e a conhecer, as credenciais de cada cliente, o que enfraquece a promessa de que a Maind não vê (`D-189`, `D-196`); ⚠️ o owner da organização deixa de conectar fontes e IA pelo Horus (a `MF-104` e a `MF-105` mudam de lugar); ⚠️ a conexão da instância, que a `D-216` cadastrava no nível da instância, perde o lugar (ver o `I-085`).
**Afeta:** `D-216`, `D-217`, `D-218`, `D-241`, `MF-101`, `MF-104`, `MF-105`, `MF-121`.
**Hipóteses a validar:** 🔎 que o time de suporte da Maind dê conta de configurar cada organização nova, antes e depois da venda, sem virar gargalo.
**Prova de valor:** o time da Maind configura, no front do middleware, o banco e a IA de uma organização nova, e o owner pergunta ao banco dele.
**Reabrir quando:** a configuração pelo time da Maind virar gargalo, ou um cliente exigir configurar sozinho na hospedagem da Maind.

### D-264 · Com o middleware fora da Maind, a organização configura a IA dela; a Maind pode lhe dar uma chave de provedor
Situação: 🟢 decidida (resposta do dono em 07/11/2026, fora das opções) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-078`. **Quando o middleware está fora da Maind (na casa do cliente), a configuração da IA é feita pela organização**, no front do middleware. A Maind **pode dar uma chave de algum provedor de IA** para a organização usar. O modelo e os dados ficam, assim, na casa do cliente (`D-189`).
**Contexto:** o PO perguntou se a organização podia usar a IA da instância (a que a Maind paga, `D-216`) agora que o ciclo da análise roda dentro do middleware (`D-258`). O dono respondeu só o caso do middleware fora da Maind: o caso do middleware hospedado pela Maind ficou no `I-083`, e quem paga a chave que a Maind dá, no `I-084`.
**Por que esta:** a organização controla a IA dela, o que a `MF-105` já prometia. Abre-se mão de: ⚠️ uma chave que a Maind dá fica na casa do cliente, e a TI dele consegue lê-la e reaproveitá-la; ⚠️ a conexão da instância sem edição na organização (`D-216`) não vale nesse caso.
**Afeta:** `D-216`, `D-217`, `D-241`, `P-032`, `MF-105`, `MF-121`.
**Hipóteses a validar:** 🔎 que o cliente aceite configurar a IA no front do middleware.
**Reabrir quando:** a chave dada pela Maind vazar na casa de um cliente.

### D-263 · A segurança dos dados por pessoa continua na v2.1, e a MF-106 passa a depender da MF-121
Situação: 🟢 decidida (resposta do dono em 07/11/2026, com a opção recomendada) · Data: 07/11/2026 · Versão: v2.1

**Decisão:** fecha o `I-081`. A `MF-106:Segurança dos dados por pessoa` **continua na v2.1** (`D-199`, `ARQ-090`). Na v2.0, o middleware autentica, guarda as pessoas (`D-261`) e dá acesso aos bancos; o "quem vê o quê dentro do banco" chega na v2.1 e roda no middleware. A dependência **se inverte**: a `MF-121` (v2.0) **deixa de depender** da `MF-106`, e a **`MF-106` passa a depender da `MF-121`**.
**Contexto:** a `D-196` fazia a `MF-121` depender da `MF-106`. Com a `MF-121` na v2.0 (`D-260`) e a `MF-106` na v2.1, a dependência ficou ao contrário.
**Opções avaliadas** (sem pontuação): **A. continua na v2.1 (recomendação do PO, escolhida pelo dono)** · B. sobe para a v2.0.
**Por que esta:** nada do que o dono já decidiu se reabre (`D-199`, `ARQ-090`) e a v2.0 não cresce mais uma mf. Abre-se mão de: ⚠️ na v2.0, o que cada pessoa vê nos dados segue como a v2.0 já decidiu, sem a segurança por pessoa.
**Afeta:** `D-196` (o "Depende de"), `MF-106` e `MF-121` nos documentos `04`, `05`, `06`, `07` e nas páginas de leitura.
**Reabrir quando:** um cliente da v2.0 exigir a segurança por pessoa nos dados.

### D-262 · O gestor cria o convite e pede a troca do assento pelo Horus; só o owner usa o front do middleware
Situação: 🟢 decidida (resposta do dono em 07/11/2026, contra a recomendação do PO, que era a opção A) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-082`. **Só o owner usa o front do middleware.** O **gestor** cria o convite, escolhe o tipo de assento e pede a troca do tipo **pelo Horus** (`D-071`, `D-072`); o **owner aprova no front do middleware**, onde a pessoa é cadastrada (`D-261`).
**Contexto:** o PO recomendou que o gestor também usasse o front do middleware, para o e-mail de quem é convidado nunca passar pelo SaaS. O dono preferiu o gestor no Horus.
**Opções avaliadas** (sem pontuação): A. o gestor também usa o front do middleware (recomendação do PO) · **B. só o owner usa o front do middleware (escolhida pelo dono)**.
**Por que esta:** o gestor continua num app só. Abre-se mão de: ⚠️ o e-mail do convidado **passa pelo SaaS** a caminho do middleware, e a regra "as pessoas ficam fora do SaaS" (`D-261`) ganha essa exceção em trânsito; o arquiteto confere se o SaaS só repassa, sem guardar (`P-048`).
**Afeta:** `D-071`, `D-072`, `D-261`, `MF-102`.
**Prova de valor:** o gestor cria um convite no Horus, o owner o aprova no front do middleware, e a pessoa entra.
**Reabrir quando:** algum cliente considerar o e-mail em trânsito pelo SaaS um vazamento.

### D-261 · As pessoas da organização ficam isoladas no middleware, fora do SaaS; o owner as gere pelo front do middleware
Situação: 🟢 decidida (resposta do dono em 07/11/2026, fora das opções, na linha da B do PO) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-076`. O **owner da organização usa o front do middleware** (o aplicativo de setup) para cadastrar e gerir as pessoas da organização, e os **dados das pessoas ficam isolados no middleware, fora do SaaS**. O motivo do dono: é mais seguro, pela separação de responsabilidade e pela segurança. O que o SaaS precisa saber de cada pessoa para funcionar é do arquiteto (`P-048`).
**Contexto:** o PO ofereceu duas opções: A. a gestão na tela do Horus, com o middleware só guardando (recomendação do PO); B. a gestão no setup do middleware. O dono respondeu na linha da B e falou só do owner: o gestor ficou no `I-082`.
**Por que esta:** as pessoas da organização não passam pelo SaaS, e quem cuida delas é quem é da organização. Abre-se mão de: ⚠️ o owner usa dois apps, o Horus e o front do middleware; ⚠️ a `MF-102` (v2.0, redesenhada inteira, `D-108`) precisa ser redesenhada para o front do middleware; ⚠️ o que o Horus mostra com nome de pessoa (a Home da organização, o rastro da Auditoria, a medida de autonomia) precisa buscar o nome no middleware, e o arquiteto confere (`P-048`).
**Afeta:** `MF-102` (onde a gestão de pessoas mora), `MF-101` (o painel da instância só enxerga contagens, `D-214`), `D-071`, `D-072`, `D-108`, `D-236`, `D-248`.
**Hipóteses a validar:** 🔎 que o owner aceite usar dois apps; 🔎 que o front do middleware comporte a gestão de pessoas que a `MF-102` definiu.
**Prova de valor:** o owner convida e gere pessoas pelo front do middleware, e nenhum dado delas está no banco do SaaS.
**Reabrir quando:** os owners reclamarem dos dois apps, ou o SaaS não conseguir funcionar sem o nome e o e-mail das pessoas.

### D-260 · A MF-121 sobe inteira para a v2.0: o middleware de cada organização, na Maind ou na casa do cliente
Situação: 🟢 decidida (resposta do dono em 07/11/2026, contra a recomendação do PO, que era a opção A) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-079`. A `MF-121:Middleware na casa do contratante` (nome provisório, que já não descreve só a casa do contratante) **passa da v2.1 (onda 2) para a v2.0, inteira**: o middleware de cada organização (`D-259`), hospedado pela Maind ou pelo cliente (`D-258`). **Não nasce mf nova**: a próxima mf nova segue sendo a `MF-124`. A regra "uma mf, uma versão" (`D-197` a `D-203`) fica intacta. A v2.0 passa a ter **19 mfs** (as 18 de antes e a `MF-121`), e a onda 2 da v2.1 perde a `MF-121` (`D-181`, `D-196`, `D-198`).
**Contexto:** a `D-258` pôs o middleware em toda organização desde a v2.0. O PO propunha uma mf nova na v2.0 (o middleware hospedado pela Maind) e deixar a `MF-121` só com a casa do cliente, na v2.1. O dono preferiu a `MF-121` inteira na v2.0.
**Opções avaliadas** (sem pontuação): A. mf nova na v2.0 e a `MF-121` só com a casa do cliente, na v2.1 (recomendação do PO) · **B. a `MF-121` inteira na v2.0 (escolhida pelo dono)**.
**Por que esta:** uma mf só, e a casa do cliente já na v2.0, com o mesmo middleware em qualquer hospedagem. Abre-se mão de: ⚠️ a v2.0 passa de 18 para 19 mfs e carrega a imagem para o cliente instalar, a atualização feita por ele e a validação com a TI dos clientes.
**Afeta:** `D-196` (a versão e a dependência da `MF-106`, que é da v2.1: ver o `I-081`), `D-188` e `D-181` (a onda 2 da v2.1), `04`, `05`, `06`, `07` e as páginas de leitura da `MF-121`.
**Hipóteses a validar:** 🔎 que a TI dos clientes aceite hospedar o middleware e liberar o endereço dele já na v2.0 (`D-195`).
**Prova de valor:** a `D-196` vale na v2.0: um cliente de cibersegurança rígida instala a imagem e faz uma pergunta de análise sobre o banco interno, e nada além da pergunta e da resposta pronta sai.
**Reabrir quando:** a v2.0 não couber com a casa do cliente.

### D-259 · Cada organização tem o seu próprio middleware, também na hospedagem da Maind
Situação: ⚪ substituída pela `D-272` (o middleware é multi-organização em qualquer hospedagem) · antes: 🟢 decidida (resposta do dono em 07/11/2026, contra a recomendação do PO, que era a opção A) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-077`. Na hospedagem da Maind, **cada organização tem o seu próprio middleware**, com a sua base de configuração. Não há middleware compartilhado entre organizações. Confirma a `D-196` ("o middleware é por organização") e passa a valer também para o SaaS, não só para a casa do cliente.
**Contexto:** o passo 4 do fluxo do dono (`D-258`: o certificado "replica a org no middleware") sugeria um middleware só para todas as organizações do SaaS. O dono escolheu um para cada.
**Opções avaliadas** (pesos da `D-015`; notas de 0 a 5, quase todas hipótese do PO): A. um só da Maind, com cada organização isolada pelo certificado: 69 · **B. um por organização: 65 (escolhida pelo dono)**. Foi empate técnico (4 pontos); o PO desempatou por reversibilidade e recomendou A.
**Por que esta:** o isolamento entre organizações é total: a credencial e as regras de uma não ficam ao alcance da outra. Abre-se mão de: ⚠️ a Maind opera um middleware por cliente, e o retorno "uma frota só, sem operar uma instalação por cliente" da `D-196` deixa de valer na hospedagem da Maind; ⚠️ criar uma organização passa a exigir subir o middleware dela (a automação é do arquiteto, `P-048`).
**Afeta:** `D-196` (o retorno), `D-258` (o passo 1: o time de implantação sobe um middleware por organização).
**Hipóteses a validar:** 🔎 que a Maind consiga criar e manter um middleware por organização sem que a criação de uma organização vire um trabalho manual.
**Prova de valor:** a Maind cria duas organizações e cada uma responde pelo seu middleware, sem nada em comum entre elas.
**Reabrir quando:** a operação de um middleware por cliente pesar mais que o isolamento.

### D-258 · Toda organização usa uma infraestrutura separada do SaaS, o middleware, desde a v2.0
Situação: 🟢 decidida (resposta do dono em 07/11/2026, contra a recomendação do PO, que era a opção A; o fluxo foi descrito por ele) · Data: 07/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-075`. **Toda organização, desde a v2.0, chega à autenticação, aos dados e à IA por uma infraestrutura separada do SaaS**: o **middleware**, com a **base de configuração** (membros e detalhes da organização) e o **aplicativo de setup**. A Maind hospeda o middleware das organizações do SaaS (v2.0). A hospedagem na casa do cliente fica no `I-079`. O contrato é o mesmo em qualquer hospedagem, e a **localização do middleware é irrelevante** para o produto, desde que a rede o alcance. O ciclo da análise (o modelo de IA e as consultas) roda dentro dele, e ao Horus SaaS chega só a pergunta e a resposta pronta (`D-189`).
O fluxo que o dono descreveu, em palavras de produto:
1. O time de implantação da Maind sobe o SaaS e o middleware em infraestruturas lógicas separadas.
2. O **administrador da instância** (a Maind) cria a organização no SaaS (`D-146`). A criação gera um **certificado digital** e uma **chave de instalação** cifrada, com os dados de que o middleware precisa.
3. O certificado é importado no middleware, que passa a ter a organização. O middleware devolve um **arquivo de configuração assinado e cifrado** com o mesmo certificado (endereço, porta etc.), e as duas pontas confirmam o **handshake**. É assim que o SaaS aprende a chegar ao middleware.
4. O administrador da instância libera no SaaS os **assentos** contratados (`D-068`). Eles vão ao middleware, onde o **owner da organização cadastra as pessoas**.
5. O endereço de acesso da organização leva um **token** que direciona a pessoa ao middleware e à organização certos, já que o endereço do SaaS é o mesmo para todas. A sessão da pessoa carrega o que o SaaS precisa para encaminhar cada pedido à organização certa.
6. As **configurações de autenticação** ficam no middleware. O **owner da organização** e o **administrador da instância** entram **sempre por usuário e senha**. Com esse usuário, o owner cadastra **outros owners (no máximo mais dois)**, ligados ao login da empresa (v2.1, `D-118`, `D-184`).
Com isso a autenticação e a autorização estão prontas, e o resto é funcionalidade.
**Contexto:** o dono rascunhou, em 07/11/2026, três infraestruturas: a do SaaS (interface, motor e banco do SaaS), a separada (middleware, base de configuração e setup) e a da organização (as pessoas, os bancos e os provedores de IA). A infraestrutura separada "pode ficar na Maind ou, se a organização achar melhor, na casa dela, para garantir que os bancos de dados não fiquem expostos de forma pública".
**Opções avaliadas** (pesos da `D-015`; notas de 0 a 5, quase todas hipótese do PO): A. só a `MF-121`, na v2.1 (onda 2): 71 · C. a `MF-121` sobe para a v2.0, só na casa do cliente: 69 · **B. toda organização, desde a v2.0: 64 (escolhida pelo dono)**. O PO recomendou A pelo tempo até o valor, porque a v2.0 está fechada com 18 mfs (`D-197` a `D-203`).
**Por que esta:** escolha do dono: a segurança e a separação valem desde o primeiro dia, com uma peça só para qualquer hospedagem. Abre-se mão de: ⚠️ a v2.0 fechada cresce (uma mf nova, mais a `MF-101` e a `MF-102`); ⚠️ a promessa "o funcionário da Maind não liga nem vê" (`D-189`, `D-196`) só vale com o middleware na casa do cliente, porque no SaaS a Maind o opera.
**Afeta (a delimitar nos impasses abertos):** `D-193` e `D-195` (quem configura e como a chave nasce), `D-188` e `D-196` (a `MF-121` deixa de ser a única porta do middleware), `D-197` a `D-203` (a v2.0 fechada), `MF-101` e `MF-102`.
**Fica de fora / adiado:** o desenho técnico (como o SaaS e o middleware sobem, o formato e o ciclo de vida do certificado, o handshake, o token no endereço, o que acontece com o middleware fora do ar): do arquiteto (`P-048`); o login da empresa, que segue na v2.1.
**Hipóteses a validar:** 🔎 que a Maind opere o middleware de todas as organizações sem ele virar ponto único de falha; 🔎 que a TI dos clientes aceite hospedar a peça ou liberar o endereço dela.
**Prova de valor:** a Maind cria uma organização, troca o certificado com o middleware, libera os assentos, e o owner cadastra uma pessoa que pergunta ao banco do cliente sem o banco ser alcançado direto pelo SaaS.
**Reabrir quando:** a v2.0 não couber com a peça, ou a operação do middleware pesar na Maind.

### D-257 · A fonte cuja tecnologia não aceita a identidade da pessoa fica só com a regra do Horus, e o owner é avisado
Situação: 🟢 decidida (resposta do dono em 06/11/2026, com a opção recomendada) · Data: 06/11/2026 · Versão: v2.1

**Decisão:** na organização que liga o login da empresa (etapa 2 da `MF-106`), a **fonte de dados cuja tecnologia não aceita a identidade da pessoa continua disponível, protegida só pela regra do Horus**, e **o owner é avisado ao ligar o login da empresa** de que, nessa fonte, as regras do banco da empresa não valem. Fecha a segunda parte do `A-25` do documento 14 (`I-074`) e, com a `D-256`, **fecha o `A-25` inteiro**.
**Contexto:** o "vale a mais restritiva" (`D-026`) pede que o banco receba a identidade da pessoa; hoje a proteção por pessoa só cobre o SQL Server (`P-033`), e nem toda tecnologia aceita essa identidade. O arquiteto recomendou manter a fonte só com a regra do Horus e avisar o owner.
**Opções avaliadas:** sem pontuação: **fica só com a regra do Horus, e o owner é avisado (recomendação do arquiteto e do PO, escolhida pelo dono)** · fica fora enquanto o login estiver ligado · o owner decide, fonte a fonte.
**Por que esta:** nenhuma fonte some da organização, e o owner decide com a informação. Abre-se mão de a regra da empresa valer em toda fonte: ⚠️ nessa fonte, só vale a regra do Horus.
**Fica de fora / adiado:** o texto do aviso ao owner (desenho); quais tecnologias aceitam a identidade da pessoa (do arquiteto, `P-033`).
**Completa a `D-026` e a `D-027`.**
**Hipóteses a validar:** 🔎 que o owner entenda o aviso e que a regra do Horus baste nessas fontes.
**Prova de valor:** o owner liga o login da empresa, recebe o aviso de que uma fonte fica só com a regra do Horus, e a fonte continua respondendo.
**Reabrir quando:** os clientes pedirem para bloquear a fonte, ou para decidir fonte a fonte.

### D-256 · Com o login da empresa ligado, o aviso de resposta limitada diz qual regra do Horus limitou e que as regras da empresa também valem
Situação: 🟢 decidida (resposta do dono em 06/11/2026, com a opção recomendada) · Data: 06/11/2026 · Versão: v2.1

**Decisão:** na organização que liga o login da empresa (etapa 2 da `MF-106`), o aviso de resposta limitada **diz qual regra do Horus limitou a resposta** e **acrescenta uma frase fixa de que os controles de acesso da empresa também valem**. Fecha a primeira parte do `A-25` do documento 14 (`I-073`).
**Contexto:** na etapa 2, o "vale a mais restritiva" (`D-026`) sai por construção, mas o Horus só explica a parte dele: o banco da empresa devolve menos linhas sem dizer por quê. O arquiteto recomendou este texto.
**Opções avaliadas:** sem pontuação (texto de uma tela): **dizer a regra do Horus e que a empresa também vale (recomendação do arquiteto e do PO, escolhida pelo dono)** · continuar o aviso de hoje, "Resposta limitada aos dados que você pode ver".
**Por que esta:** a pessoa entende por que viu menos, mesmo quando a causa é uma regra da empresa que o Horus não consegue explicar. Abre-se mão de um aviso sem detalhe: ⚠️ ele mostra à pessoa a regra do Horus que a limitou.
**Fica de fora / adiado:** o texto exato do aviso e da frase fixa (desenho); a segunda parte do `A-25` (a fonte cuja tecnologia não aceita a identidade da pessoa, `I-074`).
**Completa a `D-026`.**
**Hipóteses a validar:** 🔎 que mostrar a regra à pessoa não revele o que a empresa quer manter reservado.
**Prova de valor:** a Carla recebe uma resposta limitada, lê qual regra do Horus a limitou e que as regras da empresa também valem, e não abre chamado para saber por que viu menos.
**Reabrir quando:** a empresa pedir para não mostrar a regra à pessoa.

### D-255 · A sessão nascida pelo login da empresa se confirma com ele a cada 8 horas
Situação: 🟢 decidida (resposta do dono em 06/11/2026, com a opção recomendada) · Data: 06/11/2026 · Versão: v2.1

**Decisão:** a sessão do Horus que nasce pelo login da empresa **se confirma com ele a cada 8 horas**. Se a empresa desligou a pessoa, ela precisa entrar de novo e não consegue. Fecha o item 3 do `A-20` do documento 14 (`I-072`) e, com a `D-253` e a `D-254`, **fecha o `A-20` inteiro**.
**Contexto:** a sessão do Horus dura até 30 dias (`ARQ-038`), e quem sai da empresa poderia continuar entrando todo esse tempo. O arquiteto recomendou confirmar com a empresa a cada 8 horas, 🔎 como hipótese a validar.
**Opções avaliadas:** sem pontuação: **a cada 8 horas (recomendação do arquiteto e do PO, escolhida pelo dono)** · só a sessão de até 30 dias de hoje · o owner define o intervalo, com 8 horas de padrão.
**Por que esta:** quem sai da empresa perde o acesso ao Horus em até 8 horas, sem esperar a sessão acabar. Abre-se mão de uma sessão que quase nunca pede para entrar de novo: ⚠️ a pessoa que a empresa desliga é a única que sente a diferença, mas o Horus passa a depender de a empresa responder à confirmação.
**Fica de fora / adiado:** o intervalo de 8 horas é hipótese do arquiteto (ele valida no desenho); o que a pessoa lê quando a confirmação falha (desenho); se o owner ajusta o intervalo.
**Completa a `D-027`.**
**Hipóteses a validar:** 🔎 *(técnica, do arquiteto)* que o login da empresa permita confirmar a sessão a cada 8 horas.
**Prova de valor:** a empresa desliga uma pessoa de manhã, e ela não consegue mais usar o Horus na mesma jornada de trabalho.
**Reabrir quando:** o arquiteto mostrar que o login da empresa não permite a confirmação, ou os clientes reclamarem de entrar de novo.

### D-254 · Na organização com o login da empresa, vale a role que ele traz
Situação: 🟢 decidida (resposta do dono em 06/11/2026, com a opção recomendada) · Data: 06/11/2026 · Versão: v2.1

**Decisão:** na organização que liga o login da empresa, **quando a role do cadastro do Horus e a do login da empresa discordam, vale a do login da empresa**; quem chega **sem valor mapeado** cai na **role padrão** da organização (`D-112`). Fecha o item 2 do `A-20` do documento 14 (`I-071`).
**Contexto:** a `D-052` deixou fora o caso de as duas roles divergirem. O arquiteto recomendou que valha a do login da empresa; a `D-118` já deixa o login da empresa para a etapa 2 da `MF-106`.
**Opções avaliadas:** sem pontuação: **a do login da empresa (recomendação do arquiteto e do PO, escolhida pelo dono)** · a do cadastro do Horus · a mais restritiva das duas.
**Por que esta:** a TI da empresa governa as roles num lugar só, e a pessoa não fica com uma permissão desatualizada. Abre-se mão de o owner mudar, no Horus, a role de quem entra pelo login da empresa: ⚠️ se o login disser outra coisa, vale o que o login diz.
**Fica de fora / adiado:** o item 3 do `A-20` (a sessão de quem sai da empresa); se o owner vê no Horus de onde veio a role de cada pessoa (desenho).
**Completa a `D-052`, a `D-112` e a `D-118`.**
**Hipóteses a validar:** 🔎 que os owners aceitem não editar a role de quem entra pelo login da empresa.
**Prova de valor:** a empresa muda a role de uma pessoa no login dela, e a pessoa passa a ter, no Horus, os botões da nova role na próxima entrada.
**Reabrir quando:** os owners pedirem para sobrescrever a role no Horus.

### D-253 · Quem chega pelo login da empresa sem convite não entra: o login só autentica
Situação: 🟢 decidida (resposta do dono em 06/11/2026, com a opção recomendada) · Data: 06/11/2026 · Versão: v2.1

**Decisão:** na organização que liga o login da empresa (etapa 2 da `MF-106`), **o login só autentica**: prova quem a pessoa é, e **só entra quem tem convite**, como na v2.0 (`D-071`). A pessoa que chega pelo login da empresa sem convite não entra, e não ocupa assento. Fecha o item 1 do `A-20` do documento 14 (`I-070`).
**Contexto:** ao escrever a documentação da `MF-106` (06/11/2026), a página declarou como aberto o que acontece com quem chega pelo login da empresa sem convite. O arquiteto recomendou manter o convite; a alternativa era a entrada automática na quarentena, que precisa de assento livre (`D-070`).
**Opções avaliadas:** sem pontuação (regra de acesso de uma organização): **só entra quem foi convidado (recomendação do arquiteto e do PO, escolhida pelo dono)** · entra sozinha, na quarentena.
**Por que esta:** ninguém ocupa um assento pago sem o owner saber, que é a regra da v2.0, e o login da empresa não muda quem pode entrar. Abre-se mão de menos trabalho para o owner: ⚠️ ele convida cada pessoa, mesmo com o login da empresa ligado.
**Fica de fora / adiado:** a mensagem que a pessoa lê quando chega sem convite (desenho); os outros dois itens do `A-20` (qual role vale quando a do cadastro e a do login da empresa discordam; a sessão de quem sai da empresa).
**Completa a `D-071` e a `D-118`.**
**Hipóteses a validar:** 🔎 que o owner prefira convidar a deixar entrar sozinho.
**Prova de valor:** a organização liga o login da empresa; uma pessoa sem convite tenta entrar por ele e não entra, e a convidada entra.
**Reabrir quando:** os owners reclamarem do trabalho de convidar todos, em empresas grandes.

### D-252 · A exportação da conversa fica registrada no rastro da Auditoria, e os downloads não
Situação: 🟢 decidida (resposta do dono em 06/11/2026, contra a recomendação do PO) · Data: 06/11/2026 · Versão: v2.0

**Decisão:** o rastro da Auditoria (`MF-116`) passa a registrar **quem exportou qual conversa em PDF ou HTML, e quando**, **sem o conteúdo** (`D-090`). **Os downloads de CSV, imagem e PDF de uma resposta continuam fora do rastro.** Fecha o `I-069`.
**Contexto:** o rastro guarda hoje as publicações, os envios, as aberturas de board e as mudanças de prazo; nenhuma ação pessoal de baixar. A `D-251` pôs a exportação no botão "Baixar" e deixou aberto se ela fica no rastro.
**Opções avaliadas:** sem pontuação: fora do rastro, como os downloads de hoje (recomendação do PO) · **só a exportação da conversa (escolhida pelo dono)** · toda saída, exportação e downloads.
**Por que esta:** o arquivo exportado leva a conversa inteira para fora do Horus, e o owner passa a poder responder "quem levou esta conversa para fora". Abre-se mão da simplicidade do rastro: ⚠️ é o primeiro registro de uma ação pessoal, e não de uma entrega a outras pessoas ou de uma abertura de board, e a `MF-116` ganha um item.
**Fica de fora / adiado:** os downloads de CSV, imagem e PDF de uma resposta; o desenho da linha na tela da auditoria (o filtro por tipo, se houver).
**Completa a `D-090`, a `D-250` e a `D-251`** e **fecha o `I-069`**. O prazo do registro é o do rastro (`D-092`).
**Hipóteses a validar:** 🔎 que o owner use esse registro; 🔎 *(técnica, do arquiteto, `P-047`)* que caiba no rastro sem guardar o conteúdo da conversa.
**Prova de valor:** o owner abre a Auditoria, filtra por pessoa e vê que a Carla exportou uma conversa em certo dia, sem ver o que havia nela.
**Reabrir quando:** o rastro ganhar volume demais, ou os clientes pedirem registrar também os downloads.

### D-251 · A exportação da conversa fica no botão Baixar da role
Situação: 🟢 decidida (resposta do dono em 06/11/2026, com a opção recomendada) · Data: 06/11/2026 · Versão: v2.0

**Decisão:** a exportação da conversa em PDF ou HTML (`D-250`) **é coberta pelo botão "Baixar"** que o owner liga e desliga por role (o botão de baixar CSV, imagem e PDF da `D-110`). Quem tem o botão exporta a conversa; quem não tem, não. **Não nasce botão novo**: a lista de botões e a regra de soma das roles (`D-111`) ficam como estão. Fecha o `I-068`.
**Contexto:** a `D-250` pôs a exportação na `MF-107` e deixou aberto quem pode usá-la, já que o arquivo sai do Horus com o que a pessoa viu.
**Opções avaliadas:** sem pontuação (uma escolha de gesto sobre o controle do owner): **junto do botão Baixar (recomendação do PO, escolhida pelo dono)** · um décimo botão da role · sem controle por role.
**Por que esta:** o owner já controla por role o que sai do Horus com o "Baixar", e a exportação é do mesmo tipo; não cria botão novo nem muda a regra de soma das roles. Abre-se mão de ligar a exportação à parte: ⚠️ quem pode baixar um CSV passa a poder exportar a conversa inteira.
**Fica de fora / adiado:** se a exportação fica no rastro da Auditoria (`I-069`).
**Completa a `D-110` e a `D-250`** e **fecha o `I-068`**.
**Hipóteses a validar:** 🔎 que o owner não precise de um controle separado para a exportação.
**Prova de valor:** o owner desliga o "Baixar" de uma role, e quem tem só essa role deixa de ver, ao mesmo tempo, o download de uma resposta e a exportação da conversa.
**Reabrir quando:** os owners pedirem para controlar a exportação à parte.

### D-250 · A exportação da conversa em PDF ou HTML é da MF-107, na v2.0
Situação: 🟢 decidida (resposta do dono em 06/11/2026, contra a recomendação do PO) · Data: 06/11/2026 · Versão: v2.0

**Decisão:** a **exportação da conversa em PDF ou HTML** (`D-249`) é um recurso da `MF-107:Perguntar aos dados em português`, **na v2.0**. A mf continua numa versão só (`D-197`); o que cresce é o que ela entrega. Fecha o `I-067`.
**Contexto:** a `D-249` disse que a investigação guiada se mostra exportando a conversa, "recurso nativo de uma conversa", sem dizer em qual mf e versão. O PO conferiu o código da v1.xx: o chat só baixa o **CSV e a imagem de um bloco** da resposta, e o PDF só existe no board; portanto a exportação da conversa é **recurso novo**. O mapa de hoje (`04`) diz que o Horus já baixa "CSV, imagem e PDF da resposta e da conversa", o que o código não confirma: o PO corrigiu o texto no mesmo trabalho.
**Opções avaliadas:** sem pontuação (o dono decide o escopo da primeira entrega): dentro da `MF-119`, na v2.1 (recomendação do PO) · mf nova na v2.1 · **`MF-107`, na v2.0 (escolhida pelo dono)** · sem versão por enquanto.
**Por que esta:** a conversa é da `MF-107`, e o dono vê a exportação como recurso de toda conversa; ela existe desde a primeira entrega, e a Investigação guiada (v2.1) já encontra o jeito de levar o caminho a uma reunião. Abre-se mão de uma v2.0 do tamanho que estava: ⚠️ cresce a `MF-107` e a primeira entrega, que já é grande.
**Fica de fora / adiado:** se a exportação é um botão das roles (`I-068`); se fica no rastro da Auditoria (`I-069`); o que o arquivo leva e o desenho técnico (do arquiteto, `P-047`); se vale também para a conversa da Pergunta rápida e do WhatsApp.
**Completa a `D-249`** (que deixou a versão a definir) e **fecha o `I-067`**. Leitura do PO *(a confirmar com o dono)*: vale para qualquer conversa de análise, e não só para a que tem uma investigação.
**Hipóteses a validar:** 🔎 *(técnica, do arquiteto, `P-047`)* que a exportação caiba na v2.0 sem atrasá-la; 🔎 que o PDF ou o HTML baste para levar a conversa a uma reunião.
**Prova de valor:** a gestora, ao fim de uma conversa de análise, exporta em PDF e leva os passos e as fontes à reunião, sem abrir a conversa a ninguém.
**Reabrir quando:** o arquiteto mostrar que a exportação não cabe na v2.0, ou os clientes pedirem para compartilhar a conversa.

### D-249 · Uma investigação guiada se mostra a outras pessoas exportando a conversa em PDF ou HTML, e a conversa nunca é compartilhada
Situação: 🟢 decidida (resposta do dono em 06/11/2026, fora das opções propostas; ele disse "em um primeiro momento talvez", e o PO a registra como a direção dele, com a ressalva como hipótese a validar) · Data: 06/11/2026 · Versão: a definir (`I-067`)

**Decisão:** para mostrar a outras pessoas o caminho de uma investigação guiada (`MF-119`), a conversa **não é compartilhada**: a pessoa **exporta a conversa em PDF ou HTML**, um **recurso nativo da conversa**, **em um primeiro momento**; e continua podendo fixar as respostas uma a uma num board (`MF-112`). Isto **corrige a consequência da `D-179`** ("a pessoa compartilha a conversa"); a decisão da `D-179`, de que o caminho fica salvo na conversa e não vai para um board, continua.
**Contexto:** ao escrever a documentação da `MF-119` (06/11/2026), a página repetiu da `D-179` que a pessoa "compartilha a conversa". O PO achou que o dono decidiu em 14/10/2026, na v1.xx, que a conversa nunca é compartilhada (a task "Análises Compartilhadas" foi cancelada), e que nenhuma mf da v2 descreve compartilhar conversa; abriu o `I-066`. O dono respondeu com um caminho fora das três opções: "em um primeiro momento talvez exportando pra pdf/html (recurso nativo de uma conversa)".
**Opções avaliadas:** sem pontuação: só fixar as respostas num board (recomendação do PO) · compartilhar a conversa (reverteria a decisão de 14/10/2026) · fixar o caminho inteiro num board (a opção B da `D-179`). **O dono escolheu uma quarta: a exportação.**
**Por que esta:** o arquivo sai do Horus e vai a quem a pessoa quiser, sem ninguém abrir a conversa dela, e a conversa continua pessoal. Abre-se mão de um jeito de mostrar o caminho dentro do Horus: ⚠️ o arquivo exportado sai do Horus, mostra o que o autor viu, e o Horus não controla quem o recebe depois.
**Fica de fora / adiado:** em que mf e em que versão a exportação entra (`I-067`); se o arquivo leva só a investigação ou qualquer conversa; se a exportação fica no rastro da Auditoria (`MF-116`); se é um botão das roles (`D-110`).
**Completa a `D-179`:** diz como a pessoa mostra o caminho a outras sem compartilhar a conversa.
**Hipóteses a validar:** 🔎 que o PDF ou o HTML baste para a reunião de resultado; 🔎 *(o dono disse "talvez")* que a exportação seja mesmo o primeiro jeito, antes de qualquer outro.
**Prova de valor:** a gestora termina a investigação, exporta a conversa em PDF e leva os passos e as fontes à reunião, sem abrir a conversa a ninguém.
**Reabrir quando:** a exportação não bastar para mostrar o caminho, ou o dono quiser rever o compartilhamento da conversa.

### D-248 · O owner liga, nas preferências da organização, a aprovação automática dos convites
Situação: 🟢 decidida (resposta do dono em 06/11/2026) · Data: 06/11/2026 · Versão: v2.0

**Decisão:** o **owner da organização** pode **ligar, nas preferências da organização, uma opção de aprovar automaticamente os convites** que os gestores pedem. Leitura do PO *(a confirmar com o dono)*: sem a opção ligada, o owner aprova cada convite, como já decidido (`D-071`); a opção é um dos tipos de aprovação que o owner liga ou desliga (`D-039`).
**Contexto:** ao escrever a documentação das mfs da v2.0 (06/11/2026), duas páginas (`MF-102`, `MF-103`) acharam uma lacuna: a `D-228` diz que todos os interruptores da organização nascem liberados, mas lista só três, e nenhum é a aprovação dos convites dos gestores. O PO perguntou se ela nasce automática ou manual. O dono respondeu com o desenho: "o owner pode configurar em preferências uma opção de aceitar automaticamente os convites".
**Opções avaliadas:** sem pontuação (dois caminhos sobre como a aprovação nasce): nasce manual, com o owner ligando a automática (recomendação do PO) · nasce automática. **O dono respondeu pelo desenho da preferência**, sem dizer como ela nasce; a leitura de que nasce desligada é do PO.
**Por que esta:** o owner decide quanto controle quer sobre quem ocupa um assento pago, e o gestor não reserva assento sem ele saber, a menos que o owner abra mão disso. Abre-se mão da entrada mais rápida da equipe no primeiro dia: ⚠️ o owner vira a espera, até ligar a opção.
**Fica de fora / adiado:** o nome e o lugar exato da opção nas preferências (desenho do arquiteto); se a opção vale também para as trocas de tipo de assento pedidas pelo gestor (`D-072`).
**Completa a `D-071` e a `D-228`:** diz como a aprovação do convite se liga e, pela leitura do PO, como nasce.
**Hipóteses a validar:** 🔎 que o owner ligue a opção quando a equipe crescer; 🔎 que a leitura de que ela nasce desligada seja a do dono.
**Prova de valor:** o gestor pede um convite e o owner o aprova; depois o owner liga a opção, e o convite seguinte sai sem aprovação, com o assento guardado.
**Reabrir quando:** os gestores reclamarem da espera pela aprovação, ou o dono quiser que a opção nasça ligada.

### D-247 · Os três pontos que dependiam do jurídico seguem como decididos, e a documentação e o setup indicam ao cliente consultar o jurídico dele
Situação: 🟢 decidida (resposta do dono em 06/11/2026; ele escolheu um caminho fora das opções propostas; a `D-274` tirou dele o ponto "a Maind vê o nome de quem ocupa o assento", e restam dois pontos) · Data: 06/11/2026 · Versão: v2.0

**Decisão:** ficam **mantidas** as três regras que dependiam da confirmação do jurídico da Maind: o **owner da organização lê as conversas de todos, sem aviso especial à pessoa** (`D-223`); **quem é excluído tem os registros apagados junto** (`D-210`); e a **Maind vê o nome de quem ocupa cada assento** (`D-157`). Em vez de esperar o jurídico da Maind, a **documentação e o setup (a implantação) de cada organização passam a indicar que o cliente deve consultar o jurídico dele** sobre esses três pontos.
**Contexto:** ao fechar as pendências para finalizar a documentação das mfs da v2.0 (06/11/2026), o PO perguntou se as confirmações do jurídico seguravam a finalização. O dono respondeu: "mantenha a decisão tomada e coloque um indicador de que possivelmente devemos consultar o jurídico do cliente durante o setup".
**Opções avaliadas:** sem pontuação (três caminhos sobre como tratar o que depende do jurídico): finalizar com o aviso "ainda em definição" (recomendação do PO) · esperar o jurídico · tirar as afirmações das páginas. **O dono escolheu um quarto caminho:** manter as regras e remeter a consulta ao jurídico do cliente, no setup.
**Por que esta:** o tratamento de dados pessoais depende do contrato e da política de cada cliente, e a consulta no setup põe a pergunta onde ela tem resposta. Abre-se mão de uma resposta única do jurídico da Maind antes da v2.0: ⚠️ se um cliente disser não, a regra pode ter de mudar para ele.
**Fica de fora / adiado:** o texto do indicador no setup e o lugar onde ele aparece no produto (desenho do arquiteto); o aviso de privacidade da instância, que segue com a `A-16` do documento 14; a conferência técnica da exclusão contra a guarda de seis meses do registro de acesso e as cópias de segurança, que segue na `P-044`, só do arquiteto.
**Fecha:** a `P-045`. **Reduz** a `P-044` ao lado técnico, do arquiteto.
**Hipóteses a validar:** 🔎 que a consulta ao jurídico do cliente aconteça no setup e não vire impedimento para fechar contrato; 🔎 que o indicador na documentação baste.
**Prova de valor:** a documentação da v2.0 traz o indicador nas páginas das mfs envolvidas, e o roteiro de implantação de uma organização pede ao cliente que consulte o jurídico dele sobre os três pontos.
**Reabrir quando:** um cliente ou o jurídico da Maind exigir o aviso à pessoa, o nome mascarado no relatório ou a guarda do registro de quem sai.

### D-246 · Definição macro da MF-105:IA sob controle da organização
Situação: ⚪ substituída em parte pelas `D-264` a `D-268` (a IA é sempre da organização, configurada no front do middleware; não há mais conexão da instância nem "nasce sem IA") · antes: 🟢 decidida (proposta do PO, confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** a `MF-105:IA sob controle da organização`, que era base herdada (`D-021`) e mudou com as `D-216` a `D-218`, `D-234` e `D-241`, fica definida assim:
- **O que é:** a conexão da organização com os modelos de IA que respondem às perguntas de análise e rodam os agentes. Há **duas origens de conexão**: a da **organização**, que o owner da organização cadastra e **a organização paga**; e a da **instância**, que o administrador da instância cadastra e **disponibiliza a uma ou mais organizações**, e **a Maind paga**; a organização não edita a da instância (`D-216`). A organização **nasce sem IA**, e o administrador disponibiliza uma ao criá-la (`D-217`). O **owner da organização escolhe os modelos** que a organização aceita, dentro das conexões que ela tem, e as roles liberam o modelo a cada pessoa (`D-110`).
- **Quem ganha:** o **owner da organização**, que decide qual IA a empresa usa e vê o consumo e o custo do que paga (`D-241`); a **Maind**, que decide a quem paga a IA e acompanha o custo pelo aviso (`D-153`); e as **pessoas**, que perguntam desde o primeiro dia.
- **Decisão que passa a ser possível:** a empresa usa o próprio contrato de IA e paga o consumo, ou usa o da Maind, sem trocar de produto.
- **Prova de valor:** o administrador cria a organização do cliente Alfa e disponibiliza a conexão da instância; a owner Carla faz a primeira pergunta de análise no primeiro dia. A organização do cliente Beta cadastra o próprio provedor de IA e vê o consumo e o custo dele. Quando a IA para, é avisado o dono da conexão (`D-218`).
- **Retorno para o negócio:** a Maind controla a quem paga a IA e atrai o cliente que já tem contrato de IA; o consumo de quem traz a própria IA não pesa no custo de atender (`D-216`).
- **O que não inclui:** o modo "tudo dentro", sem versão (`D-188`); o teto automático de custo, que não entra na v2.0 (`D-234`); o owner ver o consumo da conexão da instância (`D-241`); a pesquisa na web, que é da `MF-109`; o middleware na casa do contratante, que é a `MF-121`, na v2.1.
- **Depende de:** `MF-101:Administração da instância` (o administrador cadastra e disponibiliza a conexão da instância); `MF-102:Organizações, pessoas e papéis` (o owner da organização e as roles).
- **Valor:** **essencial**: sem IA conectada a organização não responde nenhuma pergunta de análise.
**Contexto:** as páginas de leitura da v2.0 (05/11/2026) mostraram que a `MF-105` seguia "só no mapa", como base herdada, mas seu comportamento mudou com a regra das duas origens da IA, e não havia uma definição que juntasse as decisões.
**Opções avaliadas:** definição direta, sem pontuação (o conteúdo já foi decidido nas decisões citadas).
**Por que esta:** junta num lugar só o que o owner, o administrador e as pessoas podem fazer com a IA, que estava espalhado em seis decisões.
**Fica de fora / adiado:** a forma de a conexão da instância chegar às organizações (`P-032`, do arquiteto); o preço do assento para quem traz a própria IA (`P-022`).
**Hipóteses a validar:** 🔎 que as organizações com contrato de IA próprio queiram usá-lo; 🔎 que a Maind queira disponibilizar a conexão da instância a todas, ao menos no começo.
**Reabrir quando:** o preço do assento for definido, ou o arquiteto devolver restrição à regra das duas origens.

### D-245 · Os boards de exemplo das organizações de demonstração ficam no espaço da organização, publicados
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-065`. Os **boards de exemplo** das organizações de demonstração (a rede de lojas e a frota, `D-233`) nascem **no espaço da organização, publicados** para todos que entram. Como, na v2.0, todas as pessoas da organização veem os mesmos dados (`D-163`), qualquer membro de exemplo vê tudo pronto.
**Completa a `D-232`:** os cenários das bases de demonstração; responde ao item `A-14` do documento 14.
**Contexto:** as páginas de leitura da v2.0 (05/11/2026) traziam a dúvida na `MF-118`; a hipótese era essa.
**Opções avaliadas:** sem pontuação (duas opções): **A. No espaço da organização, publicados** (escolhida; recomendação do PO) · B. Cada membro de exemplo tem os dele.
**Por que esta:** qualquer membro de exemplo vê os boards prontos, sem depender de quem os "criou". Abre-se mão de mostrar o board pessoal de um membro ouro: ⚠️ o que o membro ouro cria para si não aparece nos boards de exemplo.
**Fica de fora / adiado:** boards pessoais de exemplo, se o vendedor precisar mostrar o que o ouro cria.
**Hipóteses a validar:** 🔎 que o espaço da organização baste para a demonstração.
**Prova de valor:** o vendedor da Maind entra na organização da rede de lojas e vê os boards de vendas e de estoque já prontos e publicados.
**Reabrir quando:** o vendedor precisar mostrar o board pessoal de um membro ouro.

### D-244 · O agendamento ou o agente que espera o sim do owner aparece marcado "aguardando aprovação"
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-064`. Quando o owner liga a aprovação (`D-038`, `D-039`), o **agendamento ou o agente** que a pessoa cria **aparece na lista dela marcado "aguardando aprovação do owner"** e **não roda**. Quando o owner decide, a marca passa a **"ativo"** ou a **"recusado"**.
**Completa a `D-038` e a `D-039`:** que deixaram "o que o usuário vê enquanto espera" fora.
**Contexto:** as páginas de leitura da v2.0 (05/11/2026) traziam a dúvida na `MF-114`. Como a organização nasce com a aprovação automática (`D-228`), isso só acontece para o owner que a liga.
**Opções avaliadas:** sem pontuação (duas opções): **A. Aparece marcado "aguardando aprovação"** (escolhida; recomendação do PO) · B. Só aparece depois de aprovado.
**Por que esta:** a pessoa sabe por que nada sai e o que está pendente. Abre-se mão de nenhum estado novo: ⚠️ "aguardando aprovação" e "recusado" são estados a mais para construir e explicar.
**Fica de fora / adiado:** se a pessoa é avisada quando o owner decide, e por qual canal: é do desenho do arquiteto.
**Hipóteses a validar:** 🔎 que o owner dê conta de aprovar sem virar gargalo (a mesma hipótese da `D-038`).
**Prova de valor:** a gestora Carla salva um agendamento; ele aparece marcado "aguardando aprovação do owner"; o owner Marcos aprova, e a marca passa a "ativo".
**Reabrir quando:** os owners reclamarem do gargalo da aprovação.

### D-243 · Se a pesquisa na web não traz fato, a resposta sai com os dados da empresa e um aviso curto
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-063`. Quando o interruptor "pesquisar na web" está ligado e a **pesquisa não traz nenhum fato**, a resposta **sai com os dados da empresa** e traz **um aviso curto** dizendo que a pesquisa na web não trouxe fatos.
**Completa a `D-130`, a `D-162` e a `D-215`:** o fato da web entra com link e data (`D-130`), e a web é um interruptor (`D-215`); esta diz o caso sem fato.
**Contexto:** as páginas de leitura da v2.0 (05/11/2026) traziam a dúvida na `MF-109`.
**Opções avaliadas:** sem pontuação (três caminhos): **A. A resposta com os dados e um aviso curto** (escolhida; recomendação do PO) · B. A resposta sem aviso sobre a web · C. O Horus diz que não conseguiu responder.
**Por que esta:** a pessoa sabe que a web foi tentada e não achou, e não fica sem a parte da empresa; mantém a regra de confiança de mostrar limites. Abre-se mão de uma resposta mais limpa: ⚠️ uma linha a mais.
**Fica de fora / adiado:** o texto exato do aviso.
**Hipóteses a validar:** 🔎 que o aviso curto não incomode quem liga a pesquisa por hábito.
**Prova de valor:** a gestora Carla liga a pesquisa, e a busca não acha o índice do setor; a resposta traz o número da empresa e a frase "a pesquisa na web não trouxe fatos".
**Reabrir quando:** a mensagem confundir as pessoas.

### D-242 · O cartão do board guarda os fatos da web da resposta que o originou, com a data à vista, e não pesquisa de novo
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-062`. O **cartão do board** que nasce de uma resposta com **fato da web** **guarda os fatos que a resposta trouxe**, com o **link e a data à vista**, e **não pesquisa a web de novo** a cada atualização. Só os números da empresa se recalculam.
**Completa a `D-130` e a `D-162`:** o fato da web entra com link e data; esta diz o que o cartão faz com ele. Responde ao item `A-09` do documento 14.
**Contexto:** as páginas de leitura da v2.0 (05/11/2026) traziam a dúvida na `MF-109`: o cartão se recalcula, mas o fato da web veio de uma pesquisa.
**Opções avaliadas:** sem pontuação (três caminhos): **A. Guarda os fatos, com a data à vista** (escolhida; recomendação do PO) · B. Pesquisa de novo a cada atualização · C. O fato da web não entra no cartão.
**Por que esta:** sem custo de pesquisa a cada atualização e sem o fato mudar sozinho. Abre-se mão de o fato estar sempre atual: ⚠️ o fato envelhece, e a data à vista avisa quem olha o board.
**Fica de fora / adiado:** uma forma de o autor atualizar o fato à mão, se pedirem.
**Hipóteses a validar:** 🔎 que a data à vista baste para a pessoa saber que o fato pode estar velho.
**Prova de valor:** a gestora Carla fixa "vendas de outubro contra a inflação do mês"; o cartão se recalcula toda noite, e a inflação continua a de outubro, com o link e a data à vista.
**Reabrir quando:** os autores reclamarem de fatos velhos nos boards.

### D-241 · O owner da organização vê o consumo e o custo de IA só da conexão que a organização paga
Situação: ⚪ substituída em parte pela `D-267` (o owner passa a ver também o consumo da chave que a Maind dá) · antes: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-061`. O **owner da organização** vê o **consumo e o custo de IA da conexão da organização**, a própria, que a organização paga, como hoje. Da **conexão da instância** ele **não vê nada de IA**, nem consumo nem custo: quem acompanha é a Maind, pelo aviso de custo da administração (`D-153`).
**Completa a `D-214` e a `D-216`:** a visão de cobrança do owner mostra só a contagem de assentos (`D-214`), e a IA tem duas origens (`D-216`).
**Contexto:** as páginas de leitura da v2.0 (05/11/2026) traziam a dúvida na `MF-105`: depois de a Maind deixar de pagar a IA de todas as organizações (`D-216`), o que o owner vê do consumo.
**Opções avaliadas:** sem pontuação (três caminhos sobre o que o owner vê): **A. Só o que a organização paga** (escolhida; recomendação do PO) · B. O consumo das duas, sem o custo da Maind · C. O consumo e o custo das duas.
**Por que esta:** o owner vê o que paga, e o custo da Maind com a conexão da instância não aparece para o cliente (como na `D-214`). Abre-se mão de o owner saber quanto a equipe usa a IA da Maind: ⚠️ ele só sabe pelo uso que a Home da organização mostra (a medida de autonomia).
**Fica de fora / adiado:** o owner ver o consumo da conexão da instância, se os owners pedirem.
**Hipóteses a validar:** 🔎 que o painel de consumo da v1.xx sirva à conexão própria sem mudar.
**Prova de valor:** a organização do cliente Alfa tem a própria conexão de IA e vê o consumo e o custo dela; a organização do cliente Beta usa a conexão da instância e não vê nada de IA além da contagem de assentos e da Home.
**Reabrir quando:** owners que usam a conexão da instância pedirem para ver o consumo.

### D-240 · Quando outro serviço da organização para, é avisado o dono do serviço
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-057`. Quando um serviço da organização que **não é a IA** para (a conta de WhatsApp com a nota de qualidade rebaixada ou bloqueada, a fonte de dados que deixou de conectar, o e-mail recusado pelo servidor), é **avisado o dono do serviço**, como na IA (`D-218`): o **owner da organização**, para a **fonte de dados** e para o **WhatsApp próprio** da organização; o **administrador da instância**, para o **número de WhatsApp compartilhado da Maind** e para o **e-mail da instância**.
**Completa a `D-218`:** e responde ao resto do item `A-22` do documento 14.
**Contexto:** a `D-218` resolveu a IA; o `I-057` guardava os outros serviços que a organização usa.
**Opções avaliadas:** sem pontuação (três caminhos): **A. O dono do serviço** (escolhida; recomendação do PO) · B. Sempre o owner da organização, e o administrador quando o serviço é da instância · C. Ninguém; a falha aparece na resposta.
**Por que esta:** o aviso vai a quem pode consertar, igual à regra da IA. Abre-se mão de avisar o owner da organização quando o serviço é da Maind: ⚠️ quem usa o número da Maind vê o canal parar sem aviso ao owner.
**Fica de fora / adiado:** por qual canal o aviso chega (a área de avisos, o e-mail da instância) e a lista exata de situações: são do desenho do arquiteto (`A-22`).
**Hipóteses a validar:** 🔎 que o owner da organização perceba pela resposta quando o serviço da Maind para.
**Prova de valor:** a Meta bloqueia a conta de WhatsApp da organização do cliente Alfa; o owner dela é avisado. Se bloqueia o número da Maind, o administrador da instância é avisado.
**Reabrir quando:** owners que usam serviços da Maind reclamarem de não saber por que um canal parou.

### D-239 · A Home mostra as perguntas respondidas divididas por canal
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-060`. A **Home da organização** mostra a **divisão das perguntas de análise respondidas por canal**: a **conversa de análise** no app, a **Pergunta rápida** e o **WhatsApp**. O canal já é guardado em cada resposta, sem o texto (`D-133`). Quem vê a divisão segue a `D-238`.
**Completa a `D-133` e a `D-238`:** e responde ao pedido de uma divisão por canal da `MF-117`.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a dúvida na `MF-117`: o canal é guardado, mas nenhuma decisão dizia se a Home o mostra.
**Opções avaliadas:** sem pontuação (duas opções): **A. Sim, mostra a divisão por canal** (escolhida; recomendação do PO) · B. Não, só o total.
**Por que esta:** é o sinal de sucesso da Pergunta rápida e do WhatsApp, e o dado já é guardado. Abre-se mão de uma Home mais enxuta: ⚠️ um card a mais.
**Fica de fora / adiado:** outras divisões, como por área ou por horário.
**Hipóteses a validar:** 🔎 que a divisão por canal ajude o owner a decidir se mantém um canal ligado.
**Prova de valor:** o owner Marcos vê que, das 1.200 perguntas de outubro, 700 vieram da conversa, 300 da Pergunta rápida e 200 do WhatsApp.
**Reabrir quando:** os owners não usarem a divisão, ou pedirem outras.

### D-238 · O gestor vê a medida de autonomia da própria equipe
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** responde à primeira metade do `I-047`. Na Home da organização, o **owner** vê a **medida de autonomia** da organização inteira e a divisão por gestor e por pessoa (`D-133`); o **gestor** vê a medida e a divisão por pessoa **da equipe que ele gere**, como nos boards. Os **membros** (ouro, prata e bronze) não veem a divisão. O **comprador** acompanha pelo relatório da Maind, fora do produto (`D-132`).
**Completa a `D-133`:** que dava o detalhe só ao owner.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a dúvida na `MF-117`: se o gestor vê a medida da própria equipe e como o comprador a acompanha. A divisão por canal virou o `I-060`.
**Opções avaliadas:** sem pontuação (duas opções): **A. O gestor vê a da própria equipe** (escolhida; recomendação do PO) · B. Só o owner vê.
**Por que esta:** o gestor acompanha a adoção da equipe e age onde a qualidade cai. Abre-se mão de a contagem ficar só com quem decide: ⚠️ o gestor vê quanto cada pessoa da equipe pergunta.
**Fica de fora / adiado:** a divisão por canal (`I-060`); o que a medida da pessoa excluída mostra, que segue a `D-211` (o total fica como número sem dono).
**Hipóteses a validar:** 🔎 que ver a contagem por pessoa não leve a equipe a perguntar por pressão e não por necessidade.
**Prova de valor:** o gestor Pedro abre a Home e vê quantas perguntas a equipe dele teve em outubro e a qualidade das respostas; o owner Marcos vê a organização inteira.
**Reabrir quando:** as equipes reclamarem de ver a própria contagem exposta ao gestor.

### D-237 · O tema dos gráficos por organização fica na v2.0, como na v1.xx
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-046`. Cada organização **mantém o tema dos gráficos** (a paleta que ela escolhe), como na v1.xx, na base herdada das Respostas visuais (`MF-108`, `D-021`). A **interface e a marca seguem as da Maind** (`D-200`). O tema do contratante para o produto inteiro continua sem versão (`D-183`).
**Completa a `D-021` e a `D-200`:** a base herdada e a marca da Maind.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou que a página da `MF-108` trazia o tema da organização nos gráficos como base herdada, enquanto o tema do contratante estava sem versão.
**Opções avaliadas:** sem pontuação (duas opções): **A. Fica como na v1.xx** (escolhida; recomendação do PO) · B. Sai: os gráficos usam o tema da Maind.
**Por que esta:** nada a retirar da base herdada, e o cliente não perde o que já tem. Abre-se mão de uma identidade só: ⚠️ há gráficos com a paleta do cliente numa interface da Maind.
**Fica de fora / adiado:** o tema do contratante para a interface inteira, sem versão (`D-183`).
**Hipóteses a validar:** 🔎 que a paleta do cliente nos gráficos não destoe da interface da Maind.
**Prova de valor:** a organização do cliente Alfa continua com a paleta de azuis nos gráficos dela, dentro da interface da Maind.
**Reabrir quando:** a identidade única da Maind for prioridade, ou o tema do contratante voltar como mf própria.

### D-236 · A planilha de convites em lote é do owner da organização
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-059`. A **planilha de convites em lote** é uma ferramenta **só do owner da organização**. **Cada linha traz o tipo de assento e o gestor** da pessoa; o lote **reserva os assentos** como o convite individual (`D-078`); a **linha sem vaga do tipo fica de fora** (`D-070`). O **gestor convida um a um** e o owner aprova (`D-071`). Na v2.0 a planilha não tem as colunas de claims (`D-199`).
**Completa a `D-056` e a `D-071`:** e responde à letra (j) da `P-008` do lado do produto.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou que a `MF-102` dizia que "a planilha convida em lote" sem dizer quem a usa nem como o lote conversa com a aprovação e a reserva.
**Opções avaliadas:** sem pontuação (duas opções): **A. Só o owner da organização** (escolhida; recomendação do PO) · B. O owner e o gestor, com o owner aprovando o lote.
**Por que esta:** o lote é para implantar uma organização, e o owner não precisa aprovar o que ele mesmo envia: não há fluxo de aprovação de lote. Abre-se mão de o gestor convidar rápido: ⚠️ o gestor com equipe grande convida um a um.
**Fica de fora / adiado:** o gestor usar a planilha, se pedirem; o formato da planilha e a validação são do arquiteto (`P-008`, letra (j)).
**Hipóteses a validar:** 🔎 que a planilha do owner baste para a implantação de organizações grandes.
**Prova de valor:** a owner Carla envia uma planilha com 60 pessoas, cada uma com o tipo de assento e o gestor; os assentos são reservados, e as linhas sem vaga ficam de fora, com a lista do que faltou.
**Reabrir quando:** gestores com equipes grandes pedirem para usar a planilha.

### D-235 · O grupo dinâmico aceita o tipo de assento como regra
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** responde à primeira metade do `I-045`. A regra do **grupo dinâmico** (o que se atualiza sozinho, `D-029`) aceita, na v2.0, o **tipo de assento**: **owner, gestor, ouro, prata ou bronze**. A regra que já existia (o papel) fica compreendida por esta.
**Completa a `D-029` e a `D-056`:** e a `D-194`, que criou os cinco tipos de assento.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou que o grupo dinâmico seguia o papel (owner, gestor, membro), sem dizer se aceita os três tipos de membro. A segunda metade, a planilha de convites em lote, virou o `I-059`.
**Opções avaliadas:** sem pontuação (duas opções): **A. Sim, o tipo de assento vira regra** (escolhida; recomendação do PO) · B. Não, só o papel.
**Por que esta:** a owner monta "todo bronze" ou "todo ouro" e o grupo se atualiza quando o assento muda. Abre-se mão de nada relevante: ⚠️ o grupo passa a mudar de membros quando o tipo de assento de alguém muda.
**Fica de fora / adiado:** outras regras de grupo (por exemplo, por gestor ou por data de entrada), se pedirem.
**Hipóteses a validar:** 🔎 que o motor de grupos da v1.xx aceite o tipo de assento como atributo.
**Prova de valor:** a owner Carla monta o grupo "todo bronze" e agenda o PDF semanal para ele; quando alguém passa a bronze, entra no grupo sozinho.
**Reabrir quando:** os owners pedirem outras regras para o grupo.

### D-234 · O teto automático de custo da IA não entra na v2.0; fica o aviso de custo
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-044`. **Não há teto automático de custo da IA** na v2.0, nem por agente nem por organização. Ficam os **tetos técnicos por execução** do arquiteto (`ARQ-030`) e o **aviso de custo** por organização na administração da instância (`D-153`), que só avisa e não corta nada sozinho. Quem responde age à mão.
**Completa a `D-062` e a `D-153`:** a `D-062` deixou o teto "a pontuar"; a `D-153` criou o aviso de custo.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a dúvida na `MF-115`. Com a `D-216`, a Maind paga a IA só das organizações que usam a conexão da instância; nas demais, quem paga é a organização.
**Opções avaliadas:** sem pontuação (três caminhos): **A. Não entra; fica o aviso de custo** (escolhida; recomendação do PO) · B. Teto por organização · C. Teto por agente.
**Por que esta:** a v2.0 já é grande, e um teto automático pode pausar sem querer um agente importante. Abre-se mão de um freio automático: ⚠️ um agente com erro pode gastar até alguém ver o aviso de custo.
**Fica de fora / adiado:** o teto automático, por agente ou por organização; sem versão, volta se o custo surpreender.
**Hipóteses a validar:** 🔎 que o aviso de custo, somado aos tetos por execução, contenha um agente com erro a tempo.
**Prova de valor:** um agente da Carla dobra o consumo; o aviso de custo da organização aparece na administração da instância, e a Maind age à mão.
**Reabrir quando:** um agente com erro causar um custo que o aviso não conteve a tempo.

### D-233 · A DRE de usina sai da vitrine da v2.0: ficam a rede de lojas e a frota
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-058`. A vitrine das bases de demonstração (`MF-118`) tem, na v2.0, **só duas organizações de exemplo**: a **rede de lojas** (McDonald's) e a **frota** (Global Fleet). A **DRE de usina sai** da vitrine da v2.0.
**Completa a `D-232` e a `D-021`:** e responde ao item `A-14` do documento 14.
**Contexto:** a página da `MF-118` dizia que só duas organizações de exemplo chegam à v2.0, sem dizer se a DRE de usina segue na vitrine.
**Opções avaliadas:** sem pontuação (duas opções): **A. Sai da v2.0; ficam as duas organizações** (escolhida; recomendação do PO) · B. Fica como terceira organização de exemplo.
**Por que esta:** menos organizações para preparar e manter com os cenários novos (`D-232`). Abre-se mão de um exemplo do ramo de energia: ⚠️ o vendedor que visitar um cliente desse ramo mostra a rede de lojas ou a frota.
**Fica de fora / adiado:** a DRE de usina volta à vitrine se um cliente do ramo pedir; sem versão.
**Hipóteses a validar:** 🔎 que duas organizações de exemplo cubram as demonstrações da v2.0.
**Prova de valor:** a vitrine da v2.0 tem a rede de lojas e a frota, ambas com os cenários novos.
**Reabrir quando:** houver cliente do ramo de energia que peça um exemplo próprio.

### D-232 · Cada prova de valor da v2.0 ganha um cenário nas bases de demonstração
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** responde à parte dos cenários do `I-043`. As **bases de demonstração** (`MF-118`) ganham, na v2.0, **um cenário para cada prova de valor da v2.0**: os agentes, o WhatsApp, o rastro da Auditoria, a faixa de avisos e números, a Pergunta rápida e os assentos prata e bronze, além do que a base herdada já mostra. O **PO escreve a lista de cenários, mf a mf**, a partir das provas de valor das 18 mfs, na página da `MF-118`. A demonstração da segurança por pessoa continua fora (`D-199`).
**Completa a `D-021` e a `D-199`:** a base herdada e a retirada da demonstração da segurança.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou que a página da `MF-118` prometia cenários dos agentes, do WhatsApp e do rastro, enquanto o inventário só dizia "base herdada, sem a demonstração da segurança por pessoa".
**Opções avaliadas:** sem pontuação (três caminhos): **A. Um cenário para cada prova de valor da v2.0** (escolhida; recomendação do PO) · B. Só o que o cliente vê primeiro (chat, boards e faixa) · C. As bases ficam como na v1.xx.
**Por que esta:** o vendedor demonstra tudo o que a v2.0 promete, em dado fictício, inclusive a parte de acompanhar e avisar. Abre-se mão de preparo barato: ⚠️ preparar dado e conta de exemplo, inclusive de WhatsApp, dá trabalho.
**Fica de fora / adiado:** a DRE de usina na vitrine (`I-058`); a lista detalhada de cenários (o PO a escreve na página); a leitura 🔎 de que os boards de exemplo ficam publicados no espaço da organização, que segue como hipótese da página.
**Hipóteses a validar:** 🔎 que seja viável ter uma conta de WhatsApp de exemplo; 🔎 que, com o SaaS numa instância só (`D-193`), as organizações de exemplo vivam na instância da Maind e a regra de "nunca na instância do contratante, salvo pedido" perca o sentido.
**Prova de valor:** o vendedor da Maind mostra, na organização de exemplo, um agente que avisa quando as vendas do Sul caem 10%, o envio por e-mail e a Auditoria registrando a entrega.
**Reabrir quando:** o trabalho de preparar os cenários pesar, e a opção de mostrar só o que o cliente vê primeiro voltar à mesa.

### D-231 · O aviso de abertura da Auditoria tem texto padrão do Horus e não pede ciência no primeiro acesso
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-042`. O Horus traz um **texto padrão** do aviso de que a Auditoria registra **quem abriu o quê** (`D-090`), já **publicado**, que o **owner da organização pode trocar** pelo dele. A pessoa o encontra por um **link**; o **primeiro acesso não pede ciência** (não há tela de "li e aceito"). Assim, a abertura nunca é registrada sem um aviso publicado.
**Completa a `D-090` e a `ARQ-043`:** e responde ao item `A-30` do documento 14. A exclusão da conta ficou resolvida pela `D-210`.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a mesma dúvida em duas páginas (`MF-112` e `MF-116`): onde fica o documento, se há texto padrão e se o primeiro acesso pede ciência.
**Opções avaliadas:** sem pontuação (três caminhos): **A. Texto padrão, sem pedir ciência** (escolhida; recomendação do PO) · B. Texto padrão e ciência no primeiro acesso · C. Sem texto padrão: o owner publica o dele.
**Por que esta:** a abertura é sempre registrada com um aviso publicado, sem uma tela de aceite para todas as pessoas. Abre-se mão da prova de que a pessoa leu: ⚠️ o Horus não consegue provar que ela foi avisada.
**Fica de fora / adiado:** o texto jurídico do aviso e o lugar exato do link, que são do jurídico da Maind e do arquiteto; a ciência no primeiro acesso, se o jurídico exigir.
**Hipóteses a validar:** 🔎 que o aviso sem ciência baste diante da proteção de dados pessoais (`P-045`, do jurídico, trata de assunto parecido).
**Prova de valor:** o gestor Pedro abre um board; no rodapé do Horus há o link do aviso padrão, e a owner Carla pode trocar o texto pelo da empresa dela.
**Reabrir quando:** o jurídico da Maind ou de um cliente exigir a ciência da pessoa.

### D-230 · No cartão descrito em texto, o autor vê o resultado antes de salvar, e salvar é aprovar
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-056`. No **cartão do board escrito por descrição**, o Horus **mostra o resultado ao autor antes de salvar**, e **salvar é a aprovação**, sem um estado à parte (rascunho, aguardando aprovação). A regra é a mesma para todo cartão do editor único: o de resposta e o de descrição.
**Completa a `D-057` e a `D-058`:** o board e o relatório de hoje se fundem num editor só; esta diz como a região por descrição entra, e responde ao item `A-23`, 2, do documento 14.
**Contexto:** no relatório de hoje, cada região de dado só fica pronta quando o gestor aprova a receita (a consulta montada), que nunca vai ao navegador; o cartão do board nasce de uma resposta já calculada, sem aprovação.
**Opções avaliadas:** sem pontuação (três caminhos sobre a aprovação): **A. Vê o resultado e salvar é aprovar** (escolhida; recomendação do PO) · B. Aprovação à parte, como no relatório de hoje · C. Sem aprovação, vai direto ao board.
**Por que esta:** uma regra só para o editor, sem estado novo para construir e explicar. Abre-se mão do passo de conferência separado: ⚠️ o autor pode salvar sem conferir direito o que o Horus montou.
**Fica de fora / adiado:** um aviso quando o Horus não tiver certeza do que montou, se o arquiteto propuser.
**Hipóteses a validar:** 🔎 que ver o resultado antes de salvar baste para o autor perceber uma consulta errada.
**Prova de valor:** o gestor Pedro descreve "margem por loja no trimestre", vê o gráfico montado e, ao salvar, o cartão passa a valer no board, sem outra etapa.
**Reabrir quando:** cartões com consulta errada chegarem a boards publicados.

### D-229 · O board maior que a folha vira um PDF de uma página só, do tamanho do board
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; a ideia veio dele, "não dá pro tamanho da folha do PDF aumentar?", e virou a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** responde à primeira metade do `I-041`. O **PDF de um board maior que a folha** tem **uma página só, do tamanho do board**: a folha **cresce** até caber, sem reduzir o board e sem cortar cartão. Completa a `D-057` (todo board, de qualquer tamanho, pode ser impresso em PDF a partir da mesma montagem).
**Contexto:** a `D-057` deixou de fora como um board grande vira PDF (item `A-23`, 1, do documento 14). O dono perguntou se o tamanho da folha podia aumentar; a arquitetura já registra que a impressão sem tela, feita pelo navegador, imprime qualquer tamanho (`ARQ-007`).
**Opções avaliadas:** sem pontuação (três caminhos): **A. A folha cresce até caber o board** (escolhida; sugestão do dono) · B. Várias folhas A4, sem cortar cartão (recomendação do PO antes da sugestão) · C. Uma folha A4, reduzida para caber.
**Por que esta:** o PDF fica legível na tela e no celular, como uma foto fiel do board, sem reduzir nem cortar. Abre-se mão do formato A4: ⚠️ impresso, a impressora reduz a página, e uma página muito maior que a folha pode ficar pequena no papel.
**Fica de fora / adiado:** um limite para o tamanho da página (um board enorme) e o aviso ao autor quando o PDF passar do teto de tamanho do canal (`D-227`).
**Hipóteses a validar:** 🔎 que a leitura em tela, a principal, baste; 🔎 que um board muito alto continue legível no celular.
**Prova de valor:** o board de vendas da Carla, com 12 cartões, sai num PDF de uma página só, do tamanho dele, com todos os cartões legíveis.
**Reabrir quando:** os autores pedirem impressão em A4 ou o PDF ficar grande demais para os canais.

### D-228 · A organização nasce com os interruptores liberados, e o owner restringe
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-039`. Quando uma organização é criada, **todos os interruptores nascem liberados** e **o owner da organização restringe o que quiser**: (1) a **aprovação dos contatos** dos conectores nasce **automática** (`D-038`, `D-039`); (2) o **gestor pode publicar** boards (`D-042`); (3) a **role padrão** nasce com **tudo ligado**, inclusive o botão do WhatsApp (`D-112`), que só funciona depois que o owner liga o canal (`D-097`).
**Completa a `D-038`, a `D-039`, a `D-042` e a `D-112`:** diziam o que cada interruptor faz; esta diz como ele nasce.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a dúvida de como nascem os interruptores em quatro páginas (`MF-112` a `MF-115`); a role padrão foi decidida antes de existirem o botão do WhatsApp e o dos conectores de saída.
**Opções avaliadas:** sem pontuação (três caminhos sobre o nascimento): **A. Todos liberados; o owner restringe** (escolhida; recomendação do PO) · B. Todos travados; o owner libera · C. Os que custam nascem travados.
**Por que esta:** tudo funciona no primeiro dia e a regra é uma só. Abre-se mão de segurança por padrão: ⚠️ o owner que não olhar as configurações deixa tudo aberto, inclusive o que gera custo, que só gasta depois que o owner liga o canal.
**Fica de fora / adiado:** uma tela de revisão das configurações no primeiro acesso do owner.
**Hipóteses a validar:** 🔎 que os owners revisem as configurações depois do primeiro dia.
**Prova de valor:** a Maind cria a organização do cliente Alfa; o gestor Pedro, convidado pela owner Carla, já publica um board e cadastra o contato dele sem esperar aprovação.
**Reabrir quando:** um cliente reclamar de ter começado com tudo liberado, ou o custo de um canal ligado por padrão surpreender.

### D-227 · O artefato que não cabe no canal não é entregue naquele canal, e o autor é avisado
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-055`. Quando o **artefato não cabe no canal** (um PDF maior que o anexo do e-mail, um alerta maior que a mensagem do WhatsApp), o Horus **não o entrega naquele canal**, **não o corta nem o altera** e **avisa o autor**, como numa falha (`D-226`). O conector segue só transportando (`D-035`).
**Completa a `D-035` e a `D-226`:** e responde ao item `A-19` do documento 14.
**Contexto:** segunda metade do `I-038`: a revisão das mfs da v2.0 (05/11/2026) achou a dúvida nas páginas dos conectores (`MF-113`) e dos agentes (`MF-115`).
**Opções avaliadas:** sem pontuação (três caminhos sobre o artefato grande): **A. Não entrega naquele canal e avisa o autor** (escolhida; recomendação do PO) · B. Entrega um link para abrir no Horus · C. Reduz o artefato para caber.
**Por que esta:** o conector não passa a alterar o artefato, e ninguém recebe um PDF cortado. Abre-se mão de o destinatário receber algo: ⚠️ ele fica sem o PDF até o autor reduzir o board ou o texto do alerta.
**Fica de fora / adiado:** o tamanho máximo de cada canal e o texto do aviso ao autor: são do desenho do arquiteto; o link para o Horus, se os autores pedirem.
**Hipóteses a validar:** 🔎 que poucos artefatos passem do limite dos canais.
**Prova de valor:** o PDF do board de fim de ano passa do anexo do e-mail; o Horus não o envia por e-mail, e a gestora Carla recebe o aviso.
**Reabrir quando:** os autores reclamarem de artefatos que não chegam, e a opção do link voltar à mesa.

### D-226 · Quando a execução de um agendamento ou agente falha, só o autor recebe o aviso
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** responde à primeira metade do `I-038`. Quando a **execução de um agendamento ou de um agente falha** (erro ou passou do teto da execução), os **destinatários não recebem nada** naquela rodada e **só o autor recebe o aviso de falha**. A **próxima rodada segue no horário normal**.
**Completa a `D-060` e a `D-062`:** e responde ao item `A-10` do documento 14.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a dúvida nas páginas dos agendamentos e dos agentes (`MF-114` e `MF-115`). A segunda metade do `I-038`, o artefato que não cabe no canal, virou o `I-055`.
**Opções avaliadas:** sem pontuação (duas opções): **A. Só o autor recebe o aviso** (escolhida; recomendação do PO) · B. O autor e os destinatários recebem aviso.
**Por que esta:** ninguém recebe um PDF quebrado ou uma mensagem confusa, e quem pode consertar fica sabendo. Abre-se mão de avisar os destinatários: ⚠️ eles ficam sem o PDF e não sabem por quê.
**Fica de fora / adiado:** por qual canal o aviso chega ao autor; quantas tentativas o Horus faz antes de desistir de uma rodada; o tamanho do alerta pelo WhatsApp: são do desenho do arquiteto.
**Hipóteses a validar:** 🔎 que o autor veja o aviso a tempo de consertar antes da próxima rodada.
**Prova de valor:** o PDF de segunda da gestora Carla falha; os 8 destinatários não recebem nada e a Carla recebe o aviso de falha; na segunda seguinte, o PDF sai normalmente.
**Reabrir quando:** os destinatários reclamarem de não saber por que o relatório não veio.

### D-225 · Quem escreve no WhatsApp sem poder conversar recebe uma resposta fixa que aponta para o app
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-037`. Quem escreve para o número de WhatsApp do Horus e **não pode conversar** (sem o número ligado, sem o botão do WhatsApp na role ou como membro bronze) recebe **uma resposta fixa, sem dado nenhum**, que diz que o Horus não conversa com aquele número e **aponta para o app** (ligar o número ou pedir acesso ao owner). A mesma mensagem vale para todos esses casos.
**Completa a `D-094` e a `D-203`:** e responde ao item `A-18` do documento 14.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a dúvida na `MF-111`: o bronze não pergunta, e o canal só abre a quem tem o número ligado e o botão. O bronze, porém, recebe PDFs pelo WhatsApp (`D-079`), então pode responder ao que recebeu.
**Opções avaliadas:** sem pontuação (três caminhos sobre a resposta): **A. Uma resposta fixa que aponta o app** (escolhida; recomendação do PO) · B. Silêncio · C. Resposta só a quem tem número ligado.
**Por que esta:** ninguém fica sem entender por que o Horus não respondeu. Abre-se mão de não responder a números desconhecidos: ⚠️ um número que ninguém ligou também recebe a mensagem, que não revela dado nenhum.
**Fica de fora / adiado:** o texto exato da mensagem e se ela cabe nas mensagens-padrão que a Meta aprova: são do desenho do arquiteto.
**Hipóteses a validar:** 🔎 que a mensagem fixa seja suficiente para o bronze entender; 🔎 que o custo da resposta fixa seja desprezível.
**Prova de valor:** o Rui, membro bronze, escreve "vendas de outubro?" no WhatsApp e recebe a mensagem fixa que diz que o Horus não conversa por ali e aponta para o app.
**Reabrir quando:** números desconhecidos gerarem custo ou abuso, ou o bronze pedir uma resposta diferente.

### D-224 · No WhatsApp, o telefone da pessoa fica ligado a uma organização por vez; é o mesmo número da conversa e dos avisos
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-036`. O **telefone de uma pessoa fica ligado a uma organização por vez**: ligá-lo numa organização **move a ligação** das outras, com **aviso à pessoa**. Assim, no número de WhatsApp compartilhado da Maind, o Horus sempre sabe qual organização responde (`D-097.2`). E a pessoa tem **um número só**, que serve à **conversa e aos avisos** dos conectores (`D-094.2`); não há um número para cada uso.
**Completa a `D-094` e a `D-097`:** e responde ao item `A-17` do documento 14.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a dúvida em três páginas (`MF-111`, `MF-113` e `MF-118`): o Horus reconhece a organização pelo número de quem escreve, e uma pessoa pode estar em duas organizações. A primeira metade (um número só) já estava respondida pela leitura `D-094.2`, confirmada.
**Opções avaliadas:** sem pontuação (três caminhos sobre quem está em duas organizações): **A. O número fica numa organização por vez** (escolhida; recomendação do PO) · B. O Horus pergunta a organização na conversa · C. Com duas organizações, só o número próprio.
**Por que esta:** o Horus sempre sabe qual organização responde, sem menu dentro do WhatsApp. Abre-se mão de a pessoa usar o mesmo telefone nas duas ao mesmo tempo: ⚠️ o consultor que atende duas organizações religa o número ao trocar de uma para outra.
**Fica de fora / adiado:** o texto do aviso à pessoa e a mensagem que ela recebe no WhatsApp quando o número foi movido: são do desenho do arquiteto.
**Hipóteses a validar:** 🔎 que poucas pessoas estejam em duas organizações no número da Maind; 🔎 que religar o número seja simples.
**Prova de valor:** o consultor Davi liga o telefone na organização Beta; a ligação com a Alfa sai, ele é avisado, e as perguntas dele no WhatsApp passam a ser respondidas pela Beta.
**Reabrir quando:** muitas pessoas estiverem em duas organizações e reclamarem de religar o número.

### D-223 · O owner da organização continua lendo as conversas de todos, sem aviso especial à pessoa
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, contra a recomendação do PO, que era ler e avisar a pessoa) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-035`. O **owner da organização continua lendo as conversas de todas as pessoas** da organização, como na v1.xx, e **nada de especial é mostrado à pessoa** sobre isso: não há aviso de privacidade que diga que o owner lê.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a dúvida em duas páginas (`MF-102` e `MF-107`; item `A-16`, 2, do documento 14): a regra veio da v1.xx sem decisão para a v2.0 e toca a proteção de dados pessoais.
**Opções avaliadas:** sem pontuação (três caminhos sobre a leitura): A. Lê, e a pessoa é avisada (recomendação do PO) · **B. Lê, sem aviso especial** (escolhida pelo dono) · C. O owner não lê as conversas.
**Por que esta:** mantém o que a v1.xx faz e não cria tela nem texto novo. Abre-se mão da transparência: ⚠️ a pessoa não sabe que o owner lê o que ela pergunta, o que cria risco com a proteção de dados pessoais, e quem pergunta sobre algo sensível pode se sentir vigiado quando descobrir.
**Fica de fora / adiado:** um aviso de privacidade sobre a leitura; o aviso de abertura da Auditoria é outra coisa (`I-042`).
**Hipóteses a validar:** 🔎 que ler as conversas sem aviso especial seja aceitável diante da proteção de dados pessoais (`P-045`, do jurídico); 🔎 que as pessoas não deixem de perguntar por isso.
**Prova de valor:** a owner Carla abre a lista de conversas da organização e lê a conversa de um membro; o membro não vê nenhum aviso sobre isso.
**Reabrir quando:** o jurídico da Maind exigir o aviso, ou um cliente o pedir, ou as perguntas dos membros caírem depois que eles descobrirem a leitura.

### D-222 · Conta como pergunta de análise respondida só a que trouxe dado da empresa ou fato da web
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-034`. Na **medida de autonomia** (`D-133`), conta como **pergunta de análise respondida** só a resposta que **trouxe dado da empresa ou fato da web, com resultado**. **Não contam**: a consulta que volta **vazia**, a **falha** (`D-004`) e a **conversa sem dado nem web**. Vale na conversa, na Pergunta rápida, salva ou não (`D-087`), e no WhatsApp.
**Completa a `D-004` e a `D-133`:** e responde ao item `A-08` do documento 14.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a mesma dúvida em três páginas (`MF-107`, `MF-110` e `MF-117`), cada uma com uma lista de casos diferente.
**Opções avaliadas:** sem pontuação (três caminhos sobre o que conta): **A. Só a que trouxe dado ou web** (escolhida; recomendação do PO) · B. Conta também a consulta vazia · C. Conta tudo o que o Horus respondeu.
**Por que esta:** o número mede análise de verdade e não infla com "oi, tudo bem?". Abre-se mão de contar uma resposta correta de "não há vendas nesse período": ⚠️ uma pergunta bem respondida, mas sem dado, não entra na medida.
**Fica de fora / adiado:** nada.
**Hipóteses a validar:** 🔎 que o número sem as respostas vazias continue refletindo o uso; 🔎 que o motor consiga distinguir a consulta vazia da que tem resultado.
**Prova de valor:** o Rui pergunta "vendas por região em outubro" e a resposta com dados conta; pergunta "vendas do Sul em 2019", que volta vazia, e "oi, tudo bem?", e nenhuma das duas conta.
**Reabrir quando:** a medida de autonomia parecer baixa demais para o cliente, ou a consulta vazia ficar frequente.

### D-221 · Só o dono do board fixa uma resposta nele; não é um botão das roles
Situação: 🟢 decidida (resposta do dono em 05/11/2026 à pergunta do `I-033`, fora das opções oferecidas; o texto dele vale como veio: "O dono do board") · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-033`. **Fixar uma resposta num board** (guardar o gráfico ou a tabela da conversa no painel) é permitido **só ao dono do board**, o autor dele. Como a prata e o bronze não criam boards (`D-203`), eles não têm board em que fixar e não veem o controle. **Não é um botão das roles**: elas continuam com nove botões. Vale na conversa e na Pergunta rápida, que herda o controle (`D-088`).
**Completa a `D-203` e a `D-044`:** só o autor edita o board (`D-044`); fixar é editá-lo.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a mesma dúvida em três páginas (`MF-102`, `MF-108`, `MF-110`): o item `A-24` do documento 14 perguntava se fixar é um botão da role ou segue o tipo de assento.
**Opções avaliadas:** sem pontuação (a resposta veio fora das opções). Oferecidas: segue o tipo de assento (recomendação do PO) · vira o décimo botão das roles. A resposta se aproxima da primeira, com a regra de quem pode: o dono do board.
**Por que esta:** fixar é editar o board, e quem edita um board é só o autor; assim não há botão novo nem regra a mais. Abre-se mão de fixar no board de outra pessoa: ⚠️ um gestor não consegue fixar uma resposta num board que o owner ou outro gestor criou.
**Fica de fora / adiado:** fixar num board de outra pessoa.
**Hipóteses a validar:** 🔎 que "dono do board" seja o autor do board; no espaço da organização, o owner da organização (`D-048`).
**Prova de valor:** a gestora Carla fixa uma resposta no board dela; o Rui, membro prata, vê a resposta mas não vê o controle de fixar.
**Reabrir quando:** as pessoas pedirem para fixar num board de outra pessoa.

### D-220 · O teto do nível de inferência é o de cada fonte; a role só pode baixá-lo
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-032`. O **teto do nível de inferência é o de cada fonte de dados**, como na v1.xx: quem conhece o dado o define na fonte. O botão de nível máximo da **role** (`D-110`) pode **baixar** esse teto para a pessoa, **nunca subir**; vale sempre o **menor**. Não há um teto único da organização, e o "teto da organização" de que as roles falam é o teto das fontes. O agente segue livre do teto (`D-024`).
**Completa a `D-111` e a `D-024`:** e responde ao item `A-13` do documento 14.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a mesma dúvida em três páginas de leitura (`MF-102`, `MF-104` e `MF-107`): as roles falavam num teto da organização, e o teto, hoje, é de cada fonte.
**Opções avaliadas:** sem pontuação (três caminhos sobre onde mora o teto): **A. Teto de cada fonte, e a role só baixa** (escolhida; recomendação do PO) · B. Um teto único da organização · C. Os dois tetos, vale o menor.
**Por que esta:** nada novo para construir e o dono do dado continua mandando no dado. Abre-se mão de um botão único "nunca passe do nível 2" para a organização inteira: ⚠️ para limitar tudo, o owner baixa a role, não a fonte.
**Fica de fora / adiado:** um teto único da organização, se os owners pedirem.
**Hipóteses a validar:** 🔎 que baixar pela role baste para o owner que quer limitar a organização inteira.
**Prova de valor:** o banco de vendas aceita até o nível 3 e o financeiro, até o 1; a role "Comercial" baixa o limite para o 2; o grupo Comercial recebe o nível 2 nas vendas e o 1 no financeiro.
**Reabrir quando:** owners pedirem um teto único para a organização inteira.

### D-219 · O modelo semântico é escrito fora do Horus e o owner da organização o carrega
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-031`. O **time de dados**, do cliente ou da Maind na implantação, **escreve o modelo semântico fora do Horus** e entrega o arquivo; o **owner da organização o carrega** na organização, como dono do modelo (`D-013`). Ninguém de fora entra na organização para escrevê-lo, nenhum assento novo é criado para isso, e a Maind segue sem ver os dados das conexões (`D-193`).
**Completa a `D-083.1` e a `D-193`:** dizem que o time de dados escreve o modelo e que a Maind não vê os dados das conexões; esta diz como as duas coisas convivem.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou que a `MF-104` listava o time de dados entre quem usa a mf, sem dizer com que assento ele escreve o modelo.
**Opções avaliadas:** sem pontuação (três caminhos sobre onde se escreve): **A. Fora do Horus; o owner carrega o arquivo** (escolhida; recomendação do PO) · B. O time de dados entra como owner da organização · C. Um acesso novo, só para o modelo.
**Por que esta:** mantém a regra de que a Maind não vê os dados do cliente e não cria papel nem assento. Abre-se mão de o time de dados testar o modelo contra os dados reais dentro do Horus: ⚠️ quem escreve o modelo só o vê funcionando depois que o owner o carrega.
**Fica de fora / adiado:** um acesso de modelagem, se os times de dados pedirem; o formato do arquivo e o carregamento são do arquiteto.
**Hipóteses a validar:** 🔎 que escrever o modelo sem testá-lo nos dados reais não atrase a implantação.
**Prova de valor:** a analista Bia, da Maind, entrega o arquivo do modelo; a owner Carla o carrega na organização, e o Horus passa a responder com as definições da empresa.
**Reabrir quando:** as implantações atrasarem por falta de teste dentro do Horus.

### D-218 · Quando a IA para, é avisado o dono da conexão
Situação: ⚪ substituída em parte pela `D-268` (não há mais conexão da instância: o owner da organização é sempre avisado, e o time da Maind também, se a chave é da Maind) · antes: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-030`. Quando a IA de uma organização para (chave recusada ou falta de crédito), é **avisado o dono da conexão**: o **owner da organização**, se a conexão é da organização, e o **administrador da instância** (a Maind), se é da instância (`D-216`). O owner de uma organização que usa a conexão da instância não recebe aviso.
**Completa a `D-216`:** dá a cada conexão o responsável por saber que ela parou.
**Contexto:** o item `A-22` do documento 14 partia de que a chave, a conta e a fonte eram da organização; a `D-216` mostrou que a conexão pode ser da instância.
**Opções avaliadas:** sem pontuação (duas opções): **A. O dono da conexão** (escolhida; recomendação do PO) · B. O dono da conexão e, sempre, o owner da organização.
**Por que esta:** o aviso vai a quem pode consertar, sem ruído para os outros. Abre-se mão de avisar o owner da organização quando a conexão é da instância: ⚠️ ele vê a IA parar sem ter sido avisado.
**Fica de fora / adiado:** por qual canal o aviso chega (a área de avisos, o e-mail da instância) e o que a pessoa vê na tela quando a IA para: são do desenho do arquiteto (`A-22`).
**Hipóteses a validar:** 🔎 que a pessoa que perguntou entenda que a IA está indisponível, mesmo sem aviso ao owner.
**Prova de valor:** o crédito da conexão da instância acaba, e o administrador da instância é avisado; nenhum owner de organização recebe o aviso.
**Reabrir quando:** owners de organizações que usam a conexão da instância reclamarem de não saber por que a IA parou.

### D-217 · A organização nasce sem IA; o administrador da instância disponibiliza uma conexão ao criá-la
Situação: ⚪ substituída em parte pela `D-266` (a IA é configurada no middleware, e não disponibilizada pelo administrador da instância) · antes: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-054`. Uma organização **nasce sem IA**. No mesmo passo em que **cria a organização e libera os assentos** (`D-146`, `D-080`), o **administrador da instância escolhe se disponibiliza** a ela uma conexão de IA da instância (`D-216`). A organização que traz a própria IA cadastra a conexão dela depois, pelo owner da organização.
**Completa a `D-216` e a `D-146`:** criar a organização passa a incluir a escolha da conexão de IA da instância.
**Contexto:** a `D-216` criou a conexão da instância, disponibilizada por organização, sem dizer o que a organização recém-criada tem.
**Opções avaliadas:** sem pontuação (três caminhos sobre a origem da primeira IA): **A. O administrador disponibiliza ao criar** (escolhida; recomendação do PO) · B. Nasce com a conexão padrão da instância · C. A organização traz a própria.
**Por que esta:** a Maind decide, caso a caso, a quem paga a IA, no passo em que já cria a organização. Abre-se mão do funcionamento automático no primeiro dia: ⚠️ se o administrador esquecer de disponibilizar uma conexão, o owner da organização não consegue fazer a primeira pergunta de análise até ele fazer ou até o owner cadastrar a dele.
**Fica de fora / adiado:** o aviso, ao administrador, de uma organização sem IA nenhuma; a forma de a conexão chegar à organização (`P-032`, do arquiteto).
**Hipóteses a validar:** 🔎 que o administrador não esqueça o passo da IA; 🔎 que uma organização sem IA seja visível na administração.
**Prova de valor:** o administrador da instância cria a organização do cliente Alfa, libera 10 assentos e disponibiliza a conexão de IA da instância; a owner Carla faz a primeira pergunta de análise no primeiro dia.
**Reabrir quando:** organizações novas ficarem sem IA por esquecimento, e a opção de uma conexão padrão voltar à mesa.

### D-216 · A IA pode ser da organização ou da instância: a Maind não paga a IA 100% das vezes
Situação: ⚪ substituída em parte pela `D-266` (a conexão da instância deixou de existir; sobra a IA da organização, e quem a paga fica no `I-084`) · antes: 🟢 decidida (resposta do dono em 05/11/2026 à pergunta do `I-029`, fora das opções oferecidas; ele corrigiu a premissa da `D-159`; o texto dele vale como veio: "Não é verdade que é a Maind que vai pagar o modelo 100% das vezes. Será possível o owner da org cadastrar o provedor de IA desejado na ORG. Será possível também cadastrar um provedor de IA no nível da Instância, e via owner da instância disponibilizar ou não para uma ou mais ORGs. No entanto uma conexão de IA de instância compartilhada com a ORG não permite edição em nível de Org.") · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-029`. Há **duas origens de conexão de IA**: (1) a **conexão da organização**, que o **owner da organização** cadastra com o provedor de IA que quiser; **quem paga é a organização**; (2) a **conexão da instância**, que o **owner da instância** (a Maind) cadastra no nível da instância e **disponibiliza ou não a uma ou mais organizações**; **quem paga é a Maind**. Uma conexão da instância compartilhada com a organização **não pode ser editada no nível da organização**.
**Substitui em parte a `D-159`:** que dizia que a Maind paga a IA de todas as organizações e a embute no preço do assento, deixando a conta própria da organização para depois. Isso vale só para as organizações que usam a conexão da instância; a conta própria da organização existe na v2.0.
**Responde ao `I-029`:** quem define os modelos que a organização pode aceitar: ficam os modelos das conexões que ela tem, as dela e as que a instância lhe disponibiliza. A Maind controla o que paga decidindo o que disponibiliza; não limita o que a organização paga com a conexão própria.
**Contexto:** a pergunta do `I-029` (a Maind limita os modelos?) partia da `D-159`. O dono explicou que há uma conexão da organização e uma da instância, e que a da instância é disponibilizada por organização.
**Opções avaliadas:** sem pontuação (a resposta veio fora das opções). Oferecidas: a Maind define a lista (recomendação do PO) · o owner escolhe livremente · a Maind escolhe o modelo.
**Por que esta:** a organização que já tem contrato com um provedor de IA pode usá-lo e arcar com o custo, e a Maind decide a quem paga a IA. Abre-se mão de um preço do assento que embuta a IA em todos os casos: ⚠️ o preço do assento passa a depender de a organização usar ou não a conexão da instância (`P-022`).
**Fica de fora / adiado:** se a organização nova nasce já com a conexão da instância ou sem IA até o administrador disponibilizar uma (`I-054`); quem é avisado quando a IA para, que agora depende de quem é a conexão (`I-030`); o teto automático de custo (`I-044`); o preço do assento para quem traz a IA própria (`P-022`); a forma de a conexão da instância chegar às organizações (`P-032`, do arquiteto).
**Hipóteses a validar:** 🔎 que as organizações que trazem a própria IA aceitem pagar o consumo; 🔎 que a Maind queira disponibilizar a conexão da instância a todas, ao menos no começo.
**Prova de valor:** a Maind cadastra um provedor de IA na instância e o disponibiliza à organização da Carla, que o usa sem editá-lo; a organização de outro cliente cadastra o próprio provedor e paga o consumo.
**Reabrir quando:** o preço do assento for definido, ou as organizações pedirem para editar a conexão da instância.

### D-215 · A web deixa de ser um modo de perguntar e vira um interruptor "pesquisar na web", ao lado dos dados
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-028`. Os **modos de perguntar** passam a ser **dois: dados e conversa**. A **web** deixa de ser um modo e vira um **interruptor "pesquisar na web"**, que a pessoa liga dentro da conversa e que roda **ao lado** da consulta aos dados (ou da conversa), quando a instância e a role autorizam (`D-162`). Na role, o botão que liga os modos passa a incluir a **pesquisa na web** no lugar do modo web; a contagem de nove botões (`D-110`, `D-122.1`) não muda.
**Completa a `D-162`:** que fez da web o modelo sair à internet quando autorizado e deixou o cadastro de páginas de fora.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou que a `MF-107` descrevia a web como um dos três modos, enquanto a `MF-109` a descrevia como pesquisa ao lado da consulta ao banco.
**Opções avaliadas:** sem pontuação (duas opções): **A. Interruptor ao lado dos dados** (escolhida; recomendação do PO) · B. Continua um modo à parte.
**Por que esta:** a pergunta que cruza o número da empresa com um fato de fora (por exemplo, as vendas de outubro e a inflação do mês) cabe numa resposta só, com link e data do fato. Abre-se mão do desenho dos três modos que quem usa a v1 conhece: ⚠️ a tela de perguntar muda.
**Fica de fora / adiado:** o tipo de fonte de páginas web da v1.xx: o arquiteto confere se some ou continua (`P-034`).
**Hipóteses a validar:** 🔎 que a pessoa entenda que a pesquisa na web é um complemento, e não um lugar de onde vêm os números da empresa.
**Prova de valor:** a gestora Carla liga "pesquisar na web" e pergunta se as vendas de outubro acompanharam a inflação; a resposta traz o número da empresa e o índice de fora, com link e data.
**Reabrir quando:** as pessoas pedirem para perguntar só à web, sem consultar os dados.

### D-214 · A visão de cobrança do owner da organização mostra só a contagem de assentos
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-027`. A **visão de cobrança** (de billing) do owner da organização (`D-193`) mostra **só a contagem de assentos**: para cada tipo (owner, gestor, ouro, prata e bronze), **quantos a organização tem, quantos usa e quantos estão livres** (`D-070`). Não mostra o custo, o relatório nem a história dos assentos, que ficam com o administrador da instância (`D-149`, `D-157`, `D-166`); o uso do Horus está na Home da organização (`MF-117`).
**Completa a `D-193`:** que deu a visão de billing ao owner da organização sem dizer o que há nela.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou a mesma dúvida em três páginas de leitura (`MF-101`, `MF-103` e `MF-105`).
**Opções avaliadas:** sem pontuação (três caminhos sobre o que se mostra): **A. Só a contagem de assentos** (escolhida; recomendação do PO) · B. A contagem mais o uso do período · C. Tudo o que a Maind vê da organização.
**Por que esta:** a Maind paga a IA e a embute no assento (`D-159`); mostrar o custo ao cliente exporia a margem, e a história de cada pessoa é só da administração. Abre-se mão de o owner conferir o custo e o uso na cobrança: ⚠️ para ver o uso, ele usa a Home da organização.
**Fica de fora / adiado:** o preço em reais (`P-022`); mostrar o uso do período na cobrança, se os owners pedirem.
**Hipóteses a validar:** 🔎 que a contagem de assentos baste para o owner conferir a fatura.
**Prova de valor:** a owner Carla abre a cobrança e vê, por tipo de assento, quantos tem, quantos usa e quantos estão livres.
**Reabrir quando:** owners pedirem o uso, o custo ou a história na cobrança.

### D-213 · A faixa é um contêiner de componentes; o aviso do owner da organização é o componente "caixa de texto livre"
Situação: 🟢 decidida (resposta do dono em 05/11/2026 à pergunta do `I-026`, fora das opções oferecidas; o texto dele vale como veio: "A faixa será um container para componentes que ainda vamos criar... um deles é um box de texto livre... ainda vamos definir outros como KPIs, ícones, etc") · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-026`. A faixa de avisos e números (`MF-120`) é um **contêiner de componentes** que ainda serão criados. O **aviso do owner da organização** não tem regra própria: é o componente **"caixa de texto livre"**, um dos componentes do catálogo da faixa (`D-173`). Os **demais componentes, como KPIs e ícones, ainda serão definidos**, e as regras de cada componente (por exemplo, hora de fim e retirada à mão, que o aviso da instância já tem, `D-165`) são definidas junto com o componente.
**Completa a `D-170`, a `D-173` e a `D-212`:** a lista e as regras dos componentes ficam para a definição deles; o card de número (`D-212`) é um deles.
**Contexto:** a pergunta do `I-026` (o aviso do owner da organização: texto livre, hora de fim, retirada à mão). O dono respondeu descrevendo o modelo da faixa como um contêiner, e não escolheu uma das três opções.
**Opções avaliadas:** sem pontuação (a resposta veio fora das opções). Oferecidas: texto livre com fim opcional e retirada à mão, como o da instância (recomendação do PO) · texto livre com hora de fim obrigatória · só avisos prontos do catálogo.
**Por que esta:** a faixa nasce como um espaço de componentes, e cada um se define a seu tempo, em vez de a faixa fixar as regras de um aviso antes de existir o catálogo. Abre-se mão de fechar já o comportamento do aviso do owner da organização: ⚠️ a hora de fim e a retirada à mão dele ficam em aberto até a definição do componente.
**Fica de fora / adiado:** a lista dos componentes (KPIs, ícones, etc.) e as regras de cada um, inclusive o ciclo de vida do aviso do owner da organização. É o que a página da `MF-120` já declara como "os componentes do catálogo" em "Ainda a decidir".
**Hipóteses a validar:** 🔎 que um contêiner de componentes, definidos aos poucos, caiba na v2.0 sem pedir corte (`D-204`).
**Prova de valor:** a owner Carla escreve, num componente de texto livre da faixa, "Fechamento do mês: lancem as despesas até sexta", e todas as pessoas da organização que não esconderam a faixa o veem.
**Reabrir quando:** o catálogo de componentes for desenhado, ou os owners pedirem um aviso com hora de fim obrigatória.

### D-212 · Num card de número da faixa, o owner escolhe a métrica do modelo semântico e o período
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-025`. O **card de número** da faixa de avisos e números (`MF-120`) é um **componente pronto do catálogo da faixa**; o owner da organização o aponta para uma **métrica já definida no modelo semântico** da organização (por exemplo, vendas ou margem) e escolhe o **período** (por exemplo, ontem, a semana, o mês). Escolher a métrica e o período **não é criar componente**: o owner segue sem criar componentes próprios (`D-170`).
**Completa a `D-170` e a `D-171`:** elas diziam que o owner só escolhe quais cards passam e em que ordem; esta diz o que ele informa em cada card de número.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou que o exemplo da página da `MF-120` mostrava o owner escolhendo "as vendas de ontem e a margem do mês", sem que nenhuma decisão dissesse como um componente genérico sabe qual é a "margem" de cada empresa.
**Opções avaliadas:** sem pontuação (três caminhos sobre um ponto): **A. A métrica do modelo semântico e o período** (escolhida; recomendação do PO) · B. Só números de uso do Horus, sem número do negócio · C. O resultado de uma pergunta de análise já salva.
**Por que esta:** o número do negócio aparece na faixa com a definição que a empresa deu (o significado de "margem" é da empresa), sem componente novo. Abre-se mão de a faixa funcionar numa organização sem modelo semântico: ⚠️ sem a métrica definida, só aparecem os números de uso.
**Fica de fora / adiado:** o owner criar componentes próprios; a lista dos componentes do catálogo.
**Hipóteses a validar:** 🔎 que as métricas mais pedidas já existam nos modelos semânticos das organizações; 🔎 que o motor de cards que a v1.xx já tem sirva a esse card (a conferir com o arquiteto, `P-036`).
**Prova de valor:** a owner Carla escolhe, na tela de configuração da faixa, o card de número "Vendas" para "ontem" e o card "Margem" para "o mês", e a faixa mostra os dois com a definição da empresa.
**Reabrir quando:** as organizações não tiverem as métricas no modelo semântico ou pedirem números que o modelo não traz.

### D-211 · O total de perguntas respondidas da organização segue como número sem dono quando alguém é excluído
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-053`. Quando uma pessoa é excluída, o **total de perguntas de análise respondidas da organização**, e a série mensal que a Home mostra, **continuam como estavam**: o número fica **sem dono**, sem ligação com a pessoa (sem nome, sem conversa, sem o que ela avaliou). O que se apaga é a ligação com a pessoa, não o número agregado.
**Completa a `D-210`**, que apaga os registros da pessoa; e **preserva a `D-133`** (a medida de autonomia).
**Contexto:** a `D-210` apagou a contagem que é da pessoa; sem esta decisão, o total de um mês passado encolheria quando alguém saísse.
**Opções avaliadas:** sem pontuação (duas opções): **A. Segue como número sem dono** (escolhida; recomendação do PO) · B. A parte da pessoa some do total.
**Por que esta:** a medida de sucesso e a economia calculada com o cliente (`D-132`) não mudam para trás. Abre-se mão de apagar até o número: ⚠️ a organização guarda um total que veio de uma pessoa apagada, sem dado pessoal.
**Fica de fora / adiado:** a proteção de dados pessoais confirmar que um número agregado sem ligação com a pessoa está fora do que se apaga (`P-044`).
**Hipóteses a validar:** 🔎 que o número agregado, sem ligação com a pessoa, não seja dado pessoal.
**Prova de valor:** o Pedro, que respondeu 300 das 1.200 perguntas de outubro, é excluído em novembro; a Home continua mostrando 1.200 em outubro.
**Reabrir quando:** o jurídico ou a proteção de dados pessoais exigirem apagar também o agregado.

### D-210 · Quem é excluído leva consigo os registros dele: o rastro, os reportes pendentes e a contagem
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, contra a recomendação do PO, que era guardar tudo, com o nome) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-052`. Quando uma pessoa é **excluída da organização**, os **registros dela são apagados junto**: o rastro da Auditoria (o que ela entregou e o que ela abriu), os reportes de resposta errada que ela fez e o owner ainda não analisou, e a contagem da medida de autonomia que é dela. Completa a `D-206` e a `D-209` (quem é excluído perde em definitivo).
**Substitui em parte** a `D-087` (que guardava a resposta reportada até o owner analisá-la) e a proposta do arquiteto de manter o rastro de quem pede a exclusão da conta até vencer o prazo do owner (`A-16`, item 3, do documento 14).
**Contexto:** a `D-206` e a `D-209` fizeram quem sai perder o que criou; faltava dizer se a organização guarda os registros que não são criação da pessoa.
**Opções avaliadas:** sem pontuação (três caminhos sobre o que se guarda): A. Guarda tudo, com o nome, até o prazo do rastro (recomendação do PO) · B. Guarda sem o nome · **C. Apaga tudo junto com a pessoa** (escolhida pelo dono).
**Por que esta:** quem sai leva tudo, sem guarda de dado pessoal, sem exceção para explicar. Abre-se mão do histórico: ⚠️ a Auditoria perde o que a pessoa entregou e abriu (o owner não consegue mais ver quem entregou o quê); o reporte pendente se perde antes de ser analisado; e a contagem de perguntas respondidas pode cair (`I-053`).
**Fica de fora / adiado:** se o total da organização na medida de autonomia cai ou segue como número sem dono (`I-053`); e se apagar tudo respeita a guarda que a lei exige do registro de acesso (a `ARQ-035` fixa seis meses) e as cópias de segurança (`P-044`, do arquiteto).
**Hipóteses a validar:** 🔎 que as organizações aceitem perder o histórico de quem sai; 🔎 que a exclusão de dados da pessoa seja compatível com a guarda legal (`P-044`).
**Prova de valor:** o gestor Pedro é excluído; a Auditoria deixa de mostrar o que ele entregou e abriu, e os reportes dele que ninguém analisou desaparecem.
**Reabrir quando:** a Auditoria ficar sem utilidade por causa dos buracos, o jurídico exigir guarda, ou os owners pedirem para guardar o histórico sem o nome.

### D-209 · Não há transferência: quem é excluído perde em definitivo, e quem é rebaixado só desabilita
Situação: 🟢 decidida (resposta do dono em 05/11/2026 à pergunta do `I-050`, fora das opções oferecidas; o texto dele vale como veio: "na verdade tínhamos definido o seguinte... uma pessoa excluída perde em definitivo. Se ela é rebaixada, apenas desabilitamos.") · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-050` e o `I-040`. O Horus **não tem transferência** do que a pessoa criou, nem na v2.0 nem na v2.1:
- **Quem é excluído da organização perde em definitivo** o que criou: boards, conversas, agendamentos e agentes (`D-206`).
- **Quem é rebaixado** (de ouro a prata ou a bronze) **tem o que criou desabilitado**, vinculado a ela e só para excluir (`D-207`); se voltar a ser ouro, reativa um a um (`D-208`).
- Não nasce a `MF-124` e a v2.1 não ganha mf de transferência. O board que o owner publicou e que calcula com o acesso dele (`D-164`) **some junto com o owner que sai**.
**Completa a `D-206`**, retirando dela a ideia de a transferência voltar "na v2.1".
**Contexto:** o PO perguntou se a transferência voltaria na v2.1 como mf própria (`D-197`). O dono respondeu que a regra já era essa: excluído perde em definitivo, rebaixado desabilita.
**Opções avaliadas:** sem pontuação (a resposta veio fora das opções). Oferecidas: mf própria na v2.1 (recomendação do PO) · sem versão · não volta. A resposta equivale à terceira, com a regra dos dois casos.
**Por que esta:** simplifica para sempre: sem transferência, sem área da organização que recebe o que sai, sem regra de quem recebe. Abre-se mão de o owner salvar o trabalho de quem sai: ⚠️ um gestor que sai leva o board que compartilhou e o PDF que agendava para a equipe; um board público some com o owner que o publicou, e quem estava na quarentena deixa de vê-lo.
**Fica de fora / adiado:** o que a organização guarda de quem sai (o rastro, os reportes pendentes e a medida de autonomia), no `I-052`.
**Hipóteses a validar:** 🔎 que owners e gestores aceitem perder o trabalho de quem sai; 🔎 que a leitura de "perde" seja excluir os dados da pessoa (e não escondê-los), a confirmar com o arquiteto e com a proteção de dados pessoais.
**Prova de valor:** o gestor Pedro é excluído da organização, e os boards e agendamentos dele deixam de existir; nenhum owner recebe nada para transferir.
**Reabrir quando:** uma organização perder trabalho importante com a saída de uma pessoa e pedir para recuperá-lo.

### D-208 · Quem volta a ser ouro reativa, um a um, o que ficou desabilitado
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-049`. Quando uma pessoa que passou de ouro a prata ou a bronze **volta a ser ouro**, o que ficou desabilitado (`D-207`) **não volta sozinho**: ela **reativa cada item**, um a um, quando quiser. Mantém a leitura `D-073.2` ("nada volta sozinho").
**Completa a `D-207`.**
**Contexto:** a `D-207` deixou o que a pessoa criou vinculado e desabilitado; faltava dizer o que acontece na volta ao ouro.
**Opções avaliadas:** sem pontuação (três caminhos sobre um estado): **A. Ela reativa um a um** (escolhida; recomendação do PO) · B. Tudo volta sozinho · C. Continua só para excluir.
**Por que esta:** nenhum agente ou agendamento antigo volta a gastar a IA que a Maind paga (`D-159`) sem que alguém peça. Abre-se mão da volta automática: ⚠️ quem recupera o assento reativa item por item.
**Fica de fora / adiado:** reativar vários de uma vez, se pedirem.
**Hipóteses a validar:** 🔎 que reativar um a um não incomode a quem tem muitos itens.
**Prova de valor:** a Júlia volta a ser ouro, e os 4 boards e o agendamento continuam desabilitados até ela reativá-los, um por um.
**Reabrir quando:** owners ou membros reclamarem de reativar muitos itens.

### D-207 · Quem passa de ouro a prata ou a bronze mantém o que criou, desabilitado e só para excluir
Situação: 🟢 decidida (resposta do dono em 05/11/2026 à pergunta do `I-051`, fora das opções oferecidas; o texto dele vale como veio: "Mantém vinculado mas fica desabilitado sem a possibilidade de uso (permitindo apenas exclusão)") · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-051`. Quando uma pessoa passa de ouro a prata ou a bronze e **continua na organização**, o que ela criou (boards, relatórios, agendamentos e agentes) **continua vinculado a ela, mas fica desabilitado, sem possibilidade de uso**. A **única ação permitida é excluir**. Os agendamentos e os agentes deixam de rodar.
**Substitui em parte** a `D-203` (a segunda parte, que mandava o que a pessoa criou para a área da organização, com agendamentos e agentes pausados até o owner transferir ou excluir) e a `D-073` (a mesma regra, para a passagem de membro full a leitor). Quem **sai** da organização segue a `D-206`: perde tudo.
**Contexto:** a `D-206` tirou a área da organização e a transferência da v2.0, e a passagem de faixa dependia dela. As três opções oferecidas eram: perder tudo como quem sai, só trocar depois de apagar, ou guardar o que criou só para ver. O dono respondeu com uma quarta, que mantém o trabalho sem custo e sem uso.
**Opções avaliadas:** sem pontuação (a resposta veio fora das opções). Oferecidas: perder tudo como quem sai (recomendação do PO) · a troca só depois de a pessoa apagar · guardado, só para ver.
**Por que esta:** reduzir um assento não apaga trabalho, e o que criou não consome a IA que a Maind paga (`D-159`) enquanto a pessoa não tem o assento que cria. Abre-se mão de uma regra só para quem sai e para quem muda de faixa: ⚠️ a v2.0 passa a ter um estado a mais (desabilitado e vinculado) para construir e explicar.
**Fica de fora / adiado:** se, ao voltar a ser ouro, o que ficou desabilitado volta a funcionar (`I-049`).
**Hipóteses a validar:** 🔎 que "desabilitado" siga o comportamento do board desabilitado da `D-044` e da `D-045`: no lugar do board aparece o aviso de board desativado para quem o abrir; 🔎 que a pessoa veja a lista do que ficou desabilitado para poder excluir, mesmo sem poder abrir.
**Prova de valor:** a Júlia, ouro com 4 boards e 1 agendamento, passa a prata; os 4 boards e o agendamento continuam dela, mas desabilitados, e ela só consegue excluí-los.
**Reabrir quando:** owners reclamarem de reduzir o assento sem poder aproveitar o que a pessoa criou.

### D-206 · Na v2.0, quem sai da organização perde o que criou: não há transferência
Situação: 🟢 decidida (resposta do dono em 05/11/2026 à pergunta do `I-048`: "vamos simplificar isso na v2.1... uma pessoa que sai da org, perde os boards, conversas, agendamentos, etc... mais fácil pra primeira versão"; o texto dele vale como veio) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-048`. Na v2.0, a pessoa que **sai da organização perde o que criou**: os **boards, as conversas, os agendamentos, os agentes** e o mais que for dela. **Não há transferência** e a área da organização **não recebe** o que as pessoas deixam. É a versão mais simples para a primeira entrega.
**Substitui** a `D-205` (que ficou sem objeto) e, para quem sai da organização, a parte da `D-044`, da `D-045` e da `D-073` que mandava o que a pessoa criou para a área da organização, onde o owner transferia ou excluía. Os agendamentos e agentes "pausados até o owner transferir" também deixam de existir na v2.0.
**Contexto:** a pergunta do `I-048` (o que acontece com os destinatários que o gestor novo não gere) nasceu da transferência da `D-205`. O dono preferiu tirar a transferência da v2.0 a regular seus detalhes.
**Opções avaliadas:** sem pontuação (a resposta veio fora das opções). As opções oferecidas eram sobre a transferência: tirar os destinatários fora da carteira, recusar a transferência, ou o owner liberar e responder.
**Por que esta:** menos regra para construir e para explicar; quem sai leva embora o que era dele. Abre-se mão de o owner salvar o trabalho de quem sai: ⚠️ um gestor que sai faz sumir o board que ele compartilhou com a equipe e o PDF que ele agendava para ela.
**Fica de fora / adiado:** a transferência. O dono falou em "simplificar na v2.1": se ela volta e como (uma mf própria, pela `D-197`) é o `I-050`. O que acontece com quem passa de ouro a prata ou a bronze, que continua na organização, é o `I-051`. O que a organização guarda de quem sai (o rastro da Auditoria, os reportes pendentes e a contagem da medida de autonomia) é o `I-052`.
**Hipóteses a validar:** 🔎 que perder o que criou, sem aviso nem transferência, não afaste owners e gestores; o aviso antes de a pessoa sair é um detalhe de desenho do arquiteto.
**Prova de valor:** o analista Rui sai da organização, e os boards, as conversas e os agendamentos dele deixam de existir; nada dele aparece na área da organização.
**Reabrir quando:** uma organização perder trabalho importante com a saída de uma pessoa e pedir a transferência.

### D-205 · O owner da organização só transfere o que ficou na área da organização a outro owner ou a um gestor
Situação: ⚪ substituída por `D-206` (era 🟢 decidida em 05/11/2026, contra a recomendação do PO, que era "owner, gestor ou ouro"; o dono tirou a transferência da v2.0) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-024`. Quando o owner da organização transfere o que ficou na **área da organização** (agendamentos, agentes e boards de quem saiu, `D-044`, `D-045`, ou de quem passou de ouro a prata ou a bronze, `D-073`, `D-203`), só pode transferi-lo a **outro owner** ou a um **gestor**. O membro ouro, a prata e o bronze não recebem. O que não for transferido continua pausado ou é excluído.
**Substitui em parte** a `D-045` e a `D-073`, que diziam que o owner transfere "para qualquer pessoa da organização".
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou que a transferência para "qualquer pessoa" batia com a `D-203` (a prata e o bronze não criam) e com a `D-059` (só o gestor e o owner entregam dados a outras pessoas, e o ouro agenda só para si). Quem recebe um agendamento de equipe precisa poder entregá-lo à equipe.
**Opções avaliadas** (sem pontuação: três caminhos sobre quem recebe): A. Owner, gestor ou ouro (recomendação do PO: só quem cria, `D-203`; o agendamento de equipe perderia destinatários nas mãos de um ouro) · **B. Só owner ou gestor** (escolhida pelo dono: só recebe quem pode entregar a outras pessoas, `D-059`) · C. Qualquer pessoa, como antes (contradiz a `D-203`: a prata e o bronze ficariam donos de agente e agendamento que não podem editar, com a IA paga pela Maind, `D-159`).
**Por que esta:** o que sai sozinho para outras pessoas fica com quem pode entregar a outras pessoas. Abre-se mão de o membro ouro herdar um board ou um agendamento: ⚠️ uma organização sem gestor só passa o que ficou a um owner.
**Fica de fora / adiado:** o que acontece com os destinatários que o novo dono não alcança (`I-048`); e como a pessoa que volta a ser ouro recebe de volta o que criou, já que a `D-073.2` dizia que o owner "devolve à mão, transferindo" (`I-049`).
**Hipóteses a validar:** 🔎 que toda organização tenha, ao menos, um owner ou um gestor para receber.
**Prova de valor:** o gestor Pedro sai, e a owner Carla transfere o agendamento da equipe dele a outro gestor; o sistema não lhe oferece um membro ouro, prata ou bronze como destino.
**Reabrir quando:** organizações pequenas, sem gestor, pedirem que o ouro herde o que ficou.

### D-204 · A MF-120 sai da lista de cortes: o aviso da instância só chega às pessoas por ela
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** fecha o `I-023`. A `MF-120:Faixa de avisos e números` **deixa de ser a candidata a corte** da v2.0 e fica nela como parte indispensável: o aviso da instância vai **só pela faixa** (`D-151`), e a `MF-101:Administração da instância`, essencial, depende dela (`D-202`).
**Substitui em parte a `D-174`**, que dava a `MF-120` como a mf mais fácil de cortar e a classificava como "acelera": o valor dela passa a **indispensável à v2.0**, pelo aviso da instância.
**Contexto:** a revisão das mfs da v2.0 (05/11/2026) achou que a `D-174` e o documento 05 davam a `MF-120` como cortável, enquanto a prova de valor da `MF-101` mostra o aviso da instância aparecendo na faixa. Cortar a `MF-120` deixaria a `MF-101` sem canal para o aviso.
**Opções avaliadas** (sem pontuação: o caso é pequeno e as três opções diferem numa escolha só): **A. A `MF-120` sai da lista de cortes** (escolhida; recomendação do PO) · B. Corte possível, com um aviso mínimo dentro da `MF-101` (o aviso seria construído duas vezes) · C. Corte possível, e o aviso volta por e-mail aos owners (desfaz parte da `D-151`; o aviso passa a depender de a pessoa ler o e-mail).
**Por que esta:** mantém a prova de valor da `MF-101` e o aviso sem e-mail (`D-151`) sem construir duas vezes. Abre-se mão da folga de cortar escopo: ⚠️ se a v2.0 apertar, o corte sai de outra mf.
**Fica de fora / adiado:** nada.
**Hipóteses a validar:** 🔎 que o custo da faixa, sobretudo o cálculo dos cards de número por pessoa (`P-036`), caiba na v2.0 sem pedir corte.
**Prova de valor:** a Maind publica um aviso de manutenção e ele aparece na faixa de todas as pessoas que não a esconderam, sem e-mail.
**Reabrir quando:** o arquiteto dimensionar a `MF-120` e o custo for desproporcional; então a opção B volta à mesa.

### D-203 · O membro prata pergunta e investiga, e criar é do ouro; quem muda de faixa deixa o que criou na área da organização
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com as opções recomendadas nas duas perguntas) · Data: 05/11/2026 · Versão: v2.0 (a investigação é da `MF-119`, v2.1) · ⚠️ a segunda parte (o que a pessoa criou vai para a área da organização) foi substituída pela `D-207`

**Decisão:** fecha o `I-022`.
- **O membro prata** usa o chat (no app, na Pergunta rápida e no WhatsApp), usa a **Investigação guiada** (`MF-119`, quando chegar) e **recebe alertas e PDFs**. **Não cria** board, relatório, agendamento nem agente. Cada faixa soma uma coisa: o **bronze vê**, a **prata pergunta**, o **ouro cria** (`D-193`, `D-194`).
- **Quem passa de ouro a prata ou a bronze** deixa o que criou (boards, relatórios, agendamentos e agentes) na **área da organização**, e os agendamentos e os agentes ficam pausados até o owner transferi-los ou excluí-los. É a regra da `D-073`, que só tratava da passagem de membro full a leitor, estendida a toda passagem para uma faixa que não cria.
**Completa a `D-194`** (que deixou de fora o que a prata faz) **e estende a `D-073`**.
**Contexto:** impasse `I-022`, achado pelas páginas de leitura. A `D-194` dizia só que a prata pergunta e não cria boards nem relatórios.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`; notas do PO, em hipótese). *O que a prata faz:* **B. Pergunta e investiga; criar é do ouro: 72 (escolhida; recomendação do PO)** · A. Prata = ouro sem boards e relatórios: 60 · C. Decidir ponto a ponto: 56. *Quem muda de faixa:* **A. O que criou vai para a área da organização: 72 (escolhida; recomendação do PO)** · B. Fica com a pessoa, só para ver: 50.
**Por que esta:** a escada fica simples de explicar e de cobrar, e a Maind não paga a IA de agentes criados por quem só pergunta (`D-159`). Abre-se mão de a prata automatizar avisos: ⚠️ quem quer um aviso periódico precisa de um assento de ouro.
**Fica de fora / adiado:** o preço da prata (`P-022`).
**Hipóteses a validar:** 🔎 que a diferença entre prata e ouro seja entendida e aceita como cobrável (`D-194`).
**Prova de valor:** o membro prata pergunta, investiga e recebe alertas e PDFs, e não vê a opção de criar boards, relatórios, agendamentos nem agentes; ao passar de ouro a prata, o que ele criou aparece na área da organização.
**Reabrir quando:** clientes pedirem avisos periódicos sem assento de ouro, ou a prata e o ouro passarem a ser cobrados do mesmo jeito.

### D-202 · Definição macro da MF-101:Administração da instância
Situação: ⚪ substituída pela `D-280` (a `MF-101` com o middleware) · antes: 🟢 decidida (proposta do PO, confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** a `MF-101:Administração da instância`, que era base herdada (`D-021`) e cresceu com as decisões `D-146` a `D-166`, fica definida assim:
- **O que é:** o painel de quem opera o Horus, que no SaaS é um **funcionário da Maind** (o administrador da instância, `D-147`, `D-193`). Nele, a Maind **cria e administra as organizações** (`D-146`, `D-148`), **libera, reduz e corta os assentos** de cada uma (`D-080`), **vê o uso e o custo** de cada organização e **baixa o relatório** dela, em planilha e PDF, com a história dos assentos (`D-149`, `D-153`, `D-157`, `D-166`), **publica o aviso da instância** (`D-151`, `D-165`), cuida do **e-mail do produto** (`D-155`) e da **marca da Maind** (`D-200`), e pode **perguntar ao próprio Horus** sobre a história da instância (`D-158`).
- **Quem ganha:** o **administrador da instância** (a Maind), que opera o SaaS sem planilha nem chamado; de forma indireta, o **owner da organização**, que recebe os assentos e os avisos.
- **Decisão que passa a ser possível:** saber quanto cada organização usa e custa, liberar ou cortar assentos, abrir uma organização nova e avisar todo mundo de uma manutenção, tudo num lugar só.
- **Prova de valor:** a Maind cria uma organização, libera os assentos dela, acompanha o uso e o custo, baixa o relatório em planilha e PDF e publica um aviso de manutenção que aparece na faixa de todas as pessoas.
- **Retorno para o negócio:** controle da receita e do custo por organização (a cobrança por assento depende dele, `D-080`) e menos suporte para operar o SaaS.
- **O que não inclui:** ver os dados das conexões das organizações (`D-193`); a marca completa do contratante, sem versão (`D-200`); o interruptor geral da segurança, que é da `MF-106` (`D-199`); o middleware e a instalação no cliente (`D-188`, `D-195`); a página pública do estado da instância (`D-154`); o preço (`P-022`).
- **Depende de:** `MF-102:Organizações, pessoas e papéis` (as pessoas e os papéis); `MF-103:Licenças e planos` (os assentos); `MF-120:Faixa de avisos e números` (onde o aviso aparece).
- **Valor:** **essencial** para operar o SaaS: sem ela a Maind não cria organizações nem libera assentos.
**Contexto:** o agente que reescreveu a página de leitura da `MF-101` notou que ela não tinha definição macro no formato da mf, só as decisões espalhadas.
**Opções avaliadas:** definição direta, sem pontuação (o conteúdo já foi decidido nas decisões citadas).
**Por que esta:** reúne num lugar só o que a `MF-101` é depois da `D-197`, sem decidir nada novo de valor.
**Hipóteses a validar:** 🔎 que o administrador da instância não precise ver os dados das conexões para dar suporte (`D-193`).
**Reabrir quando:** o suporte da Maind pedir ver mais, ou o dono quiser mudar o que a mf inclui.

### D-201 · Definição macro da MF-122:Conectores de chat corporativo e da MF-123:Fonte AWS Athena
Situação: 🟢 decidida (proposta do PO, confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.1 (onda 1)

**Decisão:** as duas mfs novas da `D-198` ficam definidas assim. Com ela, a `P-043` se fechou.

**`MF-122:Conectores de chat corporativo`** (nome provisório)
- **O que é:** dois conectores novos para o "carteiro" da `MF-113`: o **Microsoft Teams** e o **Google Chat**. O agente e o agendamento entregam o aviso, o PDF ou a imagem a um canal do Teams ou a um espaço do Google Chat, **só a usuários do Horus** (`D-035`).
- **Quem ganha:** o **gestor e os membros** que recebem avisos onde a equipe já conversa; o **owner da organização**, que liga o conector, com a aprovação da TI do cliente (`D-124`).
- **Decisão que passa a ser possível:** receber o aviso no chat da empresa, sem depender de abrir o e-mail ou o WhatsApp.
- **Prova de valor:** o aviso de um agente chega a um canal do Teams e a um espaço do Google Chat (`D-182`).
- **Retorno para o negócio:** adoção e retenção, porque o aviso chega onde a equipe já está; abre as empresas que vivem no Teams ou no Google Workspace (a Maind, primeiro cliente, usa o Google Workspace).
- **O que não inclui:** outros conectores (o Slack, por exemplo); entregar a quem não é usuário do Horus; conversar com o Horus pelo chat corporativo (isso é a `MF-111`, no WhatsApp, `D-099`); o desenho técnico da integração (do arquiteto, `P-038`).
- **Depende de:** `MF-113:Conectores de Saída` (o carteiro); `MF-114` e `MF-115` (o que gera o aviso); a aprovação da TI de cada cliente.
- **Valor:** **expande**.

**`MF-123:Fonte AWS Athena`** (nome provisório)
- **O que é:** o **AWS Athena** passa a **responder perguntas de análise**, como as outras fontes vivas (hoje ele só cadastra, `D-161`).
- **Quem ganha:** o **gestor e o executivo** de uma organização cujos dados estão no Athena; o **owner**, que conecta a fonte.
- **Decisão que passa a ser possível:** perguntar em português aos dados que estão no AWS, sem pedir ao time de dados.
- **Prova de valor:** uma organização conecta um Athena e recebe uma resposta de análise (`D-161`).
- **Retorno para o negócio:** abre as empresas com dados no AWS. ⚠️ Não há demanda conhecida (`D-161`).
- **O que não inclui:** outras fontes novas; a segurança por pessoa no Athena além do que a `MF-106` cobrir (hoje só cobre o SQL Server, `P-033`); o desenho técnico do conector e do dialeto (do arquiteto, `P-033`).
- **Depende de:** `MF-104:Conectar as fontes vivas` (a base das fontes); `MF-107:Perguntar aos dados em português`; `MF-106:Segurança dos dados por pessoa`.
- **Valor:** **expande**.

**Contexto:** a `D-198` criou as duas mfs a partir das partes da `MF-113` e da `MF-104`, e a `P-043` pedia a definição no formato da mf. O conteúdo vem das `D-182` e `D-161`; o PO só reuniu e completou o que o formato pede.
**Opções avaliadas:** definição direta, sem pontuação (o conteúdo já foi decidido pelo dono nas `D-161` e `D-182`).
**Por que esta:** cumpre o formato da mf sem decidir nada novo de valor. Abre-se mão de nada.
**Hipóteses a validar:** 🔎 que o Teams e o Google Chat saiam juntos, numa mf só; 🔎 que a `MF-123` caiba na onda 1 junto da `MF-106` (`P-033`).
**Reabrir quando:** a onda 1 apertar, ou um dos dois conectores de chat pedir tratamento diferente.

### D-200 · Na v2.0 a marca é a da Maind; a marca completa do contratante fica sem versão
Situação: 🟢 decidida (dita pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era a marca por organização) · Data: 05/11/2026 · Versão: v2.0 (a marca da Maind) e sem versão (a marca do contratante)

**Decisão:** na v2.0, **a marca do produto é a da Maind**: o nome, os logos e o rodapé que o administrador da instância configura (`D-011`) e o e-mail do produto valem para todas as organizações. A **marca completa do contratante** (`D-183`: logo, nome e e-mail do cliente em todo o produto, até no remetente) **sai da v2.0 e da v2.1 e fica sem versão**: o dono vai pensar depois em como mudar isso.
- **A `MF-101:Administração da instância` continua inteira na v2.0** (`D-197`), agora sem a marca completa.
- 🔎 *Leitura do PO, a confirmar:* se a marca do contratante voltar, volta como **mf própria**, e não como parte da `MF-101` (`D-197`). O logo de cada organização, que o backend já guarda, não muda com esta decisão.
**Contexto:** a `D-197` trouxe a marca completa para a v2.0 e deixou uma hipótese: a marca é da instância ou de cada organização? O PO recomendou a marca por organização. O dono respondeu que, na v2.0, ela é da Maind. O SaaS é uma instância só da Maind (`D-192`, `D-193`).
**Opções avaliadas:** resposta do dono, sem pontuação. A recomendação do PO (a marca por organização) não foi a escolhida.
**Por que esta:** a v2.0 sai com menos escopo e o SaaS tem uma marca só. Abre-se mão de o cliente ver a própria marca no produto e no remetente das mensagens: ⚠️ o white label da `D-007` fica sem entrega até lá.
**Consequências:**
- A `D-183` e o trecho da `D-197` sobre a marca completa ficam substituídos neste ponto; a `D-121` (a nº 6) e a `D-181` ficam sem a marca. O tema (as cores e a aparência) continua sem versão, como a `D-183` o deixou.
- O objetivo da v2.1 (`D-136`) cita "a própria marca", e o mapa de objetivos (`07`) também: a ajustar na `P-028`.
- O modelo de dados da `MF-101` não reserva coluna para a marca do contratante.
**Hipóteses a validar:** 🔎 que o primeiro cliente, a própria Maind (`D-009`), e os seguintes aceitem a marca da Maind no SaaS.
**Prova de valor:** a v2.0 sai sem tela nem coluna de marca do contratante, e nenhum cliente deixa de comprar por isso.
**Reabrir quando:** um cliente exigir a própria marca, ou o dono decidir como mudar isso.

### D-199 · O interruptor geral e as demais peças da segurança por pessoa passam a ser da MF-106, na v2.1
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada nas duas perguntas) · Data: 05/11/2026 · Versão: v2.1

**Decisão:** para cumprir a `D-197`, tudo o que só vale com a segurança por pessoa passa a ser da `MF-106:Segurança dos dados por pessoa`, inteira na v2.1 (`D-145`). Saem das mfs da v2.0 e entram nela:
- o **interruptor geral da segurança** (estava na `MF-101:Administração da instância`);
- os **grupos dinâmicos por claims** e as **colunas de claims da planilha de convites** (estavam na `MF-102:Organizações, pessoas e papéis`, `D-019`, `D-056`);
- a **liberação de dados do gestor no board** (`D-051`, `D-053`, `D-054`; estava na `MF-112:Boards e Relatórios`);
- o **registro dessas liberações no rastro** (estava na `MF-116:Auditoria`, `D-090`, `D-093`);
- a **demonstração da segurança por pessoa** (estava na `MF-118:Bases de demonstração`).
**As cinco mfs da v2.0 ficam inteiras**: a `MF-101`, a `MF-102`, a `MF-112`, a `MF-116` e a `MF-118` não têm mais nada na v2.1. As definições dessas peças continuam valendo como foram decididas; só mudam de mf. As dependências que outras mfs têm da `MF-106` (a `D-145` as lista) são dependências, e não partes: ficam como estão.
**Contexto:** fecha o `I-021`. O `06-versoes.md` listava o interruptor na `MF-101` e na `MF-106`, e a `D-145` deixou outras peças nas mfs de origem, com a volta marcada para a v2.1.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`; notas do PO, em hipótese). *Interruptor:* **A. Da `MF-106`: 66 (escolhida; recomendação do PO)** · B. Da `MF-101`, na v2.0: 54. *Demais peças:* **A. Passam à `MF-106`: 68 (escolhida; recomendação do PO)** · B. Cada peça vira mf própria na v2.1: 59.
**Por que esta:** o interruptor e as peças só têm efeito com a segurança por pessoa, então a mf dela é onde fazem sentido, e a v2.0 não carrega peça sem uso. Abre-se mão de uma `MF-106` enxuta: ⚠️ ela passa a reunir regras que estavam espalhadas em cinco mfs.
**Fica de fora / adiado:** as partes da casa do contratante (`MF-103`, `MF-104` e `MF-105`), sem versão desde a `D-188`.
**Hipóteses a validar:** 🔎 que o administrador da instância aceite não ter o interruptor até a v2.1, já que na v2.0 a organização é a fronteira dos dados.
**Prova de valor:** a v2.0 sai sem nenhum interruptor ou tela que dependa da segurança por pessoa.
**Reabrir quando:** a `MF-106` crescer a ponto de pedir divisão em duas mfs.

### D-198 · Teams e Google Chat viram a MF-122 e o Athena vira a MF-123, ambas na v2.1
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.1 (onda 1)

**Decisão:** para cumprir a `D-197`, as duas partes da v2.1 que pertenciam a mfs da v2.0 viram **mfs próprias** na onda 1 da v2.1 (`D-181`):
- **`MF-122:Conectores de chat corporativo`** (nome provisório): o **Microsoft Teams** e o **Google Chat** como conectores de saída, como definiu a `D-182`. Usam o mesmo "carteiro" da `MF-113` (`D-041`), com a aprovação da TI de cada cliente (`D-124`).
- **`MF-123:Fonte AWS Athena`** (nome provisório): o **AWS Athena terminado**, respondendo perguntas de análise, como definiu a `D-161`.
- **A `MF-113:Conectores de Saída` fica inteira na v2.0**, com o e-mail e o WhatsApp (`D-124`). **A `MF-104:Conectar as fontes vivas` fica inteira na v2.0**, sem o Athena. A próxima mf livre passa a ser a `MF-124`.
**Depende de:** a `MF-122` depende da `MF-113` (o carteiro); a `MF-123` depende da `MF-104` (o conector) e da `MF-106:Segurança dos dados por pessoa` (que hoje só cobre o SQL Server, `P-033`).
**Contexto:** primeira aplicação da `D-197` (`I-021`). O dono já tinha escolhido as versões das duas partes (`D-161`, `D-182`) e quis mantê-las.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`; notas do PO, em hipótese): **A. Cada parte vira mf nova na v2.1: 66 (escolhida; recomendação do PO)** · C. Decidir mf a mf: 60 · B. As partes sobem para a v2.0: 50.
**Por que esta:** mantém as datas que o dono escolheu e não engorda a v2.0, que já ganhou a marca completa (`D-197`). Abre-se mão de ter menos mfs: ⚠️ são duas mfs novas, pequenas, para acompanhar.
**Fica de fora / adiado:** outros conectores (Slack, por exemplo, `D-182`) e as partes da casa do contratante (`MF-103`, `MF-104` e `MF-105`), sem versão desde a `D-188`. 🔎 *Leitura do PO, a confirmar:* se a porta de volta abrir, essas partes entram como mf própria, e não como parte das mfs da v2.0.
**Hipóteses a validar:** 🔎 que o Teams e o Google Chat saiam juntos, numa mf só; 🔎 que a `MF-123` caiba na onda 1 junto da segurança por pessoa (`P-033`).
**Prova de valor:** a `MF-122`: o aviso de um agente chega a um canal do Teams e a um espaço do Google Chat. A `MF-123`: uma organização conecta um Athena e recebe uma resposta de análise.
**Reabrir quando:** a onda 1 da v2.1 apertar e o dono quiser tirar uma das duas, ou os dois conectores de chat pedirem tratamentos diferentes.

### D-197 · Uma macro funcionalidade não se divide em duas versões; a MF-101 fica inteira na v2.0
Situação: 🟢 decidida (regra dita pelo dono em 05/11/2026; a aplicação às outras mfs foi o `I-021`, fechado; a marca completa saiu da `MF-101` pela `D-200`) · Data: 05/11/2026 · Versão: geral

**Decisão:** cada mf pertence a **uma versão só**. Não existe mf com uma parte na v2.0 e outra na v2.1: a parte que o dono quer numa versão diferente **vira uma mf nova** ou **sobe para a versão da mf**, e a escolha é do dono, mf a mf (`I-021`).
- **A `MF-101:Administração da instância` fica inteira na v2.0**, com a marca completa do contratante: logo, nome e e-mail em todo o produto, inclusive o remetente das mensagens (`D-183`). O tema (as cores e a aparência) continua sem versão.
- **Substitui a leitura da `D-137`** ("uma mf entra na entrega em que aparece primeiro; as que têm partes na v2.1 contam como da v2.0") e a `D-137.1` do documento da v2.0.
**Contexto:** o dono disse "MF 101 de administração da instância fica na v2.0" e, ao ver a marca completa ainda listada para ela na v2.1, explicou a regra por trás: uma mf não se divide em duas versões. Hoje o `06-versoes.md` lista a `MF-101`, a `MF-103`, a `MF-104`, a `MF-105` e a `MF-113` nas duas tabelas.
**Opções avaliadas:** regra do dono, sem pontuação (ele decidiu direto).
**Por que esta:** cada mf tem uma versão só, e quem lê o plano não precisa somar pedaços. Abre-se mão de cortar escopo por parte de mf: ⚠️ a v2.0 cresce com a marca completa, e o que o dono quiser numa versão diferente tem de virar mf própria.
**Consequências:**
- A marca completa (`D-183`) passa da onda 1 da v2.1 para a v2.0; a `D-181` e a `D-121` perdem esse item. O modelo de dados da `MF-101` deixa de reservar as colunas da marca e passa a tê-las (a ajustar, `P-028`).
- Ficam com parte em outra versão e dependem do `I-021`: a `MF-113` (Teams e Google Chat na onda 1 da v2.1, `D-182`), a `MF-104` (o AWS Athena na v2.1, `D-161`) e o interruptor geral da segurança, que o `06-versoes.md` lista em duas mfs (`D-145`). As partes da casa do contratante (`MF-103`, `MF-104` e `MF-105`) estão sem versão desde a `D-188` (a porta de volta).
**Hipóteses a validar:** 🔎 que a marca completa, como a `D-183` a definiu para "o contratante", continue fazendo sentido no SaaS de uma instância só da Maind (`D-192`, `D-193`): a marca é da instância ou de cada organização?
**Prova de valor:** nenhuma mf aparece em mais de uma versão no `06-versoes.md`.
**Reabrir quando:** uma parte de mf não puder virar mf nova nem subir de versão sem quebrar uma dependência.

### D-196 · Definição macro da MF-121:Middleware na casa do contratante
Situação: ⚪ substituída em parte pelas `D-258`, `D-259`, `D-260` e `D-263` (a `MF-121` sobe inteira para a v2.0; é um middleware por organização, na Maind ou na casa do cliente; e ela deixa de depender da `MF-106`) · antes: 🟢 decidida (confirmada pelo dono em 05/11/2026, com um ajuste dele: o protocolo fica em aberto) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** a `MF-121:Middleware na casa do contratante` (nome provisório, mf nova) fica definida assim. Com ela, a onda 2 da v2.1 (`D-181`, `D-188`) está definida.
- **O que é:** uma **imagem de container** que a Maind disponibiliza e o cliente instala na infraestrutura dele (`D-195`). Ela expõe um **endereço público** e um **par de chaves cadastrado no Horus SaaS**, na organização (`D-195`). O Horus a usa para chegar aos **dados, à internet e à IA** do cliente (`D-190`), e o cliente governa o caminho por **IP e porta**. **O protocolo fica em aberto**: pode ser um servidor MCP, uma API REST ou gRPC, **de preferência gRPC**; a escolha é do arquiteto (`P-042`).
- **Quem ganha:** o **cliente com exigência de privacidade e segurança**, que mantém a governança pela cibersegurança e pela infraestrutura dele; o **owner da organização**, que conecta e configura; as pessoas perguntam como sempre.
- **Decisão que passa a ser possível:** usar o Horus SaaS sobre dados e modelos de IA que **não podem sair de casa**, sem instalar o Horus no cliente.
- **A regra do que sai:** só a **pergunta** e a **resposta pronta** (`D-189`); o **owner da organização** pode permitir o comando da consulta, o CSV e outras saídas; o funcionário da Maind, que administra a instância, **não liga nem vê** (`D-193`, `D-195`).
- **Prova de valor:** um cliente de cibersegurança rígida instala a imagem, cadastra a chave no Horus, libera só o IP do Horus no firewall e faz uma pergunta de análise sobre o banco interno, e nada além da pergunta e da resposta pronta sai.
- **Retorno para o negócio:** abre os clientes que exigiam on-premises ou "tudo dentro", **com uma frota só** e sem operar uma instalação por cliente.
- **O que não inclui:** a instalação completa do Horus no cliente, que só volta se um cliente exigir (`D-188`) e leva consigo o arquivo de licença e a rede interna (`D-175`, `D-176`, `D-186`, `D-187`); instância dedicada por cliente; middleware por instância (é por organização); o desenho técnico e o protocolo (do arquiteto, `P-040`, `P-042`).
- **Depende de:** `MF-104:Conectar as fontes vivas` (as fontes alcançam o banco pelo middleware); `MF-105:IA sob controle da organização` (o modelo do cliente, `D-185`); `MF-109:A web como fonte` (a saída para a internet); `MF-106:Segurança dos dados por pessoa`; as configurações da organização.
- **Valor:** **expande**: amplia o público a quem exige privacidade.
**Corrige a redação das `D-190` e `D-195`:** elas diziam "servidor MCP". O dono deixou o protocolo em aberto.
**Contexto:** o dono propôs o middleware (`I-020`, fechado) e, ao ver a definição, ajustou só o protocolo.
**Por que esta:** abre o Horus a quem exige privacidade sem instalar o Horus no cliente e com uma frota só. Abre-se mão do "tudo dentro" total: ⚠️ ele só existe na instalação completa, a porta de volta; e o endereço do middleware é público, protegido por chave e por IP e porta.
**Hipóteses a validar:** 🔎 que a TI dos clientes aceite hospedar a imagem e expor um endereço público protegido; 🔎 que o protocolo escolhido atravesse os proxies e firewalls corporativos (o gRPC pede HTTP/2).
**Reabrir quando:** a TI dos clientes recusar o endereço público, ou o protocolo escolhido não atravessar a rede dos clientes.

### D-195 · O middleware é uma imagem de container da Maind, com endereço público e par de chaves; as permissões e a conexão são da organização
Situação: ⚪ substituída em parte pela `D-258` (a chave nasce de um certificado criado com a organização, e a Maind faz a troca; as permissões e a conexão são configuradas no front do middleware, `D-265`) · antes: 🟢 decidida (confirmada pelo dono em 05/11/2026, com um acréscimo dele; o protocolo "servidor MCP" ficou em aberto pela `D-196`) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** o dono **confirmou** as leituras da `D-193`: as **permissões de saída** (`D-189`) e a **conexão do middleware** são **configurações da organização**, do owner dela, funcionário do cliente; o **middleware é por organização**; o funcionário da Maind, que administra a instância, **não liga nem vê** essas saídas. E **acrescentou**: o middleware é uma **imagem de container disponibilizada pela Maind**, que o cliente instala. Ela expõe um **endereço público** e um **par de chaves**, que é **cadastrado no Horus SaaS** (na organização), o que permite à infraestrutura do cliente **bloquear por IP e porta**.
**Contexto:** quinta dúvida do `I-020`, a última. Com ela, o `I-020` se fechou: o Horus chega ao cliente por um middleware, e a instalação completa só volta se um cliente exigir (`D-188`).
**Por que esta:** o cliente instala uma imagem pronta, sem Kubernetes, e governa o acesso por IP e porta, com a chave que ele mesmo cadastra. Abre-se mão de um middleware que só conecta de dentro para fora: ⚠️ o endereço é público, e a proteção depende da chave e do bloqueio por IP e porta.
**Fica de fora / adiado:** o desenho técnico da imagem, das chaves e da atualização (do arquiteto, `P-040`, `P-042`); o que sai de cada ferramenta do middleware.
**Hipóteses a validar:** 🔎 que a TI dos clientes aceite expor um endereço público protegido por chave e por IP; 🔎 que o cliente atualize a imagem quando a Maind publicar uma nova.
**Prova de valor:** o owner de uma organização instala a imagem, cadastra a chave no Horus, o cliente libera só o IP do Horus no firewall, e a pessoa faz uma pergunta de análise sobre o banco dele.
**Reabrir quando:** a TI dos clientes recusar o endereço público, ou a atualização da imagem por parte do cliente falhar com frequência.

### D-194 · Os tipos de assento passam a ser cinco: owner, gestor e os membros ouro, prata e bronze
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era a prata como role do membro full; o que a prata faz foi decidido na `D-203`; a leitura do PO sobre o ouro e o bronze foi confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** os **tipos de assento** passam a ser **cinco**: **owner**, **gestor**, **membro ouro**, **membro prata** e **membro bronze**. O ouro faz perguntas e cria boards e relatórios para si, sem compartilhar; a **prata** faz perguntas, mas **não cria boards nem relatórios**; o bronze só exibe os dashboards já criados e compartilhados (`D-193`). A Maind libera, reduz e conta cada tipo à parte (`D-067`, `D-068`).
**Substitui em parte a `D-069`**, que tinha quatro tipos (owner, gestor, membro full e membro leitor). Leitura do PO *(a confirmar com o dono)*: o **ouro** é o que a `D-069` chamava de membro full e o **bronze**, o membro leitor; e os nomes ouro, prata e bronze são os nomes dos tipos, no lugar de "membro full" e "membro leitor".
**Contexto:** o dono descreveu os papéis na `D-193`, e a prata não existia como tipo. O PO perguntou se ela seria um quinto tipo ou uma role do membro full (nota 77 contra 66).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): B. A prata é uma role do membro full: 77 (recomendação do PO) · **A. A prata é um quinto tipo de assento: 66 (escolhida)**.
**Por que esta:** os nomes ouro, prata e bronze viram a oferta por faixa, e a contagem de cada tipo fica explícita. Abre-se mão de um modelo com quatro tipos: ⚠️ o modelo de dados, as telas e a cobrança ganham um tipo novo, e a prata precisa de um preço (`P-022`).
**Fica de fora / adiado:** o preço da prata; quem pergunta e quem conta para o limiar de custo por assento que pergunta (a prata pergunta, e o bronze não).
**Hipóteses a validar:** 🔎 que a Maind queira cobrar a prata diferente do ouro e do bronze.
**Prova de valor:** a Maind libera assentos de prata a uma organização, e o membro de prata pergunta e não vê a opção de criar boards nem relatórios.
**Reabrir quando:** a prata e o ouro passarem a ser cobrados do mesmo jeito, ou os clientes não distinguirem os dois.

### D-193 · O SaaS é uma instância só, da Maind; o owner da organização, funcionário do cliente, a configura, inclusive o middleware
Situação: ⚪ substituída em parte pelas `D-258` e `D-265` (o SaaS segue sendo uma instância só; mas quem cria o certificado e faz a troca com o middleware é a Maind, e quem configura bancos e IA é a organização ou, na hospedagem da Maind, o time da Maind) · antes: 🟢 decidida (confirmada pelo dono em 05/11/2026, em resposta própria, que desfez a leitura de instância por cliente) · Data: 05/11/2026 · Versão: geral e v2.1 (onda 2)

**Decisão:** o dono descreveu o modelo assim, e ele vale:
- O **SaaS é hospedado pela Maind e atende a todos os clientes dela**: é uma instância só. **Alguns clientes** poderão usar o **middleware** (`D-188`, `D-190`) para intermediar o Horus SaaS e os dados e a IA deles.
- O **usuário da instância do SaaS é um funcionário da Maind**, com **visão macro de todas as organizações** e **sem visão dos dados das conexões** de dados.
- Na **organização**, quem a configura é o **owner da organização**, que é um **funcionário do cliente**. Ele tem a **visão de billing** e das **configurações** da organização.
- Abaixo do owner, **por enquanto**: os **gestores**, que criam e gerem grupos de membros, fazem perguntas e análises, criam boards e os compartilham com os grupos de que são donos; e os **membros**, em três faixas: **ouro** (faz perguntas e cria boards e relatórios para si, sem compartilhar), **prata** (faz perguntas, sem criar boards nem relatórios) e **bronze** (só exibe os dashboards já criados e compartilhados).
**Desfaz:** a leitura de que o cliente do middleware teria uma instância própria do Horus (`D-191`, `D-192`). O pedido de "um controle de criação de instâncias mais eficiente" da `D-192` fica entendido, **a confirmar**, como a criação de organizações no SaaS (`MF-101`, `D-146`); a `P-041` fica sujeita a essa confirmação.
**Leituras do PO** *(a confirmar com o dono)*: (1) as **permissões de saída** da `D-189` (o comando da consulta, o CSV e outras) e a **conexão do middleware** são configurações **da organização**, do owner dela, e não do administrador da instância (a Maind): a `D-191` as dava ao "dono da instância"; (2) o middleware é **por organização**, e não por instância; (3) as três faixas de membro têm uma **diferença para a `D-069`** (quatro tipos de assento: owner, gestor, membro full e membro leitor): a prata (pergunta, mas não cria boards nem relatórios) não existe hoje como tipo. É a dúvida seguinte.
**Contexto:** quinta dúvida do `I-020`. O PO perguntou o que o cliente recebe quando a Maind liga uma saída extra; o dono respondeu que a pergunta partia de uma confusão, e descreveu o modelo.
**Por que esta:** o cliente configura o que é dele, e a Maind mantém a visão macro sem ver os dados. Abre-se mão de a Maind ligar as saídas por ele: ⚠️ o suporte da Maind depende de o owner da organização liberar o que for preciso.
**Fica de fora / adiado:** a instância dedicada por cliente; a visão de billing do owner (o que ela inclui).
**Hipóteses a validar:** 🔎 que os owners das organizações aceitem configurar o middleware e as saídas.
**Prova de valor:** o owner de uma organização conecta o middleware dele ao Horus SaaS, liga a saída do CSV, e o funcionário da Maind continua sem ver os dados das conexões.
**Reabrir quando:** um cliente precisar de uma instância própria, ou o suporte da Maind não funcionar sem ver mais.

### D-192 · O Horus fica no SaaS da Maind, que é a dona das instâncias; o cliente tem o middleware, e a Maind precisa criar instâncias com mais eficiência
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, em resposta própria: ele corrigiu a leitura do PO; a decisão foi desfeita em parte pela `D-193`: o SaaS é uma instância só, e o pedido de criação de instâncias está a confirmar) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** o **Horus fica no SaaS**, na infraestrutura da Maind, que continua **dona das instâncias** (`D-013`). **O cliente não é dono de uma instância do Horus**: ele hospeda o **middleware** (`D-190`) na infraestrutura dele. A Maind precisa de um **controle de criação de instâncias mais eficiente** do que o de hoje.
**Corrige a leitura do PO na `D-191`:** o PO tinha lido que o cliente do middleware tem a sua instância, da qual é o dono. O dono respondeu que não. A `D-191` continua valendo no resto: as permissões de saída moram no Horus, nas configurações da instância, e o middleware é por instância, e não por organização.
**Contexto:** confirmação final da terceira dúvida do `I-020`. O PO perguntou duas vezes quem é o dono da instância, e a resposta desfez a leitura de que o cliente seria o dono.
**Por que esta:** o Horus continua uma frota só, operada pela Maind, e o cliente governa o caminho pelo middleware (IP e porta). Abre-se mão de o cliente ser o dono do que sai: ⚠️ quem liga as saídas da `D-189` é o dono da instância, a Maind, e o cliente só se protege pelo contrato e pelo controle do middleware (por exemplo, cortando o acesso por IP e porta). Essa lacuna é a dúvida seguinte.
**Fica de fora / adiado:** a instância dedicada de propriedade do cliente.
**Hipóteses a validar:** 🔎 que a cibersegurança do cliente aceite que a Maind ligue as saídas, com o controle do middleware como limite.
**Prova de valor:** a Maind cria uma instância para um cliente em pouco tempo, e o cliente conecta o middleware a ela.
**Reabrir quando:** um cliente exigir ser dono da instância, ou o controle de criação de instâncias não der conta do volume.

### D-191 · As permissões de saída moram no Horus, nas configurações da instância, e o middleware é por instância
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, em resposta própria, fora das opções do PO; a leitura do PO sobre o cliente ter a sua instância foi corrigida pela `D-192`; a parte que dá as permissões ao dono da instância foi corrigida pela `D-193`) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** as **permissões do que pode sair da casa do cliente** (`D-189`: o comando da consulta gerada, o CSV dos dados e outras saídas) **moram no Horus**, nas **configurações da instância**, e quem as liga é o **dono da instância**. O **middleware é por instância**, e **não por organização** (por enquanto): uma instância tem um middleware, que serve às organizações dela.
**Corrige a leitura do PO na `D-190`:** o PO tinha lido que "não há instância dedicada por cliente". A leitura estava errada: se o middleware é por instância e o dono da instância decide o que sai, o cliente do middleware tem **a sua instância**. Se ela é hospedada pela Maind (o Horus "permanece SaaS") e o cliente é o dono, é a dúvida de confirmação seguinte do `I-020`.
**Contexto:** quarta dúvida do `I-020`. O PO propôs a permissão no middleware, configurada pela TI do cliente (nota 79), nos dois níveis (72) ou no Horus pelo owner da organização (55). O dono respondeu: no Horus, pelo dono da instância.
**Por que esta:** a configuração fica no produto e na mão de quem é dono da instância, e o middleware serve a todas as organizações dela. Abre-se mão de a TI do cliente controlar a permissão no próprio middleware: ⚠️ a governança de cibersegurança do cliente cobre o caminho (IP e porta, `D-190`), mas não o que o Horus pede.
**Fica de fora / adiado:** o middleware por organização.
**Hipóteses a validar:** 🔎 que o dono da instância seja alguém que a cibersegurança do cliente aceite como responsável pelo que sai.
**Prova de valor:** o dono de uma instância liga, na configuração dela, a saída do comando da consulta, e as pessoas passam a ver o SQL na resposta; desligada, não vêem.
**Reabrir quando:** um cliente precisar de middlewares diferentes para organizações da mesma instância, ou a TI de um cliente exigir controlar a permissão no middleware.

### D-190 · O middleware é um servidor MCP na infraestrutura do cliente; o Horus continua SaaS e o usa para chegar aos dados, à internet e à IA
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, em resposta própria, fora das opções do PO; a leitura do PO sobre a instância dedicada foi corrigida pela `D-191`; o protocolo "servidor MCP" ficou em aberto pela `D-196`) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** o **middleware** (`D-188`) é um **servidor MCP**, hospedado **na infraestrutura do cliente**, com **permissão de acesso por IP e porta**, configurada ponto a ponto: o cliente define quem alcança o middleware e o que o middleware alcança. O **Horus continua SaaS**: ele usa o middleware **para acessar os dados do cliente e para sair para a internet e para a IA**. Assim, o time de cibersegurança e de infraestrutura do cliente governa todo o caminho de saída do que é dele.
**Contexto:** terceira dúvida do `I-020`. O PO perguntou se o cliente do middleware teria uma instância própria, hospedada pela Maind, com o cliente como administrador (nota 76), ou se usaria a instância compartilhada (62). O dono respondeu fora das duas: o Horus **permanece SaaS**, e o que muda é o middleware do cliente. Não há instância dedicada por cliente.
**Leitura do PO** *(a confirmar com o dono)*: o middleware é a **porta única** do cliente: tudo o que o Horus lê dos dados dele, e tudo o que vai à internet e à IA em nome dele, passa por ele. Isso é compatível com a `D-189`: o Horus pede, e o middleware acessa os dados, a IA e a internet e devolve a resposta pronta.
**Por que esta:** o cliente mantém a governança sobre o que sai, com as ferramentas que a TI dele já usa (regras de IP e porta), e a Maind opera uma frota só. Abre-se mão de a Maind controlar a qualidade do caminho: ⚠️ a disponibilidade e o desempenho do middleware dependem da infraestrutura do cliente.
**Fica de fora / adiado:** onde moram as permissões de saída da `D-189` (no middleware ou no Horus), que é a dúvida seguinte; a instância dedicada por cliente.
**Hipóteses a validar:** 🔎 que a TI dos clientes aceite hospedar um servidor MCP; 🔎 que o desempenho da pergunta de análise, passando pelo middleware, seja aceitável.
**Prova de valor:** um cliente instala o middleware, libera o IP do Horus no firewall e faz uma pergunta de análise que acessa o banco dele sem nenhuma porta aberta além da combinada.
**Reabrir quando:** a TI dos clientes não aceitar hospedar o middleware, ou o desempenho pelo middleware não servir.

### D-189 · Pelo middleware, só a pergunta e a resposta pronta saem da casa do cliente; o dono da instância pode permitir mais
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, em resposta própria: a opção recomendada, com uma extensão dele) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** pelo middleware (`D-188`), **o que sai da casa do cliente para a Maind é só a pergunta e a resposta pronta**, os blocos que a pessoa vê. O **dono da instância** pode **permitir mais, nas configurações da instância**: o **comando da consulta gerada**, o **CSV dos dados** e **outras saídas que possam ser consideradas vazamento**. Cada saída é uma permissão do dono da instância; sem ela, a saída não acontece.
**Leitura do PO** *(a confirmar com o dono)*: cada saída é uma permissão **separada, desligada por padrão**, e quem a liga assume a responsabilidade (como o gestor, `D-054`, e o owner, `D-164`). A lista completa das saídas que contam como vazamento (por exemplo, o esquema, as linhas lidas e a cópia de um resultado para o suporte) fica para o desenho. **Quem é o dono da instância do cliente do middleware** é a dúvida seguinte do `I-020`.
**Contexto:** segunda dúvida do `I-020`. O PO propôs três portas: só a resposta pronta (nota 78), também o SQL e o esquema (71) e também as linhas (58). O dono escolheu a primeira como padrão e acrescentou que o dono da instância pode abrir as outras.
**Por que esta:** o padrão é a promessa que a cibersegurança do cliente aceita, e o dono da instância decide, instância por instância, o que mais pode sair. Abre-se mão de um suporte da Maind com visão do que acontece no cliente: ⚠️ no padrão, o suporte fica no escuro, e só vê mais se o dono da instância permitir.
**Fica de fora / adiado:** a lista completa das saídas; como o suporte da Maind diagnostica um erro sem ver o esquema.
**Hipóteses a validar:** 🔎 que os clientes aceitem a pergunta e a resposta pronta passarem pela Maind; 🔎 que os donos de instância liberem o que o suporte precisa quando precisar.
**Prova de valor:** um cliente de cibersegurança rígida usa o Horus pelo middleware e confirma que nada além da pergunta e da resposta saiu de casa; depois, o dono da instância libera o CSV de um resultado.
**Reabrir quando:** o suporte não conseguir diagnosticar erros sem ver o esquema, ou um cliente exigir que nem a pergunta saia.

### D-188 · A casa do contratante é atendida primeiro por um middleware; a instalação completa do Horus só volta se um cliente exigir
Situação: ⚪ substituída em parte pela `D-260` (o middleware deixa de ser da v2.1, onda 2, e passa a ser da v2.0; a instalação completa continua sem versão) · antes: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada; a ideia do middleware é do dono) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** a onda 2 da v2.1 (`D-181`) passa a ser um **middleware**: uma peça instalada na infraestrutura do contratante, que conversa com o Horus e vai até o modelo de IA, às bases de dados e às análises, para o time de cibersegurança e de infraestrutura do cliente manter a governança. O **Horus fica sempre na Maind**, em uma frota e uma versão só. A **instalação completa do Horus no contratante** (o on-premises da `D-007`) **só volta se um cliente exigir** que nada, nem a pergunta, saia de casa.
**Substitui em parte a `D-181`:** a composição da onda 2 (a ativação dos assentos no on-premises, a rede interna e o "tudo dentro"). As decisões `D-175`, `D-176`, `D-185`, `D-186` e `D-187` valem para a instalação completa, que passa a ser a porta de volta, e deixam de ser da onda 2.
**Contexto:** impasse `I-020`. O dono propôs o middleware ao ver as opções do que a Maind exige do contratante (a `ARQ-060` pedia um Kubernetes). O padrão tem precedente (o gateway de dados local do Power BI) e a `ARQ-052` o listou como a opção 3, deixada de fora por ser "quase o on-premises".
**Opções avaliadas** (nota provisória de 0 a 100, pesos da `D-015`, com a suposição de que o middleware executa e o Horus orquestra): **C. Primeiro o middleware, a instalação completa só se um cliente exigir: 77 (escolhida; recomendação do PO)** · A. O middleware substitui de vez: 75 · B. As duas formas convivem na onda 2: 68. C e A ficaram a menos de 5 pontos, e o desempate foi a reversibilidade.
**Por que esta:** atende à maior parte dos clientes com uma frota só e deixa a instalação completa como porta de volta. Abre-se mão do "tudo dentro" total: ⚠️ com o Horus na Maind, a pergunta e a resposta passam por ela, e só o dado bruto fica em casa.
**Fica de fora / adiado:** a instalação completa, até um cliente exigi-la; o desenho do middleware (o que ele faz e o que sai da casa do cliente), que são as dúvidas seguintes do `I-020`.
**Hipóteses a validar:** 🔎 que a maioria dos clientes aceite que a pergunta e a resposta passem pela Maind.
**Prova de valor:** um cliente que não admite os dados fora de casa usa o Horus pelo middleware, sem instalar o Horus.
**Reabrir quando:** um cliente exigir que nada saia de casa, nem a pergunta, ou o middleware não der conta do que o on-premises daria.

### D-187 · O owner da organização alcança qualquer endereço interno; o administrador da instância não limita as redes
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** no on-premises, o **owner da organização** que autoriza uma fonte (`D-186`) pode apontá-la para **qualquer endereço interno** da rede do contratante. O **administrador da instância não limita** as redes que os owners alcançam: não há uma lista de redes permitidas.
**Contexto:** segunda parte da dúvida da `MF-104:Conectar as fontes vivas` na onda 2 da v2.1. A `D-040` usa dois andares para os conectores de saída (o administrador libera o tipo, e o owner liga dentro do que foi liberado); o PO propôs o mesmo desenho para a rede interna.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): A. O administrador define as redes permitidas, e o owner escolhe dentro delas: 77 (recomendação do PO) · **B. O owner alcança qualquer endereço interno: 58 (escolhida)**.
**Por que esta:** uma configuração a menos, e a confiança fica com o owner de cada organização. Abre-se mão de proteger servidores que o contratante não queria expostos: ⚠️ um owner pode apontar uma fonte para um servidor que não devia alcançar, e a guarda de rede só confere o endereço de cada operação.
**Fica de fora / adiado:** a lista de redes permitidas, definida pelo administrador da instância.
**Hipóteses a validar:** 🔎 que os owners das organizações do cliente apontem só o que devem.
**Prova de valor:** o owner de uma organização autoriza uma fonte a um banco da rede interna sem precisar do administrador da instância.
**Reabrir quando:** um owner apontar uma fonte para um servidor que o contratante não queria exposto, ou um cliente exigir limitar as redes.

### D-186 · O owner de cada organização autoriza, fonte por fonte, o alcance à rede interna
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, a opção de menor nota) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** no on-premises, é o **owner de cada organização** quem **autoriza, fonte por fonte**, que a fonte alcance a rede interna do contratante. Sem a autorização, a fonte não alcança endereço interno, como hoje (`ARQ-052`).
**Contexto:** parte da `MF-104:Conectar as fontes vivas` na onda 2 da v2.1 (`D-181`). A guarda de rede da v1.xx impede a fonte da organização de alcançar endereços internos; no on-premises, o banco do contratante mora na rede dele.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): A. O administrador da instância libera, com uma chave só: 71 (recomendação do PO) · B. O administrador libera, organização por organização: 69 · **C. O owner de cada organização libera, fonte por fonte: 54 (escolhida)**.
**Por que esta:** a decisão fica com quem conhece a fonte e a organização. Abre-se mão de um controle central: ⚠️ o owner da organização poderia apontar uma fonte para qualquer servidor da rede, mesmo um que não devesse alcançar. Esse risco é a dúvida seguinte.
**Fica de fora / adiado:** a chave única da instância; a liberação por organização pelo administrador.
**Hipóteses a validar:** 🔎 que os owners das organizações do cliente saibam o que podem apontar.
**Prova de valor:** o owner de uma organização autoriza uma fonte a alcançar o banco na rede interna do cliente, e a fonte responde; sem a autorização, a fonte é recusada.
**Reabrir quando:** uma fonte alcançar na rede interna um servidor que o contratante não queria exposto.

### D-185 · No modo "tudo dentro", o contratante traz o próprio modelo de IA
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.1 (onda 2)

**Decisão:** no modo **"tudo dentro"** (`D-010`), a IA vem de **um modelo que o contratante traz**: ele aponta o endereço do modelo dele, que fala o protocolo compatível com o da OpenAI, e o Horus o usa como mais uma conexão de IA da organização. A Maind **não empacota modelo nem máquina**. No modo, **nada sai** da infraestrutura do contratante: a pesquisa na web fica desligada e os conectores de saída ficam bloqueados até a instância liberar (`D-040`).
**Contexto:** a `ARQ-051` deixou "a IA dentro de casa da v2.1" para ser escolhida com o dono. A `D-010` criou o modo e adiou o que ele oferece.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. O contratante traz o próprio modelo: 81 (escolhida; recomendação do PO)** · C. Só o Amazon Bedrock na conta do contratante: 64 · B. A Maind entrega um modelo no pacote: 61.
**Por que esta:** não obriga a Maind a empacotar modelo nem máquina com GPU, e o contratante usa o que já tem ou escolhe o modelo que a segurança dele aceita. Abre-se mão de uma qualidade garantida: ⚠️ um modelo menor, em casa, responde pior que os de hoje, e o Horus não promete a mesma qualidade nesse modo.
**Fica de fora / adiado:** a Maind fornecer ou recomendar um modelo; a qualidade mínima aceita (`P-039`).
**Hipóteses a validar:** 🔎 que os contratantes que exigem "tudo dentro" já tenham um modelo próprio; 🔎 que a qualidade de um modelo em casa sirva à pergunta de análise.
**Prova de valor:** um contratante em "tudo dentro" aponta o modelo dele, faz uma pergunta de análise e recebe a resposta sem que nada saia de casa.
**Reabrir quando:** os contratantes não tiverem modelo próprio, ou a qualidade em casa não servir.

### D-184 · O login corporativo da onda 1 é só OpenID Connect; o SAML só com decisão nova
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.1 (onda 1)

**Decisão:** o login corporativo da `MF-106:Segurança dos dados por pessoa` (etapa 2, onda 1 da v2.1, `D-181`) usa **só o OpenID Connect**, ligado em cada organização pelo owner (`D-027`). O **SAML** só entra por decisão nova, quando um cliente-âncora o exigir.
**Contexto:** a `ARQ-054` propôs o protocolo, e a escolha muda o que o cliente precisa ter para ligar o login da empresa. Os grandes provedores de identidade de empresa falam OpenID Connect 🔎 (Microsoft Entra ID, Google Workspace, Okta). A Maind, o primeiro cliente (`D-009`), usa o Google Workspace.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. Só OpenID Connect: 70 (escolhida; recomendação do PO, por desempate de reversibilidade)** · B. OpenID Connect e SAML: 69 · C. Um intermediário de identidade na frente: 54. A e B ficaram a menos de 5 pontos.
**Por que esta:** cobre os provedores comuns sem peça nova na stack. Abre-se mão de quem só tem SAML: ⚠️ um cliente que só tenha SAML fica de fora até uma decisão nova.
**Fica de fora / adiado:** o SAML; o intermediário de identidade.
**Hipóteses a validar:** 🔎 que os clientes grandes usem provedores que falam OpenID Connect; 🔎 que o provedor do primeiro cliente da onda 1 o fale.
**Prova de valor:** uma pessoa de uma organização com o login da empresa ligado entra com o crachá da empresa, e o Horus lê dali a role dela.
**Reabrir quando:** um cliente-âncora exigir SAML ou outro protocolo.

### D-183 · A marca completa da onda 1 é logo, nome e e-mail em todo o produto; o tema continua sem versão
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada; a marca passou da v2.1 para a v2.0 pela `D-197` e depois ficou sem versão pela `D-200`) · Data: 05/11/2026 · Versão: v2.1 (onda 1), depois v2.0 (`D-197`), depois sem versão (`D-200`)

**Decisão:** a marca completa do contratante (`MF-101:Administração da instância`, onda 1 da v2.1, `D-181`) leva o **logo, o nome e o e-mail do contratante a todo o produto**, inclusive ao remetente das mensagens que o Horus envia. O **tema** (as cores e a aparência) **continua fora**, sem versão definida, como a `D-011` deixou.
**Contexto:** o `06-versoes.md` dizia "logo, nome e e-mail em todo o produto", e a `D-011` deixou o tema para "uma versão futura, ainda a ordenar". Como não há v2.2, o tema precisava de uma casa; o dono o manteve sem versão.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. Logo, nome e e-mail, sem o tema: 75 (escolhida; recomendação do PO)** · B. Também a cor principal: 67 · C. A aparência completa: 55.
**Por que esta:** entrega a marca do contratante com pouco trabalho, que é o que a `D-011` queria. Abre-se mão de o produto ter a cor do contratante: ⚠️ o produto continua com a aparência do Horus.
**Fica de fora / adiado:** o tema do contratante, sem versão.
**Hipóteses a validar:** 🔎 que os clientes não exijam uma cor própria.
**Prova de valor:** o contratante vê a própria marca em todo o produto e no remetente das mensagens, e o usuário final não encontra a marca da Maind.
**Reabrir quando:** um cliente exigir cor ou aparência próprias.

### D-182 · A onda 1 da v2.1 acrescenta o Teams e o Google Chat como conectores de saída
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era só o Google Chat; virou a `MF-122` pela `D-198`) · Data: 05/11/2026 · Versão: v2.1 (onda 1)

**Decisão:** na onda 1 da v2.1 (`D-181`), a `MF-113:Conectores de Saída` acrescenta o **Microsoft Teams** e o **Google Chat** ao e-mail e ao WhatsApp da v2.0 (`D-124`).
**Contexto:** o `06-versoes.md` trazia só "os demais conectores, como Teams e Google Chat 🔎". A Maind, o primeiro cliente (`D-009`), usa o Google Workspace; cada conector novo depende da aprovação da TI do cliente (`D-124`).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. Teams e Google Chat: 74 (escolhida)** · B. Só o Google Chat: 70 (recomendação do PO, por desempate de aprendizado) · C. Nenhum conector novo: 62. A e B ficaram a menos de 5 pontos.
**Por que esta:** cobre as duas plataformas de chat corporativo mais comuns de uma vez. Abre-se mão de uma onda 1 mais enxuta: ⚠️ são duas integrações novas, sem aprendizado prévio de um primeiro conector, e a demanda pelo Teams é hipótese.
**Fica de fora / adiado:** outros conectores (Slack, por exemplo).
**Hipóteses a validar:** 🔎 que os clientes usem o Teams; 🔎 que a TI dos clientes aprove os dois.
**Prova de valor:** o aviso de um agente chega a um canal do Teams e a um espaço do Google Chat.
**Reabrir quando:** a TI de um cliente não aprovar um dos dois, ou a onda 1 apertar.

### D-181 · A v2.1 sai em duas ondas: o SaaS primeiro, depois a casa do contratante
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada; a composição da onda 2 foi substituída pela `D-188` e, depois, a `MF-121` subiu para a v2.0 pela `D-260` e a onda 2 ficou sem mfs, a marca completa da onda 1 passou para a v2.0 pela `D-197` e depois ficou sem versão pela `D-200`, e os conectores de chat e o Athena viraram a `MF-122` e a `MF-123` pela `D-198`) · Data: 05/11/2026 · Versão: v2.1

**Decisão:** a v2.1 sai em **duas ondas**. A **onda 1, o SaaS**, leva a `MF-119:Investigação guiada` (`D-180`), a `MF-106:Segurança dos dados por pessoa` nas duas etapas, a marca completa do contratante (`MF-101`), os demais conectores de saída (`MF-113`) e o AWS Athena (`MF-104`, `D-161`). A **onda 2, a casa do contratante**, leva a ativação dos assentos no on-premises (`MF-103`, `D-175`, `D-176`), a fonte alcançando a rede interna (`MF-104`) e o modo "tudo dentro" (`MF-105`).
**Contexto:** o que trava a v2.1 no `06-versoes.md` incluía "a forma de entrega (de uma vez só ou em ondas)", que não tinha sido decidida. Para a v2.0, o dono escolheu uma entrega só (`D-109`). A v2.1 é grande e tem duas naturezas: o que serve ao SaaS e o que só faz sentido na casa do contratante, que espera um primeiro contratante-âncora (`ARQ-060`).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **B. Em duas ondas, o SaaS primeiro: 80 (escolhida; recomendação do PO)** · C. Cada mf sai quando ficar pronta: 71 · A. De uma vez só, como a v2.0: 54.
**Por que esta:** o valor chega mais cedo, e o on-premises espera quem o peça. Abre-se mão de uma v2.1 coesa numa entrega só: ⚠️ são duas entregas para coordenar.
**Fica de fora / adiado:** a divisão da onda 1 em partes menores; a data de cada onda.
**Hipóteses a validar:** 🔎 que a segurança por pessoa seja o que mais pese na onda 1; 🔎 que um contratante-âncora peça o on-premises depois da onda 1.
**Prova de valor:** a onda 1 chega a um cliente em SaaS sem esperar a casa do contratante.
**Reabrir quando:** um contratante-âncora exigir o on-premises antes da onda 1, ou a onda 1 crescer a ponto de pedir outra divisão.

### D-180 · Definição macro da MF-119:Investigação guiada
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.1

**Decisão:** a `MF-119:Investigação guiada` fica definida assim. Com ela, a `P-018` se fechou.
- **O que é:** a pessoa vê que um número ou gráfico mudou e aciona **"investigar"** na resposta (`D-177`). O Horus a conduz **passo a passo** (`D-178`): mostra as partes que mais explicam a variação (por loja, produto, período), a pessoa escolhe qual aprofundar, e cada passo traz a fonte à vista. O caminho **fica na conversa** (`D-179`).
- **Quem ganha:** quem faz perguntas de análise: **owner, gestor e membro full** (`D-069`). O membro leitor só vê boards, então não investiga. Qualquer área.
- **Decisão que passa a ser possível:** descobrir o **porquê** de uma variação sem abrir chamado à área de dados (`D-081`).
- **Prova de valor:** a gestora vê a margem do Sul cair numa resposta, aciona "investigar" e, em poucos passos, chega às lojas e ao produto que explicam a queda, cada passo com a fonte, sem chamado.
- **Retorno para o negócio:** autonomia (menos pedidos ao time de dados, `D-125`) e retenção: atende ao problema nº 2 do norte, que era o único sem nenhuma mf.
- **O que não inclui:** começar por pergunta em texto ou por aviso de agente (a pergunta em texto continua pela conversa); a decomposição inteira de uma vez; só a conclusão; fixar o caminho num board (`D-177` a `D-179`).
- **Depende de:** `MF-107:Perguntar aos dados em português`; `MF-108:Respostas visuais` (a ação "investigar" nos blocos); `MF-106:Segurança dos dados por pessoa` (cada passo no acesso de quem investiga); `MF-109:A web como fonte` e o nível de inferência (a causa vinda de fora dos dados só aparece a partir do nível 4, `D-130`).
- **Valor:** **essencial** para a promessa do problema nº 2 do norte.
- **A nota:** a nota provisória (61, `D-104`) continua; só seria refeita se a mf voltasse a disputar a v2.0.
**Contexto:** a necessidade nasceu na `D-081`, e a definição foi adiada pelo dono (`D-104`) por pedir muita conversa. As três dúvidas de desenho foram respondidas em 05/11/2026 (`D-177` a `D-179`), e o dono confirmou a definição completa.
**Por que esta:** entrega o caminho guiado de "o que mudou e por quê" que a conversa de hoje não dá, sem refazer a conversa: o caminho continua nela. Abre-se mão de levar a investigação a um board e de começar por aviso de agente.
**Hipóteses a validar:** 🔎 *(técnica, do arquiteto, `P-008`, letra (v))* que o motor comporte decompor uma variação nas partes que mais a explicam; 🔎 que o gestor chegue ao porquê sem abrir chamado.
**Reabrir quando:** o arquiteto derrubar a hipótese técnica, ou a medida de autonomia mostrar que a conversa já dá conta do problema nº 2.

### D-179 · O caminho da investigação guiada fica na conversa, como qualquer resposta
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.1

**Decisão:** o caminho percorrido numa investigação guiada (`MF-119:Investigação guiada`) **fica salvo na conversa**, como qualquer resposta do Horus, e a pessoa o reabre e continua. Fixar o caminho num board não entra na primeira entrega.
**Contexto:** terceira dúvida da `P-018`. A conversa já fica salva, e a pessoa já pode fixar uma resposta num board (`MF-112:Boards e Relatórios`).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. Só na conversa: 76 (escolhida; recomendação do PO)** · B. Na conversa, e a pessoa pode fixar o caminho num board: 74. A e B ficaram a menos de 5 pontos, e o desempate foi a reversibilidade.
**Por que esta:** reaproveita o que existe e mantém a primeira entrega enxuta. Abre-se mão de levar o caminho à reunião de resultado num board: ⚠️ para mostrar a investigação a outros, a pessoa compartilha a conversa ou fixa as respostas uma a uma.
**Fica de fora / adiado:** fixar o caminho inteiro num board, com os passos e as fontes.
**Hipóteses a validar:** 🔎 que a pessoa queira mostrar a investigação a outras.
**Prova de valor:** a pessoa fecha a conversa, volta no dia seguinte e continua a investigação de onde parou.
**Reabrir quando:** as pessoas pedirem para fixar o caminho num board.

### D-178 · A investigação guiada conduz a pessoa passo a passo, e ela escolhe qual parte aprofundar
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.1

**Decisão:** na `MF-119:Investigação guiada`, o Horus conduz a pessoa **passo a passo**: mostra as partes que mais explicam a variação (por loja, produto, período) e a **pessoa escolhe qual aprofundar**. **Cada passo traz a fonte à vista**, como toda resposta do Horus.
**Contexto:** segunda dúvida da `P-018`. A `D-081` já descrevia o caminho como passo a passo.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. Passo a passo: 79 (escolhida; recomendação do PO)** · B. De uma vez, a decomposição inteira numa resposta: 74 · C. Só a conclusão: 53.
**Por que esta:** a pessoa mantém o controle e vê de onde vem cada parte, o que serve ao invariante "confiança antes de beleza". Abre-se mão da rapidez de uma resposta única.
**Fica de fora / adiado:** a decomposição completa numa resposta só; entregar só a conclusão.
**Hipóteses a validar:** 🔎 que o passo a passo não canse quem quer só o resultado; 🔎 *(técnica, do arquiteto, `P-008`)* que o motor comporte decompor a variação nas partes que mais a explicam.
**Prova de valor:** a gestora aciona "investigar" e, em poucos passos, escolhe as lojas e o produto que explicam a queda, cada passo com a fonte.
**Reabrir quando:** as pessoas pedirem a decomposição inteira de uma vez.

### D-177 · A investigação guiada começa pelo número ou gráfico que mudou
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.1

**Decisão:** na primeira entrega da `MF-119:Investigação guiada`, a pessoa **começa pelo número ou gráfico que mudou**: a resposta traz uma ação "investigar" que leva da variação ao porquê. Começar por uma pergunta em texto e por um aviso de agente não ficam proibidos; só não são a primeira porta.
**Contexto:** primeira dúvida da `P-018`, a que ficou sem resposta desde a `D-104`. A conversa de hoje já responde a perguntas em sequência, mas não tem um caminho guiado de "o que mudou e por quê" (`D-081`).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. Pelo número ou gráfico que mudou: 80 (escolhida; recomendação do PO)** · B. Pela pergunta em texto: 70 · C. Pelo aviso de um agente: 65.
**Por que esta:** é o momento da descoberta, e entrega o que a conversa de hoje não dá. Abre-se mão de começar pelo aviso do agente, que ligaria os problemas nº 2 e nº 3.
**Fica de fora / adiado:** começar pela pergunta em texto e pelo aviso de um agente.
**Hipóteses a validar:** 🔎 que a pessoa queira investigar a partir do número que viu.
**Prova de valor:** a gestora vê a margem do Sul cair numa resposta, aciona "investigar" e chega às lojas e ao produto que explicam a queda, sem abrir chamado.
**Reabrir quando:** as pessoas investigarem mais por pergunta em texto ou por aviso do que pelo número.

### D-176 · O arquivo de licença do on-premises traz um teto por tipo de assento para a instância inteira
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada; a leitura do PO sobre o assento de owner está a confirmar) · Data: 05/11/2026 · Versão: v2.1

**Decisão:** o arquivo de licença do on-premises (`D-175`) traz um **teto por tipo de assento para a instância inteira**: gestor, membro full e membro leitor (`D-069`). O **administrador da instância do contratante reparte** esses assentos entre as organizações dele, no mesmo painel do SaaS. A Maind não precisa saber quantas organizações existem.
**Leitura do PO** *(a confirmar com o dono)*: o assento de owner, que é grátis em cada organização (`D-123`), **não conta no teto**.
**Contexto:** segunda parte da pendência `P-016`. No SaaS, a Maind libera os assentos por organização e por tipo; no on-premises, quem cria as organizações é o administrador do cliente (`D-146`).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. Um teto por tipo, para a instância inteira: 75 (escolhida; recomendação do PO)** · C. Um teto total, sem distinguir o tipo: 65 · B. Um teto por tipo e por organização: 62.
**Por que esta:** o cliente reparte os assentos como já faz no SaaS, e a Maind não emite um arquivo novo a cada organização. Abre-se mão de conferir a divisão entre as organizações: ⚠️ ela é do cliente.
**Fica de fora / adiado:** o teto por organização; o que acontece com a organização cujos assentos o cliente reduz abaixo do ocupado (vale a `D-076`).
**Hipóteses a validar:** 🔎 que os clientes on-premises tenham mais de uma organização.
**Prova de valor:** o administrador de um cliente on-premises importa o arquivo e reparte os assentos entre duas organizações, sem passar do teto de nenhum tipo.
**Reabrir quando:** um cliente exigir que a Maind controle o teto de cada organização.

### D-175 · No on-premises, a Maind controla os assentos por um arquivo de licença com chave
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era não ter trava técnica; a opção escolhida teve a nota mais alta, por 1 ponto) · Data: 05/11/2026 · Versão: v2.1

**Decisão:** numa instalação **on-premises**, a Maind emite um **arquivo de licença com chave**, que o administrador da instância do contratante importa. O arquivo dá o **teto de assentos** e funciona **sem internet**. Retoma a ideia do arquivo com chave que a `D-067` deixou de lado "por ora". No SaaS nada muda: o painel da instância libera os assentos (`D-067`, `D-068`).
**Contexto:** primeira parte da pendência `P-016`. No on-premises, a instância é operada pelo próprio cliente, que poderia liberar mais assentos do que contratou. A versão é a mesma nas duas formas de entrega (`D-017`), o produto não tem data de expiração (`D-068`) e a cobrança fica fora do produto (`D-080`).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **B. Arquivo de licença com chave: 69 (escolhida)** · A. Sem trava técnica, com o limite contratual: 68 (recomendação do PO, por desempate de reversibilidade) · C. Ativação online, a instância consulta a Maind: 57. B e A ficaram a menos de 5 pontos.
**Por que esta:** protege a receita e funciona sem internet, o que combina com o modo "tudo dentro" (`D-010`). Abre-se mão de uma v2.1 mais enxuta: ⚠️ é uma peça nova (assinar, importar e conferir o arquivo), e a v2.1 já leva o on-premises, a marca completa e o Athena (`D-121`, `D-161`).
**Fica de fora / adiado:** o que o arquivo traz (o teto vale para a instância ou para cada organização), que é a dúvida seguinte da `P-016`; uma data de validade do arquivo (o produto não tem expiração, `D-068`).
**Hipóteses a validar:** 🔎 que os contratantes aceitem um arquivo emitido pela Maind; 🔎 que a peça caiba na v2.1 (`P-037`).
**Prova de valor:** um cliente on-premises importa o arquivo, libera assentos até o teto e não consegue passar dele.
**Reabrir quando:** um cliente recusar o arquivo, ou a v2.1 não comportar a peça.

### D-174 · Definição macro da MF-120:Faixa de avisos e números
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; em parte substituída pela `D-204`: a mf deixa de ser a mais fácil de cortar e passa a indispensável) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** a `MF-120:Faixa de avisos e números` (nome provisório) fica definida assim. Com ela, a `P-027` se fechou.
- **O que é:** uma faixa contínua abaixo do cabeçalho, que passa **avisos** e **números do negócio**, com cards em duas categorias, cada uma com identidade visual própria: os **Instance Cards**, que o owner da instância configura, e os **Organization Cards**, que o owner da organização configura (`D-152`).
- **Quem ganha:** **todas as pessoas**, que veem os avisos e, dos números, só o que o acesso delas permite; **o owner da instância e o owner da organização**, que montam a faixa.
- **Decisão que passa a ser possível:** saber o que importa sem abrir nada nem perguntar (um aviso de manutenção, o número do dia); e o owner falar com todos sem mandar e-mail (`D-151`).
- **Prova de valor:** o aviso da instância aparece na faixa de todas as pessoas; o owner monta uma faixa com cinco cards, e cada pessoa vê só o que o acesso dela permite; poucas pessoas escondem a faixa.
- **Retorno para o negócio:** adoção (a faixa lembra o Horus a cada tela) e menos aviso por e-mail.
- **O que não inclui:** e-mail aos owners (`D-151`); horário por card (`D-171`); edição na própria faixa (`D-172`); componentes criados pelo owner e cards da Home na faixa (`D-170`, `D-173`); a página de manutenção (`D-154`).
- **Depende de:** `MF-101:Administração da instância` (o aviso da instância e a configuração dos Instance Cards); as preferências da organização (a configuração dos Organization Cards); `MF-106:Segurança dos dados por pessoa` (o acesso de quem vê, `D-167`); `MF-104:Conectar as fontes vivas`.
- **Valor:** **acelera**: aumenta a adoção, mas a v2.0 entrega valor sem ela.
- **As regras decididas:** os avisos são públicos (`D-170`), com hora de fim opcional e retirada à mão (`D-165`); os cards de número usam o acesso de quem vê a faixa (`D-167`) e o card sem acesso não aparece (`D-169`); a pessoa pode esconder a faixa inteira (`D-168`); o planejamento define quais cards passam e em que ordem (`D-171`), se monta em telas separadas (`D-172`) e usa um catálogo próprio de componentes (`D-173`).
**Contexto:** a ideia do dono de uma faixa contínua, o "painel infinito", nasceu da dúvida sobre o aviso da instância (`D-151`) e cresceu na `D-152`. As dúvidas de desenho foram respondidas em 05/11/2026 (`D-167` a `D-173`), e o dono confirmou a definição completa.
**Por que esta:** junta numa mf só o que é a mesma coisa para a pessoa (o que passa na faixa) e a separa da `MF-101` (quem administra a instância). Abre-se mão de ela ser essencial: ⚠️ é a mf mais fácil de cortar se a v2.0 apertar, e traz dois custos que o dono escolheu: dois catálogos (`D-173`) e números diferentes por pessoa, calculados um a um (`P-036`).
**Hipóteses a validar:** 🔎 que as pessoas não estranhem faixas diferentes; 🔎 que o catálogo próprio seja pequeno o bastante.
**Reabrir quando:** a v2.0 apertar a ponto de cortar mfs que não são essenciais, ou o cálculo por pessoa pesar.

### D-173 · A faixa tem um catálogo próprio de componentes, separado do da Home
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era um catálogo só com a Home) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** os componentes com que o owner monta a faixa de avisos e números (`MF-120`, nome provisório, `D-170`) formam um **catálogo próprio da faixa**, separado do catálogo de cards da Home (`MF-117:Home da organização`). Os cards de número da faixa são pensados para o formato dela.
**Contexto:** sétima e última dúvida da `P-027`, sobre a relação com a `MF-117` e a `MF-112`.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): A. Um catálogo só, com a Home: 87 (recomendação do PO) · **B. Um catálogo próprio da faixa: 62 (escolhida)**.
**Por que esta:** o dono quer componentes feitos para o formato da faixa, e não cards da Home espremidos. Abre-se mão de reaproveitar: ⚠️ é um segundo conjunto de componentes para construir e manter, e o owner passa a ter dois catálogos.
**Fica de fora / adiado:** reaproveitar um card da Home na faixa.
**Hipóteses a validar:** 🔎 que o catálogo próprio da faixa seja pequeno o bastante para o custo de mantê-lo valer a pena.
**Prova de valor:** o owner escolhe, na tela de configuração da faixa, componentes feitos para ela, e a faixa os mostra.
**Reabrir quando:** os dois catálogos passarem a ter os mesmos componentes, ou o custo de manter dois pesar.

### D-172 · O planejamento de exibição da faixa se monta em telas de configuração separadas
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era montar na própria faixa, em modo de edição) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o planejamento de exibição da faixa (`MF-120`, nome provisório, `D-170`, `D-171`) se monta em **telas de configuração separadas**: o owner da instância monta os **Instance Cards** na administração da instância (`MF-101:Administração da instância`), e o owner da organização monta os **Organization Cards** nas preferências da organização. A faixa em si não tem modo de edição.
**Contexto:** sexta dúvida da `P-027`. Mudar ou criar um gesto é decisão do dono.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): B. Na própria faixa, em modo de edição: 74 (recomendação do PO) · **A. Em telas de configuração separadas: 70 (escolhida)** · C. Dentro da Home da organização: 67. A e B ficaram a menos de 5 pontos.
**Por que esta:** a configuração fica num lugar previsível e à parte do que as pessoas veem, e a faixa continua só de leitura. Abre-se mão de ver o resultado enquanto se monta: ⚠️ o owner configura sem ver a faixa como ela fica.
**Fica de fora / adiado:** uma prévia da faixa dentro da tela de configuração; um modo de edição na própria faixa.
**Hipóteses a validar:** 🔎 que o owner acerte a montagem sem ver a faixa ao vivo.
**Prova de valor:** o owner da organização monta, na tela de preferências, uma faixa com cinco cards, e as pessoas a veem como montada.
**Reabrir quando:** os owners errarem a montagem com frequência ou pedirem para editar na própria faixa.

### D-171 · O planejamento de exibição da faixa define só quais cards passam e em que ordem
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o **planejamento de exibição** que o owner monta na faixa (`MF-120`, nome provisório, `D-170`) define **quais cards passam e em que ordem**. Não define dias nem horários por card. O horário de um aviso continua sendo o dele (`D-165`).
**Contexto:** quinta dúvida da `P-027`: o tamanho do "planejamento de exibição" que o dono citou na `D-170`.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. Só quais cards e em que ordem: 77 (escolhida)** · B. Também quando cada card aparece: 62.
**Por que esta:** é simples de montar e de entender, e o aviso já tem datas próprias. Abre-se mão de mostrar um card só em certos dias ou horas.
**Fica de fora / adiado:** horários e dias por card.
**Hipóteses a validar:** 🔎 que os owners não precisem de horário por card.
**Prova de valor:** o owner monta uma faixa com cinco cards numa ordem e as pessoas os veem nessa ordem.
**Reabrir quando:** os owners pedirem horários por card.

### D-170 · Os avisos da faixa são públicos, e o owner monta um planejamento de exibição com os componentes que o produto oferece
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, em resposta própria, fora das opções do PO) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** na faixa de avisos e números (`MF-120`, nome provisório, `D-152`): (1) os **avisos são públicos**: todas as pessoas os veem; (2) **o owner decide o que colocar** na faixa, o owner da instância nos Instance Cards e o owner da organização nos Organization Cards; (3) a faixa é montada por **N componentes que o produto disponibiliza**, com os quais o owner monta um **planejamento de exibição dos dados**.
**Leitura do PO** *(a confirmar com o dono)*: quem vê cada card de número é **quem tem acesso à fonte dele** (`D-167`, `D-169`). Os números da instância, que só os administradores acessam, só eles veem. Não há uma configuração de público por card. O que o "planejamento de exibição" inclui (só quais cards e em que ordem, ou também quando cada um aparece) é a dúvida seguinte da `P-027`.
**Contexto:** quarta dúvida da `P-027` (quem vê cada categoria). O PO perguntou se os números da instância são só dos administradores ou também do owner da organização (notas 79 e 72); o dono respondeu fora das duas.
**Por que esta:** o owner conhece o que importa à organização, e os componentes prontos mantêm a faixa consistente e sujeita ao acesso por pessoa. Abre-se mão de uma regra fixa de público por categoria: ⚠️ cada owner pode montar faixas muito diferentes.
**Fica de fora / adiado:** o owner criar componentes próprios (só os que o produto oferece); a lista dos componentes.
**Hipóteses a validar:** 🔎 que um catálogo de componentes prontos baste.
**Prova de valor:** o owner da organização monta uma faixa com dois avisos e três números, e cada pessoa vê só o que o acesso dela permite.
**Reabrir quando:** os owners pedirem componentes que o catálogo não tem.

### D-169 · O card de número ao qual a pessoa não tem acesso não aparece na faixa dela
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** na faixa de avisos e números (`MF-120`, nome provisório), o card de número ao qual a pessoa **não tem acesso não aparece**: a faixa dela mostra só o que ela pode ver, e ninguém descobre que existe um número que não pode ver.
**Contexto:** terceira dúvida da `P-027`, consequência da `D-167` (os cards de número usam o acesso de quem vê a faixa).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. O card some: 80 (escolhida)** · B. O card aparece vazio, com "sem acesso": 60.
**Por que esta:** o título de um card já é informação do negócio ("Margem do Sul"), e a faixa fica limpa. Abre-se mão da transparência de quem quer saber o que não vê: ⚠️ faixas de pessoas diferentes ficam diferentes.
**Fica de fora / adiado:** um aviso de que há cards escondidos.
**Hipóteses a validar:** 🔎 que as pessoas não estranhem faixas diferentes.
**Prova de valor:** uma pessoa sem acesso à fonte de um card abre a faixa e não vê nem o card nem o título dele.
**Reabrir quando:** pessoas pedirem para saber que existem números que não veem.

### D-168 · Cada pessoa pode esconder a faixa de avisos e números inteira
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era esconder só os números) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** cada pessoa pode **esconder a faixa inteira** (`MF-120`, nome provisório, `D-152`), avisos e números, e mostrá-la de novo quando quiser. Leitura do PO *(a confirmar com o dono)*: a faixa nasce visível, e a escolha é uma preferência da própria pessoa, no perfil.
**Contexto:** segunda dúvida da `P-027`. A faixa traz avisos, que precisam chegar (`D-151`), e números, que são conveniência.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): C. A pessoa esconde os números, mas não os avisos: 78 (recomendação do PO) · B. Não esconde nada: 64 · **A. Esconde a faixa inteira: 60 (escolhida)**.
**Por que esta:** o dono quis que cada pessoa decida o que ocupa a própria tela. Abre-se mão de que todo aviso chegue a todas as pessoas: ⚠️ quem esconde a faixa não vê o aviso da instância nem o do owner. O aviso de indisponibilidade chega pela página de manutenção (`D-154`), que não depende da faixa.
**Fica de fora / adiado:** uma exceção para avisos críticos (hoje não há).
**Hipóteses a validar:** 🔎 que poucas pessoas escondam a faixa; 🔎 que a página de manutenção cubra os avisos que não podem ser perdidos.
**Prova de valor:** uma pessoa esconde a faixa, e ela continua escondida na sessão seguinte.
**Reabrir quando:** um aviso importante deixar de chegar por causa da faixa escondida.

### D-167 · Os cards de número da faixa calculam os dados com o acesso de quem vê a faixa
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era o acesso do owner que configurou o card) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** na faixa de avisos e números (`MF-120`, nome provisório, `D-152`), os cards de **número do negócio** calculam os dados com o **acesso de quem vê a faixa**: cada pessoa vê só o que o acesso dela permite. Os **avisos** (da instância e do owner da organização) não dependem de acesso: todos os veem.
**Contexto:** primeira dúvida da `P-027`. O dono decidiu dois casos parecidos em sentidos diferentes: o board do espaço da organização usa o acesso de quem abre (`D-163`) e o board público, o do owner que o publicou (`D-164`).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): B. O acesso do owner que configurou o card: 80 (recomendação do PO) · **A. O acesso de quem vê a faixa: 73 (escolhida)** · C. O owner escolhe, card a card: 71.
**Por que esta:** segue o invariante de que quem pergunta vê só o que pode ver e evita que um owner libere dados pela faixa sem perceber. Abre-se mão de que todos vejam os mesmos números: ⚠️ a faixa mostra números diferentes, ou nada, a pessoas diferentes, e o cálculo é por pessoa (`P-036`).
**Fica de fora / adiado:** o que a pessoa sem acesso à fonte de um card vê no lugar dele (um card vazio ou nenhum card); fica entre as dúvidas que a `P-027` ainda tem.
**Hipóteses a validar:** 🔎 que calcular os cards por pessoa não pese na abertura da tela.
**Prova de valor:** duas pessoas com acessos diferentes veem a mesma faixa com números diferentes, cada uma só com o que o acesso dela permite.
**Reabrir quando:** os owners reclamarem de que a faixa não mostra o mesmo número a todos, ou o cálculo por pessoa pesar.

### D-166 · O relatório da organização se baixa em planilha e em PDF
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era só a planilha) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o administrador da instância baixa o relatório da organização (`D-149`, `D-157`) em **planilha** e em **PDF**.
**Contexto:** pendência `P-031` (Q14 da modelagem da `MF-101:Administração da instância`). O relatório traz o uso e o custo e a história completa dos assentos, com nomes. A Maind o usa para conferir a cobrança e para guardar o que ficou antes de excluir uma organização.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): A. Só planilha: 76 (recomendação do PO) · B. Só PDF: 72 · **C. Planilha e PDF: 69 (escolhida)**. A e B ficaram a menos de 5 pontos.
**Por que esta:** a planilha serve à conferência da cobrança, que pede somar e filtrar; o PDF serve a guardar e a mostrar o que ficou antes da exclusão. Abre-se mão de uma primeira entrega mais enxuta: ⚠️ são dois geradores.
**Fica de fora / adiado:** outros formatos.
**Hipóteses a validar:** 🔎 que a conferência da cobrança seja o uso principal da planilha e a guarda, o do PDF.
**Prova de valor:** o administrador baixa os dois arquivos de uma organização antes de excluí-la, e os números batem.
**Reabrir quando:** um dos dois formatos não for usado.

### D-165 · O aviso da instância pode ter hora de fim opcional e ser retirado à mão a qualquer momento
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o administrador da instância pode marcar uma **hora de fim opcional** no aviso que passa na faixa e pode **retirá-lo à mão a qualquer momento**. Sem hora de fim, o aviso fica até ser retirado.
**Contexto:** pendência `P-030` (Q13 da modelagem da `MF-101:Administração da instância`). A `D-151` fez o aviso passar só pela faixa, e a `D-152` ampliou a faixa. O modelo de dados já guarda os dois (o horário de fim e o evento `retirado`).
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **C. Os dois, horário opcional e retirar à mão: 73 (escolhida)** · A. Só o horário de fim, obrigatório: 64 · B. Só à mão: 60.
**Por que esta:** serve ao aviso de manutenção, que tem hora de acabar, e ao de instabilidade, que não tem, com uma data opcional e um botão. ⚠️ Um aviso sem hora de fim pode ficar esquecido na faixa.
**Fica de fora / adiado:** um limite máximo de duração para o aviso sem hora de fim.
**Hipóteses a validar:** 🔎 que o administrador use os dois casos.
**Prova de valor:** o administrador publica um aviso de manutenção com hora de fim e um de instabilidade sem hora de fim, e retira o segundo à mão.
**Reabrir quando:** ficarem avisos esquecidos na faixa.

### D-164 · O board público calcula os dados com o acesso do owner que o tornou público
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o board que o owner define como **público** (`D-048`), e que até a quarentena vê, **calcula os dados com o acesso do owner que o tornou público**, e mostra os mesmos números a todas as pessoas que o abrem. O owner **responde pelo que publica**, como o gestor responde pelo que libera (`D-054`). Os outros boards do espaço da organização seguem a `D-163`.
**Contexto:** impasse `I-019`. A `D-163` manda calcular o board com o acesso de quem o abre, e quem está na quarentena não tem acesso a dados: o board público apareceria vazio para quem a `D-048` quis atender.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **B. O acesso do owner que o tornou público: 73 (escolhida)** · C. O owner escolhe, board a board, entre o acesso de quem abre e o dele: 68 · A. O acesso de quem abre: 64.
**Por que esta:** o board público faz o que a `D-048` prometeu, e a responsabilidade fica com quem o publicou, por escolha explícita. Abre-se mão de uma regra única: ⚠️ este é o único caso em que um board entrega dados a quem não tem permissão para vê-los.
**Fica de fora / adiado:** o owner escolher, board a board, com qual acesso o board público roda (opção C).
**Hipóteses a validar:** 🔎 que o owner tenha acesso aos dados que publica (a `D-048` diz que o owner não é dono de dados); 🔎 que os owners entendam que publicar um board é liberar os números dele.
**Prova de valor:** um membro em quarentena abre um board público e vê os números, e o registro mostra qual owner o publicou.
**Reabrir quando:** um cliente quiser que o board público respeite o acesso de quem abre, ou o owner publicar um board com dado que não devia.

### D-163 · Os boards do espaço da organização calculam os dados com o acesso de quem os abre
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada; a leitura do PO sobre os agendamentos e os agentes foi confirmada pelo dono em 05/11/2026, junto com a de que, na v2.0, todas as pessoas da organização veem os mesmos dados, porque a organização é a fronteira, `D-145`) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** um board que está no **espaço da organização** (porque o autor saiu ou passou a leitor, `D-044`, `D-073`) **calcula os dados com o acesso de quem o abre**: cada pessoa vê só o que o acesso dela permite, e o mesmo board pode mostrar números diferentes a pessoas diferentes.
**Leitura do PO** *(a confirmar com o dono)*: os agendamentos e os agentes que vão para o espaço da organização ficam **pausados** (`D-073`) e, quando o owner os transfere (`D-044`), passam a rodar **em nome de quem os recebeu**, com o acesso dessa pessoa.
**Contexto:** impasse `I-018` (`A-11` do documento 14, letra (o) da `P-008`). O owner não é dono de dados (`D-048`), e o board perde o autor quando ele sai. A v1.xx roda o painel corporativo com acesso total.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **A. O acesso de quem abre: 78 (escolhida; era a recomendação do arquiteto e a do PO)** · B. Acesso total: 59 · C. O acesso do último autor, congelado: 51.
**Por que esta:** segue o invariante de que quem pergunta vê só o que pode ver e evita que o acesso de quem saiu da empresa continue valendo. Abre-se mão de números iguais para todos.
**Fica de fora / adiado:** o que os boards públicos mostram à quarentena (`D-048`): com o acesso de quem abre, quem está na quarentena não tem dados a ver. É o `I-019`.
**Hipóteses a validar:** 🔎 que o mesmo board mostrar números diferentes por pessoa seja bem aceito.
**Prova de valor:** dois membros com acessos diferentes abrem o mesmo board da organização e cada um vê só o que o seu acesso permite.
**Reabrir quando:** clientes estranharem números diferentes no mesmo board.

### D-162 · A web como fonte entra na v2.0 como o modelo poder sair à web quando autorizado
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, em resposta própria: esclareceu o que a peça é e que ela entra na v2.0) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o que o documento 14 chamava de "fonte de páginas web" entra na **v2.0**, entendido como **o modelo poder sair para a web quando autorizado**: a pesquisa na web já decidida (`D-130`, `D-131`) e desenhada na `ARQ-027`, em que só a pergunta vai à busca do provedor, o fato volta com o link e a data, e a pesquisa só roda onde a instância e a role da pessoa a autorizam. O dono a considera simples, e a v2.0 a entrega terminada.
**Contexto:** segunda parte do impasse `I-017` (`A-04` do documento 14). O PO a tinha descrito como um cadastro de páginas escolhidas, a partir do código da v1.xx (uma conexão do tipo `web`, que o chat lê no lugar de planejar uma consulta). O dono esclareceu que, para ele, a peça é a saída do modelo para a web quando autorizada.
**Opções avaliadas:** o PO propôs A (fora da v2.0), C (v2.1) e B (terminada na v2.0), com notas 68, 65 e 52. O dono respondeu fora das opções, com a leitura acima, que coincide com a B sem o cadastro de páginas.
**Por que esta:** a saída para a web autorizada é o que a pessoa espera de "a web como fonte" (`MF-109:A web como fonte`), já está desenhada e custa pouco. Abre-se mão de nada novo: o cadastro de páginas escolhidas, se existir como tipo de fonte, é assunto do arquiteto (`P-034`).
**Fica de fora / adiado:** o cadastro de páginas específicas como tipo de fonte, até o arquiteto confirmar o que a v1.xx tem e se a `ARQ-027` o cobre.
**Hipóteses a validar:** 🔎 que a "fonte de páginas web" da v1.xx e "o modelo sair à web" sejam, para o cliente, a mesma coisa.
**Prova de valor:** a pessoa liga a pesquisa na web e recebe um fato de fora com link e data (`D-130`).
**Reabrir quando:** um cliente pedir para cadastrar páginas específicas como fonte.

### D-161 · O AWS Athena sai da v2.0 e entra, terminado, na v2.1
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO, que era deixá-lo fora até um cliente pedir; virou a `MF-123` pela `D-198`) · Data: 05/11/2026 · Versão: v2.1

**Decisão:** o AWS Athena **não entra na v2.0**: ele passa a ser entregue **terminado na v2.1**, ou seja, o Horus passa a responder perguntas de análise com ele. Até lá, continua fora da tela, como no MVP (`D-139`), e a base herdada da v2.0 (`D-021`) deixa de contá-lo.
**Contexto:** primeira parte do impasse `I-017` (`A-04` do documento 14). Hoje o Athena só cadastra: o Horus não responde nada com ele. A v2.0 o contava como parte da `MF-104:Conectar as fontes vivas`, que é base herdada.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): A. Fora da v2.0, volta quando um cliente pedir: 68 (recomendação do PO) · **C. Entra na v2.1: 65 (escolhida)** · B. Entra terminado na v2.0: 47. A e C ficaram a menos de 5 pontos.
**Por que esta:** o dono quer a fonte entregue, com data, e não à espera de um cliente; a v2.0 não atrasa. Abre-se mão de espaço na v2.1: ⚠️ ela já leva o on-premises e a marca completa (`D-121`) e agora também uma fonte sem demanda conhecida.
**Fica de fora / adiado:** o Athena na v2.0.
**Hipóteses a validar:** 🔎 que haja organização que queira o Athena na v2.1; 🔎 que o conector e a segurança por pessoa, que hoje só cobre o SQL Server, caibam na v2.1 (do arquiteto, `P-033`).
**Prova de valor:** uma organização conecta um Athena e recebe uma resposta de análise.
**Reabrir quando:** a v2.1 não comportar o conector junto do resto, ou nenhum cliente o pedir até a v2.1.

### D-160 · Quando a organização usa o número de WhatsApp da Maind, ela paga as mensagens que gerar
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** quando uma organização **autoriza o uso do número da Maind** no WhatsApp (`D-097`), ela **paga as mensagens que gerar**: a Maind repassa o custo cobrado pela Meta, medido por organização na `MF-101:Administração da instância` (`ARQ-084`), e a cobrança fica **fora do produto** (`D-080`, `D-116`). Quem usa o **próprio número** paga a Meta diretamente, como já decidido na `D-097`.
**Contexto:** segunda parte do impasse `I-016` (`A-03` do documento 14), a primeira foi a `D-159`. A conta da Maind no WhatsApp custa de US$ 70 a 250 por mês para a instância inteira 🔎 (documento 13), e usar o número da Maind é uma escolha da organização, ao contrário da IA.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **B. A organização paga o que usar: 75 (escolhida)** · A. A Maind absorve e embute no assento: 66.
**Por que esta:** o custo fica transparente por organização, e a Maind não subsidia uma conveniência que o cliente escolheu. Abre-se mão da simplicidade de um preço só: a Maind precisa cobrar por fora do plano de assentos o que a organização consumir.
**Fica de fora / adiado:** como e quando a Maind faz a cobrança (é comercial e financeiro, fora do produto); uma franquia de mensagens incluída no assento.
**Hipóteses a validar:** 🔎 a faixa de custo da conta da Maind; 🔎 o volume de mensagens que agentes e avisos geram por organização.
**Prova de valor:** a Maind consulta, na `MF-101`, o custo de WhatsApp de uma organização que usa o número dela e o repassa.
**Reabrir quando:** o custo repassado desestimular o uso do número da Maind, ou a Maind quiser incluir uma franquia no assento.

### D-159 · No SaaS, a Maind paga a IA de todas as organizações e a embute no preço do assento
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, com a opção recomendada; em parte substituída pela `D-216`: a Maind paga só a conexão da instância, e a organização pode ter a dela; e, depois, pelas `D-266` e `D-267`: não há mais conexão da instância, e a Maind paga só a chave que dá à organização) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** no SaaS, a **conta do provedor de IA é da Maind**: ela paga a IA de todas as organizações, e o custo vai **embutido no preço do assento** (`D-115`). A organização não abre conta no provedor nem compra crédito para obter a primeira resposta de análise. O **aviso de custo** da `MF-101:Administração da instância` (`ARQ-017`) vigia o consumo de cada organização. No on-premises, o contratante é o dono da instância e paga a própria conta.
**Contexto:** primeira parte do impasse `I-016` (`A-03` do documento 14). No envelope do primeiro ano, a IA é quase todo o custo variável, de US$ 220 a 770 por organização por mês 🔎 (documento 13). A segunda parte, o WhatsApp, segue aberta no `I-016`.
**Opções avaliadas** (nota de 0 a 100, pesos da `D-015`): **B. A Maind paga a IA e embute no assento: 77 (escolhida)** · C. A organização escolhe entre a conta da Maind e a própria: 73 · A. O cliente traz a própria conta: 54. B e C ficaram a menos de 5 pontos, e o desempate foi a reversibilidade: B pode virar C depois, e C não volta a B sem tirar uma função de quem já a usa.
**Por que esta:** o cliente não tem trabalho nenhum antes da primeira resposta útil, que é o critério de maior peso. Abre-se mão de que a Maind carrega o risco do consumo: se uma organização usar muito mais que o previsto, quem paga é a Maind, e o preço do assento (`P-022`) precisa cobrir a média.
**Fica de fora / adiado:** a organização trazer a própria conta de IA (opção C), que pode entrar depois sem desfazer esta decisão.
**Hipóteses a validar:** 🔎 a faixa de US$ 220 a 770 por organização por mês; 🔎 que o preço do assento cubra o consumo médio.
**Prova de valor:** uma organização nova faz a primeira pergunta de análise sem abrir conta em provedor de IA.
**Reabrir quando:** o consumo médio por organização passar do que o preço do assento cobre, ou clientes exigirem usar a própria conta.

### D-158 · O administrador da instância pergunta ao próprio Horus sobre a história dos dados da instância
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, ao seguir as recomendações; a `D-274` tirou o nome de quem ocupa o assento da resposta, e a `D-276` a manteve, com uma chave de IA da instância só para ela) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o administrador da instância faz perguntas em linguagem natural ao próprio Horus sobre a **história** da instância: quem ocupou cada assento e quando, os cortes e as reativações, os administradores, os limiares de custo cruzados, as mudanças de situação das organizações. A resposta traz o **nome** de quem ocupou (`D-157`). Para isso a história tem um banco próprio, consultável como uma fonte de dados (`ARQ-097`).
**Contexto:** na modelagem da `MF-101:Administração da instância`, o dono pediu que os dados representem o processo e o histórico, e que se possa apontar para um momento do tempo; e lembrou que o próprio Horus será usado para perguntar sobre esses dados. Esta decisão substitui as dúvidas Q16 e Q17 da modelagem (a Maind consulta o registro de administração e os avisos de custo por uma tela).
**Opções avaliadas:** A) o Horus pergunta sobre o banco de log (recomendada, escolhida) · B) uma tela própria para cada consulta (a Q16 e a Q17 originais). Sem pontuação: decisão pequena e reversível.
**Por que esta:** reaproveita o que o produto já faz, em vez de construir telas de consulta. Abre-se mão de relatórios prontos para cada pergunta: a resposta é tão boa quanto o Planejador entende o modelo da história.
**Fica de fora / adiado:** o owner da organização perguntar sobre a história da organização dele (pediria regra por linha, que hoje só existe para SQL Server); o rastro da `MF-116`, que continua na organização (`D-091`).
**Hipóteses a validar:** 🔎 que o Planejador responda bem sobre as tabelas de log; 🔎 que a guarda de rede aceite o banco de log como fonte da instância.
**Prova de valor:** o administrador pergunta "quem ocupava os assentos da organização X em 15/05?" e recebe a lista com os nomes.
**Reabrir quando:** o Planejador errar a pergunta com frequência, ou o owner da organização pedir o mesmo para a organização dele.

### D-157 · O relatório da organização mostra a história completa dos assentos, com o nome de quem os ocupou
Situação: ⚪ substituída em parte pela `D-274` (a história segue, mas sem o nome de quem ocupou o assento) · antes: 🟢 decidida (confirmada pelo dono em 05/11/2026; escolheu contra a recomendação do PO; a leitura sobre a `D-091.1` foi confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o relatório da organização (`D-149`) mostra, além dos assentos de hoje, a **história de cada assento**: quem o ocupou (com o nome da pessoa) e quando, as reservas por convite, as devoluções, os cortes e as reativações. Substitui **só** o trecho da `D-149` que dizia "sem histórico"; o resto da `D-149` segue (relatório a qualquer momento, uso apagado junto com a organização).
**Contexto:** o dono corrigiu a modelagem da `MF-101:Administração da instância` em 05/11/2026: os dados precisam representar o processo e guardar o histórico, e cada assento passou a ser um registro, com o membro que o ocupa, a situação e a ocupação. Com a história gravada, a dúvida (Q15) foi se o relatório a mostra e com que detalhe.
**Opções avaliadas:** A) só a situação de hoje, com a história gravada e sem tela · B) a história em números, mês a mês, sem nome de pessoa (recomendação do PO) · **C) a história completa, com nomes (escolhida pelo dono)**. Sem pontuação: decisão pequena e reversível (a tela some sem perder a história gravada).
**Por que esta:** a Maind confere a cobrança e o suporte responde, para qualquer mês, quem ocupava cada assento. Abre-se mão de ficar só com números: ⚠️ o administrador da instância passa a ver o nome de quem ocupa cada assento de cada organização.
**Leitura do PO** *(confirmada pelo dono em 05/11/2026)*: isso não fere a `D-091.1`, que impede o owner da instância de consultar o **rastro de auditoria** das organizações. Quem ocupa um assento é dado de licenciamento, não conteúdo de conversa, de board nem de rastro, e a pessoa e a conta já são da instância (`ARQ-033`). O relatório segue sem conteúdo de organização.
**Fica de fora / adiado:** o relatório para o **owner da organização** (continua decisão à parte, como na `D-149`); o conteúdo das conversas, dos boards e do rastro.
**Hipóteses a validar:** 🔎 que os clientes aceitem que a Maind veja o nome de quem ocupa cada assento (no on-premises, o administrador é do contratante); 🔎 que o aviso de privacidade do produto cubra isso (LGPD, a conferir com o arquiteto no documento 07, Segurança).
**Prova de valor:** o administrador baixa o relatório de uma organização e confere, assento a assento, quem o ocupou e quando, inclusive o corte e a reativação.
**Reabrir quando:** um cliente recusar que a Maind veja o nome dos membros dele, ou a LGPD exigir minimização.

### D-156 · Quatro dúvidas da modelagem da MF-101 já tinham resposta nas decisões anteriores
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, ao seguir as recomendações; era proposta, leitura do PO) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** a modelagem de dados da `MF-101:Administração da instância` segue quatro leituras que decorrem de decisões já tomadas: (1) o `EmailContato` e o `Copyright` da v1.xx **não migram**, porque as páginas institucional e de propaganda saíram do produto (`D-011`); o rodapé da marca continua; (2) o painel **não marca** qual assento é o grátis, porque o preço fica fora do produto (`D-116`) e o produto só garante que a organização nasce com um assento de owner (`D-123`); (3) a **aparência** (o tema) fica fora da v2.0, como a `D-011` deixou para uma versão futura; (4) a **pergunta de análise respondida** é contada como na medida de autonomia da `MF-117:Home da organização` (`D-133`).
**Contexto:** a modelagem de dados da MF-101 (documento `modelo-de-dados/mf-101-gestao-da-instancia.md`, no repositório do backend da v2, de 05/11/2026) levantou doze dúvidas; estas quatro (Q4, Q8, Q10 e Q12) não precisaram de pergunta ao dono.
**Opções avaliadas:** nenhuma bifurcação: cada leitura repete uma decisão do dono. Sem pontuação.
**Por que esta:** reabrir uma decisão do dono sem fato novo não agrega valor; a leitura só a aplica ao modelo.
**Fica de fora / adiado:** o tema da marca (`D-011`) e o preço (`D-116`).
**Hipóteses a validar:** nenhuma nova.
**Prova de valor:** o modelo da MF-101 sai sem coluna de contato, de aviso legal, de tema nem de assento grátis, e a contagem de perguntas é a mesma da MF-117.
**Reabrir quando:** o dono pedir uma delas, ou a `D-133` mudar a definição de pergunta respondida.

### D-155 · O ritmo de envio de e-mail e o tempo de guarda do cache de prompt continuam na administração da instância
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, ao seguir as recomendações; era proposta, do PO) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o administrador da instância continua ajustando, pela tela de administração, os dois parâmetros que a v1.xx já tem: o **ritmo de envio de e-mail** da instância (de 1 a 600 por minuto; padrão 60) e o **tempo de guarda do cache de prompt**, isto é, por quanto tempo o produto reaproveita a parte repetida das instruções enviadas à IA (cinco minutos, uma hora ou desligado; padrão uma hora).
**Contexto:** dúvida Q5 da modelagem da MF-101. A `ARQ-046` fez do ritmo de e-mail o orçamento da instância, e as duas telas existem hoje na administração da v1.xx.
**Opções avaliadas:** manter os dois, como estão (recomendação do PO) · tirá-los da administração. Sem pontuação: decisão pequena e reversível.
**Por que esta:** não há ganho em esconder um ajuste que o administrador já usa. Abre-se mão de nada.
**Fica de fora / adiado:** qualquer parâmetro novo de desempenho.
**Hipóteses a validar:** 🔎 que os dois seguem úteis ao administrador da v2.0.
**Prova de valor:** o administrador muda o ritmo de e-mail e o tempo do cache sem mexer em arquivo.
**Reabrir quando:** o arquiteto de soluções mostrar que um deles deixou de fazer sentido.

### D-154 · Durante uma manutenção, uma página com a hora de volta substitui o app; a página pública do estado da instância fica fora da v2.0
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, ao seguir as recomendações; era proposta, do PO) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** quando a instância para para uma troca ou uma janela de manutenção, quem abre o app vê uma **página com o motivo e a hora de volta**, no lugar da tela de entrada funcionando com as respostas falhando. A **página pública do estado da instância** (um endereço aberto que mostra se o Horus está de pé) **fica fora da v2.0**.
**Contexto:** pendência `A-21` (agora `P-025`). Hoje, com a API parada, o servidor da web segue mostrando a tela de entrada e as respostas falham, e a pessoa conclui que o Horus quebrou (`horus@318db52b:infra/README.md`, "Sintoma que engana"). A `D-151` cobre o aviso antes da parada; esta cobre o durante. As duas partes são a recomendação do arquiteto de soluções (documento 14, `A-21`).
**Opções avaliadas:** a página de manutenção com a hora de volta (recomendada) · seguir como hoje · a página de manutenção mais a página pública do estado (cortada por ora). Sem pontuação: o caso é pequeno e o arquiteto já recomendou.
**Por que esta:** protege a confiança com custo pequeno; a página pública do estado serve a quem não é da casa e não resolve o caso principal. Abre-se mão de um endereço de estado para os contratantes.
**Fica de fora / adiado:** a página pública do estado; o aviso por e-mail aos owners (`D-151`).
**Hipóteses a validar:** 🔎 que as janelas de manutenção serão frequentes o bastante no começo para a página valer o custo.
**Prova de valor:** numa parada de manutenção, ninguém abre o app e vê uma tela de entrada funcionando seguida de falha; vê a hora de volta.
**Reabrir quando:** um contratante exigir uma página pública do estado, ou um incidente mostrar que só o aviso não basta.

### D-153 · Os números de uso, os assentos e o aviso de custo continuam na MF-101 e viram Instance Cards prontos
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026, ao seguir as recomendações; era proposta, leitura do PO) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o que o administrador da instância precisa ver de cada organização continua na `MF-101` como **dado** e como **card pronto da categoria Instance Cards** (`D-152`): os assentos liberados e ocupados por tipo; as perguntas de análise respondidas; as execuções de agente; o custo de IA do mês; as mensagens de WhatsApp e o custo; e os envios de e-mail (só a quantidade, porque o e-mail não conta em dinheiro, `ARQ-084`). Soma-se o **aviso de custo**: a Maind é avisada quando uma organização passa de um limite que ela ajusta caso a caso, e nada se corta sozinho (`ARQ-017`). A montagem do painel é da `MF-120`. Só números, nunca conteúdo (`D-091.1`), e o custo fixo de operação não entra (`ARQ-084`).
**Contexto:** pendência `A-29` (agora `P-026`). A hipótese era o painel mostrar esses números por organização e por mês. Perguntado entre os seis números como tela fixa (A) e só o essencial (B), o dono respondeu com outra ideia: o owner configura a exibição com componentes e KPIs previamente criados, em duas categorias (`D-152`). Esta decisão é a leitura do PO: os números viram o catálogo inicial dos Instance Cards, dentro da MF-101; quais o owner pode mostrar e onde é assunto da `MF-120` (`P-027`).
**Opções avaliadas:** A) os seis números como tela fixa · B) só assentos e custo de IA · cards prontos e configuráveis (a ideia do dono, `D-152`). Sem pontuação, porque a resposta do dono mudou a forma da pergunta.
**Por que esta:** casa com o que o dono pediu (cards prontos) sem espalhar o dado por mais de uma mf: quem produz o número é a MF-101; quem monta a tela é a MF-120.
**Fica de fora / adiado:** a montagem e a configuração do painel (`MF-120`, `P-027`); o histórico de assentos mês a mês (`D-149`).
**Hipóteses a validar:** 🔎 que esses números bastam ao primeiro catálogo; 🔎 que o motor de cards que a v1.xx já tem na Home da organização serve também à categoria da instância (a confirmar com o arquiteto de soluções).
**Prova de valor:** o administrador da instância vê, por organização e por mês, esses números e o aviso de custo, só em números.
**Reabrir quando:** o dono quiser outros números no catálogo, ou o aviso de custo se mostrar ruidoso.

### D-152 · A faixa de avisos e números entra na v2.0 como a MF-120 (provisória), com cards prontos em duas categorias
Situação: 🟢 decidida (o dono escolheu em 05/11/2026; a definição da mf está pendente, `P-027`) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** a v2.0 tem uma **faixa contínua** ("painel infinito") logo abaixo do cabeçalho do app, que passa informações diversas: os **avisos** e os **números do negócio** da organização. Os itens são **cards prontos** (componentes e KPIs previamente criados), e o owner configura a exibição, em duas categorias: **Instance Cards**, que só o owner da instância configura, e **Organization Cards**, que só o owner da organização configura. Cada categoria tem **identificação visual própria**, para distinguir o aviso do owner da instância do aviso do owner da organização. É uma **macro funcionalidade nova, a `MF-120`** (o próximo número livre; o nome é provisório), e fica fora da `MF-101`.
**Contexto:** ao decidir o aviso da instância (`D-151`), o dono ampliou a ideia: em vez de uma faixa só de manutenção, um canal permanente dentro do app. Perguntado o que pode passar nela, escolheu a opção C: avisos mais os números do negócio da organização. Depois explicou as duas categorias de card. Objetivo da versão: a v2.0 resolve o problema nº 1 do norte (`D-106`); esta mf amplia o que a pessoa vê sem pedir.
**Opções avaliadas:** A) só avisos do administrador da instância (recomendação do PO) · B) avisos do administrador e do owner de cada organização · C) avisos e números do negócio (escolhida pelo dono). Sem pontuação: a opção C é uma mf nova e ainda sem definição.
**Por que esta:** é a decisão do dono. Leitura do PO: dá vida ao app, reaproveita a ideia de card pronto que o produto já usa e separa o que é da instância do que é da organização. Abre-se mão de uma v2.0 mais enxuta: a lista ganha uma mf, como a `D-119` e a `D-122` já fizeram.
**Consequências:**
- A faixa mostra a cada pessoa **só os números que ela já pode ver** no produto: a segurança por pessoa (`D-025`, `MF-106:Segurança dos dados por pessoa`) vale aqui, e duas pessoas da mesma organização podem ver faixas diferentes.
- Todo número na faixa deve poder ser aberto para mostrar **origem e período**, como em qualquer resposta do produto.
- Texto em movimento contínuo precisa poder ser **pausado**; o gesto e o visual são do dono e do arquiteto.
**Fica de fora / adiado:** a definição macro (quem ganha, que decisão passa a ser possível, prova de valor, retorno, o que não inclui e do que depende): `P-027`; quem vê cada categoria; a montagem e o lugar de configurar; a relação com a Home da organização (`MF-117`) e com os boards (`MF-112`).
**Hipóteses a validar:** 🔎 que o motor de cards da Home da v1.xx serve a esta mf (arquiteto de soluções); 🔎 que números do negócio na faixa ajudam a decidir, e não só enfeitam.
**Prova de valor:** *a definir na `P-027`.*
**Reabrir quando:** a definição da MF-120 mostrar que ela não cabe na v2.0.

### D-151 · O aviso da instância entra na v2.0, em faixa contínua abaixo do cabeçalho, só pela faixa
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** a v2.0 tem um **aviso da instância**: o administrador da instância escreve o texto, a data e a hora, e o aviso aparece para todas as pessoas na faixa contínua abaixo do cabeçalho (`D-152`). Vai **só pela faixa**: não há aviso por e-mail aos owners.
**Contexto:** pendência `A-21` (agora `P-025`). O produto só tem a área de avisos de cada conta (`D-128`); não tem um aviso geral da instância, e a pessoa que abre o app durante uma parada vê a tela de entrada funcionando e as respostas falhando. Objetivo da versão: a v2.0 abre com confiança desde o primeiro cliente (`D-105`). O dono quis o aviso na v2.0 e deu à faixa o formato de painel contínuo.
**Opções avaliadas** (pesos da `D-015`; notas de 0 a 5, quase todas hipótese do PO):

| Opção | Missão (25) | Tempo (25) | Confiança (20) | Retorno (15) | Aprendizado (5) | Alavancagem (10) | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A. Entra na v2.0, em faixa no topo do app | 3 | 4 | 4 | 3 | 4 | 3 | **70** |
| B. Fica para a v2.1 | 3 | 2 | 3 | 3 | 5 | 3 | 57 |
| C. Não entra no produto | 2 | 3 | 1 | 1 | 4 | 1 | 38 |

- **A.** Prós: protege a confiança desde o primeiro cliente; custo pequeno. Contras: mais um item numa v2.0 que já é grande. Certa quando as janelas de manutenção podem vir antes da v2.1.
- **B.** Prós: v2.0 mais enxuta. Contras: a primeira janela pode acontecer antes da v2.1. Certa se a abertura da v2.0 for tão restrita que dê para avisar por fora.
- **C.** Prós: nada a construir. Contras: quem não recebe o aviso por fora fica no escuro.

Sobre o canal, uma segunda escolha: **também por e-mail aos owners** (recomendação do PO, pelo e-mail da instância) ou **só pela faixa**. O dono escolheu **só pela faixa**.
**Por que esta:** é a opção que ganha em tempo até o valor e em confiança. Abre-se mão de avisar por e-mail quem não abre o app.
**Fica de fora / adiado:** o aviso por e-mail aos owners (escolha do dono, contra a recomendação do PO); a página pública do estado (`D-154`).
**Hipóteses a validar:** 🔎 que as janelas de manutenção serão frequentes no começo; 🔎 que a faixa basta num incidente, sem e-mail.
**Prova de valor:** na véspera de uma manutenção, quem abre o app vê a faixa com o horário; na hora, ninguém acha que o Horus quebrou.
**Reabrir quando:** um incidente exigir falar com quem não abre o app (voltar ao aviso por e-mail aos owners, `ARQ-068`).

### D-150 · O uso e o custo diários ficam guardados enquanto a organização existir
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o painel e o relatório de uso guardam o uso e o custo de cada organização, **por dia**, **enquanto a organização existir**, sem prazo. O dia é contado no horário de Brasília (escolha técnica do arquiteto de soluções).
**Contexto:** dúvida Q7 da modelagem da MF-101. A proposta era guardar 25 meses, a mesma regra do consumo de IA (`ARQ-035`), para comparar um mês com o mesmo mês do ano anterior.
**Opções avaliadas:** A) 25 meses (recomendação do PO) · B) enquanto a organização existir (escolhida pelo dono). Sem pontuação: decisão pequena.
**Por que esta:** é a decisão do dono. Leitura do PO: o volume é pequeno (cerca de 66 mil linhas por ano para 30 organizações), não precisa de rotina de limpeza e o relatório (`D-149`) ganha todo o histórico. Abre-se mão de uma regra única de retenção com o consumo de IA.
**Consequências:** o consumo bruto de IA, nos bancos das organizações, segue com 25 meses (`ARQ-035`); o arquiteto de soluções ajusta a retenção do resumo no banco mestre.
**Fica de fora / adiado:** o histórico dos assentos (`D-149`).
**Hipóteses a validar:** 🔎 que a tabela cresce devagar o bastante para nunca pesar.
**Prova de valor:** o administrador consulta o uso de uma organização de três anos atrás.
**Reabrir quando:** o volume crescer a ponto de pesar, ou a Maind pedir um prazo.

### D-149 · A Maind tem um relatório da organização, para ver e baixar a qualquer momento; excluir a organização apaga o uso junto
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026; a leitura de quem vê o relatório é do PO, a confirmar) · **o trecho "sem histórico" dos assentos foi substituído pela `D-157`** · Data: 05/11/2026 · Versão: v2.0

**Decisão:** o administrador da instância tem um **relatório de cada organização**, para ver e baixar **a qualquer momento**, só com números, nunca conteúdo (`D-091.1`). Por isso, **excluir uma organização apaga também o uso e o custo dela**: a Maind pode baixar o relatório antes. O relatório mostra os assentos **como estão hoje, sem histórico** mês a mês.
**Contexto:** dúvidas Q9 e Q2 da modelagem da MF-101. A regra de arquitetura é "tudo sai" quando a organização é excluída (`ARQ-037`), mas a Maind pode precisar fechar a fatura do mês. O dono respondeu com uma terceira via: um relatório disponível a qualquer momento, e a exclusão fica segura. Sobre o histórico, perguntado se o relatório mostra os assentos mês a mês, escolheu que não.
**Opções avaliadas:** Q9) A. o uso some junto, a fatura fecha fora e antes (recomendada) · B. os totais mensais ficam · **o relatório sempre disponível, com o uso somando junto (a ideia do dono, escolhida)**. Q2) A. histórico dos assentos mês a mês e datas de corte (recomendação do PO) · B. só a situação de hoje (escolhida). Sem pontuação: decisões pequenas e reversíveis.
**Por que esta:** o relatório resolve a dúvida da fatura sem tabela de sobra nem exceção ao "tudo sai". Abre-se mão do histórico de assentos: ⚠️ sem ele, a Maind só vê a situação de hoje, e conferir a cobrança de meses passados exige guardar a conta por fora, já que o preço fica fora do produto (`D-116`).
**Fica de fora / adiado:** o histórico de assentos mês a mês; o relatório para o **owner da organização** (leitura do PO: o relatório é do administrador da instância; se o dono quiser o owner da organização vendo o próprio uso, é uma decisão nova).
**Hipóteses a validar:** 🔎 que o relatório sem histórico de assentos basta à conciliação da cobrança.
**Prova de valor:** o administrador baixa o relatório de uma organização, exclui a organização e não resta dado de uso dela.
**Reabrir quando:** a Maind não conseguir conferir uma fatura por falta do histórico de assentos.

### D-148 · A organização tem três situações, e cortar é inativar a organização inteira
Situação: ⚪ substituída em parte pela `D-277` (a organização só passa a ativa depois de o middleware ligado e dos bancos e da IA configurados) · antes: 🟢 decidida (confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** a organização tem **três situações**: **em configuração** (recém-criada, ainda sem o responsável ou sem as fontes; é o começo de toda organização), **ativa** e **inativa**. O administrador da instância marca a organização como ativa quando achar que está pronta; "em configuração" não bloqueia ninguém. **Cortar é inativar a organização inteira**: as pessoas perdem o acesso, os agendamentos, os alertas e os agentes dela param, nada se apaga e reativar devolve tudo.
**Contexto:** dúvida Q3 da modelagem da MF-101, em duas partes. O corte já estava decidido (`D-068`, `D-075`: o administrador desativa os assentos de uma organização) e a leitura "a organização inteira" só confirma. "Em configuração" é a situação que o painel de hoje já mostra. Com a `D-146`, toda organização nasce pelas mãos do administrador e passa por essa fase.
**Opções avaliadas:** A) manter as três situações (recomendada, escolhida) · B) só ativa e inativa. Sem pontuação: decisão pequena e reversível.
**Por que esta:** o painel do administrador separa quem ainda não começou a usar de quem usa, e a Maind sabe a quem dar um empurrão. Abre-se mão de um estado a menos para explicar.
**Fica de fora / adiado:** o corte por tipo de assento (a `D-075` descreve o corte da organização toda).
**Hipóteses a validar:** 🔎 que o administrador queira a lista de organizações "em configuração".
**Prova de valor:** a Maind cria cinco setores numa segunda e, na sexta, o painel mostra quantos ainda estão em configuração.
**Reabrir quando:** a Maind pedir cortar só alguns tipos de assento.

### D-147 · A instância tem um papel de administrador só; "owner da instância" é o nome comercial
Situação: 🟢 decidida (confirmada pelo dono em 05/11/2026) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** a instância tem **um papel só: o administrador da instância**. "Owner da instância" (`D-013`) é o nome comercial da Maind, não um papel à parte. Todos os administradores têm os mesmos poderes, inclusive promover e remover outros administradores, e a instância nunca fica sem administrador.
**Contexto:** dúvida Q1 da modelagem da MF-101. A MF-101 usa os termos "owner da instância" e "administradores da instância", e nenhuma decisão dá poderes diferentes a eles. A `D-068` já leu o "administrador do SaaS" como o owner da instância, com os administradores da instância.
**Opções avaliadas** (pesos da `D-015`; notas de 0 a 5, quase todas hipótese do PO):

| Opção | Missão (25) | Tempo (25) | Confiança (20) | Retorno (15) | Aprendizado (5) | Alavancagem (10) | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A. Um papel só | 3 | 4 | 3 | 3 | 4 | 3 | **66** |
| B. Dois papéis: owner e administrador | 3 | 3 | 4 | 3 | 2 | 3 | 63 |

- **A.** Prós: simples de explicar e de operar; criar o segundo papel depois é acrescentar uma coluna. Contras: qualquer administrador promove ou remove outro; a proteção é a regra de que a instância nunca fica sem administrador. Certa quando os administradores são poucos e de confiança.
- **B.** Prós: só o owner promove e remove administradores. Contras: mais regra, mais tela, mais explicação; difícil de desfazer. Certa se o suporte nunca puder remover quem manda na instância.

**Por que esta:** empate técnico (diferença de 3 pontos, menor que 5); desempatou o aprendizado e a reversibilidade, em que A ganha. Abre-se mão da proteção extra de um papel acima dos administradores.
**Fica de fora / adiado:** um segundo papel de administração.
**Hipóteses a validar:** 🔎 que a Maind terá poucos administradores, todos de confiança.
**Prova de valor:** a Maind opera a instância com uma lista só de administradores, sem pedir um papel acima.
**Reabrir quando:** algum poder precisar ser exclusivo de um papel mais alto (por exemplo, promover e remover administradores).

### D-146 · Só o administrador da instância cria organizações
Situação: 🟢 decidida (o dono escolheu a opção A em 05/11/2026) · Data: 05/11/2026 · Versão: v2.0

**Decisão:** só o **administrador da instância** cria organizações. No SaaS, é a Maind; no on-premises, é o administrador do contratante. Com ela, o `I-015` se fechou.
**Contexto:** impasse `A-02` do documento 14 (agora `I-015`). Hoje qualquer pessoa logada cria uma organização e vira owner dela (`horus@318db52b:apps/server/Horus.Api/Endpoints/OrgEndpoints.cs`). A `D-123` supõe que, no SaaS, quem cria as organizações é a Maind, e com o assento de owner grátis por organização isso precisava virar regra. Objetivo da versão: a v2.0 cobra por assentos desde o primeiro cliente (`D-107`).
**Opções avaliadas** (pesos da `D-015`; notas de 0 a 5, quase todas hipótese do PO):

| Opção | Missão (25) | Tempo (25) | Confiança (20) | Retorno (15) | Aprendizado (5) | Alavancagem (10) | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A. Só o administrador da instância | 3 | 3 | 4 | 4 | 4 | 4 | **70** |
| C. O administrador cria, mais um pedido de nova organização aprovado por ele | 3 | 3 | 4 | 3 | 3 | 3 | 64 |
| B. Qualquer pessoa logada, como na v1.xx | 3 | 4 | 1 | 1 | 2 | 2 | 48 |

- **A.** Prós: casa com a `D-123`, a `D-013` e a `D-068`; protege a receita do assento grátis; vale no SaaS e no on-premises; é reversível (abrir o autoatendimento depois). Contras: cada setor novo espera um operador criar a organização. Certa quando o primeiro contratante tem poucos setores (`D-009`).
- **C.** Prós: reduz a espera sem perder o controle. Contras: é funcionalidade nova que ninguém pediu (tela e fila de pedidos). Certa se o comercial pedir autoatendimento para setores já no primeiro cliente.
- **B.** Prós: nenhuma espera. Contras: contradiz a premissa da `D-123`; a Maind perde o controle da cobrança; difícil voltar atrás depois que as pessoas são owners.

**Por que esta:** ganha em governança e em retorno, e é a única que a `D-123` supunha. Abre-se mão do autoatendimento de setores.
**Fica de fora / adiado:** o pedido de nova organização pelo owner (opção C) e o autoatendimento (opção B).
**Hipóteses a validar:** 🔎 que a espera por um operador não incomoda com um contratante só e poucos setores.
**Prova de valor:** uma empresa com cinco setores pede as cinco organizações à Maind, e cada uma nasce com o seu owner grátis; nenhuma organização aparece sem a Maind saber.
**Reabrir quando:** o comercial pedir autoatendimento de setores, ou algum cliente reclamar da espera.

### D-139 · No MVP da v1.xx, as seis peças pela metade saem todas da tela
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: v1.xx (MVP) · ⚠️ número repetido: cite como `D-139 (MVP)`

**Decisão:** as seis peças que hoje aparecem na tela e não funcionam até o fim **saem todas da tela** no MVP (`D-138`): a fonte AWS Athena; a fonte de páginas web; a dica do campo Rede que anuncia redes privadas; os três provedores de IA "em breve" (Anthropic, OpenAI e Gemini); as preferências "Tabela-gêmea sempre aberta" e "Animação ao desenhar"; o campo "Período" do cabeçalho do relatório.
**Contexto:** a `D-138` escolheu tirar da tela, em vez de terminar, o que está pela metade. Faltava saber se alguma peça era condição de uso de algum cliente.
**Opções avaliadas:** todas saem (recomendação do PO, escolhida) · alguma fica e é terminada no MVP (não escolhida).
**Por que esta:** nenhuma das seis funciona até o fim hoje, e terminá-las é trabalho da v2.0, não conserto.
**Fica de fora / adiado:** terminar qualquer uma delas. Saem da tela, ficam no código e voltam quando estiverem prontas.
**Hipóteses a validar:** 🔎 nenhuma organização do HML usa uma fonte Athena ou de páginas web.
**Prova de valor:** a rodada de uso no HML da `D-138` não encontra nenhuma das seis.
**Reabrir quando:** um cliente pedir uma delas como condição de uso.

### D-138 · A v1.xx fecha como MVP no HML: o que existe funciona bem, e o que está pela metade sai da tela
Situação: 🟢 decidida (o dono escolheu a opção A em 02/11/2026) · Data: 02/11/2026 · Versão: v1.xx (MVP) · ⚠️ número repetido: cite como `D-138 (MVP)`

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
Situação: 🟢 decidida (as peças da segurança por pessoa que moravam em outras mfs passaram à `MF-106` pela `D-199`) · Data: 03/11/2026 · Versão: v2.0 e v2.1

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
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026) · Data: 02/11/2026 · Versão: geral · ⚠️ número repetido: cite como `D-139 (conversão)`

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
Situação: 🟢 decidida · Data: 02/11/2026 · Versão: geral · ⚠️ número repetido: cite como `D-138 (numeração)`

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

⚪ **Marcada em 05/11/2026:** essa leitura foi substituída pela `D-197`: uma mf não se divide em duas versões.

**Reabrir quando:** a ordem de construção que o arquiteto definir for muito diferente da ordem dos números.

### D-136 · Os objetivos do Horus v2 ficam confirmados: o da v2.0, o da v2.1 e os oito objetivos do mapa
Situação: 🟢 decidida (confirmada pelo dono em 02/11/2026; em 05/11/2026 o dono confirmou que o objetivo da v2.1 perde "a própria marca", `D-200`, e troca "os dados dentro de casa" por um middleware, `D-188`) · Data: 02/11/2026 · Versão: geral

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
Situação: 🟢 decidida (as nº 7, 12 e 13, o aviso, voltaram para a v2.0 pela `D-122`; a v2.1 ficou com quatro candidatas; a nº 6, a marca completa, passou para a v2.0 pela `D-197` e depois ficou sem versão pela `D-200`) · Data: 02/11/2026 · Versão: v2.1

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
Situação: 🟢 decidida (as leituras do PO foram confirmadas pelo dono em 02/11/2026; a regra foi estendida a toda passagem para uma faixa que não cria pela `D-203`; a transferência "para qualquer pessoa" foi substituída em parte pela `D-205`, e a área da organização saiu da v2.0 pelas `D-206` e `D-207`) · Data: 31/10/2026 · Versão: a pontuar

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
Situação: 🟢 decidida · **os tipos de assento passaram a ser cinco pela `D-194`** (a diretriz; os detalhes seguem em perguntas na `P-014`; o assento de owner grátis é **um por organização**, pela `D-123`, de 02/11/2026, que fechou o `I-013`) · Data: 31/10/2026 · Versão: a pontuar

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
Situação: 🟢 decidida (a transferência "para qualquer pessoa" foi substituída em parte pela `D-205`, e a área da organização saiu da v2.0 pela `D-206`) · Data: 31/10/2026 · Versão: a pontuar

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
