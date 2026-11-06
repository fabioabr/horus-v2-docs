# As versões do Horus, mf a mf

Situação: 🟢 v2.0 decidida (`D-105` a `D-119`, `D-122` e as decisões de 05/11/2026) · 🟢 v2.1 decidida: tudo o que ficou fora da v2.0 (`D-121`, `D-122`), em duas ondas (`D-181`, `D-188`). Não há v2.2 por ora.

Última atualização: 05/11/2026 (as `D-204` a `D-240`, da revisão das mfs da v2.0: as duas origens da IA, quem sai perde o que criou, a faixa indispensável e as bases de demonstração com duas organizações; antes, a `D-197` a `D-200`: uma mf não se divide em duas versões, e a marca da v2.0 é a da Maind).

As entregas do **Horus v2.xx** se chamam v2.0 e v2.1 (`D-135`); o Horus de hoje é a v1.xx (`D-134`). Uma tabela por versão, em ordem numérica de macro funcionalidade (mf). Se houver divergência, vale o [backlog estratégico](backlog-estrategico.md). O detalhe da v2.0 está em [A v2.0 consolidada](05-v2.0-consolidada.md).

**Regra (`D-197`): cada mf está numa versão só.** Uma parte que o dono quer numa versão diferente vira mf nova ou sobe para a versão da mf. Foi assim que o Teams e o Google Chat viraram a `MF-122` e o Athena virou a `MF-123` (`D-198`), e que o interruptor geral da segurança, os grupos por claims, a liberação de dados do gestor, o registro dessas liberações e a demonstração da segurança passaram à `MF-106` (`D-199`). A `MF-101` é toda da v2.0; a marca completa do contratante saiu dela e ficou sem versão, porque na v2.0 a marca é a da Maind (`D-200`).

Legenda: "nº" é o número da candidata e "nota" é a da pontuação (de 0 a 100, pesos da `D-015`) · ✋ entrou por decisão do dono, acima do corte da v2.0 · 🔎 leitura do PO, a confirmar.

## 🟢 v2.0: a pergunta na hora, com confiança, o acompanhamento e o aviso

Dezoito mfs: as treze candidatas pontuadas, a base herdada e a `MF-120`, que nasceu da conversa de 05/11/2026 (`D-152`) e é indispensável, porque o aviso da instância só chega às pessoas por ela (`D-204`). Entrega em SaaS, de uma vez só (`D-016`, `D-109`). Na v2.0, a organização é a fronteira dos dados: a segurança por pessoa (a nº 10) foi para a v2.1 (`D-145`).

