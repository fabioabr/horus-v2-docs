# Documentação das macro funcionalidades do Horus v2

Esta pasta é a **documentação para quem vai usar ou contratar o Horus**: uma página por macro funcionalidade (MF), em linguagem
simples, com perguntas frequentes e, quando um fluxo ajuda, um diagrama. Ela é **gerada com o plugin DocX** (design da Kinto) e é
**separada do portal de `docs/`**, que continua como está.

**Situação:** em refinamento. Escritas: **as 18 macro funcionalidades da v2.0** (MF-101 a MF-105, MF-107 a MF-118 e MF-120). Ficam de fora as 5 da v2.1 (MF-106, 119, 121, 122 e 123), que aparecem nas páginas só como “chega na versão 2.1”.

## O que há aqui

```
documentacao/
├── docx.json              ← a configuração do portal (as macro funcionalidades, as seções, os diagramas)
├── content/               ← os fragmentos HTML, que são a fonte editável
│   ├── como-ler.html      ← o que é uma MF, como cada página é organizada, o glossário
│   └── mf-101.html … mf-120.html   ← uma página por macro funcionalidade
├── diagramas/             ← os diagramas (fonte JSON do Archify, em fontes/, e a página pronta de cada um)
└── (a saída gerada fica em ../docs, que o GitHub Pages serve; não se edita à mão)
```

A marca (logos e cor do Horus) vem de `.claude/plugins-data/kbr-docs/docs-brand.yml`, na raiz do repositório.

## O formato de cada página de MF

Todas seguem a mesma ordem: **o que é** (com uma imagem do dia a dia) → **como funciona na prática** (quem faz o quê, passo a passo,
com um diagrama) → **nos bastidores** (a tecnologia, só o bastante para a história fazer sentido) → **o que ela não faz** e as
**funcionalidades ligadas** → **perguntas frequentes** (6 por página). Sem códigos de decisão (`D-nnn`, `ARQ-nnn`) no texto: eles
ficam só nas tabelas de fontes abaixo. Um aviso “Ainda em definição” traz, em linguagem de cliente, o que as fontes deixam em aberto.

## De onde veio o conteúdo

Cada afirmação das páginas vem de documentos deste repositório: a **leitura do PO** (`docs/leitura/mfs/mf-10X-*.md`, de 05/11/2026), o
**backlog estratégico** (`docs/raw/produto/backlog-estrategico.md`, seções `### D-nnn`) e o **registro de decisões de arquitetura**
(`docs/raw/arquitetura/02-registro-de-decisoes.md`, seções `### ARQ-nnn`). Quando a leitura e uma decisão divergem, vale a decisão
mais recente e específica.

### MF-101 · Administração da instância

| Assunto da página | Fonte |
|---|---|
| O que é, as seis coisas que a administração faz, os limites | leitura da MF-101 |
| As situações da organização, suspender e excluir | `D-148`, `D-149`; `ARQ-037` |
| Os cinco tipos de assento | `D-069`, `D-193`, `D-194`, `D-203` |
| A IA da instância e a da organização | `D-216`, `D-217`, `D-218`, `D-241` |
| Uso, custo, aviso de custo e relatório | `D-149`, `D-153`, `D-157`, `D-166`, `D-158`; `ARQ-017`, `ARQ-084`; a visão de cobrança do owner: `D-214` |
| Avisos, faixa e página de manutenção | `D-151`, `D-154`, `D-165`, `D-168`; quem é avisado quando um serviço para: `D-218`, `D-240` |
| Nos bastidores | `ARQ-010`, `ARQ-088`, `ARQ-097`, `ARQ-046`; `docs/raw/arquitetura/07-seguranca.md` §3.1 |

### MF-102 · Organizações, pessoas e papéis

