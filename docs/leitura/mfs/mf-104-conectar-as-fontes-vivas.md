---
codigo: MF-104
nome: Conectar as fontes vivas
entrega: v2.0 + v2.1
situacao: só no mapa
camada: 🔌 Dados e IA
objetivos: [O1, O8]
quem_usa: [owner da organização, time de dados, gestor, membro full]
complexidade: baixa
relacionadas: [MF-107, MF-105, MF-106, MF-109, MF-112]
atualizado: 2026-11-03
fontes:
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
  - docs/raw/arquitetura/06-dados.md
  - docs/raw/arquitetura/07-seguranca.md
  - docs/raw/arquitetura/08-integracoes.md
  - docs/raw/arquitetura/14-conferencia-do-produto.md
---

# Conectar as fontes vivas

> **Em uma frase:** ligar o Horus aos bancos de dados da empresa, só para ler, para que cada resposta traga o número
> de agora, e não o de uma planilha de ontem.

## 🧭 O que é

Uma **fonte de dados** é um banco da empresa ligado ao Horus: o de vendas, o de estoque, o financeiro. Ela é **viva**
porque o Horus consulta o próprio banco na hora da pergunta de análise, e não uma cópia exportada.

O Horus de hoje já faz isso, e a v2.0 mantém esta macro funcionalidade (mf) quase como está. Cada fonte tem o seu
**modelo semântico**, o documento que explica ao Horus o que cada tabela e cada palavra querem dizer na empresa
("faturamento", "loja ativa"). O **owner da organização**, que cuida das pessoas e dos dados de um setor ou de um
cliente, cadastra as fontes; o time de dados escreve o modelo semântico.

Na v2.0, cada organização guarda as suas fontes num espaço só dela. Na v2.1, com o Horus dentro da casa do
contratante, a fonte passa a alcançar a rede interna dele, com autorização explícita.

> 💡 A credencial só de leitura é como o acesso de "só consulta" que o banco dá ao contador: ele vê o extrato, mas
> não faz transferência. Onde a comparação falha: o Horus não confia na palavra de quem cadastra e confere com o
> próprio banco.

> 📌 **Exemplo** (personagens ilustrativos): o Marcos, owner da área comercial de uma rede de lojas, cadastra o banco
> de vendas, que a TI não expõe na internet. Escolhe o túnel, informa a credencial só de leitura e clica em
> "Testar": a conexão responde. O time de dados escreve o modelo semântico, e a gestora Carla pergunta quanto cada
> loja vendeu na semana: o número sai do banco na hora.

## ✨ Características

- **Cinco tecnologias:** SQL Server, PostgreSQL, Oracle, MongoDB e BigQuery.
- **Só lê:** o Horus nunca altera um dado; toda consulta passa por uma porta única que recusa escrita e traz até 500
  linhas em até 30 segundos.
- **Dois caminhos até o banco:** o endereço público, que a TI do cliente libera no firewall, ou o túnel SSH, uma
  passagem segura pela máquina de entrada da rede dele.
- **Credencial no cofre:** cifrada, nunca volta à tela; o botão "Testar" confere a conexão sem gastar IA.
- **Um modelo semântico por fonte:** o Horus o lê a cada pergunta; melhorá-lo é do time de dados.
- **Um teto de inferência por fonte:** até onde o Horus pode interpretar além do número; com várias fontes na
  conversa, vale o menor teto.
- **Idade mínima do dado:** dentro de um intervalo que a fonte define, a mesma consulta reaproveita o resultado já
  buscado, em vez de perguntar de novo ao banco.
- **Longe da rede interna:** a fonte nunca alcança a rede interna da máquina onde o Horus roda; a exceção da v2.1 vale
  só na instalação do contratante.
- **Os dados da organização inteira:** na v2.0, quem pergunta vê tudo o que a fonte tem; o papel e as roles (pacotes
  de botões que o owner monta) decidem quem pergunta, e o recorte por pessoa vem com a Segurança dos dados por pessoa
  (MF-106), na v2.1. Um setor que precise de dados à parte ganha a sua própria organização.

## 📈 O valor que gera

- **Para quem usa:** o número sai do banco de verdade, na hora, sem pedir exportação a ninguém.
- **Para a empresa que contrata o Horus:** os bancos ficam intocados, e a TI decide por onde o Horus entra.
- **Para o Horus como produto:** é a base da conversa, dos boards e dos agentes.

**Como vamos saber que funcionou:** as fontes de cada organização respondem com o número do banco, e nenhuma
enxerga a de outra.

## 🚶 Como se usa no Horus

**O owner da organização:**

1. Cadastra a fonte: a tecnologia, o caminho e a credencial só de leitura.
2. Clica em "Testar": o Horus confere que conecta e que a credencial só lê.
3. Ajusta o teto de inferência e a idade mínima do dado.
4. Passa a fonte ao time de dados, que escreve o modelo semântico.

**Quem pergunta** (o owner, o **gestor** e o **membro full**; o **membro leitor** só vê boards) escolhe as fontes na
conversa e pergunta.

