# Mapa de objetivos e funcionalidades do Horus v2

Situação: ✅ objetivos confirmados pelo dono (`D-136`) · ✅ funcionalidades e entregas decididas (`D-105` a `D-135`, as de 05/11/2026, até a `D-240`, e as de 07/11/2026, `D-258` a `D-269`).

Última atualização: 07/11/2026 (as decisões `D-258` a `D-269`: toda organização usa o seu middleware desde a v2.0, e a `MF-121` sobe inteira para a v2.0; a v2.1 fica com quatro mfs, todas da onda 1; as pessoas, os bancos e a IA passam ao front do middleware, e a conexão da instância deixa de existir; antes, em 05/11/2026, as decisões `D-204` a `D-240`, da revisão das mfs da v2.0: as duas origens da IA, a web como interruptor, a faixa como contêiner de componentes e as bases de demonstração com duas organizações; antes, as `D-146` a `D-201`: uma mf numa versão só, a v2.1 em duas ondas, as novas `MF-120` a `MF-123`; antes, a `D-145`: a segurança dos dados por pessoa inteira na v2.1).

É o mapa para **iniciar o desenvolvimento de forma estruturada** (`D-134`). Para cada objetivo do produto, mostra as funcionalidades que o cumprem, a entrega em que cada uma sai e onde está a definição. **Ele não decide nada novo:** resume e aponta para o [backlog estratégico](backlog-estrategico.md). Se houver divergência, vale o backlog.

Legenda: ✅ decidido pelo dono · 🆕 proposto pelo PO, aguardando o dono · 🔎 leitura do PO, a confirmar. A **v2.0** é a primeira entrega do Horus v2, e a **v2.1**, a segunda (`D-135`). A **v1.xx** é o Horus de hoje, ponto de partida e fonte de reaproveitamento (`D-134`). **Macro funcionalidade (mf)** é cada peça do [mapa das mfs](04-macro-funcionalidades-de-hoje.md), citada como `MF-nnn:Nome`.

## 1. O objetivo do produto ✅

| Campo | O que diz | Decisão |
| --- | --- | --- |
| 🧭 **Norte** | Autonomia: o gestor e o executivo decidem com dados sem depender do time de dados | `D-001` |
| 💬 **Promessa** | "Informação na palma da mão" (nome de trabalho; a frase final mora na comunicação da Maind) | `D-012` |
| ⚡ **"Em segundos"** | Rápido em comparação com o pedido ao time de dados, que às vezes leva dias; não é um tempo cronometrado | `D-125` |
| 📈 **Como se mede** | No produto, as perguntas de análise respondidas e a qualidade das respostas. Fora dele, com cada cliente, o saving | `D-004`, `D-132` |
| 🚫 **Limite** | O Horus só lê: nunca altera dados nem age nos sistemas da empresa | `D-001`, `D-022` |
| 👥 **Para quem** | O gestor de área, o executivo e o comprador, numa empresa que usa o Horus por dentro, em SaaS primeiro | `D-009`, `D-016` |

## 2. Os objetivos das entregas ✅

| Entrega | Objetivo | De onde vem |
| --- | --- | --- |
| 🟢 **v2.0** | O gestor e o executivo **perguntam e têm a resposta na hora**, **acompanham o negócio** em boards e **são avisados** quando algo muda. A resposta é confiável, com a fonte à vista, e cada organização vê só os próprios dados (`D-145`). A empresa mede a adoção e paga por assento. | O objetivo confirmado na `D-106` (o problema nº 1), ampliado pela `D-119` (o acompanhamento) e pela `D-122` (o aviso) |
| 🔵 **v2.1** | A pessoa **descobre o porquê** de uma mudança, passo a passo, e o Horus **chega a empresas mais exigentes**: com login e segurança corporativos ou com os dados dentro de casa, por um middleware. *(A marca do contratante saiu da v2.1, `D-200`, e os dados dentro de casa viraram o middleware, `D-188`: o dono confirmou o texto em 05/11/2026. Em 07/11/2026, o middleware subiu para a v2.0, em toda organização, `D-258` e `D-260`: 🔎 o texto deste objetivo, e se o da v2.0 ganha o middleware, a confirmar com o dono.)* | As candidatas da `D-121`, em duas ondas (`D-181`, `D-188`); a onda 2 ficou sem mfs (`D-260`) |

Os dois objetivos foram propostos pelo PO e confirmados pelo dono em 02/11/2026 (`D-136`). O da v2.0 atualiza o texto da `D-106`, que falava só do problema nº 1, com a ampliação da `D-119` e da `D-122`.