| Mf | Nome | O que entra | Nº | Nota | Decisão |
| --- | --- | --- | --- | --- | --- |
| `MF-101` | Administração da instância | Base herdada, com o painel dos assentos; só o administrador da instância cria organizações (`D-146`); o aviso da instância (`D-151`, `D-165`); o relatório da organização em planilha e PDF (`D-166`), com a história dos assentos (`D-157`, `D-158`); a marca é a da Maind (`D-011`, `D-200`); as conexões de IA da instância, que o administrador disponibiliza a cada organização (`D-216`, `D-217`) | — | — | `D-021`, `D-080`, `D-146`, `D-197`, `D-200`, `D-216`, `D-217` |
| `MF-102` | Organizações, pessoas e papéis | A gestão de pessoas inteira, com quarentena, grupos e roles; os grupos dinâmicos, pelo tipo de assento (`D-235`), e a planilha de convites em lote, só do owner (`D-236`); quem é excluído perde o que criou, e quem é rebaixado o mantém desabilitado (`D-206` a `D-209`) | 9 | 55 ✋ | `D-108`, `D-114`, `D-145`, `D-199`, `D-206` a `D-209`, `D-235`, `D-236` |
| `MF-103` | Licenças e planos | A cobrança por assentos, num plano só, no SaaS, com os cinco tipos de assento (`D-194`); a visão de cobrança do owner mostra só a contagem de assentos (`D-214`); a IA só entra no preço nas organizações que usam a conexão da instância (`D-216`; se o preço muda para quem traz a própria IA é a `P-022`) | 15 | 42 ✋ | `D-107`, `D-117`, `D-159`, `D-194`, `D-203`, `D-207`, `D-214`, `D-216` |
| `MF-104` | Conectar as fontes vivas | Base herdada, sem o Athena (`MF-123`) e sem a fonte alcançando a rede interna | — | — | `D-016`, `D-021`, `D-198` |
| `MF-105` | IA sob controle da organização | Definida (`D-246`): sem o modo "tudo dentro"; duas origens de IA: a conexão da organização, que ela paga, e a da instância, que a Maind paga e disponibiliza por organização (`D-216`); a organização nasce sem IA (`D-217`); sem teto automático de custo (`D-234`) | — | — | `D-016`, `D-021`, `D-159`, `D-216` a `D-218`, `D-234`, `D-241`, `D-246` |
| `MF-107` | Perguntar aos dados em português | Base herdada; a resposta em segundos na reunião; o retorno do usuário (👍🏻, 👎🏻 e 🚫); os modos passam a ser dois, dados e conversa (`D-215`) | 1 e 2 | 77 e 81 | `D-021`, `D-105`, `D-215`, `D-220`, `D-223` |
| `MF-108` | Respostas visuais | Base herdada, com o tema dos gráficos por organização (`D-237`) | — | — | `D-021`, `D-237` |
| `MF-109` | A web como fonte | Base herdada; a web como fonte viva completa, com link e data; o modelo sai à web quando autorizado (`D-162`), pelo interruptor "pesquisar na web", ao lado dos dados (`D-215`) | 3 | 67 | `D-021`, `D-105`, `D-162`, `D-215` |
| `MF-110` | Pergunta rápida | Perguntar sem sair da tela, num botão flutuante | 14 | 67 | `D-089`, `D-105`, `D-221`, `D-222` |
| `MF-111` | Chat pelo WhatsApp | Conversar com o Horus pelo WhatsApp; o telefone da pessoa fica ligado a uma organização por vez (`D-224`) | 18 | 50 ✋ | `D-099`, `D-119`, `D-224`, `D-225` |
| `MF-112` | Boards e Relatórios | O redesenho inteiro, com o PDF automático pelo agendador e pelos conectores; o board do espaço da organização usa o acesso de quem o abre, e o público, o do owner que o publicou (`D-163`, `D-164`); o espaço da organização não recebe o que as pessoas deixam, e o board público some com o owner que o publicou (`D-206`, `D-209`); o PDF do board maior que a folha tem uma página só (`D-229`) | 8 | 59 ✋ | `D-058`, `D-119`, `D-163`, `D-164`, `D-199`, `D-206`, `D-209`, `D-229`, `D-230` |
| `MF-113` | Conectores de Saída | O carteiro: por onde o Horus entrega, só a usuários do Horus. Na v2.0, o e-mail e o WhatsApp; quem usa o número da Maind paga as mensagens (`D-160`) | 12 | 47 ✋ | `D-041`, `D-122`, `D-124`, `D-160`, `D-198`, `D-227`, `D-240` |
| `MF-114` | Módulo de Agendamentos de Agentes | O relógio: quando gerar e enviar | 13 | 47 ✋ | `D-060`, `D-122`, `D-206` a `D-209`, `D-226` |
| `MF-115` | Agentes ativos | O trabalhador de IA que extrai, analisa e avisa | 7 | 49 ✋ | `D-062`, `D-122`, `D-206` a `D-209`, `D-226`, `D-234` |
| `MF-116` | Auditoria | O rastro de quem entregou o quê e de quem abriu | 17 | 41 ✋ | `D-093`, `D-119`, `D-199`, `D-210`, `D-231` |
| `MF-117` | Home da organização | Base herdada; a medida de autonomia, com a divisão por canal; o gestor vê a da própria equipe (`D-238`, `D-239`) | 4 | 66 | `D-021`, `D-105`, `D-222`, `D-238`, `D-239` |
| `MF-118` | Bases de demonstração | Base herdada, com duas organizações de exemplo, a rede de lojas e a frota, e um cenário para cada prova de valor da v2.0 (`D-232`, `D-233`); sem a DRE de usina e sem a demonstração da segurança por pessoa | — | — | `D-021`, `D-199`, `D-232`, `D-233` |
| `MF-120` | Faixa de avisos e números | A faixa no alto do produto, um contêiner de componentes: o aviso da instância, a caixa de texto livre do owner e os cards de número, conforme o acesso de quem os vê; indispensável à v2.0, porque o aviso da instância só chega às pessoas por ela (nome provisório) | — | — | `D-152`, `D-167` a `D-174`, `D-204`, `D-212`, `D-213` |

