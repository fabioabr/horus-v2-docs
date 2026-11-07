# As versões do Horus, mf a mf

Situação: 🟢 v2.0 decidida (`D-105` a `D-119`, `D-122`, as decisões de 05/11/2026 e as de 07/11/2026, `D-258` a `D-280`) · 🟢 v2.1 decidida: tudo o que ficou fora da v2.0 (`D-121`, `D-122`), em duas ondas (`D-181`, `D-188`); a onda 2 ficou sem mfs desde que a `MF-121` subiu para a v2.0 (`D-260`; 🔎 se a v2.1 passa a ter uma onda só, a confirmar com o dono). Não há v2.2 por ora.

Última atualização: 07/11/2026 (as `D-271` a `D-280`: o middleware é multi-organização em qualquer hospedagem, e a `D-259` sai; o owner da organização configura os bancos e a IA em qualquer hospedagem; a `MF-101` redefinida com o middleware (`D-280`, substitui a `D-202`), e as organizações de exemplo da `MF-118` também só passam a ativas depois das condições da `D-277`; antes, no mesmo dia, as `D-258` a `D-269`: toda organização usa o middleware desde a v2.0, um por organização (a `D-259`, que a `D-272` substituiu), e a `MF-121` sobe inteira para a v2.0; as pessoas, os bancos e a IA passam ao front do middleware, e a conexão da instância deixa de existir; antes, em 05/11/2026, as `D-204` a `D-240`, da revisão das mfs da v2.0: as duas origens da IA, quem sai perde o que criou, a faixa indispensável e as bases de demonstração com duas organizações; antes, a `D-197` a `D-200`: uma mf não se divide em duas versões, e a marca da v2.0 é a da Maind).

As entregas do **Horus v2.xx** se chamam v2.0 e v2.1 (`D-135`); o Horus de hoje é a v1.xx (`D-134`). Uma tabela por versão, em ordem numérica de macro funcionalidade (mf). Se houver divergência, vale o [backlog estratégico](backlog-estrategico.md). O detalhe da v2.0 está em [A v2.0 consolidada](05-v2.0-consolidada.md).

**Regra (`D-197`): cada mf está numa versão só.** Uma parte que o dono quer numa versão diferente vira mf nova ou sobe para a versão da mf. Foi assim que o Teams e o Google Chat viraram a `MF-122` e o Athena virou a `MF-123` (`D-198`), e que o interruptor geral da segurança, os grupos por claims, a liberação de dados do gestor, o registro dessas liberações e a demonstração da segurança passaram à `MF-106` (`D-199`). A `MF-101` é toda da v2.0; a marca completa do contratante saiu dela e ficou sem versão, porque na v2.0 a marca é a da Maind (`D-200`). A `MF-121` subiu inteira da v2.1 para a v2.0, sem mf nova (`D-260`).

Legenda: "nº" é o número da candidata e "nota" é a da pontuação (de 0 a 100, pesos da `D-015`) · ✋ entrou por decisão do dono, acima do corte da v2.0 · 🔎 leitura do PO, a confirmar.

## 🟢 v2.0: a pergunta na hora, com confiança, o acompanhamento e o aviso

Dezenove mfs: as treze candidatas pontuadas, a base herdada, a `MF-120`, que nasceu da conversa de 05/11/2026 (`D-152`) e é indispensável, porque o aviso da instância só chega às pessoas por ela (`D-204`), e a `MF-121`, que subiu inteira da v2.1 porque toda organização usa o middleware desde a v2.0 (`D-258`, `D-260`). Entrega em SaaS, de uma vez só (`D-016`, `D-109`); o middleware é multi-organização: o da Maind atende todas as organizações do SaaS, e o da casa do cliente, as organizações desse cliente (`D-258`, `D-260`, `D-272`). Na v2.0, a organização é a fronteira dos dados: a segurança por pessoa (a nº 10) foi para a v2.1 (`D-145`).

