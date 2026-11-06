---
codigo: MF-101
nome: Administração da instância
entrega: v2.0
situacao: definida
camada: 🧱 Plataforma
objetivos: [O7]
quem_usa: [administradores da instância (o owner da instância)]
complexidade: alta
relacionadas: [MF-102, MF-103, MF-105, MF-106, MF-113, MF-116, MF-120]
atualizado: 2026-11-05
fontes:
  - docs/raw/produto/04-macro-funcionalidades-de-hoje.md
  - docs/raw/produto/05-v2.0-consolidada.md
  - docs/raw/produto/06-versoes.md
  - docs/raw/produto/07-mapa-de-objetivos-e-funcionalidades.md
  - docs/raw/produto/03-inventario-de-lacunas.md
  - docs/raw/produto/backlog-estrategico.md
  - docs/raw/arquitetura/README.md
  - docs/raw/arquitetura/01-estrategia-da-solucao.md
  - docs/raw/arquitetura/02-registro-de-decisoes.md
  - docs/raw/arquitetura/04-software.md
  - docs/raw/arquitetura/06-dados.md
  - docs/raw/arquitetura/07-seguranca.md
  - docs/raw/arquitetura/14-conferencia-do-produto.md
---

# Administração da instância

> **Em uma frase:** o painel de quem opera o Horus: criar as organizações, liberar os assentos, acompanhar o uso
> e o custo de cada uma e avisar todas as pessoas antes de uma parada.

## 🧭 O que é

Uma instalação do Horus, a **instância**, serve várias **organizações**: cada setor de uma empresa, ou cada
cliente, é uma. Na v2.0, o Horus é um serviço (SaaS) com uma instância só, a da Maind. Quem a opera é o
**administrador da instância**, um funcionário da Maind ("owner da instância" é o nome comercial do papel): ele vê
todas as organizações em números, sem ver os dados delas. O **owner da organização** é outro papel, de um
funcionário do cliente, que configura a organização dele.

Hoje a administração guarda a marca do produto, os administradores e o envio de e-mail. Na v2.0, ela passa a criar
as organizações e ganha o **painel dos assentos**. Um assento é uma vaga de uso contratada, de um tipo: owner,
gestor, membro ouro (pergunta e cria boards e relatórios para si), membro prata (pergunta e recebe alertas e PDFs,
sem criar nada) ou membro bronze (só vê os painéis já compartilhados). A prata pergunta no app, na Pergunta rápida
(MF-110) e no WhatsApp e, quando chegar, usa a Investigação guiada (MF-119), da v2.1, mas não cria boards,
relatórios, agendamentos nem agentes, os trabalhos automáticos de IA: o bronze vê, a prata pergunta, o ouro cria.
No painel, a Maind libera as vagas, acompanha o uso e o custo e corta quem não paga. Ganha também as conexões de IA
da instância, que a Maind paga e disponibiliza, ou não, a cada organização, e um aviso a todas as pessoas, para as
paradas da instância.

> 📌 **Exemplo:** a Maind cria a organização da área comercial de uma rede de lojas, que nasce com o assento de
> owner do Marcos, libera 30 assentos de membro ouro e 100 de membro bronze e lhe disponibiliza a conexão de IA da
> instância. No fim do mês, vê as 1.200 perguntas de análise respondidas e o gasto de IA, sem ler nenhuma conversa,
> e baixa o relatório para conferir a cobrança.

## ✨ Características

- **Quem usa:** só os administradores da instância, todos com os mesmos poderes, inclusive promover e remover
  outro; a instância nunca fica sem administrador.
- **As organizações:** só a administração as cria. Cada uma nasce **em configuração**, sem bloquear ninguém, e
  fica **ativa** quando o administrador a dá por pronta.
- **A IA da instância:** o administrador cadastra provedores de IA no nível da instância e disponibiliza cada
  conexão, ou não, a uma ou mais organizações. A Maind paga o que se consome por ela, e a organização a usa sem
  poder editá-la. A organização nasce sem IA: ao criá-la e liberar os assentos, o administrador escolhe se lhe
  disponibiliza uma conexão da instância. A organização que traz a própria IA cadastra a conexão dela, pelo owner,
  na IA sob controle da organização (MF-105), e paga o consumo.