## 3. Os objetivos e as funcionalidades

As funcionalidades estão agrupadas em **oito objetivos**, propostos pelo PO e confirmados pelo dono (`D-136`). Cada funcionalidade é uma candidata da pontuação (nº) ou uma parte da base herdada da v1.xx.

| Objetivo | Problema do norte | Entregas |
| --- | --- | --- |
| **O1** ⚡ Perguntar e ter a resposta na hora | nº 1, a pergunta de análise na hora | v2.0 |
| **O2** 🛡️ Confiar no que vê | nº 1, a confiança | v2.0, com a auditoria; a segurança por pessoa o completa na v2.1 (`D-145`) |
| **O3** 📌 Acompanhar o negócio | o acompanhamento recorrente | v2.0 |
| **O4** 🔔 Ser avisado sem perguntar | nº 3, o aviso | v2.0; os conectores de chat vêm na v2.1 (`MF-122`) |
| **O5** 🔍 Descobrir o porquê | nº 2, a investigação | v2.1 |
| **O6** 📈 Provar o valor e vender | a medida do norte | v2.0 |
| **O7** 🏢 Organizar as pessoas e cobrar | as condições da organização e do negócio | v2.0 |
| **O8** 🏛️ Atender empresas com exigências próprias | a expansão para clientes maiores | v2.0, com o middleware (`MF-121`, `D-260`); a segurança corporativa vem na v2.1 |