| Mf | Nome | O que entra | Nº | Nota | Decisão |
| --- | --- | --- | --- | --- | --- |
| `MF-101` | Administração da instância | Redefinida com o middleware (`D-280`, que substitui a `D-202`). Base herdada, com o painel dos assentos; só o administrador da instância cria organizações (`D-146`), e a criação liga a organização ao middleware, com o certificado digital e a chave de instalação (`D-258`), e cria o usuário do owner no front do middleware (`D-271`); a organização nasce em configuração e só passa a ativa com o middleware ligado, um banco e a IA configurados pelo owner (`D-273`, `D-277`); os assentos que o administrador libera vão ao middleware, onde o owner da organização cadastra as pessoas (`D-258`); o estado e a versão do middleware que atende cada organização (`D-275`); o uso e o custo, com o consumo de IA só das chaves que a Maind dá (`D-279`); o relatório da organização em planilha e PDF (`D-149`, `D-166`), com a história dos assentos em números, sem o nome de quem os ocupou (`D-274`); o aviso da instância (`D-151`, `D-165`); a marca é a da Maind (`D-011`, `D-200`); a pergunta ao próprio Horus sobre a história da instância, com uma chave de IA da instância só para isso (`D-158`, `D-276`); excluir a organização apaga também o que há dela no middleware (`D-278`); sem conexão de IA para as organizações e sem o passo de disponibilizar uma conexão ao criar a organização, porque a conexão da instância deixou de existir (`D-266`); quando a IA com a chave da Maind para, o time da Maind é avisado (`D-268`) | — | — | `D-021`, `D-080`, `D-146`, `D-197`, `D-200`, `D-258`, `D-266`, `D-268`, `D-271`, `D-273` a `D-280` |
| `MF-102` | Organizações, pessoas e papéis | A gestão de pessoas inteira, com quarentena, grupos e roles; o owner cadastra e gere as pessoas no front do middleware, e elas ficam isoladas fora do SaaS (`D-261`); o gestor cria o convite e pede a troca do tipo de assento pelo Horus, e o owner aprova no front do middleware (`D-262`); os grupos dinâmicos, pelo tipo de assento (`D-235`), e a planilha de convites em lote, só do owner (`D-236`); quem é excluído perde o que criou, e quem é rebaixado o mantém desabilitado (`D-206` a `D-209`) | 9 | 55 ✋ | `D-108`, `D-114`, `D-145`, `D-199`, `D-206` a `D-209`, `D-235`, `D-236`, `D-261`, `D-262` |
| `MF-103` | Licenças e planos | A cobrança por assentos, num plano só, no SaaS, com os cinco tipos de assento (`D-194`); até mais dois owners além do primeiro, cada um num assento de owner contratado, e só o primeiro é grátis (`D-269`); a visão de cobrança do owner mostra só a contagem de assentos (`D-214`); sem a conexão da instância (`D-266`), se a IA que a Maind dá, e paga (`D-267`), entra ou não no preço do assento é a `P-022` | 15 | 42 ✋ | `D-107`, `D-117`, `D-194`, `D-203`, `D-207`, `D-214`, `D-266`, `D-267`, `D-269` |
| `MF-104` | Conectar as fontes vivas | Base herdada, sem o Athena (`MF-123`) e sem a fonte alcançando a rede interna, que é da instalação completa, sem versão (`D-188`); os bancos são configurados no front do middleware pelo owner da organização, em qualquer hospedagem, com o suporte do time da Maind (`D-265`, `D-273`) | — | — | `D-016`, `D-021`, `D-198`, `D-265`, `D-273` |
| `MF-105` | IA sob controle da organização | Definida (`D-246`), com o que mudou em 07/11/2026: sem o modo "tudo dentro"; a IA é sempre da organização, configurada no front do middleware pelo owner da organização, em qualquer hospedagem, com o suporte do time da Maind, e a conexão da instância deixa de existir (`D-265`, `D-266`, `D-273`); a Maind pode dar uma chave de provedor de IA, que ela paga e o owner cadastra (`D-264`, `D-267`, `D-273`); o owner da organização vê o consumo e o custo de toda a IA dela (`D-267`); quando a IA para, é avisado o owner da organização e, se a chave é da Maind, também o time da Maind (`D-268`); sem teto automático de custo (`D-234`) | — | — | `D-016`, `D-021`, `D-234`, `D-246`, `D-264` a `D-268`, `D-273` |
| `MF-107` | Perguntar aos dados em português | Base herdada; a resposta em segundos na reunião; o retorno do usuário (👍🏻, 👎🏻 e 🚫); os modos passam a ser dois, dados e conversa (`D-215`); a exportação da conversa em PDF ou HTML (`D-250`) | 1 e 2 | 77 e 81 | `D-021`, `D-105`, `D-215`, `D-220`, `D-223`, `D-250` |
| `MF-108` | Respostas visuais | Base herdada, com o tema dos gráficos por organização (`D-237`) | — | — | `D-021`, `D-237` |
| `MF-109` | A web como fonte | Base herdada; a web como fonte viva completa, com link e data; o modelo sai à web quando autorizado (`D-162`), pelo interruptor "pesquisar na web", ao lado dos dados (`D-215`) | 3 | 67 | `D-021`, `D-105`, `D-162`, `D-215` |
| `MF-110` | Pergunta rápida | Perguntar sem sair da tela, num botão flutuante | 14 | 67 | `D-089`, `D-105`, `D-221`, `D-222` |
| `MF-111` | Chat pelo WhatsApp | Conversar com o Horus pelo WhatsApp; o telefone da pessoa fica ligado a uma organização por vez (`D-224`) | 18 | 50 ✋ | `D-099`, `D-119`, `D-224`, `D-225` |
| `MF-112` | Boards e Relatórios | O redesenho inteiro, com o PDF automático pelo agendador e pelos conectores; o board do espaço da organização usa o acesso de quem o abre, e o público, o do owner que o publicou (`D-163`, `D-164`); o espaço da organização não recebe o que as pessoas deixam, e o board público some com o owner que o publicou (`D-206`, `D-209`); o PDF do board maior que a folha tem uma página só (`D-229`) | 8 | 59 ✋ | `D-058`, `D-119`, `D-163`, `D-164`, `D-199`, `D-206`, `D-209`, `D-229`, `D-230` |
| `MF-113` | Conectores de Saída | O carteiro: por onde o Horus entrega, só a usuários do Horus. Na v2.0, o e-mail e o WhatsApp; quem usa o número da Maind paga as mensagens (`D-160`) | 12 | 47 ✋ | `D-041`, `D-122`, `D-124`, `D-160`, `D-198`, `D-227`, `D-240` |
| `MF-114` | Módulo de Agendamentos de Agentes | O relógio: quando gerar e enviar | 13 | 47 ✋ | `D-060`, `D-122`, `D-206` a `D-209`, `D-226` |
| `MF-115` | Agentes ativos | O trabalhador de IA que extrai, analisa e avisa | 7 | 49 ✋ | `D-062`, `D-122`, `D-206` a `D-209`, `D-226`, `D-234` |
| `MF-116` | Auditoria | O rastro de quem entregou o quê, de quem abriu e de quem exportou uma conversa (`D-252`) | 17 | 41 ✋ | `D-093`, `D-119`, `D-199`, `D-210`, `D-231`, `D-252` |
| `MF-117` | Home da organização | Base herdada; a medida de autonomia, com a divisão por canal; o gestor vê a da própria equipe (`D-238`, `D-239`) | 4 | 66 | `D-021`, `D-105`, `D-222`, `D-238`, `D-239` |
| `MF-118` | Bases de demonstração | Base herdada, com duas organizações de exemplo, a rede de lojas e a frota, e um cenário para cada prova de valor da v2.0 (`D-232`, `D-233`); as organizações de exemplo também só passam a ativas com o middleware ligado, um banco e a IA configurados (`D-277`); sem a DRE de usina e sem a demonstração da segurança por pessoa | — | — | `D-021`, `D-199`, `D-232`, `D-233`, `D-277` |
| `MF-120` | Faixa de avisos e números | A faixa no alto do produto, um contêiner de componentes: o aviso da instância, a caixa de texto livre do owner e os cards de número, conforme o acesso de quem os vê; indispensável à v2.0, porque o aviso da instância só chega às pessoas por ela (nome provisório) | — | — | `D-152`, `D-167` a `D-174`, `D-204`, `D-212`, `D-213` |
| `MF-121` | Middleware da organização | O middleware, numa infraestrutura separada do SaaS, com a base de configuração e o aplicativo de setup (o front do middleware), hospedado pela Maind ou pelo cliente, na casa dele, com o mesmo contrato (`D-258`, `D-260`); multi-organização em qualquer hospedagem: o da Maind atende todas as organizações do SaaS, cada uma isolada pelo seu certificado, e o do cliente, as organizações desse cliente (`D-272`); por ele a organização chega à autenticação, aos dados e à IA, e o ciclo da análise roda dentro dele: ao Horus SaaS só chegam a pergunta e a resposta pronta (`D-189`, `D-258`); as configurações de autenticação ficam nele, e o owner da organização e o administrador da instância entram sempre por usuário e senha (`D-258`); na casa do cliente, é a imagem que ele instala (`D-195`, `D-260`); na hospedagem da Maind, a Maind o opera e cria o usuário do owner da organização, que configura nele os bancos e a IA, como na casa do cliente, e o time da Maind só dá suporte (`D-258`, `D-271`, `D-273`); não depende mais da `MF-106` (`D-263`) (nome decidido pelo dono, `D-270`) | parte da 5 | — ✋ | `D-188`, `D-189`, `D-195`, `D-196`, `D-258`, `D-260`, `D-263`, `D-265`, `D-271` a `D-273` |

