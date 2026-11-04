---
codigo: MF-109
nome: A web como fonte
entrega: v2.0
situacao: definida
camada: 💬 Motor de análise
objetivos: [O1]
quem_usa: [owner da organização, gestor, membro full]
complexidade: média
relacionadas: [MF-102, MF-104, MF-105, MF-107, MF-108, MF-111, MF-112, MF-115]
atualizado: 2026-11-03
fontes:
  - docs/raw/produto/02-norte-do-produto.md
  - docs/raw/produto/03-inventario-de-lacunas.md
  - docs/raw/produto/04-macro-funcionalidades-de-hoje.md
  - docs/raw/produto/05-v2.0-consolidada.md
  - docs/raw/produto/06-versoes.md
  - docs/raw/produto/07-mapa-de-objetivos-e-funcionalidades.md
  - docs/raw/produto/backlog-estrategico.md
  - docs/raw/arquitetura/01-estrategia-da-solucao.md
  - docs/raw/arquitetura/02-registro-de-decisoes.md
  - docs/raw/arquitetura/04-software.md
  - docs/raw/arquitetura/05-motor-de-analise-e-ia.md
  - docs/raw/arquitetura/08-integracoes.md
  - docs/raw/arquitetura/14-conferencia-do-produto.md
---

# A web como fonte

> **Em uma frase:** cruzar o número da empresa com o que acontece lá fora, como a inflação ou a concorrência, sem
> sair da conversa e sabendo de onde veio e de quando é cada fato.

## 🧭 O que é

A web é a segunda fonte viva do Horus, ao lado dos bancos da empresa: complementa os números com o contexto de
mercado, responde sozinha à pergunta sobre algo de fora e serve de régua. Hoje o Horus já pesquisa na web, mas cita
a fonte no meio do texto, sem data.

Na v2.0, todo fato da web traz o **link da fonte** e a **data de publicação**, separado do dado da empresa. O fato
entra em qualquer **nível de inferência**, a régua de 1 a 5 de quanto a resposta pode ir além do número; a causa
vinda de fora, só a partir do nível 4.

> 📌 **Exemplo:** no nível padrão, a gestora Carla liga a pesquisa e pergunta "as vendas de outubro acompanharam a
> inflação?". Recebe o gráfico das vendas e "inflação de outubro: 0,4%", com o link do IBGE e a data de publicação.
> Se pergunta por que as vendas caíram, a resposta não culpa a inflação, a não ser que ela suba para o nível 4.

## ✨ Características

- **Duas formas de usar a web:** a **pesquisa na web**, que a pessoa liga na conversa de análise, a tela de Perguntar
  aos dados em português (MF-107), e o **modo web**, que lê as páginas que a organização cadastrou como fonte.
- **Link e data em todo fato:** a data é lida na própria página, e sem ela aparece o aviso de data não identificada.
- **O fato em qualquer nível:** até no nível 1, que só descreve, o fato entra; a causa vinda de fora, só do nível 4
  em diante, rotulada como hipótese.
- **Separado do dado da empresa:** os fatos aparecem à parte do texto, e um link que a pesquisa não trouxe sai da
  resposta.
- **Em todo modo e canal:** vale nos modos dados, web e conversa, na Pergunta rápida (MF-110), no Chat pelo WhatsApp
  (MF-111), com o link e a data no texto, nos boards e nos agentes.
- **Quem usa:** o owner da organização, que cuida das pessoas e dos dados dela, o gestor, que gere uma equipe, e o
  membro full, que pergunta e cria boards, se a role da pessoa (o pacote de permissões que o owner dá) tiver o modo
  web ligado.
- **Segue a conexão de IA:** a busca é a do provedor de IA da organização, e quando ele não pesquisa, como o Amazon
  Bedrock, a opção não aparece.
- **Só a pergunta sai:** à busca vai só o texto da pergunta, nunca dados do banco nem o modelo semântico, o
  dicionário de termos da empresa.
- **Corre ao lado da consulta:** se a busca não volta a tempo, a resposta sai sem ela.

## 📈 O valor que gera

- **Para quem usa:** explica um resultado com o contexto de fora antes de mostrá-lo ao CEO, sabendo de onde veio
  cada fato.
- **Para a empresa que contrata o Horus:** menos pedidos ao time de dados para buscar um índice de fora.
- **Para o Horus como produto:** respostas mais completas sem perder a confiança, que é a prova do produto.

**Como vamos saber que funcionou:** nenhuma informação da web aparece sem o link, e nenhuma aparece sem a data ou
sem o aviso de que ela não foi identificada.

## 🚶 Como se usa no Horus

**Quem pergunta:**

1. Liga a pesquisa na web na conversa.
2. Faz a pergunta de análise, no nível que quiser.
3. Recebe o número da empresa e, à parte, os fatos de fora, cada um com link e data.
4. Abre o link para conferir o fato antes de levá-lo adiante.
5. Sobe para o nível 4 quando quer que a resposta arrisque uma causa de fora.

