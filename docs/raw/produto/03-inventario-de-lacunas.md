# Inventário de lacunas: o norte contra o produto de hoje

Situação: 🔎 levantamento preliminar, recorte do **problema nº 1** (a pergunta de análise na hora) e dos pressupostos transversais.

Última atualização: 02/11/2026.

Este documento compara o que o [norte](02-norte-do-produto.md) afirma com o que o Horus faz hoje. Segue a `D-003`: a diferença é uma **lacuna a fechar**, não um motivo para encolher o norte. Ele não decide quando nem como fechar cada lacuna: a ordem sai da composição das versões, e o como é do arquiteto de soluções.


> Os caminhos de código e de documento citados aqui (`apps/…`, `docs/produto/horus-visao-geral.md`, `.backlog/` e outros) são do **repositório `horus`, a v1.xx**, e não da pasta da v2 (`D-140`).

## Como este levantamento foi feito

- Busca no código de `apps/web` e `apps/server`, em 30/10/2026, e leitura do `CLAUDE.md` do repositório.
- **Não executei o produto nem medi tempos de resposta.** O que está marcado como “não encontrei” significa que a busca não achou, e não que a prova da ausência foi feita.
- Cada linha precisa ser confirmada pelo arquiteto de soluções.

Legenda: ✅ já existe · 🟡 existe em parte · ❌ não encontrei · ❓ não verificado.

## Problema nº 1: a pergunta de análise na hora

| # | O que o norte pede | O que o produto faz hoje | Situação |
| --- | --- | --- | --- |
| 1 | O gestor faz uma pergunta de análise e recebe a resposta na hora | Existe a conversa de análise (rota `/analise`), com motor de chat que responde em modo dados e em modo web | ✅ |
| 2 | A resposta vem por **gráfico, texto ou os dois**, com visual claro | Os blocos de resposta são KPI, gráfico, tabela, mapa de calor e fluxo, com no máximo dois blocos por resposta | ✅ |
| 3 | A resposta chega em **segundos** (momento-âncora) | Não medi o tempo de resposta | ❓ |
| 4 | O nível de inferência autorizado pela organização | Existem cinco níveis (descritivo, explicativo, comparativo, hipótese, especulativo), com padrão no nível 2 | ✅ |
| 5 | A **web como fonte viva** em todos os usos | O modo web existe; os fatos buscados entram com fonte citada só do nível 4 em diante (`composerLogica.ts`) | 🟡 |
| 6 | Toda informação da web com **link e data**, ou aviso de data não identificada (`D-006`) | Não encontrei exigência de data de publicação nem o aviso de data não identificada | ❌ |
| 7 | Retorno do usuário: **👍🏻 Gostei, 👎🏻 Não gostei, 🚫 Reportar** (`D-005`) | Não encontrei botões de avaliação nas respostas do chat | ❌ |
| 8 | O reporte chega ao **owner da organização** (`D-014`) | Não existe o reporte; logo, não existe o encaminhamento | ❌ |
| 9 | Medida-norte: perguntas de análise respondidas sem chamado (`D-004`) | Existe uma leitura de uso por organização (`Uso/UsoDaOrg`); não confirmei se ela conta a “pergunta respondida” como definimos. O “sem chamado” depende do ponto de partida, que é pendência | ❓ |

## Pressupostos transversais

| # | O que o norte pede | O que o produto faz hoje | Situação |
| --- | --- | --- | --- |
| 10 | **Qualquer dispositivo**: computador, celular e tablet (`D-002`) | Há regras de adaptação de tela espalhadas pelo front (66 ocorrências em 43 arquivos), inclusive no compositor e no cabeçalho da conversa; não testei em tela de celular ou tablet | 🟡 |
| 11 | **Dois owners**: da instância e da organização (`D-013`) | A área Administração (identidade, desempenho, segurança, homologações, administradores) e a área Organização (informações, bases, modelos, IA, gráficos, membros, segurança de acesso) já existem separadas | ✅ |
| 12 | **Várias organizações** por instalação (`D-008`) | A lista de organizações (`/orgs`) e o layout próprio de cada organização existem | ✅ |
| 13 | **Marca branca**: logo, nome e e-mail (`D-011`) | A tela Identidade configura nome, logos (claro e escuro) e rodapé, e vale para todas as organizações. O envio de e-mail existe e usa remetente de opções do servidor, mas não encontrei tela do owner da instância para o remetente | 🟡 |
| 14 | **Entrega on-premises e SaaS** (`D-007`) | Existe roteiro de publicação em servidor da Maind; não avaliei a instalação na infraestrutura do contratante | ❓ |
| 15 | **A fonte da organização alcança a infraestrutura do contratante** (consequência do on-premises) | Por regra de segurança, a fonte cadastrada pela organização **não alcança a rede interna**; a saída existe só por configuração do servidor, que nunca vai aos ambientes publicados (`CLAUDE.md`) | ❌ |
| 16 | Modo **“tudo dentro”** para IA e web (`D-010`) | As conexões de IA aceitam só dois provedores externos (OpenRouter e Bedrock); não há provedor que rode dentro da infraestrutura do contratante | ❌ |

