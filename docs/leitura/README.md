# Documentação de leitura do Horus v2

Esta pasta é a versão **para ler** da documentação do Horus v2: cada tema com começo, meio e fim, em linguagem
simples. O objetivo de cada página é um só: o leitor entender o que o Horus e cada macro funcionalidade (mf) fazem,
e quais são as características deles.

**Comece pela [visão geral](visao-geral.md)**: o que o Horus é, para quem, que problemas resolve, como funciona e as
19 mfs, cada uma com o link para a sua página.

| Pasta ou arquivo | O que tem |
| --- | --- |
| `visao-geral.md` | O Horus v2 do começo ao fim, em uma página |
| `mfs/` | Uma página por mf, no modelo de `mfs/_modelo.md` |

O inventário completo, com cada decisão, pendência e conferência, continua em `docs/raw/` (o produto, a
arquitetura e o backlog). Toda página daqui diz, em "Para saber mais", de que trechos do inventário saiu. Quando o
inventário muda, a página de leitura é reescrita a partir dele; ela nunca é a fonte de uma decisão (`D-144`). Quem
escreve e mantém estas páginas é a skill do PO (`product-owner-horus`), na seção "Documentação de leitura".

No portal da documentação (o site do repositório `horus-v2-docs`), a visão geral é a entrada de "Comece aqui", e o título de cada cartão
de mf abre a página de leitura dela; os links "Produto" e "Arquitetura" do cartão abrem tudo o que o inventário diz da
mf, assunto por assunto.