| Assunto da página | Fonte |
|---|---|
| O que é, os papéis, os limites, as funcionalidades ligadas | leitura da MF-102; `D-013`, `D-047`, `D-048`, `D-056`, `D-074`, `D-108`; mais de um owner: `D-069`, `ARQ-039` |
| Como uma pessoa entra (convite, aprovação, assento reservado, prazo) | `D-070`, `D-071`, `D-077`, `D-078`; só entra quem tem convite: `07-seguranca.md` §3.1 |
| A planilha de convites em lote | `D-236`, `D-145`, `ARQ-090` |
| A quarentena e os boards públicos | `D-047`, `D-048`, `D-056`, `D-071` |
| Trocar de faixa ou de gestor | `D-072`, `D-046`, `D-049` |
| Quando alguém muda de faixa ou sai | `D-206` a `D-210`; o gestor que sai: `D-056` |
| Grupos | `D-019`, `D-029`, `D-049`, `D-055`, `D-235`, `D-199` |
| Roles, os nove botões e as regras; tudo nasce liberado | `D-110` a `D-114`, `D-119`, `D-122`, `D-215`, `D-220`, `D-221`; `D-228` |
| Dados, conversas, perfil e avisos | `D-145`, `ARQ-090`, `D-223`, `D-094`, `D-128`, `D-118` |
| Nos bastidores; o que não faz | `ARQ-008`, `ARQ-038`, `ARQ-039`; `07-seguranca.md` §3.1 e §3.2; `D-118`, `D-184`, `D-199`, `D-209`, `D-234` |
| Diagrama “O caminho de um convite” | `D-070`, `D-071`, `D-077`, `D-047`, `D-048`, `D-078` |

### MF-103 · Licenças e planos

| Assunto da página | Fonte |
|---|---|
| O que é; plano único, cobrado por assento e por tipo; preço fora do produto | leitura da MF-103; `D-080`, `D-107`, `D-115`, `D-116`, `D-117` |
| Quem cuida de quê | `D-067`, `D-068`, `D-146`, `D-193` |
| As três faixas de membro | `D-069`, `D-079`, `D-193`, `D-194`, `D-203`; teto do assento sobre as roles: `D-114`, `ARQ-039` |
| Owner grátis, mais de um owner, owner e gestor num assento só | `D-123`, `D-069`, `D-074` |
| Quarentena e assento guardado contam como ocupados | `D-071`, `D-047`, `D-048`, `D-076` |
| O convite, a aprovação, a reserva e o prazo | `D-070`, `D-071`, `D-078`, `D-039`, `D-236` |
| Mudar o tipo; o que a pessoa criou; sem transferência | `D-072`, `D-206` a `D-209`; `05-v2.0-consolidada.md` §8 |
| Visão de cobrança, pedir mais, reduzir, o corte | `D-214`, `D-077`, `D-069`, `D-076`, `D-068`, `D-075`, `D-148` |
| O que o assento inclui e o que se paga à parte | `D-159`, `D-160`, `D-216`, `D-117` |
| Nos bastidores; o que não faz | `ARQ-005`, `ARQ-008`, `ARQ-039`; `04-software.md` §3.3; `06-dados.md` §3; `D-157`; `D-080`, `D-188`, `D-175`, `D-176`, `D-196` |
| Diagrama “A vida de um assento” | `D-068`, `D-071`, `D-072`, `D-076` |

### MF-104 · Conectar as fontes vivas

| Assunto da página | Fonte |
|---|---|
| O que é, quem faz o quê, os passos | leitura da MF-104; `D-013`, `D-021`, `D-193`, `D-194`, `D-219` |
| As tecnologias (cinco na v2.0, o Athena na v2.1) | `D-161`, `D-198`, `D-201`; `ARQ-052`; `08-integracoes.md` §3.5 |
| Os dois caminhos, a VPN fora da v2.0, o middleware na v2.1 | `ARQ-052`; `08-integracoes.md` §3.5; `D-188`, `D-196` |
| Só ler (o “Testar”, a porta única, 500 linhas e 30 s) | `D-001`, `D-022`; `ARQ-052`, `ARQ-077`, `ARQ-090`; `05-motor-de-analise-e-ia.md` |
| A credencial no cofre; a Maind não vê os dados | `07-seguranca.md` §3.7; `D-193` |
| O modelo semântico; o teto de inferência | `D-083`, `D-219`, `D-005`, `D-014`; `D-220`, `D-110`, `D-024`; `05-motor-de-analise-e-ia.md` §3.4 e §3.5 |
| A idade mínima do dado | leitura da MF-104 (o sentido vem do código da v1.xx); `04-software.md` §3.2 |
| Quem vê os dados; a organização como fronteira | `D-145`; `ARQ-010`, `ARQ-034`, `ARQ-090` |
| Quando a fonte deixa de conectar | `D-240` |
| Nos bastidores; o que não faz | `04-software.md`; `ARQ-010`, `ARQ-034`, `ARQ-052`, `ARQ-077`, `ARQ-060`; `D-022`, `D-083`, `D-161`, `D-198`, `D-186` a `D-188`, `D-196` |