## O que salta aos olhos

- ✅ **A base está de pé.** A conversa de análise, os blocos visuais, os níveis de inferência, os dois níveis de owner e as várias organizações já existem.
- ❌ **O retorno do usuário não existe.** É a lacuna mais clara do problema nº 1, e sem ele não há como medir a qualidade da resposta (`D-004`, `D-005`).
- ⚠️ **Para a mesma versão rodar em qualquer instância (`D-017`)**, faltam duas capacidades: a fonte alcançar a rede interna do contratante (linha 15) e a IA dentro da infraestrutura (linha 16). Não são uma escolha entre SaaS e on-premises; são requisitos do produto.
- ❓ **O tempo de resposta não está medido.** Sem ele, a promessa da cena da reunião não tem número.

## Candidatas à v2.0 (lista fechada pelo dono em 01/11/2026)

Macro funcionalidades (mf) que saíram das lacunas, em linguagem de cliente. As candidatas 1 a 6 vieram do inventário; as **7 a 9 o dono acrescentou em 31/10/2026**, ao ler o [mapa das mfs de hoje](04-macro-funcionalidades-de-hoje.md) (`D-018` a `D-020`); a **10 e a 11** vieram do redesenho da MF-106:Segurança dos dados por pessoa (`D-025`); a **12 e a 13** o dono acrescentou em 31/10/2026 (`D-033`, `D-036`); a **14 e a 15** o dono acrescentou em 31/10/2026, ao responder se faltava alguma (`D-065`, `D-066`, refinada pelas `D-067` a `D-069`); a **16 e a 17** o PO apontou como lacunas do norte e o dono incluiu em 01/11/2026 (`D-081`, `D-082`); a **18** o dono acrescentou em 01/11/2026 (`D-084`). O dono fechou a lista com as 18 em 01/11/2026 (`D-103`); ela foi pontuada com os pesos da `D-015`, e a composição da v2.0 está decidida na `D-105`.