**O owner da organização:**

1. Liga o modo web nas roles de quem pode usar a web.
2. Cadastra a conexão de IA da organização, que decide se a pesquisa existe.

```mermaid
flowchart LR
  a[Pergunta com a pesquisa ligada] --> b[Busca na web, ao lado da consulta]
  b --> c[Fatos com link e data]
  c --> d[Resposta com o dado da empresa e os fatos de fora, separados]
  d --> e[Pessoa confere pelo link]
```

## 🧩 Grau de complexidade: média

Vêm da v1 a busca do provedor de IA e o leitor de páginas do servidor. É nova a etapa própria da web, que devolve
os fatos com link e data e tira do texto o link que não veio da busca. Depende da busca do provedor de IA e de o
modelo respeitar a regra da causa abaixo do nível 4, o que só a medição mostra; não é alta porque não mexe na base
nem traz parceiro novo.

> ⚠️ É a leitura do PO a partir dos documentos de arquitetura. A estimativa de esforço é do arquiteto.

## 🔗 Macro funcionalidades relacionadas

| mf | Como se relaciona |
| --- | --- |
| Perguntar aos dados em português (MF-107) | **depende de**: a web entra na mesma conversa e obedece aos mesmos níveis de inferência |
| IA sob controle da organização (MF-105) | **depende de**: a busca é a do provedor da conexão de IA da organização |
| Organizações, pessoas e papéis (MF-102) | **depende de**: o modo web é um botão da role |
| Conectar as fontes vivas (MF-104) | **depende de**: o modo web lê a fonte de páginas da web cadastrada ali |
| Respostas visuais (MF-108) | **complementa**: o bloco mostra o número da empresa, e o fato de fora vem à parte, com link e data |
| Chat pelo WhatsApp (MF-111), Boards e Relatórios (MF-112) e Agentes ativos (MF-115) | **é a base de**: o fato com link e data vale também na mensagem, no cartão e no que o agente entrega |

## 🚧 O que ela não faz

- **Selos de confiança** nas fontes, nem uma lista de fontes aprovadas pela organização.
- **Causa vinda da web abaixo do nível 4.**
- **Guardar cópias das páginas** consultadas.
- **Buscar em sites que pedem login.**
- **Pesquisar por outro caminho:** sem a busca da conexão de IA, nenhum outro serviço pesquisa no lugar dela.

## ⏳ Ainda a decidir

- **O modo web:** ele depende da fonte de páginas da web, hoje fora da tela; falta decidir se a v2.0 a traz pronta.
- **O cartão do board:** se guarda os fatos da resposta que o originou, com a data à vista, em vez de pesquisar de novo.
- **A resposta sem fatos:** o que a tela mostra quando a pesquisa não traz fato nenhum.

## 📚 Para saber mais

| Trecho do inventário | O que traz |
| --- | --- |
| `docs/raw/produto/02-norte-do-produto.md`, as fontes | A web como fonte viva, ao lado dos bancos, e os usos dela |
| `docs/raw/produto/04-macro-funcionalidades-de-hoje.md`, o mapa e a tabela de conversão | O que a mf entrega hoje e a camada dela |
| `docs/raw/produto/05-v2.0-consolidada.md`, §3.1, §3.2, §4 e §5.4 | A candidata nº 3, a base herdada, o passo 5 da prova de valor e a regra da web |
| `docs/raw/produto/backlog-estrategico.md` | A definição macro da web como fonte viva completa (`D-131`); o link e a data (`D-006`); o fato em qualquer nível (`D-130`, leituras `D-130.1` e `D-130.2`); o modo web nas roles (`D-110`); a base herdada (`D-021`) |
| `docs/raw/produto/03-inventario-de-lacunas.md`, linhas 5 e 6 | A lacuna da web em todos os usos e da data |
| `docs/raw/produto/06-versoes.md` e `07-mapa-de-objetivos-e-funcionalidades.md` | A mf na v2.0, no objetivo O1 |
| `docs/raw/arquitetura/02-registro-de-decisoes.md`, `ARQ-025` a `ARQ-027` | O nível em toda etapa que escreve texto, a web como etapa própria e a busca nativa da conexão de IA, escolhida pelo dono |
| `docs/raw/arquitetura/05-motor-de-analise-e-ia.md`, §3.5, §3.6, §3.10 e §5 | Os níveis, a lista de fatos, o Bedrock sem busca e os riscos da web |
| `docs/raw/arquitetura/01-estrategia-da-solucao.md`, §4, `04-software.md` e `08-integracoes.md` | A estratégia da mf, as peças e a integração com os provedores |
| `docs/raw/arquitetura/14-conferencia-do-produto.md`, §1 a §4 | A separação do fato e da causa (`P-008`, letra aa), o que se reaproveita (`P-003`) e os itens devolvidos ao PO: a fonte de páginas web (A-04), o cartão do board (A-09) e a correção do inventário sobre a web (A-12, A-26) |