### MF-105 · IA sob controle da organização

| Assunto da página | Fonte |
|---|---|
| O que é, as cinco escolhas | leitura da MF-105; `D-246` |
| De onde vem a IA, nasce sem IA, conexão da instância sem edição | `D-216`, `D-217` |
| Os provedores (OpenRouter e Bedrock); fabricantes via OpenRouter | `ARQ-051`; `08-integracoes.md` §3.4 |
| Pesquisa na web só com provedor que pesquisa; só a pergunta vai à busca | `ARQ-027`, `ARQ-031` |
| Curadoria, modelo padrão, modelo por tarefa, troca pela role | `D-216`, `D-110`; `05-motor-de-analise-e-ia.md` §3.3 e §3.10 |
| Modelo dos agentes | `D-061`, `D-062`, `D-063`; `ARQ-031` |
| O modelo nunca muda em silêncio | `ARQ-051`; `08-integracoes.md` §3.4 |
| Consumo, estimativa e quem vê o quê | `ARQ-083`, `ARQ-017`, `ARQ-084`; `D-241`, `D-153` |
| Sem corte automático; limites por execução; alavancas do owner | `D-234`, `ARQ-030`, `D-062`, `D-244` |
| Quando a IA para | `D-218` |
| Onde a IA processa os dados (Brasil); “tudo dentro”; middleware 2.1 | `ARQ-051` (nota de 02/11); `D-010`, `D-185`, `D-188`, `D-190`, `D-196` |

### MF-107 · Perguntar aos dados em português

| Assunto da página | Fonte |
|---|---|
| O que é, quem pergunta, onde aparece, os passos | leitura da MF-107; `D-125`, `D-126`, `D-193`, `D-194`, `D-088`, `D-095`, `D-096`; `ARQ-006` |
| Os números vêm do banco; o conserto de uma tentativa | `D-001`, `D-022`; `05-motor-de-analise-e-ia.md` §1 e §3.3 |
| Os ajustes, as roles e a soma; os dois modos e a web ao lado | `D-110`, `D-111`, `D-215`; `D-162`, `D-243`; `ARQ-026`, `ARQ-027`; `05-motor-de-analise-e-ia.md` §3.6 |
| Os níveis de inferência na conversa | `D-220`, `D-024`, `D-130`; `ARQ-025`; `05-motor-de-analise-e-ia.md` §3.5 |
| O que aparece na resposta; a Análise avançada; fixar num board | `D-021`, `D-126`, `D-221`; `05-motor-de-analise-e-ia.md` §3.3 e §3.7 |
| O retorno, o reporte, os três motivos, o “recebido” | `D-005`, `D-014`, `D-127`, `D-128`, `D-129`, `D-087`; `ARQ-028` |
| As perguntas respondidas; a divisão por gestor e por pessoa | `D-004`, `D-222`, `D-133`, `D-132`, `D-087`, `D-238`; `ARQ-029` |
| As conversas, o prazo, o owner que lê; aviso “Na implantação” | `D-095`, `D-223`, `D-247`; `ARQ-035`; `06-dados.md` §3.3 |
| Nos bastidores; o que não faz | `ARQ-006`, `ARQ-024`, `ARQ-028`, `ARQ-029`, `ARQ-035`, `ARQ-013`; `D-125`, `D-128`, `D-145`, `ARQ-090`; leitura da MF-107 |

### MF-108 · Respostas visuais