- **A marca e o e-mail:** a marca é a da Maind, e o nome, os logos e o rodapé valem para todas as organizações.
  Convites, recuperação de senha e avisos da conta saem pelo e-mail da instância, num ritmo que a administração
  ajusta, como ajusta por quanto tempo o produto reaproveita as instruções repetidas que manda à IA.
- **Liberar e cortar:** os assentos se liberam só aqui, tipo a tipo, sem validade e sem reduzir abaixo do ocupado.
  Cortar é inativar a organização: o acesso, os agendamentos, os alertas e os agentes param, nada se apaga, e
  reativar devolve tudo.
- **O uso e o custo:** por organização e por dia, guardados enquanto ela existir: as perguntas de análise
  respondidas, as execuções dos agentes (os trabalhos automáticos de IA), o custo de IA e de WhatsApp e o número de
  e-mails. A Maind é avisada quando uma organização passa de um limite de custo que a própria Maind ajusta caso a
  caso; nada se corta sozinho.
- **O relatório e a história:** a qualquer momento, a administração vê e baixa, em planilha e em PDF, o uso, o
  custo e a história de cada assento, com o nome de quem o ocupou e quando. Também pergunta ao próprio Horus, em
  português, como a instância estava numa data. Excluir a organização apaga junto o uso e essa história. O owner da
  organização não vê nada disso: a visão de cobrança dele mostra só a contagem dos assentos de cada tipo.
- **Quando um serviço da instância para:** se a conexão de IA da instância deixa de responder (chave recusada,
  falta de crédito), se o número de WhatsApp compartilhado da Maind é bloqueado ou se o servidor recusa o e-mail da
  instância, quem é avisado é o administrador, e não o owner da organização. Quando o que para é da organização (a
  conexão de IA própria, a fonte de dados, o WhatsApp próprio), o aviso vai ao owner dela.
- **O aviso da instância:** o administrador escreve o texto, a data e a hora, com hora de fim opcional, e pode
  retirá-lo a qualquer momento. Ele aparece, sem e-mail, na Faixa de avisos e números (MF-120), a faixa no alto de
  toda tela, de quem não a escondeu: cada pessoa pode esconder a faixa, e quem a esconde deixa de ver os avisos.
  Durante a parada, quem abre o app vê, no lugar dele, uma página de manutenção com o motivo e a hora de volta.
- **Só números:** a administração vê quem ocupa cada assento, mas não lê conversas, boards, rastro nem dados de
  organização nenhuma.

## 📈 O valor que gera

- **Para quem usa:** a Maind cuida do acesso de cada cliente num lugar só, decide caso a caso a quem paga a IA, vê
  o custo antes da fatura de IA e sabe quem ocupava cada assento em qualquer mês.
- **Para a empresa que contrata o Horus:** recebe os assentos do contrato e fica sabendo de uma parada pelo próprio
  app, sem achar que o Horus quebrou.
- **Para o Horus como produto:** a cobrança por assento funciona desde o primeiro cliente, com o custo de cada
  organização à vista.

**Como vamos saber que funcionou:** a Maind cria uma organização, libera os assentos e, no fim do mês, confere no
relatório o uso, o custo e quem ocupou cada assento.

## 🚶 Como se usa no Horus

1. O administrador da instância cria a organização, que nasce com o assento do primeiro owner e sem IA.
2. Combina os assentos com o cliente, fora do produto, libera-os no painel, tipo a tipo, e escolhe se disponibiliza
   à organização uma conexão de IA da instância.
3. Marca a organização como ativa; o owner dela convida pessoas dentro do limite.
4. Acompanha o uso e o custo, baixa o relatório quando precisa e recebe o aviso quando um serviço da instância para.
5. Antes de uma parada, publica o aviso da instância.
6. Se o cliente deixa de pagar, inativa a organização; reativar devolve tudo.

```mermaid
flowchart LR
  a[Cria a organização e escolhe a IA da instância] --> b[Libera os assentos]
  b --> c[Owner da organização convida]
  c --> d[Acompanha uso, custo e relatório]
  d --> e{O cliente pagou?}
  e -->|sim, e pediu mais| b
  e -->|não| f[Inativa a organização]
  f -->|voltou a pagar| g[Reativa: tudo volta]
```