1. ⚡ **Resposta em segundos na reunião:** a velocidade medida e garantida. *(Corrigido pela `D-125`, de 02/11/2026: “em segundos” é uma comparação com o pedido ao time de dados, que às vezes leva dias, e não um tempo garantido.)*
2. 👍🏻 **Retorno do usuário sobre a resposta:** Gostei, Não gostei e Reportar, com o reporte indo ao owner da organização.
3. 🌐 **A web como fonte viva completa:** em todos os usos, com fonte e data.
4. 📈 **Medida de autonomia:** perguntas de análise respondidas e o saving da área de dados.
5. 🏢 **Horus rodando dentro da infraestrutura do contratante:** a fonte alcança a rede interna e a IA fica dentro de casa.
6. 🎨 **Marca completa do contratante:** logo, nome e e-mail.
7. 🤖 **Agentes ativos que extraem, analisam e avisam** (MF-115:Agentes ativos): agentes criados com instruções em texto, que extraem e analisam dados e entregam artefatos e alertas pelos conectores de saída, no horário do agendamento (`D-020`, `D-022`, `D-037`, `D-061`), com a interpretação configurada pelo usuário, inclusive o nível de inferência (`D-023`, `D-024`). Atende ao problema nº 3 do norte, o aviso. O dono a incluiu na v2.0, acima do corte da pontuação (`D-122`).
8. 🧩 **Boards e relatórios como uma coisa só** (MF-112:Boards e Relatórios, que substitui a MF-006:Acompanhar em boards e a MF-008:Relatórios em PDF agendados): um editor único; todo board é vivo e pode ser impresso em PDF, de qualquer tamanho (`D-018`, `D-057`, `D-058`). O dono a incluiu na v2.0, acima do corte da pontuação (`D-119`).
9. 👥 **Grupos de pessoas, estáticos e dinâmicos** (melhora a MF-102:Organizações, pessoas e papéis): montados à mão ou por claims e papéis (`D-019`; na v2.0, os dinâmicos só por papel, e por claims na v2.1, `D-145`), criados pelos gestores, só com as pessoas que eles gerem (`D-049`), ou pelo owner, para a organização inteira (`D-055`), usados para permissão de acesso a boards, receber relatórios, destino de alertas e outros usos (`D-029`). As funcionalidades do Horus, como o acesso à web, a Análise avançada e a escolha do modelo de IA no chat, são liberadas ou limitadas pelo owner por meio de roles (`D-050`). O dono a incluiu na v2.0, com a gestão de pessoas inteira da `MF-102` (`D-108`). O owner liga e desliga por role tudo o que a conversa oferece, botão a botão (`D-110`). Quando a pessoa tem mais de uma role, vale a soma (`D-111`). Quem não tem nenhuma role usa a role padrão da organização (`D-112`). Uma role nova começa do zero ou como cópia de outra, à escolha do owner (`D-113`). A definição completa está decidida na `D-114`, e a `P-009` está fechada.
10. 🛡️ **Acesso configurado dentro do Horus** (etapa 1 da MF-106:Segurança dos dados por pessoa): o usuário define quem vê quais dados pelo documento semântico de segurança, para empresas sem controle próprio (`D-025`). Vai para a v2.1, com a etapa 2 (`D-145`).
11. 🔐 **Segurança corporativa integrada** (etapa 2 da MF-106:Segurança dos dados por pessoa): o Horus usa os controles de acesso das tecnologias de dados da empresa e reaproveita as claims e os papéis do token do IDP (`D-025`). Quando também houver regra do Horus, as duas valem e vale a mais restritiva (`D-026`). O IDP é ligado em cada organização, pelo owner da organização (`D-027`).
12. 📤 **Conectores de saída** (MF-113:Conectores de Saída): os canais que só transportam o que o Horus produz (alertas, relatórios exportados…) e só a usuários do Horus, ligados pelo owner da organização (`D-033`, `D-034`, `D-035`). O formato do que sai é outro assunto. Hoje a única saída é o e-mail. Atende ao problema nº 3 do norte, o aviso, e serve também à mf única de boards e relatórios. O dono a incluiu na v2.0, acima do corte da pontuação (`D-122`).
13. ⏰ **Módulo de agendamentos de agentes** (MF-114:Módulo de Agendamentos de Agentes): um agendador único que decide quando gerar o PDF de um board ou executar um agente, no mesmo nível, e entrega o artefato (PDF, JSON…) por conectores aos destinos (`D-035`, `D-036`, `D-064`). Todo agente usa IA (`D-063`). Hoje só existe a agenda dos relatórios em PDF. O dono a incluiu na v2.0, acima do corte da pontuação (`D-122`).
14. 💬 **Pergunta rápida** (MF-110:Pergunta rápida): um botão flutuante de chat que abre um popup para a pessoa fazer a pergunta sem sair da tela em que está, para um uso mais dinâmico das perguntas (`D-065`). Atende ao problema nº 1 do norte. Pelo que a busca encontrou, hoje a pergunta só se faz na tela da conversa de análise (🔎 a confirmar com o arquiteto). O popup é um atalho para a conversa de análise e não sabe em que tela a pessoa está (`D-085`). A conversa fica no popup, e a pessoa pode limpá-la e escolher salvar (`D-086`). A pergunta limpa sem salvar conta na medida de autonomia e recebe retorno como as outras (`D-087`). O popup traz tudo o que a conversa oferece (`D-088`). A definição macro está decidida na `D-089`.
15. 🎫 **Licenças e planos** (MF-103:Licenças e planos): a cobrança por quantidade de usuários e por plano (por exemplo, Básico, Gold e Diamond). Os assentos são liberados e desativados pelo administrador do SaaS num painel de controle, só no modo SaaS (o on-premises fica para depois); não há data de expiração no produto, porque a validade é assunto comercial; e a permissão dos usuários é desabilitada quando os assentos são desativados (`D-066` a `D-068`). Os assentos têm quatro tipos: owner, gestor, membro full (pergunta, cria boards e alertas) e membro leitor (só vê boards de outras pessoas); cada organização traz um assento de owner grátis (`D-123`) (`D-069`). Sem assento livre do tipo, a pessoa não entra até o administrador liberar mais (`D-070`). O gestor cria o convite e escolhe o tipo de assento; o owner aprova; a aprovação envia o e-mail e reserva o assento por N dias, e depois o convite expira e o assento volta a ficar livre (`D-071`). A troca do tipo de assento de quem já entrou segue o mesmo caminho: o gestor pede, o owner aprova, e precisa haver assento livre do tipo novo (`D-072`). Quando alguém passa de full a leitor, o que ela criou (boards, alertas e agendamentos) vai para a área da organização, como quando o autor sai (`D-073`). Quem acumula owner e gestor ocupa um assento só, o de owner (`D-074`). Quando o administrador desativa os assentos, os agendamentos, alertas e agentes da organização também param, e as configurações ficam guardadas (`D-075`). O painel não deixa reduzir os assentos de um tipo abaixo do que está ocupado; o owner libera antes (`D-076`). O owner pede mais assentos fora do produto, por contato comercial com a Maind (`D-077`). O owner define, nas preferências da organização, por quantos dias o assento fica reservado para um convite (`D-078`). O membro leitor também recebe alertas e PDFs pelos conectores (`D-079`). A definição macro está decidida na `D-080`. Não atende a um dos três problemas do norte: sustenta o negócio da Maind. Não encontrei nada disso no produto de hoje (🔎 a confirmar com o arquiteto). O dono a incluiu na v2.0 inteira (`D-107`). A v2.0 abre com um plano só, com todas as funcionalidades (`D-115`); o preço em reais fica fora dos documentos de produto (`D-116`); a definição dos planos está decidida na `D-117`, e a `P-015` está fechada.