| Assunto da página | Fonte |
|---|---|
| O que é, as cinco coisas, o alcance novo | leitura da MF-108; `D-021`, `D-001`; `05-v2.0-consolidada.md` §3.2 |
| Quem vê e quem ajusta; baixar e fixar | `D-203`, `D-221`, `D-110`, `D-237` |
| Os seis tipos, quinze variantes, dois blocos, sem edição | `05-v2.0-consolidada.md` §3.2; `14-conferencia-do-produto.md` §2 e §3 (correção A-26); `ARQ-007` |
| O fluxo nasce do modelo semântico, só no modo dados | leitura da MF-108; `05-motor-de-analise-e-ia.md` §3.3, §3.4 e §4 |
| A IA escolhe a forma, os números são do banco; sem dado, sem desenho | `D-001`; `01-estrategia-da-solucao.md` §1; `05-motor-de-analise-e-ia.md` §1, §3.3 e §4; agente: `ARQ-030` |
| Um desenho só em todo lugar; WhatsApp com imagem e link | `ARQ-007`; `D-096`; `D-088`; `08-integracoes.md` (WhatsApp: texto e mídia) |
| O tema dos gráficos | `D-237`, `D-200`, `D-183` |
| Nos bastidores; o que não faz | `ARQ-007`; `04-software.md`; `05-motor-de-analise-e-ia.md` §3.3, §3.7 e §4; `D-180` |
| Celular e tablet (“Ainda em definição”) | `D-002`; `03-inventario-de-lacunas.md` linha 10; `14-conferencia-do-produto.md` §2; `12-qualidade-e-testes.md` |

### MF-109 · A web como fonte

| Assunto da página | Fonte |
|---|---|
| O que é, os três usos, o interruptor, quem usa | leitura da MF-109; `D-162`, `D-215`, `D-131`, `D-110`, `D-194`, `D-114` |
| Hoje e na v2.0 (fonte no meio do texto, sem data; a web como modo) | leitura da MF-109; `D-215`; `05-motor-de-analise-e-ia.md` §3.5 |
| Quando o interruptor aparece (instalação, provedor, role) | `ARQ-027`, `ARQ-031`, `D-010`, `D-110`, `D-215` |
| Link e data, data lida na página, conferência dos links, fato à parte | `D-006`, `D-131`; `ARQ-026`; `05-motor-de-analise-e-ia.md` §3.6 e §5 |
| O fato em qualquer nível, a causa só do nível 4 | `D-130`; `ARQ-025`; `05-motor-de-analise-e-ia.md` §3.5 |
| Quando a pesquisa não traz fato; o prazo próprio da busca | `D-243`; `05-motor-de-analise-e-ia.md` §5 |
| Em todo canal; o cartão do board; os agentes | `D-131`, `D-242`; `05-motor-de-analise-e-ia.md` §3.6; leituras da MF-110 e da MF-111 |
| Nos bastidores; o que não faz; o middleware na v2.1 | `ARQ-026`, `ARQ-027`, `ARQ-031`; `07-seguranca.md`; `D-006`, `D-130`, `D-242`; `D-190`, `D-196` |
| Páginas cadastradas, tipo de fonte `web` (“Ainda em definição”) | `D-162`, `D-215`, `P-034` |

### MF-110 · Pergunta rápida

| Assunto da página | Fonte |
|---|---|
| O que é; onde o botão aparece; independente da tela | leitura da MF-110; `D-065`, `D-085`, `D-089` |
| Quem tem o botão; o assento antes da role; a role padrão; o owner fora das roles | `D-089`, `D-107`, `D-110`, `D-112`, `D-114`, `D-194`, `D-203` |
| A conversa do popup: fica, salva, apaga, uma por vez | `D-086`; `ARQ-020`, `ARQ-029` |
| Tudo o que a conversa oferece; a web como interruptor; fixar num board | `D-088`, `D-215`, `D-220`, `D-221` |
| O que conta na medida; a divisão por canal na Home | `D-087`, `D-133`, `D-222`, `D-239` |
| O reporte guardado; quem é excluído leva os reportes pendentes; aviso “Na implantação” | `D-087`, `D-129`, `D-210`, `D-247`; `ARQ-028` |
| Nos bastidores; o que não faz | `ARQ-006`, `ARQ-020`, `ARQ-024`, `ARQ-028`, `ARQ-029`; `04-software.md` §3.5; `05-motor-de-analise-e-ia.md` §3.8; `D-085`, `D-086`, `D-089`, `D-145` |