| Objetivo | Mf | Funcionalidade | Nº | Entrega | Definição |
| --- | --- | --- | --- | --- | --- |
| O1 | `MF-107:Perguntar aos dados em português` | A conversa de análise, com os dois modos (dados e conversa) e a pesquisa na web, os cinco níveis de inferência e a Análise avançada | base | v2.0 | `D-021`, `D-215` |
| O1 | `MF-107:Perguntar aos dados em português` | Resposta em segundos na reunião | 1 | v2.0 | `D-126` |
| O1 | `MF-107:Perguntar aos dados em português` | Retorno do usuário: 👍🏻, 👎🏻 e 🚫, com o reporte ao owner | 2 | v2.0 | `D-129` |
| O1 | `MF-107:Perguntar aos dados em português` | Exportar a conversa em PDF ou HTML, para levá-la a outras pessoas sem compartilhá-la | — | v2.0 | `D-249`, `D-250` |
| O1 | `MF-108:Respostas visuais` | Gráficos, tabelas, KPIs, mapa de calor, chaveamento e fluxo | base | v2.0 | `D-021` |
| O1 | `MF-110:Pergunta rápida` | Perguntar de qualquer tela, num botão flutuante | 14 | v2.0 | `D-089` |
| O1 | `MF-111:Chat pelo WhatsApp` | Conversar com o Horus pelo WhatsApp | 18 | v2.0 | `D-099` |
| O1 | `MF-104:Conectar as fontes vivas` | Os bancos e as fontes da empresa, com o modelo semântico, configurados no front do middleware | base | v2.0 | `D-021`, `D-265` |
| O1 | `MF-123:Fonte AWS Athena` | O Athena terminado, respondendo perguntas de análise (nome provisório) | — | v2.1 | `D-161`, `D-198`, `D-201` |
| O1 | `MF-109:A web como fonte` | A web como fonte viva completa, com link e data, em qualquer nível, pelo interruptor "pesquisar na web" | 3 | v2.0 | `D-131`, `D-215` |
| O1 | `MF-105:IA sob controle da organização` | A IA da organização, configurada no front do middleware (a conexão da instância deixou de existir), com a chave de provedor que a Maind pode dar e pagar; o modelo por função; o consumo e o custo de toda a IA, à vista do owner da organização | base | v2.0 | `D-021`, `D-246`, `D-264` a `D-267` |
| O2 | `MF-106:Segurança dos dados por pessoa` | Acesso configurado dentro do Horus (etapa 1) | 10 | v2.1 | `D-028`, `D-145`, `D-263` |
| O2 | `MF-106:Segurança dos dados por pessoa` | O interruptor geral, os grupos por claims, a liberação de dados do gestor no board, o registro dessas liberações e a demonstração da segurança | — | v2.1 | `D-199` |
| O2 | `MF-116:Auditoria` | O rastro de quem entregou o quê, de quem abriu e de quem exportou uma conversa | 17 | v2.0 | `D-093`, `D-252` |
| O3 | `MF-112:Boards e Relatórios` | Boards e relatórios como uma coisa só: o board vivo e em PDF e a publicação (a liberação de dados do gestor é da `MF-106`) | 8 | v2.0 | `D-058`, `D-145`, `D-199` |
| O4 | `MF-115:Agentes ativos` | O trabalhador de IA que extrai, analisa e avisa | 7 | v2.0 | `D-062` |
| O4 | `MF-114:Módulo de Agendamentos de Agentes` | O relógio: quando gerar e enviar | 13 | v2.0 | `D-060` |
| O4 | `MF-113:Conectores de Saída` | O carteiro, com o e-mail e o WhatsApp | 12 | v2.0 | `D-041`, `D-124` |
| O4 | `MF-122:Conectores de chat corporativo` | O Teams e o Google Chat como conectores de saída (nome provisório) | parte da 12 | v2.1 | `D-182`, `D-198`, `D-201` |
| O4 | `MF-120:Faixa de avisos e números` | A faixa contínua, um contêiner de componentes: o aviso da instância, a caixa de texto livre do owner e os cards de número (nome provisório; objetivo 🔎) | — | v2.0 | `D-152`, `D-174`, `D-204`, `D-212`, `D-213` |
| O5 | `MF-119:Investigação guiada` | Descobrir o porquê de uma mudança, passo a passo | 16 | v2.1 | `D-081`, `D-180` (definição decidida) |
| O6 | `MF-117:Home da organização` | A medida de autonomia e a qualidade das respostas, na Home, com a divisão por canal | 4 | v2.0 | `D-133`, `D-238`, `D-239` |
| O6 | `MF-118:Bases de demonstração` | Duas organizações de exemplo, a rede de lojas e a frota, com um cenário para cada prova de valor da v2.0, para demonstrar e vender | base | v2.0 | `D-021`, `D-232`, `D-233` |
| O7 | `MF-102:Organizações, pessoas e papéis` | A gestão de pessoas inteira: gestor, quarentena, grupos e roles; o owner gere as pessoas no front do middleware, e o gestor convida e pede a troca do assento pelo Horus | 9 | v2.0 | `D-056`, `D-114`, `D-261`, `D-262` |
| O7 | `MF-101:Administração da instância` | A administração da instância, com o painel dos assentos, o relatório da organização, o aviso da instância e a marca da Maind; criar a organização gera o certificado e a chave de instalação do middleware dela | base | v2.0 | `D-021`, `D-080`, `D-146`, `D-166`, `D-200`, `D-258` |
| O7 | `MF-103:Licenças e planos` | A cobrança por assento, num plano só, com cinco tipos de assento e um owner grátis por organização; até mais dois owners, cada um num assento de owner contratado | 15 | v2.0 | `D-080`, `D-117`, `D-123`, `D-194`, `D-269` |
| O8 | `MF-106:Segurança dos dados por pessoa` | A segurança corporativa integrada, com o login corporativo só por OIDC (etapa 2) | 11 | v2.1 | `D-028`, `D-118`, `D-184` |
| O8 | — | A marca completa do contratante (white label) | 6 | sem versão | `D-183`, `D-200` |
| O8 | `MF-121:Middleware da organização` | O middleware de cada organização, separado do SaaS, hospedado pela Maind ou pelo cliente, na casa dele: as configurações de autenticação, as pessoas e a configuração dos bancos e da IA ficam nele, e ao Horus SaaS só chegam a pergunta e a resposta pronta (nome decidido pelo dono, `D-270`; 🔎 o objetivo, agora que serve a toda organização, a confirmar com o dono) | parte da 5 | v2.0 | `D-188`, `D-189`, `D-196`, `D-258` a `D-261`, `D-265` |
| O8 | — | A instalação completa do Horus no cliente (arquivo de licença, rede interna e "tudo dentro"): a porta de volta; se voltar, volta como mf própria (`D-198`) | parte da 5 | sem versão | `D-175`, `D-185` a `D-188` |

## 4. As entregas num relance

```mermaid
flowchart LR
    N["🧭 Norte: autonomia<br/>para o gestor e o executivo"]
    subgraph E1["🟢 v2.0"]
        O1["O1 ⚡ Resposta na hora"]
        O2["O2 🛡️ Confiança"]
        O3["O3 📌 Acompanhamento"]
        O4["O4 🔔 Aviso"]
        O6["O6 📈 Provar o valor"]
        O7["O7 🏢 Pessoas e cobrança"]
        O8a["O8 🏛️ O middleware"]
    end
    subgraph E2["🔵 v2.1"]
        O5["O5 🔍 O porquê"]
        O8["O8 🏛️ Empresas exigentes"]
        O4b["O4 🔔 Outros conectores"]
    end
    N --> E1
    N --> E2
```