**O que trava a `MF-121` na v2.0** (do arquiteto de soluções): 🕓 o fluxo do dono, com o SaaS e o middleware em infraestruturas separadas e cada organização nova adicionada ao middleware, que é multi-organização (`P-048`, `D-272`), e o protocolo e o desenho do middleware (`P-040`, `P-042`).

## 🟢 v2.1: tudo o que ficou fora da v2.0

Decidida pelo dono (`D-121`). Quatro mfs, todas da onda 1, o SaaS (`D-181`); a onda 2, a casa do contratante (`D-188`), ficou sem mfs, porque o middleware subiu inteiro para a v2.0, em toda organização (`D-258`, `D-260`). O Horus fica sempre na Maind. As notas são as da pontuação da v2.0; quando a v2.1 for a próxima, as candidatas voltam a ser pontuadas contra o objetivo dela.

### Onda 1: o SaaS

| Mf | Nome | O que entra | Nº | Nota | Decisão |
| --- | --- | --- | --- | --- | --- |
| `MF-106` | Segurança dos dados por pessoa | As duas etapas: o acesso configurado dentro do Horus (veio da v2.0) e a segurança corporativa integrada, com o login corporativo só por OIDC (`D-184`) e as roles pelo crachá. Com ela voltam o interruptor geral da segurança, os grupos por claims e as colunas de claims da planilha de convites, a liberação de dados do gestor no board, o registro dessas liberações no rastro e a demonstração da segurança; roda no middleware e passa a depender da `MF-121`, que está na v2.0 (`D-263`) | 10 e 11 | 78 e 58 | `D-028`, `D-118`, `D-121`, `D-145`, `D-184`, `D-199`, `D-263` |
| `MF-119` | Investigação guiada | Descobrir o porquê de uma mudança, passo a passo, a partir de "investigar" na resposta; o caminho fica na conversa | 16 | 61 (provisória) | `D-081`, `D-104`, `D-121`, `D-177` a `D-180` |
| `MF-122` | Conectores de chat corporativo | O Microsoft Teams e o Google Chat como conectores de saída (nome provisório) | parte da 12 | — | `D-182`, `D-198` |
| `MF-123` | Fonte AWS Athena | O AWS Athena terminado, respondendo perguntas de análise (nome provisório) | — | — | `D-161`, `D-198` |