### MF-111 · Chat pelo WhatsApp

| Assunto da página | Fonte |
|---|---|
| O que é; só conversa individual; quem conversa (o bronze não) | leitura da MF-111; `D-084`, `D-099`, `D-119`, `D-194`, `D-203`, `D-225`, `D-228` |
| Do número ligado à primeira resposta; o owner liga o canal; as mensagens-padrão da Meta | `D-094` a `D-098`, `D-099`, `D-228`; `ARQ-048`, `ARQ-049`; `08-integracoes.md` §3.3 |
| Quem escreve sem poder conversar: a resposta fixa | `D-225`; `ARQ-039`, `ARQ-050` |
| O número como credencial (código, um número por pessoa, uma organização por vez, desligar) | `D-094`, `D-224`, `D-124`; `ARQ-050`; `08-integracoes.md` §3.3 |
| O que chega no WhatsApp (texto, até duas imagens, link, web com link e data) | `D-096`, `D-098`, `D-099`, `D-131`; `ARQ-007`, `ARQ-048` |
| A mesma conversa do app (histórico, retorno, medida, divisão por canal) | `D-095`, `D-096`, `D-133`, `D-222`, `D-239`; `ARQ-024`, `ARQ-029` |
| De quem é o número e quem paga; quem é avisado se a conta parar | `D-097`, `D-160`, `D-240`; `ARQ-050` |
| Nos bastidores; o que não faz; “Na implantação” | `ARQ-006`, `ARQ-007`, `ARQ-024`, `ARQ-039`, `ARQ-048`, `ARQ-049`, `ARQ-073`; `D-099`, `D-188`, `D-198`; `D-223`, `D-247` |

### MF-112 · Boards e Relatórios

| Assunto da página | Fonte |
|---|---|
| O que é, as cinco coisas, o que vem do Horus de hoje | leitura da MF-112; `D-018`, `D-057`, `D-058` |
| Quem faz o quê; o owner não é dono de board | `D-042`, `D-048`, `D-069`, `D-193`, `D-194`, `D-203` |
| Um board, da resposta ao PDF; os cartões | `D-058`, `D-119`, `D-221`, `D-230`, `D-242`; `ARQ-006` |
| Vivo na tela e em PDF; o board maior que a folha | `D-057`, `D-059`, `D-229`; `ARQ-007` |
| O PDF que chega sozinho; aviso no lugar do board desabilitado | `D-064`, `D-122`, `D-059`, `D-044`, `D-045`; `ARQ-022` |
| Publicar: as quatro visibilidades, os grupos, o gestor que nasce liberado | `D-042`, `D-043`, `D-049`, `D-056`, `D-058`, `D-228` |
| Editar, desabilitar, o espaço da organização, os boards públicos | `D-043`, `D-044`, `D-045`, `D-048`, `D-054`, `D-163`, `D-164`, `D-206`, `D-207`, `D-209` |
| Os dados do board; quando o autor muda de faixa ou sai | `D-145`, `D-163`, `D-199`; `ARQ-090`; `D-206` a `D-209` |
| O que fica registrado; o aviso de abertura | `D-058`, `D-090`, `D-231`; `ARQ-043` |
| Nos bastidores; o que não faz | `ARQ-006`, `ARQ-007`, `ARQ-023`; `04-software.md` §3.3 e §3.4; `D-058`, `D-199`, `D-209`, `D-242`, `D-167` |

### MF-113 · Conectores de Saída