```mermaid
flowchart LR
  a[Owner cadastra a fonte] --> b[Testar: conecta e só lê]
  b --> c[Time de dados escreve o modelo semântico]
  c --> d[Pessoa escolhe a fonte e pergunta]
  d --> e[Horus consulta o banco ou reaproveita o resultado recente]
```

## 🧩 Grau de complexidade: baixa

🟢 Quase tudo vem pronto da v1: os conectores, o túnel, a barreira contra a rede interna, o cofre, o reaproveitamento
das consultas e o modelo semântico. Na v2.0, só o acesso muda, para respeitar o espaço de cada organização, e nada
externo é novo. Depende da separação entre organizações, que é da plataforma, e da instalação na casa do contratante,
na v2.1; o grau sobe se a v2.0 tiver de terminar as duas fontes que hoje saem da tela.

> ⚠️ É a leitura do PO a partir dos documentos de arquitetura. A estimativa de esforço é do arquiteto.

## 🔗 Macro funcionalidades relacionadas

| mf | Como se relaciona |
| --- | --- |
| Perguntar aos dados em português (MF-107) | **é a base de**: a conversa transforma a pergunta numa consulta a estas fontes, guiada pelo modelo semântico |
| IA sob controle da organização (MF-105) | **complementa**: a IA escreve a consulta e o texto, e os números saem da fonte; na v2.1, as duas entram juntas na casa do contratante |
| Segurança dos dados por pessoa (MF-106) | **complementa**: na v2.1, recorta o que cada pessoa vê de cada fonte; até lá, vale a organização inteira |
| A web como fonte (MF-109) | **complementa**: a web é a outra fonte viva, ao lado dos bancos da empresa |
| Boards e Relatórios (MF-112) | **é a base de**: os cartões consultam as mesmas fontes e reaproveitam o resultado dentro da idade mínima do dado |

## 🚧 O que ela não faz

- **Escrever nos bancos** ou agir nos sistemas da empresa.
- **Montar o modelo semântico sozinha:** é do time de dados.
- **Conectar por VPN ou pela rede privada de uma nuvem:** fica fora da v2.0.
- **Recortar os dados por pessoa:** é da Segurança dos dados por pessoa, na v2.1.

## ⏳ Ainda a decidir

- **O AWS Athena e a fonte de páginas web**, fora da tela no MVP da v1: voltam terminados na v2.0 ou ficam de fora.
- **O teto de inferência:** as roles falam num "teto da organização", e hoje ele é de cada fonte.

## 📚 Para saber mais

- `docs/raw/produto/04-macro-funcionalidades-de-hoje.md`: o mapa (o que a mf entrega hoje), a tabela de conversão
  (camada 🔌 Dados e IA) e "Previsto e ainda não construído" (o Athena, as redes privadas, o assistente de modelagem).
- `docs/raw/produto/backlog-estrategico.md`: **D-021** (base herdada); **D-001** e **D-022** (o Horus só lê); **D-016**,
  **D-017** e **D-121** (a rede interna do contratante na v2.1); **D-083** (o modelo semântico com o time de dados);
  **D-013** (o owner da organização); **D-138** e **D-139** (o Athena e as páginas web fora da tela no MVP);
  **D-110** (os botões da role); **D-145** (a organização é a fronteira dos dados na v2.0; a segurança por pessoa inteira na v2.1).
- `docs/raw/produto/05-v2.0-consolidada.md` (§1, §3.2, §5.4 e §6), `06-versoes.md`, `07-mapa-de-objetivos-e-funcionalidades.md`
  (O1 e O8) e `03-inventario-de-lacunas.md` (linha 15 e candidata nº 5).
- `docs/raw/arquitetura/01-estrategia-da-solucao.md`: §1 ("O que continua valendo"), §4 (a linha da MF-104) e §6 (os
  marcos M2 e M10).
- `docs/raw/arquitetura/02-registro-de-decisoes.md`: **ARQ-052** (as cinco tecnologias e os dois caminhos),
  **ARQ-010** e **ARQ-034** (a fonte de uma organização só), **ARQ-077** (as travas do banco e do driver),
  **ARQ-090** (o que fica na v2.0 sem a segurança por pessoa) e **ARQ-060** (o on-premises da v2.1).
- `docs/raw/arquitetura/04-software.md` (§3.2 e §3.6: o catálogo de fontes, os conectores, o histórico de execuções e o
  ponto único de execução), `05-motor-de-analise-e-ia.md` (§3.4: o modelo semântico e o teto por fonte),
  `06-dados.md` (§3.2: o isolamento entre organizações), `07-seguranca.md` (§3.7: o cofre e a guarda de rede) e
  `08-integracoes.md` (§3.5: as fontes dos clientes e os tetos por consulta).
- `docs/raw/arquitetura/14-conferencia-do-produto.md`: §3 (o que se reaproveita) e §4: **A-04** (o Athena e as páginas
  web), **A-13** (o teto de inferência) e **A-24** (escolher as fontes não está entre os botões da role).
- O sentido da "idade mínima do dado", que o mapa só nomeia, vem do código da v1.xx:
  `horus@318db52b:apps/server/Horus.Core/Data/Connections/ConnectionCatalog.cs` (`IdadeMinimaPadraoMinutos`).
