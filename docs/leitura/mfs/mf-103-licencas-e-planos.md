---
codigo: MF-103
nome: Licenças e planos
entrega: v2.0
situacao: definida
camada: 🧱 Plataforma
objetivos: [O7]
quem_usa: [owner da instância, owner da organização, gestor]
complexidade: alta
relacionadas: [MF-101, MF-102, MF-105, MF-112, MF-114, MF-115, MF-113, MF-110, MF-111, MF-117]
atualizado: 2026-11-05
fontes:
  - docs/raw/produto/04-macro-funcionalidades-de-hoje.md
  - docs/raw/produto/05-v2.0-consolidada.md
  - docs/raw/produto/06-versoes.md
  - docs/raw/produto/07-mapa-de-objetivos-e-funcionalidades.md
  - docs/raw/produto/03-inventario-de-lacunas.md
  - docs/raw/produto/backlog-estrategico.md
  - docs/raw/arquitetura/01-estrategia-da-solucao.md
  - docs/raw/arquitetura/02-registro-de-decisoes.md
  - docs/raw/arquitetura/04-software.md
  - docs/raw/arquitetura/07-seguranca.md
  - docs/raw/arquitetura/14-conferencia-do-produto.md
---

# Licenças e planos

> **Em uma frase:** a empresa paga pelas pessoas que usam o Horus, por tipo de pessoa, e quem usa nunca passa do
> que foi contratado.

## 🧭 O que é

Hoje o Horus não controla licenças: qualquer número de pessoas entra numa organização. Na v2.0, cada organização
passa a ter **assentos**: as vagas de uso que a empresa contratou, de cinco tipos, cada pessoa ocupando uma.

O Horus contratado como serviço (SaaS) é uma instância só, da Maind. Quem cria as organizações e libera e corta os
assentos é o **owner da instância**, a Maind, no painel da Administração da instância (MF-101). O **owner da
organização**, um funcionário do cliente, decide quem ocupa cada um e acompanha a cobrança. A v2.0 tem um plano só,
com tudo o que ela oferece, e o preço é combinado em contrato, fora do produto. A IA entra no preço quando a
organização usa a conexão de IA da instância, que a Maind paga; a organização que traz a própria IA paga o consumo
dela.

> 📌 **Exemplo:** a Maind cria a organização do Marcos e libera o assento de owner grátis, 10 de membro ouro, 30 de
> prata e 100 de bronze. A gestora Carla convida um analista como membro ouro; o Marcos aprova, o e-mail sai e o
> assento fica guardado. Quando os 10 acabam, o Marcos pede mais à Maind. Se a empresa deixa de pagar, a Maind
> corta a organização, e nada mais roda.

## ✨ Características

- **Os cinco tipos:** owner da organização; gestor (quem gere uma equipe); membro ouro (pergunta e cria boards, os
  painéis de acompanhamento, e relatórios para si, sem compartilhar); membro prata (pergunta e recebe alertas e
  PDFs, sem criar nada); e membro bronze (só vê os boards já criados e compartilhados e recebe alertas e PDFs por
  e-mail e WhatsApp; não pergunta em canal nenhum). A prata pergunta no app, na Pergunta rápida (MF-110) e no
  WhatsApp e, quando chegar, usa a Investigação guiada (MF-119), da v2.1, mas não cria boards, relatórios,
  agendamentos nem agentes, os trabalhos automáticos de IA. Cada faixa soma uma coisa: o bronze vê, a prata
  pergunta, o ouro cria. O ouro e o bronze seguem as regras do antigo membro full e do antigo leitor.
- **O owner grátis:** só o primeiro owner de cada organização não paga. Quem é owner e gestor ao mesmo tempo ocupa
  um assento só, o de owner.
- **Sem vaga, não entra:** sem assento livre do tipo, ninguém entra nele. O owner da organização pede mais à Maind,
  fora do produto, e o convite pendente mostra que falta vaga.
- **A reserva:** aprovado o convite, o assento fica guardado pelo prazo que o owner da organização define; depois,
  o convite expira e a vaga volta. Quem espera na quarentena, por ter entrado sem gestor, já ocupa o assento.