### Onda 2: a casa do contratante

Ficou sem mfs. A `MF-121:Middleware da organização`, a única que ela tinha, subiu inteira para a v2.0, porque toda organização usa o middleware desde a v2.0, hospedado pela Maind ou pelo cliente (`D-258`, `D-260`). 🔎 Leitura do PO, a confirmar com o dono: a v2.1 fica sem onda 2.

**O que trava a v2.1** (todas são do arquiteto de soluções):
- 🕓 O Athena: o conector, o dialeto e a segurança por pessoa, que hoje só cobre o SQL Server (`P-033`).
- 🕓 Como o Teams e o Google Chat se integram (`P-038`).

## ➖ Sem versão

| Item | Por quê | Decisão |
| --- | --- | --- |
| A instalação completa do Horus no contratante (a ativação dos assentos por arquivo de licença, a fonte alcançando a rede interna e o modo "tudo dentro") | É a porta de volta: só entra se um cliente exigir que nada, nem a pergunta, saia de casa. 🔎 Se entrar, volta como mf própria | `D-175`, `D-176`, `D-185` a `D-188` |
| A marca completa do contratante: logo, nome e e-mail do cliente em todo o produto, até no remetente (era a nº 6, nota 29) | Na v2.0 a marca é a da Maind, e o dono vai pensar depois em como mudar isso. 🔎 Se voltar, volta como mf própria | `D-183`, `D-200` |
| O tema do contratante (as cores e a aparência) | O dono manteve o tema sem versão. O tema dos gráficos por organização fica na v2.0, como na v1.xx | `D-011`, `D-183`, `D-237` |
| O teto automático de custo da IA, por agente ou por organização | Na v2.0 ficam só os tetos técnicos por execução e o aviso de custo; volta se o custo surpreender | `D-234` |
| A DRE de usina na vitrine das bases de demonstração | Na v2.0 ficam a rede de lojas e a frota; volta se um cliente do ramo pedir | `D-233` |
| A transferência do que a pessoa criou | Não existe em nenhuma versão: quem é excluído perde o que criou, e quem é rebaixado o mantém desabilitado | `D-206`, `D-209` |

## ➖ Fora do produto

| Item | Por quê | Decisão |
| --- | --- | --- |
| Melhoria do modelo semântico | Não é mf: fica com o time de dados por enquanto | `D-083` |

## Em números

| Versão | Mfs | Situação |
| --- | --- | --- |
| v2.0 | 19 | 🟢 decidida |
| v2.1 | 4 (todas na onda 1; a onda 2 ficou sem mfs, `D-260`) | 🟢 decidida |

As 23 mfs, da `MF-101` à `MF-123`, estão distribuídas, cada uma numa versão só (`D-197`). A `MF-122` e a `MF-123` têm a definição decidida (`D-201`).

## Como manter

- A v2.0 acompanha o backlog e o [documento da v2.0](05-v2.0-consolidada.md). A v2.1 acompanha a `D-121`, a `D-181`, a `D-188` e a `D-260`.
- Quando a v2.0 estiver entregue, as mfs da v2.1 voltam à pontuação contra o objetivo da v2.1, e esta página muda junto.
- Toda parte nova que o dono quiser numa versão diferente da mf de origem vira mf própria (`D-197`).
- A proposta anterior do PO (v2.1, v2.2 e "sem versão") ficou registrada na `D-120`, substituída.
