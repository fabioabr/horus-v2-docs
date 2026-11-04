# Norte do produto Horus

Situação: 🟢 decidido pelo dono em entrevista (decisão `D-001` do [backlog estratégico](backlog-estrategico.md)).

Última atualização: 31/10/2026.

Este documento diz **para onde o Horus vai**: por que existe, para quem, que problema resolve primeiro, o que promete e como saberemos que deu certo. Toda priorização e toda escolha entre caminhos é pontuada contra ele.

> 🧭 **O norte guia o produto, e não o contrário.** Estamos dando um passo atrás para estruturar o crescimento do Horus. O produto de hoje é o ponto de partida: mostra o que já existe e quais são as lacunas até o norte, mas não limita o que o norte afirma (`D-003`).

## 🎯 Propósito

Dar **autonomia** a quem decide. A pessoa pergunta às **fontes vivas** — os dados da empresa e a web — e entende a resposta na hora, sem depender de ninguém.

A autonomia traz dois ganhos, um para cada lado:

- 🙋 **Para quem usa:** a sensação de poder sobre os dados da própria área.
- 💰 **Para quem paga:** economia com o time que hoje monta dashboards sob encomenda.

Também importam, mas em segundo plano: a **confiança** nos números, a **produtividade** da área de dados e a **antecipação** de problemas. Se fosse preciso escolher um só propósito, é a autonomia.

## 👥 Quem atendemos primeiro

| Papel | Quem é | O que ganha |
| --- | --- | --- |
| 👔 **Gestor de área** | Gerente ou coordenador (vendas, financeiro, operações…) que hoje espera a área de dados montar o relatório. | Responde sozinho, sem abrir chamado. |
| 🏢 **Executivo** | Diretor, CEO ou dono. | Tem o número certo na hora, sem aprender ferramenta. |
| 💰 **Comprador** | Quem aprova e paga a contratação. | Vê o saving com o time de montagem de dashboards. |

**Quem contrata primeiro:** a empresa que usa o Horus por dentro, para os próprios setores (cada setor, uma organização). A revenda a clientes vem depois (`D-009`).

### 📌 Momento-âncora

Reunião de resultado. O CEO pergunta: “e se tirarmos as lojas do Sul, como fica a margem?”. Hoje a resposta é “abro um chamado e te retorno amanhã”. Com o Horus, o gestor responde ali mesmo, na frente de todos.

Consequências dessa cena:

- ⏱️ A velocidade se mede em segundos, porque a pessoa está diante de todos.
- 🛡️ Um número errado diante do CEO é pior que nenhum número; a confiança é condição da cena, não detalhe.

## 🥇 Problemas a resolver, em ordem

1. ⚡ **A pergunta de análise na hora:** surge uma dúvida de negócio e a resposta sai ali, em segundos.
2. 🔍 **A investigação:** a pessoa vê que algo mudou e descobre o porquê, aprofundando passo a passo.
3. 🔔 **O aviso:** o Horus avisa quando algo muda, sem ninguém perguntar.

O **acompanhamento recorrente** (o mesmo relatório toda semana ou todo mês) não entra nesta ordem: será tratado quando decidirmos a funcionalidade de **Board**.

## 💬 Promessa

**“Informação na palma da mão”** (nome de trabalho; a redação final fica para o documento de posicionamento). Esta frase vive na **comunicação comercial da Maind**, voltada a quem contrata; dentro do produto, cada contratante usa a sua marca (`D-012`).

- 🎨 **O visual faz parte da promessa.** A forma como a resposta é construída, em texto ou gráfico, é o que dá conforto para entender o resultado. Visual não é enfeite nem limite: é valor central.
- 🛡️ **A prova é a confiança.** Toda resposta identifica a fonte de cada informação, para a pessoa saber o que pode mostrar como fato da empresa e o que veio de fora.
- 📱 **Pressuposto: em qualquer dispositivo.** A pessoa acessa o dado no computador, no celular ou no tablet, e a experiência se adapta a cada um (responsividade). Isso vale para todas as versões e não é uma funcionalidade a priorizar; como cada tela se comporta é assunto do arquiteto de soluções (`D-002`).

## 🌐 Fontes

O Horus é o chat de todas as **fontes vivas** que ajudam a decidir:

- 🏦 **Interna:** os bancos de dados da organização.
- 🌐 **Externa:** a pesquisa na web.