- **A troca de tipo:** o gestor pede, o owner da organização aprova, e precisa haver vaga do tipo novo; a antiga se
  libera na hora. Quem é **rebaixado**, de ouro a prata ou a bronze, continua na organização e mantém o que criou
  (boards, relatórios, agendamentos e agentes) vinculado a si, mas **desabilitado**: nada se abre nem roda, e a
  única ação é excluir. Se voltar a ser ouro, reativa cada item, um a um; nada volta sozinho. Já quem é
  **excluído**, porque sai ou é retirado da organização, perde em definitivo o que criou: nada passa a outra pessoa.
- **A visão de cobrança:** o owner da organização vê só a contagem dos assentos: de cada tipo, quantos tem, quantos
  usa e quantos estão livres. O custo, o relatório e a história dos assentos ficam com a Maind, e o uso do Horus
  aparece na Home da organização (MF-117).
- **Reduzir:** não dá para reduzir abaixo do ocupado, e os reservados contam como ocupados; o owner da organização
  desocupa antes.
- **O corte:** cortar é inativar a organização inteira: as pessoas perdem o acesso, e os agendamentos, os alertas e
  os agentes (os trabalhos automáticos de IA) param. Os dados, os boards e as conversas ficam guardados; ao
  reativar, os agendamentos seguem do próximo horário. Não há data de validade: renovação, carência e corte são
  decisão comercial da Maind.
- **O que o assento inclui:** na organização que usa a conexão de IA da instância, cadastrada e paga pela Maind, a
  IA vai embutida no preço, e a organização não abre conta em provedor de IA. A que cadastra a própria conexão, com
  o provedor que quiser, paga o consumo. À parte, fora do produto, só as mensagens de quem usa o número de WhatsApp
  da Maind.
- **Um plano só:** controla só os assentos. O que cada pessoa usa fica com as roles, os pacotes de botões das
  Organizações, pessoas e papéis (MF-102).

## 📈 O valor que gera

- **Para quem usa:** o owner da organização sabe quanto tem e quanto sobra, e ninguém perde o acesso de surpresa
  numa redução.
- **Para a empresa que contrata o Horus:** paga por quem usa, por tipo, sem escolher entre planos; com a IA da
  instância, começa sem abrir conta de IA, e quem já tem contrato com um provedor de IA pode usá-lo.
- **Para o Horus como produto:** receita por assento desde o primeiro cliente, e o corte de quem não paga.
- ⚠️ **O cuidado:** a Maind carrega o risco do consumo de IA das organizações que usam a conexão da instância; o
  preço do assento delas precisa cobrir a média.

**Como vamos saber que funcionou:** o primeiro cliente fecha contrato só com a conta de assentos, e o que ele pedir
a mais mostra onde caberia um segundo plano.

## 🚶 Como se usa no Horus

**A Maind, owner da instância:**

1. Combina os assentos com o cliente, fora do produto.
2. Cria a organização e libera no painel a quantidade de cada tipo.
3. Libera mais quando o owner da organização pede, ou reduz depois que ele desocupa os assentos.
4. Corta a organização se o cliente deixa de pagar, e a reativa depois.

**O owner da organização:**

1. Acompanha, na visão de cobrança, quantos assentos tem, usa e tem livres.
2. Aprova os convites e as trocas de tipo que os gestores pedem, quando há vaga.
3. Ajusta o prazo da reserva nas preferências da organização.

```mermaid
flowchart LR
  a[Maind cria a organização e libera os assentos] --> b[Gestor cria o convite]
  b --> c{Há vaga do tipo?}
  c -->|sim| d[Owner aprova e o assento fica guardado]
  c -->|não| e[Owner pede mais à Maind]
  e --> a
  d --> f[A pessoa aceita e ocupa o assento]
```

## 🧩 Grau de complexidade: alta