## 🟢 v2.1: tudo o que ficou fora da v2.0

Decidida pelo dono (`D-121`). Cinco mfs, em duas ondas (`D-181`, `D-188`): o SaaS primeiro, depois a casa do contratante, que o dono quer atender por um middleware (o Horus fica sempre na Maind). As notas são as da pontuação da v2.0; quando a v2.1 for a próxima, as candidatas voltam a ser pontuadas contra o objetivo dela.

### Onda 1: o SaaS

| Mf | Nome | O que entra | Nº | Nota | Decisão |
| --- | --- | --- | --- | --- | --- |
| `MF-106` | Segurança dos dados por pessoa | As duas etapas: o acesso configurado dentro do Horus (veio da v2.0) e a segurança corporativa integrada, com o login corporativo só por OIDC (`D-184`) e as roles pelo crachá. Com ela voltam o interruptor geral da segurança, os grupos por claims e as colunas de claims da planilha de convites, a liberação de dados do gestor no board, o registro dessas liberações no rastro e a demonstração da segurança | 10 e 11 | 78 e 58 | `D-028`, `D-118`, `D-121`, `D-145`, `D-184`, `D-199` |
| `MF-119` | Investigação guiada | Descobrir o porquê de uma mudança, passo a passo, a partir de "investigar" na resposta; o caminho fica na conversa | 16 | 61 (provisória) | `D-081`, `D-104`, `D-121`, `D-177` a `D-180` |
| `MF-122` | Conectores de chat corporativo | O Microsoft Teams e o Google Chat como conectores de saída (nome provisório) | parte da 12 | — | `D-182`, `D-198` |
| `MF-123` | Fonte AWS Athena | O AWS Athena terminado, respondendo perguntas de análise (nome provisório) | — | — | `D-161`, `D-198` |

### Onda 2: a casa do contratante

| Mf | Nome | O que entra | Nº | Nota | Decisão |
| --- | --- | --- | --- | --- | --- |
| `MF-121` | Middleware na casa do contratante | Uma imagem de container da Maind que o cliente instala na infraestrutura dele, com endereço público e par de chaves cadastrado no Horus, para o Horus chegar aos dados, à internet e à IA do cliente; só a pergunta e a resposta pronta saem de casa (nome provisório) | parte da 5 | — | `D-188`, `D-189`, `D-195`, `D-196` |

**O que trava a v2.1** (todas são do arquiteto de soluções):
- 🕓 O protocolo e o desenho do middleware (`P-040`, `P-042`).
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
| v2.0 | 18 | 🟢 decidida |
| v2.1 | 5 (4 na onda 1 e 1 na onda 2) | 🟢 decidida |

As 23 mfs, da `MF-101` à `MF-123`, estão distribuídas, cada uma numa versão só (`D-197`). A `MF-122` e a `MF-123` têm a definição decidida (`D-201`).

## Como manter

- A v2.0 acompanha o backlog e o [documento da v2.0](05-v2.0-consolidada.md). A v2.1 acompanha a `D-121`, a `D-181` e a `D-188`.
- Quando a v2.0 estiver entregue, as mfs da v2.1 voltam à pontuação contra o objetivo da v2.1, e esta página muda junto.
- Toda parte nova que o dono quiser numa versão diferente da mf de origem vira mf própria (`D-197`).
- A proposta anterior do PO (v2.1, v2.2 e "sem versão") ficou registrada na `D-120`, substituída.