A web serve a todos os usos: **complementa** os números da empresa (contexto de mercado), responde **sozinha** quando a pergunta é externa, serve de **régua** (benchmark) e **ajuda a investigar** o porquê de uma variação. O que é dado interno e o que é dado de fora nunca se confunde. Toda informação da web aparece com o **link da fonte** e a **data de publicação**; quando a data não puder ser identificada, o Horus avisa que não foi possível identificá-la (`D-006`).

## 📦 Como o Horus é entregue

- 🏷️ **Plataforma white label:** pode levar a marca de quem a contrata (`D-007`).
- 🎨 **A marca do contratante, no começo, é só logo, e-mail e nome;** o tema fica para uma versão futura. As páginas institucional e de propaganda ficam apartadas do produto (`D-011`).
- 🧩 **Uma versão só:** a versão do produto é a mesma em SaaS e on-premises; a diferença está na instância (`D-017`).
- 🏢 **Duas formas de entrega:** **on-premises**, na infraestrutura do contratante, ou **SaaS**, na infraestrutura da Maind (`D-007`).
- 🎚️ **O contratante escolhe o que sai da infraestrutura dele:** a IA e a pesquisa web funcionam no modo **“com serviços externos autorizados”** (padrão) ou no modo **“tudo dentro”** (`D-010`).
- 🔑 **Dois níveis de owner:** o **owner da instância** configura a marca e o que vale para todas as organizações; o **owner da organização (ou área)** convida pessoas, configura preferências e cuida do que é da organização (`D-013`).
- 🗂️ **Várias organizações por instalação:** uma organização pode ser um cliente (B2B) ou um setor dentro de uma empresa (`D-008`).

## 📈 Como saberemos que deu certo

| Medida | Para quem | O que mede |
| --- | --- | --- |
| 🙋 **Perguntas de análise respondidas sem chamado** (norte) | Usuário | A porcentagem das perguntas de análise que o gestor resolve sozinho, sem acionar a área de dados. |
| 💰 **Saving da área de dados** | Comprador | Horas ou chamados que a área de dados deixou de atender. |

**Pergunta de análise respondida** é aquela em que o Horus consegue responder, com gráfico, texto ou os dois, independentemente da satisfação do usuário (`D-004`). Se o Horus diz que não consegue, não conta. A qualidade da resposta é medida à parte, pelo retorno do usuário e pelos chamados que ainda chegam à área de dados.

**Retorno do usuário (`D-005`):** cada resposta pode receber 👍🏻 Gostei, 👎🏻 Não gostei ou 🚫 Reportar. Ao reportar, a pessoa escolhe o que está reportando, e o **owner da organização** analisa uma possível falha no modelo semântico ou nos dados (`D-014`).

> Exemplo: numa semana, os gestores fizeram 100 perguntas; 80 foram respondidas sem chamado. A autonomia é de 80%.

## 🚫 O que o Horus não é

- 👀 **Só lê as fontes.** Nunca altera dados nem executa ações nos sistemas da empresa (pesquisar na web também é ler). Pode enviar alertas por canais de saída, como e-mail, WhatsApp ou Teams (`D-022`); como isso funciona está em desenho (`P-007`).
- 🧹 **Não arruma os dados.** Usa os dados como estão nos bancos conectados, sem limpar nem reconciliar.

A decisão continua humana. O Horus trabalha com **níveis de inferência autorizados pela organização**: hoje são cinco — descritivo, explicativo, comparativo, hipótese e especulativo —, e quanto mais alto o nível, mais a resposta pode afirmar além do que está nos dados, sempre dizendo que é hipótese ou especulação. **O agente ativo é a exceção:** o usuário que o cria define o nível dele, sem o teto da organização (`D-024`).

## 🧱 Lacunas entre o norte e o produto de hoje

O levantamento completo está no [inventário de lacunas](03-inventario-de-lacunas.md). O exemplo abaixo é a primeira lacuna identificada.

O que o norte afirma e o produto atual ainda não faz. São entradas para o inventário e para o arquiteto de soluções, não motivo para encolher o norte.

| Lacuna | Hoje | O norte pede |
| --- | --- | --- |
| **A web como fonte viva em todos os usos** | Abaixo do nível 4 de inferência, a pesquisa web só ajuda no vocabulário; os fatos buscados entram com fonte citada a partir do nível 4 (`composerLogica.ts`). | A web complementa, responde, serve de régua e ajuda a investigar, com a fonte sempre à vista. |

## 🔎 Pendências e impasses

Ficam num lugar só, para não divergirem: a seção “Pendências e impasses” do [backlog estratégico](backlog-estrategico.md). Impasse em definição estratégica não é deixado para depois.