## 🧩 Grau de complexidade: alta

A marca, os administradores, o envio de e-mail e as telas de administração vêm da v1 quase como estão. Novos são o
painel dos assentos, com cada assento como um registro, o painel do uso, que junta os números de organizações com
bancos separados, o relatório, o aviso e as conexões de IA da instância, disponibilizadas por organização. A
história fica num banco próprio, que o Horus consulta como uma fonte, e isso mexe na base de dados e em vários
módulos; de fora, depende só do serviço de e-mail de hoje.

> ⚠️ É a leitura do PO a partir dos documentos de arquitetura. A estimativa de esforço é do arquiteto.

## 🔗 Macro funcionalidades relacionadas

| mf | Como se relaciona |
| --- | --- |
| Organizações, pessoas e papéis (MF-102) | **depende de**: as pessoas e os papéis vêm de lá; a administração cria a organização e cuida da instância, e o owner da organização cuida das pessoas e das preferências dela. |
| Licenças e planos (MF-103) | **depende de, e é a base de**: os assentos e as regras dos cinco tipos de assento são de lá; o painel onde a Maind libera e corta os assentos é daqui. |
| IA sob controle da organização (MF-105) | **complementa**: é aqui que a Maind cadastra as conexões de IA da instância, as disponibiliza a cada organização, vê o custo de IA de cada uma e recebe o aviso de custo e o de que a IA da instância parou; a conexão própria da organização, que ela paga, é de lá. |
| Segurança dos dados por pessoa (MF-106) | **complementa**: o interruptor geral da segurança, que a administração tem hoje, passa a ser de lá, na v2.1; na v2.0, a organização é a fronteira dos dados. |
| Conectores de Saída (MF-113) | **é a base de**: o conector de e-mail usa o mesmo servidor de e-mail da instância; quando ele ou o número de WhatsApp compartilhado da Maind param, quem é avisado é o administrador da instância. |
| Auditoria (MF-116) | **complementa**: o rastro de quem abriu e entregou o quê é de lá, só do owner de cada organização; a história guardada aqui é a da instância, sem conteúdo das organizações. |
| Faixa de avisos e números (MF-120) | **depende de, e é a base de**: o aviso da instância aparece na faixa, que é de lá; o aviso e os cards prontos com os números da instância se escrevem e se configuram aqui. |

## 🚧 O que ela não faz

- **Cobrar:** o preço, a fatura e o pagamento ficam com o comercial da Maind; há um plano só.
- **Ligar a segurança dos dados por pessoa:** o interruptor geral vai com a Segurança dos dados por pessoa
  (MF-106), na v2.1.
- **Mostrar a marca do cliente:** o logo, o nome, o e-mail e as cores do cliente no produto estão sem versão.
- **Configurar a casa do cliente:** o Middleware na casa do contratante (MF-121), da v2.1, a peça que o cliente
  instala para o Horus chegar aos dados dele, é do owner da organização; instalar o Horus inteiro no cliente está
  sem versão.
- **Mostrar ao público se o Horus está de pé:** uma página aberta com o estado da instância não entra na v2.0.

## ⏳ Ainda a decidir

- **No setup de cada organização,** o cliente deve consultar o jurídico dele sobre a Maind ver o nome de quem ocupa
  cada assento; o produto parte de mostrar os nomes.
- Como a conexão de IA da instância chega às organizações: é do desenho do arquiteto.

## 📚 Para saber mais

- `docs/raw/produto/04-macro-funcionalidades-de-hoje.md`: o mapa (o que a v1.xx entrega) e a tabela de conversão (a
  camada 🧱 Plataforma).
- `docs/raw/produto/05-v2.0-consolidada.md`: §1 (mf a mf), §3.2 (a base herdada), §4 (o passo 1) e as leituras
  **D-067.1**, **D-068.1** e **D-128.3**.
- `docs/raw/produto/06-versoes.md`: a MF-101 inteira na v2.0 (**D-197**), o interruptor na MF-106 (**D-199**) e a
  marca do contratante sem versão (**D-200**).
- `docs/raw/produto/07-mapa-de-objetivos-e-funcionalidades.md`: o painel dos assentos na v2.0 (O7).
- `docs/raw/produto/03-inventario-de-lacunas.md`: as linhas 11 (os dois owners), 12 (várias organizações) e 13 (a
  marca branca).