| Entrega | Objetivos | Candidatas | Base herdada da v1.xx |
| --- | --- | --- | --- |
| 🟢 v2.0 | O1, O2, O3, O4, O6, O7 e parte do O8 (o middleware, `D-260`) | 13: as nº 1, 2, 3, 4, 7, 8, 9, 12, 13, 14, 15, 17 e 18, mais a `MF-120` e a `MF-121`, parte da nº 5 (`D-260`); 19 mfs no total | As oito mfs da `D-021` |
| 🔵 v2.1 | O5, o resto do O8, o resto do O4 e o resto do O2 | 4 mfs, todas da onda 1: `MF-106`, `MF-119`, `MF-122` e `MF-123`; a onda 2 ficou sem mfs (`D-260`). A nº 6 está sem versão (`D-200`) | — |

O detalhe da v2.0 (as regras de cada funcionalidade, os riscos e as dependências) está em [A v2.0 consolidada](05-v2.0-consolidada.md). A tabela por entrega, mf a mf, está em [As versões](06-versoes.md).

## 5. O que a v2 pode reaproveitar da v1.xx 🔎

A v1.xx já entrega boa parte da base. O que se reaproveita, e quanto, quem confere é o arquiteto (`P-003`, `P-008`).

| O que a v1.xx tem | Serve de partida para |
| --- | --- |
| A conversa de análise, os blocos visuais, as fontes vivas, a web, a IA por função, a Home e as bases de demonstração | O1, O6 e a base herdada (`D-021`) |
| A segurança por pessoa (claims, reescrita e verificação da consulta) | O2 e O8, as duas etapas da `MF-106:Segurança dos dados por pessoa`, na v2.1 (`P-008`, c; `D-145`) |
| Owner, gestor, membro, convites e várias organizações | O7, a `MF-102:Organizações, pessoas e papéis` (`P-008`, j, k, l) |
| Os boards e os relatórios em PDF | O3, a `MF-112:Boards e Relatórios` (`P-008`, a, n) |
| A agenda e o envio por e-mail dos relatórios | O4, a `MF-114:Módulo de Agendamentos de Agentes` e a `MF-113:Conectores de Saída` (`P-008`, f, g) |

## 6. O que falta para começar o desenvolvimento

| Item | Quem | Trava |
| --- | --- | --- |
| `P-002`: confirmar o inventário de lacunas e medir o tempo de resposta | O arquiteto | A v2.0 |
| `P-003`: conferir o que da v1.xx se reaproveita | O arquiteto | A v2.0 |
| `P-008`: confirmar as 27 hipóteses técnicas, 25 delas sobre a v2.0 | O arquiteto | A v2.0 |
| `P-032`, `P-034`, `P-035` e `P-036`: as dúvidas técnicas novas da v2.0 (como a conta de IA da Maind chega às organizações, agora sem a conexão da instância, `D-266`; a fonte `web`, o board público e a faixa) | O arquiteto | A v2.0 |
| `P-048`, `P-040` e `P-042`: o fluxo do dono (o SaaS e o middleware em infraestruturas separadas, um middleware por organização) e o protocolo e o desenho do middleware, que subiu para a v2.0 (`D-260`) | O arquiteto | A v2.0 |
| `P-044`: apagar tudo de quem é excluído, diante da guarda técnica do registro de acesso. O owner ler as conversas sem aviso e apagar tudo de quem sai seguem decididos, e o cliente consulta o jurídico dele no setup (`D-247`) | O arquiteto | Pode mudar uma regra da v2.0 |
| `P-033` e `P-038`: o Athena, o Teams e o Google Chat | O arquiteto | A v2.1 |
| `P-022`: o preço em reais | O dono e o comercial da Maind | Não trava |

A skill do arquiteto de soluções existe; a `P-002`, a `P-003` e a `P-008` estão com ele.

## 7. Como manter

- O mapa **resume e aponta**. Quando uma decisão mudar, o backlog muda primeiro, e este mapa o acompanha.
- Funcionalidade nova entra numa linha da seção 3, com o objetivo, a mf, a entrega e a decisão que a sustenta.
- Os objetivos (O1 a O8) estão confirmados (`D-136`). Mudar um objetivo pede uma decisão nova no backlog.