| Assunto da página | Fonte |
|---|---|
| O que é, os dois canais, quem faz o quê, o que não faz | leitura da MF-113; `D-033`, `D-034`, `D-035`, `D-041`, `D-124`, `D-182`, `D-197`, `D-198`, `D-201` |
| Quem pode receber, quem cria envios, o botão nas roles | `D-079`, `D-122`, `D-228`, `D-193`, `D-194`; `D-059` |
| O contato de cada pessoa e a aprovação | `D-038`, `D-039`, `D-228`, `D-094` |
| O conector de e-mail | `D-128`; `ARQ-046`; `08-integracoes.md` §3.2 |
| O conector de WhatsApp, quem paga, um número por pessoa | `D-097`, `D-124`, `D-160`, `D-224` |
| O que não cabe no canal; quando um canal para | `D-227`, `D-226`, `D-240` |
| Cada entrega registrada; a empresa no controle do que sai | `D-090`, `D-122`, `D-022`, `D-034`; `ARQ-022` |
| Nos bastidores | `ARQ-022`, `ARQ-046`, `ARQ-048`, `ARQ-049`; `04-software.md`; `08-integracoes.md` §3.2 e §3.3 |

### MF-114 · Módulo de Agendamentos de Agentes

| Assunto da página | Fonte |
|---|---|
| O que é: agendador único, o PDF de um board ou um agente | leitura da MF-114; `D-035`, `D-036`, `D-037`, `D-060`, `D-064`; `05-v2.0-consolidada.md` §5.10 |
| Quem agenda e para quem | `D-059`, `D-060`, `D-079`, `D-193`, `D-194`, `D-203` |
| Do começo ao fim; registro na Auditoria; board desabilitado | `D-035`, `D-064`, `D-090`, `D-122`, `D-044`, `D-045`; `ARQ-022` |
| A aprovação do owner (por tipo, nasce automática, as três marcas) | `D-038`, `D-039`, `D-228`, `D-244`; `D-062` |
| Roda como quem criou, com as permissões lidas na hora | `D-060`, `D-145`, `D-163`; `ARQ-030`, `ARQ-041`, `ARQ-090` |
| Quando não roda: falha, não cabe no canal, corte, rebaixado, excluído | `D-226`, `D-227`, `D-075`, `D-206` a `D-209` |
| Nos bastidores; o que não faz | `D-036`; `ARQ-004`, `ARQ-005`, `ARQ-022`; `04-software.md` |

### MF-115 · Agentes ativos

| Assunto da página | Fonte |
|---|---|
| O que é, quem faz o quê, a corrente das quatro MFs | leitura da MF-115; `D-020`, `D-062`, `D-063`, `D-064`, `D-022`, `D-194`, `D-203`, `D-059` |
| Um agente, do texto à entrega | `D-061`, `D-062`, `D-024`, `D-064` |
| A aprovação do owner e as situações do agente | `D-038`, `D-039`, `D-228`, `D-244`; `D-043`, `D-044`, `D-207` |
| As instruções, a conferência e o nível de inferência | `D-023`, `D-024`, `D-061`, `D-062`; `ARQ-025`, `ARQ-030` |
| Na hora marcada: o ciclo, as permissões, a web, a entrega | `ARQ-006`, `ARQ-007`, `ARQ-022`, `ARQ-024`, `ARQ-030`; `05-motor-de-analise-e-ia.md` §3.6 e §3.9; `D-060`, `D-145`, `D-035`, `D-059`, `D-124` |
| Quando algo dá errado; o custo de um agente | `D-226`, `D-227`, `D-206` a `D-209`, `D-075`; `D-216`, `D-153`, `D-234`; `ARQ-031` |
| Nos bastidores; o que não faz | `ARQ-006`, `ARQ-007`, `ARQ-030`, `ARQ-031`, `ARQ-095`; `ARQ-029`, `D-133`; `D-022`, `D-035`, `D-062`, `D-090`, `D-232` |

### MF-116 · Auditoria