Nada disso existe na v1: os cinco tipos de assento, a reserva, a troca, a contagem, o corte e o estado desabilitado
do que o rebaixado criou são novos. O tipo de assento passa a ser a primeira coisa que o porteiro único das
permissões confere, e o corte atravessa o produto, parando agendamentos, agentes e envios. Não depende de ninguém
de fora: vale só no SaaS da Maind.

> ⚠️ É a leitura do PO a partir dos documentos de arquitetura. A estimativa de esforço é do arquiteto.

## 🔗 Macro funcionalidades relacionadas

| mf | Como se relaciona |
| --- | --- |
| Administração da instância (MF-101) | **depende de**: o painel onde a Maind cria as organizações e libera e corta os assentos fica lá. |
| Organizações, pessoas e papéis (MF-102) | **depende de**: o convite, a aprovação, a quarentena e os papéis vêm de lá; em troca, o tipo de assento é o teto do que as roles liberam. |
| IA sob controle da organização (MF-105) | **complementa**: a IA da conexão da instância, que a Maind cadastra e disponibiliza à organização, é paga pela Maind e vai embutida no preço do assento; a conexão que a própria organização cadastra é paga por ela. |
| Boards e Relatórios (MF-112) | **depende de**: o que a pessoa criou fica com ela, desabilitado e só para excluir, quando ela é rebaixada a prata ou a bronze, e só volta a funcionar quando ela, de novo ouro, reativa cada item. |
| Módulo de Agendamentos de Agentes (MF-114) e Agentes ativos (MF-115) | **depende de**: param no corte e voltam do próximo horário quando a organização volta; os de quem é rebaixado deixam de rodar até ele, de novo ouro, reativá-los. |
| Conectores de Saída (MF-113) | **depende de**: é por eles que o membro bronze recebe alertas e PDFs; as mensagens pelo número de WhatsApp da Maind se pagam à parte. |
| Pergunta rápida (MF-110) | **é a base de**: o tipo de assento vem antes da role, e o membro bronze não ganha o botão. |
| Chat pelo WhatsApp (MF-111) | **é a base de**: o tipo de assento decide quem pode perguntar, e o membro bronze não conversa. |
| Home da organização (MF-117) | **depende de**: a adoção medida lá sustenta a renovação e a compra de mais assentos. |

## 🚧 O que ela não faz

- **Cobrar e receber:** o preço em reais, a fatura, o pagamento e o repasse do WhatsApp ficam com o comercial da
  Maind.
- **Vários planos:** nomes, seletor e limite de funcionalidades por plano ficam para quando houver mais de um.
- **Cobrar pelo uso do mês:** a conta da Maind é por assento, e não por perguntas ou consumo; a IA vai embutida
  quando a organização usa a conexão da instância, e a que traz a própria paga o consumo dela.
- **A instalação completa do Horus na casa do cliente (on-premises)**, com os assentos ativados por um arquivo de
  licença: fica sem versão, e só volta se um cliente exigir que nada saia de casa, nem a pergunta. Quem precisa dos
  dados em casa usa o Middleware na casa do contratante (MF-121).

## ⏳ Ainda a decidir

- O preço do membro prata, que é novo: se a Maind o cobra diferente do ouro e do bronze.
- Se o preço do assento muda para a organização que traz a própria IA e paga o consumo dela.

## 📚 Para saber mais

