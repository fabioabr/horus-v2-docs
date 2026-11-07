---
codigo: MF-123
nome: Fonte AWS Athena
entrega: v2.1
situacao: definida
camada: 🔌 Dados e IA
objetivos: [O1]
quem_usa: [owner da organização, gestor, executivo]
complexidade: média (provisória)
relacionadas: [MF-104, MF-107, MF-106, MF-121]
atualizado: 2026-11-07
fontes:
  - docs/raw/produto/06-versoes.md
  - docs/raw/produto/backlog-estrategico.md
  - docs/raw/arquitetura/02-registro-de-decisoes.md
  - docs/raw/arquitetura/08-integracoes.md
  - docs/raw/arquitetura/14-conferencia-do-produto.md
---

# Fonte AWS Athena

> **Em uma frase:** perguntar em português aos dados que a empresa guarda na nuvem da Amazon, sem pedir ao time de
> dados.

## 🧭 O que é

**Como é hoje.** O Horus responde perguntas de análise sobre cinco tecnologias de banco: SQL Server, PostgreSQL,
Oracle, MongoDB e BigQuery. O **AWS Athena**, o serviço da Amazon (AWS) para consultar dados guardados na nuvem dela,
só se cadastra: o Horus não responde nada com ele, e ele saiu da tela no Horus de hoje. A v2.0 não o traz.

**O que passa a existir.** Esta macro funcionalidade (mf), de nome ainda provisório, termina o Athena: ele passa a
responder **perguntas de análise**, as perguntas sobre os números da empresa, como as outras **fontes vivas**, os
bancos da empresa que o Horus consulta na hora da pergunta.

**Como fica o dia a dia.** O Athena é conectado como toda fonte, no **front do middleware**, o aplicativo do
**Middleware da organização** (MF-121): a peça que fica entre o Horus e os bancos da organização, guarda quem são as
pessoas, os bancos e a IA dela e responde pelo caminho até eles. Quem conecta é o **owner da organização**, o
funcionário do cliente que administra a organização, em qualquer hospedagem, com o middleware na casa do cliente ou
hospedado pela Maind; o time da Maind dá suporte técnico, mas não conecta por ele. Depois, o gestor pergunta ao
Athena como pergunta a qualquer outra fonte.

> 📌 **Exemplo** *(personagens ilustrativos)*: os dados de vendas de uma rede de lojas ficam na AWS. O
> Athena é conectado no front do middleware da organização, e a gestora Carla pergunta quanto cada loja vendeu na
> semana: o número sai do Athena, sem ninguém exportar planilha.

## ✨ Características

- **O que muda:** o Athena deixa de só se cadastrar e passa a responder perguntas de análise.
- **Como as outras fontes:** segue a base das fontes vivas, a de Conectar as fontes vivas (MF-104).
- **Só lê:** como em toda fonte, o Horus nunca altera um dado do Athena.
- **Quem conecta:** como em toda fonte, a conexão é feita no front do middleware pelo owner da organização, em
  qualquer hospedagem; o time da Maind dá suporte técnico, antes e depois da venda.
- **Quem ganha:** o **gestor**, quem responde por uma equipe, e o **executivo** de uma organização cujos dados estão
  no Athena.
- **A mesma conversa:** a pergunta passa pelo mesmo motor de Perguntar aos dados em português (MF-107), que
  transforma a pergunta numa consulta à fonte.
- **O recorte por pessoa:** vale o que a Segurança dos dados por pessoa (MF-106) cobrir no Athena; hoje ela só cobre
  o SQL Server.
- **Uma fonte a mais, só:** nenhuma outra fonte nova vem com ela.
- **Quando chega:** na v2.1; na v2.0, o Athena fica fora.

## 📈 O valor que gera

- **Para quem usa:** pergunta em português aos dados que estão na AWS, sem pedir ao time de dados.
- **Para a empresa que contrata o Horus:** os dados guardados na AWS entram nas respostas como os dos outros bancos.
- **Para o Horus como produto:** abre as empresas com dados na AWS. ⚠️ Ainda não há demanda conhecida: nenhum
  cliente pediu o Athena até aqui.

**Como vamos saber que funcionou:** uma organização conecta um Athena e recebe uma resposta de análise.

## 🚶 Como se usa no Horus

**O owner da organização**, que conecta a fonte em qualquer hospedagem:

1. Conecta o Athena como uma fonte da organização, no front do middleware.
2. Como em toda fonte, passa-a ao time de dados, que escreve o **modelo semântico**, o dicionário que explica ao
   Horus o que cada coluna significa na empresa.