| Assunto da página | Fonte |
|---|---|
| O que é, os seis pontos, quem vê o rastro | leitura da MF-116; `D-082`, `D-090`, `D-091`, `D-093`, `D-054`; `ARQ-009` |
| Quem recebeu o board de outubro? (passos) | `D-093`, `D-092`, `D-231`; `ARQ-035` |
| O que entra e o que fica de fora; a tela da auditoria | `D-090`, `D-122`, `D-093`, `D-199`; `ARQ-035` |
| Um rastro que serve de prova; o prazo; encurtar apaga | `D-092`, `D-093`, `D-210`; `ARQ-009`, `ARQ-035`; `06-dados.md` §3.3 |
| O aviso de que a abertura é registrada | `D-090`, `D-231`; `ARQ-043` |
| Quando alguém é excluído; aviso “Na implantação” | `D-209`, `D-210`, `D-211`, `D-247`; `P-044` (lado técnico) |
| Nos bastidores; o que não faz | `ARQ-009`, `ARQ-010`, `ARQ-012`, `ARQ-035`; `04-software.md`; `D-093`, `D-091`, `D-145`, `D-199` |

### MF-117 · Home da organização

| Assunto da página | Fonte |
|---|---|
| O que é; a Home de hoje | leitura da MF-117; `D-021`; `05-v2.0-consolidada.md` §3.2; `04-software.md` §3.2 |
| A medida de autonomia e a qualidade; onde aparecem | `D-133`, `D-004`, `D-005`, `D-129` |
| Um mês na Home (passos, números ilustrativos) | leitura da MF-117; `D-132`, `D-133`, `D-238`, `D-239` |
| A grade do owner; a faixa separada | leitura da MF-117; `D-170`, `D-172`, `D-173`, `D-174` |
| O que entra na conta; a divisão por canal | `D-004`, `D-222`, `D-087`, `D-095`, `D-239`; `ARQ-029` |
| Quem vê o quê | `D-133`, `D-238`, `D-132` |
| Quando alguém sai; aviso “Na implantação”; o prazo (400 dias) | `D-210`, `D-211`, `D-247`; `ARQ-035`; `06-dados.md` §3.3 e §3.5 |
| Nos bastidores; o que não faz | `ARQ-029`; `05-motor-de-analise-e-ia.md` §3.8; `11-observabilidade.md` §3.5; `D-132`, `D-125`, `ARQ-013`, `D-241` |

### MF-118 · Bases de demonstração

| Assunto da página | Fonte |
|---|---|
| O que é, quem usa, a vitrine, a demonstração passo a passo | leitura da MF-118; `D-021`, `D-109`, `D-193`, `D-233`; `ARQ-011` |
| O que já vem pronto e o que não vem | `ARQ-011`, `ARQ-089`; `06-dados.md` §3.5 |
| Os boards publicados no espaço da organização | `D-245`, `D-163` |
| Um cenário para cada funcionalidade | `D-232`; a tabela de cenários da leitura |
| Nos bastidores | `ARQ-059`, `ARQ-089`, `ARQ-012`; `09-infraestrutura-e-ambientes.md` §3.7; `12-qualidade-e-testes.md` |
| O que não faz | `D-199`, `D-197`, `D-145`, `D-233`, `D-245`; `ARQ-090` |

**Escolha editorial:** a leitura, a `D-233` e a `ARQ-011` dão nomes de marcas reais às organizações de exemplo; a página diz só “rede de lojas” e “frota”, para não pôr uma marca real ao lado de dados inventados.

### MF-120 · Faixa de avisos e números

| Assunto da página | Fonte |
|---|---|
| A faixa: o que é, as duas categorias, quem monta e quem vê | `D-152`, `D-174`, `D-204`, `D-170`, `D-147`, `D-193`; leitura da MF-120; `05-v2.0-consolidada.md` §5.13 |
| Os avisos e a caixa de texto livre do owner | `D-151`, `D-165`, `D-170`, `D-213` |
| O card de número (métrica do modelo semântico e período) | `D-212` |
| O catálogo próprio; a montagem (sem prévia, telas separadas) | `D-173`, `D-171`, `D-172`; leitura da MF-117 |
| Quem vê os números (o acesso de quem vê, o card que some, a v2.0 com a organização inteira) | `D-167`, `D-169`, `D-163`, `D-145` |
| Os números da instância (Instance Cards) | `D-153`, `D-170` (leitura do PO, ainda a confirmar) |
| Esconder a faixa e a página de manutenção | `D-168`, `D-154` |

## Pontos em aberto que as páginas declaram