- `docs/raw/produto/backlog-estrategico.md`
  - **D-080**: a definição macro da MF-103 (reúne D-066 a D-079).
  - **D-117**: a definição macro dos planos da v2.0 (reúne D-115 e D-116).
  - **D-194** (os cinco tipos de assento: owner, gestor e os membros ouro, prata e bronze; a prata precisa de um
    preço), que substitui em parte a **D-069**, com a leitura **D-194.1** do documento da v2.0 (o ouro é o antigo
    membro full, e o bronze, o antigo membro leitor), confirmada pelo dono em 05/11/2026.
  - **D-203** (o que a prata faz: pergunta, investiga e recebe alertas e PDFs, sem criar board, relatório,
    agendamento nem agente), que estende a **D-073**; a segunda parte dela, que mandava o que o rebaixado criou para
    a área da organização, foi substituída pela **D-207**.
  - **D-206** a **D-209** (não há transferência: quem é excluído perde em definitivo o que criou; quem é rebaixado
    o mantém vinculado e desabilitado, só para excluir, e o reativa um a um se voltar a ser ouro).
  - **D-214** (a visão de cobrança do owner da organização mostra só a contagem de assentos por tipo: quantos tem,
    usa e estão livres).
  - **D-123** (o owner grátis por organização), **D-070** e **D-077** (sem vaga, não entra; o pedido fora do
    produto), **D-071**, **D-072** e **D-078** (o convite, a troca e a reserva), **D-073** (de full, hoje ouro, a
    leitor, hoje bronze), **D-074** (owner e gestor num assento só), **D-075** e **D-076** (o corte e a redução),
    **D-079** (o leitor, hoje bronze, recebe), **D-067** e **D-068** (o painel, só no SaaS, sem data de validade).
  - **D-146** (só o administrador da instância cria organizações), **D-148** (cortar é inativar a organização
    inteira) e **D-193** (o SaaS é uma instância só, da Maind; o owner da organização, funcionário do cliente, tem a
    visão da cobrança).
  - **D-159** (a Maind paga a IA e a embute no assento) e **D-160** (quem usa o número de WhatsApp da Maind paga
    as mensagens que gerar). A **D-159** foi substituída em parte pela **D-216**: a Maind paga só a conexão de IA
    da instância, e a organização que cadastra a própria paga o consumo.
  - **D-107** (a MF-103 inteira na v2.0) e **D-197** (uma mf numa versão só).
  - **D-175** e **D-176** (o arquivo de licença com chave e o teto por tipo para a instância inteira, que fecharam a
    **P-016**), sem versão desde a **D-188** (a instalação completa é a porta de volta); a **D-121** (o on-premises
    na v2.1) fica substituída nesse ponto.
  - **P-022** (o preço em reais, inclusive o da prata, e se ele muda para quem traz a própria IA) e **P-008**,
    letras s, t e u.
- `docs/raw/produto/04-macro-funcionalidades-de-hoje.md`: a direção do dono e a tabela de conversão.
- `docs/raw/produto/05-v2.0-consolidada.md`: §1, §4 (os passos 1 e 12), §5.3 (as regras), §8 (os riscos) e as leituras
  **D-069.1**, **D-070.2**, **D-071.3** a **D-071.5**, **D-072.1**, **D-073.1**, **D-075.2**, **D-075.3**,
  **D-076.1**, **D-077.1**, **D-078.1**, **D-194.1** e **D-198.1**.
- `docs/raw/produto/06-versoes.md`: a candidata nº 15 na v2.0 e a instalação completa, sem versão.
- `docs/raw/produto/07-mapa-de-objetivos-e-funcionalidades.md`: a candidata nº 15 (O7). A ativação dos assentos por
  arquivo de licença no on-premises (parte da nº 5, O8) está sem versão: é a porta de volta da instalação completa
  e, se voltar, volta como mf própria (**D-188** e **D-198**, com a leitura **D-198.1**; ver também o `05` e o
  `06`).
- `docs/raw/produto/03-inventario-de-lacunas.md`: a candidata 15.
- `docs/raw/arquitetura/01-estrategia-da-solucao.md`: §4 (a linha da MF-103) e §6 (os marcos M1 e M10).
- `docs/raw/arquitetura/04-software.md`: §3.2, os componentes Assentos, Painel dos assentos e Avaliador de permissões.
- `docs/raw/arquitetura/02-registro-de-decisoes.md`: **ARQ-008** e **ARQ-039** (o tipo de assento como primeira leitura
  do avaliador; o corte como estado da organização), **ARQ-005** (o corte pausa o que roda sozinho), **ARQ-060**
  (o on-premises, hoje sem versão).
- `docs/raw/arquitetura/07-seguranca.md`: §3.2 (a ordem do avaliador).
- `docs/raw/arquitetura/14-conferencia-do-produto.md`: §1 (as letras s, t e u), §3 (tudo é novo) e §4 (**A-02**).
