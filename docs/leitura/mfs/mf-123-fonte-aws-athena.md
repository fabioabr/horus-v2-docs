---
codigo: MF-123
nome: Fonte AWS Athena
entrega: v2.1
situacao: definida
camada: 🔌 Dados e IA
objetivos: [O1]
quem_usa: [owner da organização, gestor, executivo]
complexidade: média (provisória)
relacionadas: [MF-104, MF-107, MF-106]
atualizado: 2026-11-05
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

**Como fica o dia a dia.** O **owner da organização**, o funcionário do cliente que configura a organização no
Horus, conecta o Athena, e o gestor pergunta a ele como pergunta a qualquer outra fonte.

> 📌 **Exemplo** *(personagens ilustrativos)*: os dados de vendas de uma rede de lojas ficam na AWS. O
> owner Marcos conecta o Athena, e a gestora Carla pergunta quanto cada loja vendeu na semana: o número sai do
> Athena, sem ninguém exportar planilha.

## ✨ Características

- **O que muda:** o Athena deixa de só se cadastrar e passa a responder perguntas de análise.
- **Como as outras fontes:** segue a base das fontes vivas, a de Conectar as fontes vivas (MF-104).
- **Só lê:** como em toda fonte, o Horus nunca altera um dado do Athena.
- **Quem conecta:** o owner da organização.
- **Quem ganha:** o **gestor**, quem responde por uma equipe, e o **executivo** de uma organização cujos dados estão
  no Athena.
- **A mesma conversa:** a pergunta passa pelo mesmo motor de Perguntar aos dados em português (MF-107), que
  transforma a pergunta numa consulta à fonte.
- **O recorte por pessoa:** vale o que a Segurança dos dados por pessoa (MF-106) cobrir no Athena; hoje ela só cobre
  o SQL Server.
- **Uma fonte a mais, só:** nenhuma outra fonte nova vem com ela.
- **Quando chega:** na onda 1 da v2.1, a do SaaS; na v2.0, o Athena fica fora.

## 📈 O valor que gera

- **Para quem usa:** pergunta em português aos dados que estão na AWS, sem pedir ao time de dados.
- **Para a empresa que contrata o Horus:** os dados guardados na AWS entram nas respostas como os dos outros bancos.
- **Para o Horus como produto:** abre as empresas com dados na AWS. ⚠️ Ainda não há demanda conhecida: nenhum
  cliente pediu o Athena até aqui.

**Como vamos saber que funcionou:** uma organização conecta um Athena e recebe uma resposta de análise.

## 🚶 Como se usa no Horus

**O owner da organização:**

1. Conecta o Athena como uma fonte da organização.
2. Como em toda fonte, passa-a ao time de dados, que escreve o **modelo semântico**, o dicionário que explica ao
   Horus o que cada coluna significa na empresa.

**Quem pergunta:**

1. Escolhe o Athena entre as fontes da conversa e pergunta.
2. Recebe a resposta com a fonte à vista, como em qualquer resposta do Horus.

```mermaid
flowchart LR
  a[Owner conecta o Athena] --> b[Time de dados escreve o modelo semântico]
  b --> c[Pessoa escolhe o Athena e pergunta]
  c --> d[Horus consulta o Athena, só para ler]
  d --> e[Resposta com a fonte à vista]
```

## 🧩 Grau de complexidade: média (provisória)

Da v1 vêm o cadastro do Athena, que hoje só guarda a conexão, e toda a base das fontes vivas. É novo fazer o Athena
responder: o conector e o jeito de escrever a consulta na língua dele, o dialeto. Depende da Segurança dos dados por
pessoa, que hoje só cobre o SQL Server, e de caber na onda 1 junto dela; de fora, só do serviço da Amazon.

> ⚠️ É a leitura do PO a partir dos documentos de arquitetura, e é provisória: o arquiteto ainda vai dimensionar o
> conector, o dialeto e a segurança por pessoa no Athena. A estimativa de esforço é do arquiteto.

## 🔗 Macro funcionalidades relacionadas

| mf | Como se relaciona |
| --- | --- |
| Conectar as fontes vivas (MF-104) | **depende de**: é a base das fontes; o Athena passa a ser mais uma delas. |
| Perguntar aos dados em português (MF-107) | **depende de**: é a conversa que transforma a pergunta numa consulta ao Athena. |
| Segurança dos dados por pessoa (MF-106) | **depende de**: o recorte do que cada pessoa vê no Athena vem dela, que hoje só cobre o SQL Server. |

## 🚧 O que ela não faz

- **Trazer outras fontes novas:** só o Athena.
- **Recortar os dados por pessoa** além do que a Segurança dos dados por pessoa (MF-106) cobrir.
- **Entrar na v2.0:** lá, o Athena fica fora.
- **Escrever nos dados da AWS:** o Horus só lê.

## ⏳ Ainda a decidir

- **Se a mf cabe na onda 1:** é hipótese a validar, junto da Segurança dos dados por pessoa, com o dimensionamento do arquiteto.
- **A segurança por pessoa no Athena:** hoje ela só cobre o SQL Server, e o que vale no Athena depende do
  dimensionamento do arquiteto.

## 📚 Para saber mais

- [Backlog estratégico](../../raw/produto/backlog-estrategico.md): `D-201`, a definição macro, confirmada pelo dono (fechou a `P-043`); `D-198`, o Athena vira a `MF-123` (nome
  provisório), na onda 1, dependendo da `MF-104` e da `MF-106`; `D-161`, o Athena sai da v2.0 e entra terminado na
  v2.1 (o dono escolheu contra a recomendação de deixá-lo fora até um cliente pedir), sem demanda conhecida; `D-139 (MVP da v1.xx)`,
  o Athena fora da tela no MVP da v1.xx; `I-017`, fechado; `D-083`, o modelo semântico com o time de dados; `D-145`, a
  segurança por pessoa inteira na v2.1; `D-197`, uma mf numa versão só; `P-033`, dimensionar o conector, o dialeto e a
  segurança por pessoa (do arquiteto).
- [Versões](../../raw/produto/06-versoes.md): a onda 1 da v2.1, a `MF-104` sem o Athena e "O que trava a v2.1".
- Arquitetura: [registro](../../raw/arquitetura/02-registro-de-decisoes.md), `ARQ-052` (as cinco tecnologias da v2.0;
  o Athena esperava o PO); [integrações](../../raw/arquitetura/08-integracoes.md), §3.5 (o Athena só cadastra);
  [conferência](../../raw/arquitetura/14-conferencia-do-produto.md), §4, `A-04` (as duas fontes que o MVP tira da
  tela, hoje `I-017`).