**Indicador “Na implantação” (decisão do dono, 06/11/2026):** as regras que tratam de dados pessoais ficam como decididas, e as páginas
indicam que o cliente deve consultar o jurídico dele durante o setup. Estão nele: a Maind ver o nome de quem ocupa cada assento (MF-101),
o owner ler as conversas de todos sem aviso e apagar tudo de quem sai (MF-102) e, quando for escrita, a MF-116 (Auditoria).

| Página | O que ainda não está fechado |
|---|---|
| MF-101 | (nada além do indicador “Na implantação”) |
| MF-102 | Do lado técnico, o arquiteto confere se apagar tudo de quem sai convive com a guarda do registro de acesso e das cópias de segurança |
| MF-103 | O preço do assento prata e se o preço muda para quem traz a própria IA; os números do prazo da reserva |
| MF-104 | Se haverá fonte de páginas da web cadastradas; o formato do arquivo do modelo semântico |
| MF-105 | O preço para quem traz a própria IA; por onde o aviso chega ao dono da conexão quando a IA para; como a falha aparece na tela |
| MF-107 | (nada além do indicador “Na implantação”, pela leitura das conversas pelo owner) |
| MF-108 | Como cada tela, com gráficos e tabelas, se comporta no celular e no tablet (desenho técnico e testes de ponta a ponta) |
| MF-109 | Se haverá fonte de páginas da web cadastradas e o destino do tipo de fonte `web` do Horus de hoje |
| MF-110 | (nada além do indicador “Na implantação”, pelos reportes de quem é excluído) |
| MF-111 | Como dar o retorno e trocar os controles por texto; o caminho técnico até a Meta e os passos para ligar a conta; os textos da resposta fixa e do aviso de número movido; se o que se vê pelo WhatsApp entra na Auditoria (mais o indicador “Na implantação”) |
| MF-112 | Se, em “Pessoas específicas”, o gestor escolhe qualquer pessoa ou só as que gere; o limite de tamanho da página do PDF de um board muito grande |
| MF-113 | O tamanho máximo de cada canal e o texto do aviso ao autor; por onde chega o aviso quando um canal para; o caminho técnico até o WhatsApp |
| MF-114 | Se a pessoa é avisada quando o owner aprova ou recusa; por qual canal chega o aviso de falha; quantas vezes o Horus tenta antes de dar uma rodada por perdida; o texto do aviso de board desativado |
| MF-115 | Os limites técnicos de cada execução (a calibrar); por onde o autor recebe o aviso de falha; se é avisado da aprovação ou recusa; o tamanho máximo do PDF e do alerta em cada canal |
| MF-116 | Se o que a pessoa vê pelo WhatsApp entra no rastro; o texto final do aviso padrão e o lugar do link (mais o indicador “Na implantação”) |
| MF-117 | (nada além do indicador “Na implantação”, pela contagem de quem é excluído) |
| MF-118 | O detalhe de cada cenário; se é viável uma conta de WhatsApp de exemplo; se duas organizações e os boards do espaço da organização bastam |
| MF-120 | O catálogo da faixa (indicadores, ícones e as regras de cada componente, inclusive se o aviso do owner terá hora de fim); o movimento e a aparência; quem vê os números da instância (leitura do PO a confirmar); o nome (provisório) |

## Como gerar de novo

Da pasta `documentacao/`, com o plugin DocX instalado (`docx@maindtech`, 0.4.0 ou superior):

```
python <plugin docx>/scripts/docx.py gerar --config docx.json
python <plugin docx>/scripts/docx.py validar --site site
```

Para os diagramas: a fonte é o JSON em `diagramas/fontes/`. Se mudar, refaça o `finalize` do Archify e a casca (`archify-maind`) e gere
de novo; a página em `diagramas/` é derivada, e editá-la à mão se perde. O DocX copia a página do diagrama sem tocá-la. As pastas
`diagramas/fontes/*-review-*` e os recibos `.finalize*.json` são evidência das verificações do Archify e não entram na documentação.

Para isolar a marca de qualquer configuração do usuário ao gerar, aponte `CLAUDE_USER_HOME` para uma pasta vazia.
