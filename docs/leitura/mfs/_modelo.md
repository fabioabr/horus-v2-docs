---
# Identificação da macro funcionalidade (mf). Copie este bloco, preencha e apague os comentários.
codigo: MF-000
nome: Nome da mf, como está no mapa do 04
entrega: v2.0                 # v2.0 · v2.1 · v2.0 + v2.1 (base na v2.0, extensão na v2.1)
situacao: definida            # definida (definição macro confirmada pelo dono) · em definição · só no mapa
camada: 💬 Motor de análise    # a camada da tabela de conversão do 04
objetivos: [O1]               # os objetivos do 07 que ela cumpre
quem_usa: [gestor de área]    # os papéis que ganham com ela, em palavras comuns
complexidade: média           # baixa · média · alta (régua no fim deste modelo)
relacionadas: [MF-000]        # as mfs da seção "Relacionadas"
atualizado: AAAA-MM-DD        # a data em que esta página foi escrita a partir do inventário
fontes:                       # o inventário de onde esta página saiu (caminhos a partir da raiz da v2)
  - docs/raw/produto/04-macro-funcionalidades-de-hoje.md
---

# Nome da mf

> **Em uma frase:** o que a mf faz por quem usa, sem jargão. Exemplo de tom: "Tirar uma dúvida sobre os números da
> empresa de qualquer tela, sem largar o que você está fazendo."

## 🧭 O que é

Dois ou três parágrafos curtos que respondem **o que a mf faz**, pelo que a pessoa vê e faz, e não pelo mecanismo:
o que existe hoje (uma frase), o que passa a existir e como fica o dia a dia.

> 📌 **Exemplo:** uma pessoa, uma situação, números simples. O personagem é ilustrativo; o que o Horus faz nele está
> no inventário.

## ✨ Características

O coração da página: **como a mf é**. De seis a dez itens, cada um com um rótulo em negrito e uma frase simples.
Escolha os que valem para esta mf, por exemplo:

- **Onde aparece:** em que telas, canais ou momentos.
- **Quem usa:** quais papéis podem usar, e quem não pode.
- **O que oferece:** o que a pessoa consegue fazer com ela.
- **Como se comporta:** a regra que a pessoa precisa saber (o que fica guardado, o que se apaga, o que conta).
- **Quem configura:** quem liga, desliga ou ajusta, e onde.
- **Limites:** o teto, a regra de segurança, a dependência de fora.

## 📈 O valor que gera

- **Para quem usa:** o tempo ou a decisão que ela ganha.
- **Para a empresa que contrata o Horus:** o que melhora no negócio dela.
- **Para o Horus como produto:** adoção, receita, retenção ou custo de atender.

**Como vamos saber que funcionou:** o sinal que se observa, numa frase.

## 🚶 Como se usa no Horus

O fluxo desejado, do ponto de vista de quem usa: de quatro a sete passos, um por linha, verbo no presente. Se houver
quem configura e quem usa, um fluxo curto para cada.

```mermaid
flowchart LR
  a[Passo 1] --> b[Passo 2] --> c[Passo 3]
```

## 🧩 Grau de complexidade: média

Três frases curtas: o que já existe na v1 e se reaproveita, o que é novo, de quem mais depende.

> ⚠️ É a leitura do PO a partir dos documentos de arquitetura. A estimativa de esforço é do arquiteto.

## 🔗 Macro funcionalidades relacionadas

| mf | Como se relaciona |
| --- | --- |
| Nome (MF-000) | **depende de** / **é a base de** / **complementa**, e por quê, numa frase |

## 🚧 O que ela não faz

Até cinco itens: o que a mf **não** faz, para ninguém esperar o que não vem (e, quando houver, onde isso entra).

## ⏳ Ainda a decidir

No máximo três itens, uma linha cada, só o que muda o que a mf faz ou como ela é. O detalhe fica no inventário. Se
não houver, escreva "Nada a decidir."

## 📚 Para saber mais

Os trechos do inventário de onde esta página saiu. Aqui, e só aqui, entram os números das decisões (`D-nnn`,
`ARQ-nnn`) e das pendências (`P-nnn`).

<!--
O objetivo da página: o leitor entender O QUE A MF FAZ e QUAIS SÃO AS CARACTERÍSTICAS DELA. Tudo o que não serve a
isso sai, ou fica no inventário.

Régua do grau de complexidade (a mesma em todas as páginas):
  🟢 baixa — quase tudo já existe na v1 ou é um comportamento novo sobre peças prontas; nada externo novo.
  🟡 média — peças novas no sistema, sobre a base que existe; dependência externa simples ou nenhuma.
  🔴 alta  — mexe na base (dados, permissões, segurança), atravessa vários módulos ou depende de terceiros que o
             Horus não controla (a Meta no WhatsApp, o login corporativo de cada cliente).

Regras de escrita (as mesmas em todas as páginas):
  - De 600 a 900 palavras no corpo, sem contar tabela, diagrama e "Para saber mais".
  - Frases curtas, voz ativa, uma ideia por frase. Termo do Horus (owner da organização, membro leitor, fonte de
    dados, modelo semântico) explicado na primeira vez em que aparece.
  - Nenhum número de decisão nem de pendência no corpo: só em "Para saber mais" e no front-matter.
  - Nada de bastidor no corpo: nada de "o arquiteto achou viável", "o dono decidiu em tal data", nome de arquivo,
    número de linha de código. O leitor quer saber como a mf é, não como se chegou a ela.
  - A mf se cita pelo nome, com o código entre parênteses na primeira vez: "a Pergunta rápida (MF-110)".
  - Nada inventado: todo comportamento sai do inventário. O que o inventário não diz não vira texto; se mudar o que
    a mf faz, vai para "Ainda a decidir".
  - A decisão mais recente do dono vale sobre o texto antigo do inventário (por exemplo, a segurança dos dados por
    pessoa foi para a v2.1 em 03/11/2026); a página descreve o produto como ficou.
-->