**Quem pergunta:**

1. Escolhe o Athena entre as fontes da conversa e pergunta.
2. Recebe a resposta com a fonte à vista, como em qualquer resposta do Horus.

```mermaid
flowchart LR
  a[Conecta o Athena no front do middleware] --> b[Time de dados escreve o modelo semântico]
  b --> c[Pessoa escolhe o Athena e pergunta]
  c --> d[Horus consulta o Athena, só para ler]
  d --> e[Resposta com a fonte à vista]
```

## 🧩 Grau de complexidade: média (provisória)

Da v1 vêm o cadastro do Athena, que hoje só guarda a conexão, e toda a base das fontes vivas. É novo fazer o Athena
responder: o conector e o jeito de escrever a consulta na língua dele, o dialeto. Depende da Segurança dos dados por
pessoa, que hoje só cobre o SQL Server, e de caber na v2.1 junto dela; de fora, só do serviço da Amazon.

> ⚠️ É a leitura do PO a partir dos documentos de arquitetura, e é provisória: o arquiteto ainda vai dimensionar o
> conector, o dialeto e a segurança por pessoa no Athena. A estimativa de esforço é do arquiteto.

## 🔗 Macro funcionalidades relacionadas

| mf | Como se relaciona |
| --- | --- |
| Conectar as fontes vivas (MF-104) | **depende de**: é a base das fontes; o Athena passa a ser mais uma delas. |
| Perguntar aos dados em português (MF-107) | **depende de**: é a conversa que transforma a pergunta numa consulta ao Athena. |
| Segurança dos dados por pessoa (MF-106) | **depende de**: o recorte do que cada pessoa vê no Athena vem dela, que hoje só cobre o SQL Server. |
| Middleware da organização (MF-121) | **depende de**: o Athena, como toda fonte, é conectado no front do middleware, e as consultas a ele rodam no middleware. |

## 🚧 O que ela não faz

- **Trazer outras fontes novas:** só o Athena.
- **Recortar os dados por pessoa** além do que a Segurança dos dados por pessoa (MF-106) cobrir.
- **Entrar na v2.0:** lá, o Athena fica fora.
- **Escrever nos dados da AWS:** o Horus só lê.

## ⏳ Ainda a decidir

- **Se a mf cabe na v2.1:** é hipótese a validar, junto da Segurança dos dados por pessoa, com o dimensionamento do arquiteto.
- **A segurança por pessoa no Athena:** hoje ela só cobre o SQL Server, e o que vale no Athena depende do
  dimensionamento do arquiteto.

## 📚 Para saber mais

- [Backlog estratégico](../../raw/produto/backlog-estrategico.md): `D-201`, a definição macro, confirmada pelo dono (fechou a `P-043`); `D-198`, o Athena vira a `MF-123` (nome
  provisório), na v2.1, dependendo da `MF-104` e da `MF-106`; `D-265`, os bancos configurados no front do
  middleware (o owner deixa de conectar as fontes pelo Horus, como dizia a `D-201`), em parte substituída pela
  `D-273` (em qualquer hospedagem, quem configura os bancos é o owner da organização, e o time da Maind só dá
  suporte), e `D-258`, as consultas rodando no middleware; `D-161`, o Athena sai da v2.0 e entra terminado na
  v2.1 (o dono escolheu contra a recomendação de deixá-lo fora até um cliente pedir), sem demanda conhecida; `D-139 (MVP da v1.xx)`,
  o Athena fora da tela no MVP da v1.xx; `I-017`, fechado; `D-083`, o modelo semântico com o time de dados; `D-145`, a
  segurança por pessoa inteira na v2.1; `D-197`, uma mf numa versão só; `P-033`, dimensionar o conector, o dialeto e a
  segurança por pessoa (do arquiteto).
- [Versões](../../raw/produto/06-versoes.md): a v2.1, a `MF-104` sem o Athena e "O que trava a v2.1";
  [a v2.0 consolidada](../../raw/produto/05-v2.0-consolidada.md), §5.17 (o middleware de cada organização).
- Arquitetura: [registro](../../raw/arquitetura/02-registro-de-decisoes.md), `ARQ-052` (as cinco tecnologias da v2.0;
  o Athena esperava o PO); [integrações](../../raw/arquitetura/08-integracoes.md), §3.5 (o Athena só cadastra);
  [conferência](../../raw/arquitetura/14-conferencia-do-produto.md), §4, `A-04` (as duas fontes que o MVP tira da
  tela, hoje `I-017`).