16. 🔍 **Investigação guiada** (MF-119:Investigação guiada): a pessoa vê que algo mudou e o Horus a leva, passo a passo, até o porquê (`D-081`). Atende ao problema nº 2 do norte. Hoje a investigação só existe pela conversa, sem um caminho guiado (🔎 a confirmar com o arquiteto). A definição macro está na `P-018`.
17. 🧾 **Auditoria** (MF-116:Auditoria): o rastro de quem viu e de quem entregou o quê a quem (`D-082`). Não atende a um dos três problemas do norte: sustenta a prova da confiança e a responsabilidade do gestor (`D-054`). Não encontrei nada disso no produto de hoje (🔎 a confirmar com o arquiteto). O rastro registra as entregas e quem as abriu, e não o conteúdo (`D-090`), e só o owner da organização o consulta (`D-091`) e define por quantos dias ele fica guardado (`D-092`). A definição macro está decidida na `D-093`. O dono a incluiu na v2.0, acima do corte da pontuação (`D-119`).

18. 📲 **Chat pelo WhatsApp** (MF-111:Chat pelo WhatsApp): a pessoa conversa com o Horus pelo WhatsApp e vê o conteúdo da resposta como no chat (`D-084`). Atende ao problema nº 1 do norte e à promessa “informação na palma da mão”. Não encontrei nada de WhatsApp no produto de hoje, nem como entrada (🔎 a confirmar com o arquiteto). A própria pessoa liga o seu número ao perfil e o confirma com um código recebido no WhatsApp (`D-094`). Tudo o que ela pergunta entra no histórico do app (`D-095`). A resposta chega com texto, imagens e um link para abrir a resposta no app (`D-096`). Cada organização usa o seu próprio número de WhatsApp, e pode autorizar o uso do número da Maind (`D-097`). A pessoa tem tudo o que a conversa de análise oferece (`D-098`). A definição macro está decidida na `D-099`. O dono a incluiu na v2.0, acima do corte da pontuação (`D-119`).

O PO apontou ainda uma terceira lacuna, a melhoria do modelo semântico (o assistente de modelagem e a lista de perguntas sem resposta), e o dono a deixou com o time de dados por enquanto (`D-083`).

## Próximo passo

Este inventário cobre o problema nº 1 e os pressupostos. Ainda faltam os problemas nº 2 (a investigação) e nº 3 (o aviso). A ordem de fechamento das lacunas sai da composição das versões, pontuada contra o norte.
