# As versões do Horus, mf a mf

Situação: 🟢 v2.0 decidida (`D-105` a `D-119` e `D-122`) · 🟢 v2.1 decidida: tudo o que ficou fora da v2.0 (`D-121`, `D-122`). Não há v2.2 por ora.

Última atualização: 03/11/2026 (a `D-145`: a segurança dos dados por pessoa inteira na v2.1).

As entregas do **Horus v2.xx** se chamam v2.0 e v2.1 (`D-135`); o Horus de hoje é a v1.xx (`D-134`). Uma tabela por versão, em ordem numérica de macro funcionalidade (mf). Se houver divergência, vale o [backlog estratégico](backlog-estrategico.md). O detalhe da v2.0 está em [A v2.0 consolidada](05-v2.0-consolidada.md).

Legenda: "nº" é o número da candidata e "nota" é a da pontuação (de 0 a 100, pesos da `D-015`) · ✋ entrou por decisão do dono, acima do corte da v2.0 · 🔎 leitura do PO, a confirmar.

## 🟢 v2.0: a pergunta na hora, com confiança, o acompanhamento e o aviso

Treze candidatas, mais a base herdada. Entrega em SaaS, de uma vez só (`D-016`, `D-109`). Na v2.0, a organização é a fronteira dos dados: a segurança por pessoa (a nº 10) foi para a v2.1 (`D-145`).

| Mf | Nome | O que entra | Nº | Nota | Decisão |
| --- | --- | --- | --- | --- | --- |
| `MF-101` | Administração da instância | Base herdada, com o painel dos assentos e sem o interruptor geral da segurança, que vai para a v2.1 | — | — | `D-021`, `D-080`, `D-145` |
| `MF-102` | Organizações, pessoas e papéis | A gestão de pessoas inteira, com quarentena, grupos e roles; os grupos dinâmicos, só por papel, e a planilha, só para os convites em lote | 9 | 55 ✋ | `D-108`, `D-114`, `D-145` |
| `MF-103` | Licenças e planos | A cobrança por assentos, num plano só, no SaaS | 15 | 42 ✋ | `D-107`, `D-117` |
| `MF-104` | Conectar as fontes vivas | Base herdada, sem a fonte alcançar a rede interna | — | — | `D-016`, `D-021` |
| `MF-105` | IA sob controle da organização | Base herdada, sem o modo "tudo dentro" | — | — | `D-016`, `D-021` |
| `MF-107` | Perguntar aos dados em português | Base herdada; a resposta em segundos na reunião; o retorno do usuário (👍🏻, 👎🏻 e 🚫) | 1 e 2 | 77 e 81 | `D-021`, `D-105` |
| `MF-108` | Respostas visuais | Base herdada | — | — | `D-021` |
| `MF-109` | A web como fonte | Base herdada; a web como fonte viva completa, com link e data | 3 | 67 | `D-021`, `D-105` |
| `MF-110` | Pergunta rápida | Perguntar sem sair da tela, num botão flutuante | 14 | 67 | `D-089`, `D-105` |
| `MF-111` | Chat pelo WhatsApp | Conversar com o Horus pelo WhatsApp | 18 | 50 ✋ | `D-099`, `D-119` |
| `MF-112` | Boards e Relatórios | O redesenho inteiro, com o PDF automático pelo agendador e pelos conectores | 8 | 59 ✋ | `D-058`, `D-119` |
| `MF-113` | Conectores de Saída | O carteiro: por onde o Horus entrega, só a usuários do Horus. Na v2.0, o e-mail e o WhatsApp | 12 | 47 ✋ | `D-041`, `D-122`, `D-124` |
| `MF-114` | Módulo de Agendamentos de Agentes | O relógio: quando gerar e enviar | 13 | 47 ✋ | `D-060`, `D-122` |
| `MF-115` | Agentes ativos | O trabalhador de IA que extrai, analisa e avisa | 7 | 49 ✋ | `D-062`, `D-122` |
| `MF-116` | Auditoria | O rastro de quem entregou o quê e de quem abriu | 17 | 41 ✋ | `D-093`, `D-119` |
| `MF-117` | Home da organização | Base herdada; a medida de autonomia | 4 | 66 | `D-021`, `D-105` |
| `MF-118` | Bases de demonstração | Base herdada | — | — | `D-021` |

## 🟢 v2.1: tudo o que ficou fora da v2.0

Decidida pelo dono (`D-121`). Cinco candidatas: o porquê (problema nº 2), a segurança por pessoa nas duas etapas (a nº 10 veio da v2.0, `D-145`), a marca completa e o Horus dentro da casa do contratante. O aviso estava aqui e foi para a v2.0 (`D-122`). As notas são as da pontuação da v2.0; quando a v2.1 for a próxima, as candidatas voltam a ser pontuadas contra o objetivo dela.

| Mf | Nome | O que entra | Nº | Nota | Decisão |
| --- | --- | --- | --- | --- | --- |
| `MF-101` | Administração da instância | A marca completa do contratante: logo, nome e e-mail em todo o produto | 6 | 29 | `D-011`, `D-121` |
| `MF-103` | Licenças e planos | A ativação dos assentos no on-premises (parte da nº 5) | 5 | eliminada da v2.0 | `D-067`, `P-016`, `D-121` |
| `MF-104` | Conectar as fontes vivas | A fonte alcançando a rede interna do contratante (parte da nº 5) | 5 | eliminada da v2.0 | `D-016`, `D-121` |
| `MF-105` | IA sob controle da organização | O modo "tudo dentro", com a IA dentro de casa (parte da nº 5) | 5 | eliminada da v2.0 | `D-016`, `D-121` |
| `MF-106` | Segurança dos dados por pessoa | As duas etapas: o acesso configurado dentro do Horus (veio da v2.0) e a segurança corporativa integrada, com o login corporativo e as roles pelo crachá. Com ela voltam os grupos por claims, a liberação de dados do gestor no board e o interruptor geral da segurança | 10 e 11 | 78 e 58 | `D-028`, `D-118`, `D-121`, `D-145` |
| `MF-113` | Conectores de Saída | Os demais conectores, como Teams e Google Chat 🔎 (parte da nº 12) | 12 | — | `D-121`, `D-124` |
| `MF-119` | Investigação guiada | Descobrir o porquê de uma mudança, passo a passo | 16 | 61 (provisória) | `D-081`, `D-104`, `D-121` |

**O que trava a v2.1:**
- 🕓 A definição macro da `MF-119:Investigação guiada` (`P-018`), que o dono adiou por pedir muita conversa.
- 🕓 Como ativar os assentos no on-premises (`P-016`).
- 🔎 A forma de entrega (de uma vez só ou em ondas), que não foi decidida.

## ➖ Fora do produto

| Item | Por quê | Decisão |
| --- | --- | --- |
| Melhoria do modelo semântico | Não é mf: fica com o time de dados por enquanto | `D-083` |

## Em números

| Versão | Candidatas | Situação |
| --- | --- | --- |
| v2.0 | 13 | 🟢 decidida |
| v2.1 | 5 | 🟢 decidida |

As 18 candidatas estão todas distribuídas: 13 + 5 (a nº 10 passou da v2.0 para a v2.1 com a `D-145`).

## Como manter

- A v2.0 acompanha o backlog e o [documento da v2.0](05-v2.0-consolidada.md). A v2.1 acompanha a `D-121` e a `D-122`.
- Quando a v2.0 estiver entregue, as candidatas da v2.1 voltam à pontuação contra o objetivo da v2.1, e esta página muda junto.
- A proposta anterior do PO (v2.1, v2.2 e "sem versão") ficou registrada na `D-120`, substituída.