- `docs/raw/produto/backlog-estrategico.md`:
  - a definição macro: **D-202** (o que a mf é, o que não inclui e de que depende: as pessoas e os papéis, os
    assentos e a faixa onde o aviso aparece);
  - a instância e quem a opera: **D-008** (várias organizações), **D-013** (os dois níveis de owner), **D-021** (a
    base herdada), **D-147** (um papel só de administrador), **D-192** e **D-193** (o SaaS é uma instância só, da
    Maind);
  - as organizações e os assentos: **D-146** (só a administração cria organizações), **D-148** (as três situações
    e o corte), **D-123** e **D-156** (o assento de owner da criação), **D-194** (os cinco tipos de assento),
    **D-203** (o que a prata faz: pergunta, investiga e recebe alertas e PDFs, sem criar nada), **D-067**,
    **D-068**, **D-076** e **D-077** (o painel e quem libera), **D-080** e **D-117** (o painel sem seletor de plano);
  - o uso, o custo e o relatório: **D-149**, **D-150**, **D-153**, **D-157**, **D-158** e **D-166**; **D-234** (sem
    teto automático de custo: fica o aviso de custo); **D-214** (a visão de cobrança do owner da organização mostra
    só a contagem de assentos); **D-159** e **D-160** (quem paga a IA e o WhatsApp; a **D-159** foi substituída em
    parte pela **D-216**);
  - a IA da instância: **D-216** (há a conexão da organização, que ela paga, e a da instância, que a Maind paga e
    disponibiliza ou não a cada organização, sem edição nela), **D-217** (a organização nasce sem IA, e o
    administrador escolhe se lhe disponibiliza a conexão da instância ao criá-la);
  - os serviços que param: **D-218** (a IA: é avisado o dono da conexão) e **D-240** (o número de WhatsApp da Maind
    e o e-mail da instância avisam o administrador; a fonte de dados e o WhatsApp próprio, o owner da organização);
  - o aviso e a parada: **D-151**, **D-154** e **D-165**; **D-168** (quem esconde a faixa deixa de ver os avisos);
    **D-152**, **D-172** e **D-174** (a faixa é a MF-120, e os cards da instância se configuram na administração);
    **D-204** (a MF-120 sai da lista de cortes: o aviso da instância só chega às pessoas pela faixa);
  - a marca e o e-mail: **D-011**, **D-128**, **D-155** e **D-200** (a marca é a da Maind; substitui a **D-121** e
    a **D-183** neste ponto);
  - o que saiu: **D-091** (o rastro é do owner da organização), **D-145** e **D-199** (a segurança por pessoa e o
    interruptor na MF-106), **D-195** (o middleware é da organização), **D-188** (a instalação no cliente sem
    versão);
  - **P-032**: como a conexão de IA da instância chega às organizações (do arquiteto).
- `docs/raw/arquitetura/README.md`, seção "O modelo de dados (MER)", e o modelo de dados da MF-101, no repositório
  do backend da v2 (`src/backend/docs/modelo-de-dados/mf-101-gestao-da-instancia.md`): o estado de hoje, o banco de
  log e os cinco diagramas.
- `docs/raw/arquitetura/01-estrategia-da-solucao.md`: §4 (a linha da MF-101) e §6 (o marco M1).
- `docs/raw/arquitetura/02-registro-de-decisoes.md`: **ARQ-017** e **ARQ-084** (o uso e o custo no painel e o aviso à
  Maind), **ARQ-046** (o e-mail da instância), **ARQ-010** e **ARQ-088** (um banco por organização; a instância no
  banco mestre), **ARQ-090** (a segurança por pessoa na v2.1), **ARQ-097** (a história num banco de log, que o
  Horus consulta).
- `docs/raw/arquitetura/04-software.md`: §3.2, os componentes Instância, Painel dos assentos e Envio de e-mail.
- `docs/raw/arquitetura/06-dados.md` (o que é da instância) e `docs/raw/arquitetura/07-seguranca.md` §3.1 (o administrador
  não lê dado de organização).
- `docs/raw/arquitetura/14-conferencia-do-produto.md`: §3 (o que se reaproveita) e §4 (**A-02**, **A-21** e **A-29**).
