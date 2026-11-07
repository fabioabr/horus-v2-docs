# Manual de geração do documento MF-xxx: o roteiro e a forma padrão

Situação: ✅ published · Data: 06/11/2026 · Vale para: as 23 mfs (19 da v2.0 e 4 da v2.1)

Um **documento MF-xxx** é a página que explica, em linguagem simples, o que uma macro funcionalidade (mf) faz: `MF-101`
é a página da Administração da instância. Este manual **registra, sem mudar**, o formato e as regras com que as 23
páginas que já existem foram escritas e aprovadas (o dono aprovou o formato nas MF-101 a MF-105 e mandou seguir).

**O objetivo deste manual** é ser duas coisas:
- o **roteiro** (roadmap): a ordem em que a documentação de produto é criada, atualizada e publicada, fase a fase e
  etapa a etapa, com o que sai de cada uma;
- a **forma padrão**: como cada página é, igual nas 23 mfs, para que dois autores que nunca se falaram entreguem páginas
  que parecem do mesmo autor.

| Parte | Seções | O que responde |
| --- | --- | --- |
| **1 · A forma padrão** | 1 a 6 | Como a página é: o leitor e o tom, o molde, os avisos, a marcação, o diagrama, a v2.1 |
| **2 · O roteiro** | 7 a 9 | Em que ordem se cria e se atualiza, quem faz cada etapa e o que sai dela |
| **3 · A régua** | 10 a 17 | As fontes, as regras de conteúdo, as conferências e as armadilhas que o roteiro consulta |

Quem for escrever uma página (uma pessoa ou um agente) lê este manual, o molde (`documentacao/content/mf-101.html`) e a
leitura da mf, e mais nada.

**Caminhos.** Os que começam por `docs/` ou `manuais/` são relativos à raiz do repositório `v2-docs`; os demais
(`content/`, `diagramas/`, `docx.json`, `README.md`) são relativos a `documentacao/`.

**Em uma frase:** a página conta o que a mf faz como se explicássemos a um possível cliente, sem tom comercial demais,
só com o que as decisões do dono dizem, com perguntas frequentes e, quando um fluxo ajuda, um diagrama.

---

# Parte 1 · A forma padrão

## 1. Para quem é a página, e como ela soa

- **O leitor** é uma pessoa que vai usar ou contratar o Horus e não conhece o jargão: um owner de organização, um
  gestor, o responsável de TI do cliente. A página **não** é comercial: não vende, não compara, não promete.
- **O tom:** frases curtas, voz ativa, uma ideia por frase. Começa por **uma imagem do dia a dia** (a Administração da
  instância é "a sala de controle de um prédio"), com personagens ilustrativos (Marcos, owner; Carla, gestora). A
  tecnologia entra **só o bastante para a história fazer sentido**, e nunca com nome de infraestrutura interna da Maind.
- **Cada termo do Horus** se explica na primeira vez. Os que se repetem vivem no glossário da página `como-ler`: não os
  redefina, aponte `href="#glossario"`.

## 2. O molde da página

O molde é `documentacao/content/mf-101.html`; os exemplos mais recentes são `mf-113.html` a `mf-120.html`. A ordem é
sempre esta:

1. **Abertura:** um ou dois parágrafos com a imagem do dia a dia e, logo depois, o aviso de versão (seção 3).
2. **O que é, em poucas palavras** (`mf-nnn-o-que-e`): a lista do que a mf faz e quem a usa.
3. **Como funciona na prática:** quem faz o quê, **passo a passo** (`ol.steps`), tabelas e o diagrama, quando houver.
4. **Nos bastidores, sem complicar** (`mf-nnn-bastidores`): a tecnologia, só para a história.
5. **O que ela não faz** (`mf-nnn-limites`) e **Funcionalidades ligadas a esta** (`h4` `mf-nnn-ligadas`), com os avisos
   que couberem ("Ainda em definição", "Na implantação").
6. **Perguntas frequentes** (`mf-nnn-faq`): sempre a última.

- **Tamanho:** de 170 a 230 linhas de HTML (linhas longas) para a mf bem definida; de 110 a 170 para a de definição
  ainda fina (como as MF-122 e 123). Proporcional ao que está decidido; sem encher linguiça.
- **Ids:** `h3` por assunto e `h4` por tópico, **todos** começando por `mf-nnn-` e **únicos no site inteiro**. O
  fragmento não tem `h1` nem `h2` (o gerador os põe) e começa em `h3`.
- **FAQ:** **seis** perguntas que um possível cliente realmente faria, resposta direta de duas a quatro frases, só com
  fatos das fontes. A primeira é `<details open>`.

## 3. Os avisos (callout)

Copie a marcação da página que já tem o aviso; o CSS depende da estrutura exata.

| Aviso | Quando | Tipo | Onde copiar |
| --- | --- | --- | --- |
| **Versão 2.0, em construção** | Toda página da v2.0, logo depois da abertura | `callout--info` | `mf-101.html` |
| **Versão 2.1, em construção** | Toda página da v2.1 (texto na seção 6) | `callout--info` | uma página da v2.1 |
| **Ainda em definição** | O que as fontes deixam em aberto e importa a um cliente, dito em linguagem de cliente | `callout--neutral` | `mf-104.html`, `mf-105.html` |
| **Na implantação** | Os dois pontos de dados pessoais (seção 11) | `callout--neutral` | `mf-102.html` |
| **Ponto de atenção** | Um risco prático que o leitor não pode perder | `callout--warning` | `mf-101.html` |

## 4. A marcação

- **Componente se copia, não se escreve de cabeça:** abra o molde, copie a marcação e troque só o texto. Os que a página
  usa: aviso (`callout`, com `ico` e um bloco de conteúdo), tabela (`table.t` dentro de `.table-wrap`, com linhas
  `class="zebra"`), passos (`ol.steps`), perguntas (`faq` com `<details>`) e selos (`badge`).
- **Negrito:** em parágrafos e listas, `<strong>`. O `<b>` só é título de aviso, e **nunca** dentro de `<li>`.
- **Selos:** o neutro é `<span class="badge">` (não existe `badge--neutral`); os outros são `--info`, `--success`,
  `--warning` e `--danger`.
- **Proibido no fragmento:** `html`, `head`, `body`, `h1`, `h2`, `script`, `style`, `link`, `form`, `iframe`, `object`,
  `embed`.
- **Links:** só para `id` que **existe hoje** em `content/*.html` (confira com `grep` antes) ou para uma página inteira
  (`#mf-101`). Qualquer outro `id` quebra a geração. Na dúvida, linke a página, e não o tópico. Mf sem página (ou sem
  `id` confirmado) aparece em texto simples, sem link.
- **Termos novos** que não estão no glossário: explique no próprio texto e **devolva-os** a quem integra; quem escreve a
  página não edita o `como-ler.html`.

## 5. O diagrama padrão

**No máximo um por página, e só se um desenho explicar melhor que o texto.** De ≤ 12 nós, só com o que as fontes
confirmam. Sem fluxo que o justifique, não se faz: as MF-110, 118, 120 e 123 não têm, de propósito.

- **Skills:** `archify` (o desenho e os gates) e `archify-maind` (a casca com abas, zoom pela roda do mouse e mãozinha).
  O DocX não desenha; **nunca** se improvisa um desenho nem um visualizador de SVG no lugar do Archify.
- **Arquivos:** a fonte é `diagramas/fontes/mf-nnn-<slug>.json`; o `finalize` grava
  `diagramas/fontes/mf-nnn-<slug>.archify.html` (artefato dos gates, que não entra na documentação); a casca vai para
  `diagramas/mf-nnn-<slug>.html`. Nunca o mesmo caminho na entrada e na saída da casca.

  ```bash
  node ~/.claude/skills/archify/bin/archify.mjs finalize workflow diagramas/fontes/mf-nnn-slug.json diagramas/fontes/mf-nnn-slug.archify.html --quality showcase --out-dir diagramas/fontes/mf-nnn-review-1 --json
  node ~/.claude/skills/archify-maind/scripts/skin.mjs --html diagramas/fontes/mf-nnn-slug.archify.html --spec diagramas/fontes/mf-nnn-slug.json --out diagramas/mf-nnn-slug.html
  ```

- **Lições:** (1) a linha de apoio **inteira** no `sublabel` (o Archify esconde o `tag` no zoom de leitura); (2) `cards`
  com dois ou três cartões curtos, para a aba Explicações não ficar vazia (cada item vira um tópico); (3) raias
  (`lanes`) quando quem age muda; (4) rótulos de aresta curtos, e desenho de três a quatro colunas, porque o largo
  demais reprova; (5) acentos corretos e legenda em português; (6) o `finalize` tem de sair com 0.
- 🪤 O Archify **trava a pasta `fontes/`** durante cada entrega. Com vários autores ao mesmo tempo, cada um usa
  `--out-dir diagramas/fontes/mf-nnn-review-N` (nunca reaproveite a pasta de recibos de outro diagrama); se falhar por
  pasta em uso, espere 30 segundos e repita sem contar como rodada de reparo.
- **No fragmento:** um parágrafo curto de apresentação e o marcador **vazio** `<dx-diagrama
  ref="mf-nnn-<slug>"></dx-diagrama>`. Declare-o em `diagrams` do `docx.json` (`id`, `title`, `description`, `source`).
- **Ao mudar a fonte** (o JSON), refaça o `finalize` e a casca. Editar a página de `diagramas/` se perde.

## 6. A versão 2.1

A v2.0 tem as 19 páginas (a da MF-121 passou da v2.1 para a v2.0 em 07/11/2026), e a v2.1 é a continuação delas. Para as 4 mfs da v2.1 (MF-106, 119, 122 e 123), valem
todas as regras deste manual **e mais estas**:

1. **O aviso de abertura** é este (mesma marcação do da v2.0): `<b>Versão 2.1, em construção</b>` — "O que está aqui é o
   que a versão 2.1 do Horus vai entregar, depois da 2.0. O produto ainda está sendo construído, e o texto é revisado
   conforme as decisões se fecham." Não fale de onda: a v2.1 tem 4 mfs, todas da antiga primeira onda, e a onda 2 ficou sem mfs (a MF-121 subiu para a v2.0). Sem datas.
2. **"Como é hoje" e "o que passa a existir".** A v2.0 é o ponto de partida: diga o que ela já faz sobre o assunto e o
   que a v2.1 acrescenta, sem contradizer as páginas da v2.0.
3. **Nome provisório.** As MF-122 e 123 têm nome provisório (a MF-120, da v2.0, também; a MF-121 tem o nome decidido, "Middleware da organização"): diga **uma vez**, perto do
   começo. Não invente outro.
4. **O que não se traduz para a página** (é conversa interna de produto): a "prova de valor", o "grau de complexidade" e
   o aviso "é a leitura do PO", as notas e pontuações de decisão, as hipóteses de negócio ("ajuda a reter o cliente",
   "ainda não há demanda conhecida") e a ordem entre mfs da equipe. O valor para quem usa e para a empresa entra **na
   história**, em linguagem de cliente. Se uma frase de valor depende de uma hipótese dessas, tire-a.
5. **Detalhe técnico em aberto** (o protocolo do middleware, a forma de integrar o Teams e o Google Chat, o dialeto do
   Athena, o desenho do motor da investigação): não se nomeia. Diga, em linguagem simples, que "a forma técnica ainda
   será definida".
6. **Selo:** `"badge":"v2.1"` no item da macro, no grupo **v2.1** do `docx.json`.

---

# Parte 2 · O roteiro

## 7. O roteiro em fases

Seis fases. As quatro primeiras já foram cumpridas; a quinta é publicação; a sexta é a rotina daqui para a frente.

| Fase | O que se fez ou se faz | O que sai | Andamento em 06/11/2026 |
| --- | --- | --- | --- |
| **1 · Molde** | Escreve-se **uma** página (a MF-101) até o dono aprovar o formato; depois as MF-102 a 105 o confirmam | O molde `mf-101.html`, este formato | ✅ Aprovado nas MF-101 a 105 |
| **2 · v2.0, em levas** | As outras mfs da v2.0, em levas de quatro a cinco, um agente por mf, com o molde pronto: MF-107 a 110; MF-111 a 115; MF-116, 117, 118 e 120 | As 19 páginas da v2.0 | ✅ 18 de 19 (a da MF-121 passou da v2.1 para a v2.0 e está reescrita, só no site local) |
| **3 · v2.1** | As 4 mfs da v2.1 (MF-106, 119, 122 e 123), com o adendo da seção 6 | As 4 páginas da v2.1 | ✅ 4 de 4 |
| **4 · Integração** | Quem integra atualiza `docx.json`, `README.md` e glossário uma vez por leva, gera, valida e olha | O site conferido | ✅ Cumprida a cada leva |
| **5 · Publicação** | **Só com ordem do dono** (seção 15): `gerar --saida ../docs`, commit nomeando os caminhos, push | O site no Pages | ✅ v2.0 em `11358d2` e v2.1 em `8ef9012`, ambos em 06/11/2026 |
| **6 · Rotina de atualização** | Sempre que uma decisão muda o que a mf faz (seção 8, rotina B) | A página em dia | ▶️ Contínua |

**Uma página nova** (uma mf que o produto crie) entra pela fase 2 ou 3, conforme a versão, e passa pela rotina A da
seção 8.

## 8. O roteiro de uma página

**Rotina A · Escrever uma página nova** (fases 1 a 3). Quem faz cada etapa: o autor (pessoa ou agente), exceto onde
dito.

| # | Etapa | O que se faz | O que sai |
| --- | --- | --- | --- |
| 1 | **Ler as fontes** | A leitura da mf, as decisões do backlog e do registro que ela cita, as páginas vizinhas (seção 10) | As afirmações que a página pode fazer, cada uma com sua fonte |
| 2 | **Escrever o fragmento** | Copia o molde e troca o texto, seguindo as seções 2 a 4 e as regras de conteúdo (seção 11). Abertura, aviso de versão, assuntos, bastidores, limites, ligadas e FAQ | `content/mf-nnn.html` |
| 3 | **Desenhar** (só se um fluxo justificar) | Segue a seção 5 | O JSON do Archify, a casca e a entrada de `diagrams` |
| 4 | **Validar numa cópia** | Cópia do `docx.json` e de `content/`, com a própria macro registrada; `gerar` e `validar` (seção 13) | O relatório de que a página gera sem erro |
| 5 | **Devolver** | Entrega, nesta ordem: caminhos e resultados; linhas da tabela de fontes do `README`; o item da macro; a entrada do diagrama; os termos novos; os pontos em aberto, as divergências e tudo que não saiu como pedido | O pacote de devolução |
| 6 | **Revisar** (quem integra) | Corta o que sobra (seção 9) e confere o texto contra as fontes | A página revisada |
| 7 | **Integrar** (quem integra) | Atualiza `docx.json`, `README.md` (fontes, pontos em aberto, divergências) e `como-ler.html`, e liga as menções "Nome (MF-nnn)" das outras páginas | Os arquivos compartilhados em dia |
| 8 | **Gerar, conferir e olhar** (quem integra) | `gerar`, `validar`, as conferências da seção 14 e o navegador | O site de teste conferido |
| 9 | **Entregar** | Links, lacunas e o aviso do logo/placeholder, se houver. **Não publica** | O dono vê |

**Rotina B · Atualizar uma página existente** (fase 6). Dispara quando uma decisão muda o que a mf faz ou como ela é:

1. O PO atualiza o inventário e a **leitura da mf** (a página nunca decide; a fonte vem antes).
2. O autor relê a fonte inteira (a leitura é editada por outras sessões) e **edita o fragmento**, não o site gerado.
3. Atualiza a tabela de fontes e os pontos em aberto do `README`, e o glossário, se houver termo novo.
4. Se o fluxo mudou, refaz o `finalize` e a casca do diagrama.
5. Gera, valida, confere e olha (etapas 4, 8 e 9 da rotina A).
6. Publica só com ordem do dono.

## 9. A produção em paralelo e a revisão

- **Um agente por mf**, sempre com `model:` explícito, e o **briefing num arquivo só** com o que vale para todos; cada
  agente recebe só os dados da própria mf.
- **O que cada agente escreve:** só o próprio `content/mf-nnn.html`, os arquivos do próprio diagrama e a própria pasta
  de trabalho. **Não edita** `docx.json`, `README.md`, `como-ler.html` nem a página de outra mf (dois agentes brigariam
  pelo mesmo arquivo).
- **A revisão de quem integra** corta o que sobra: frase derivada, número sem fonte, comparação inventada, exemplo com
  marca real, **recomendação própria do agente** ("vale conferir o modelo semântico"), "embutido no preço" fora da
  MF-103 e qualquer coisa que contradiga outra página.
- **Ordem das levas:** o molde primeiro; depois levas de quatro a cinco mfs. As páginas que tocam dados pessoais (a
  MF-116, por exemplo) levam o aviso "Na implantação".

---

# Parte 3 · A régua

## 10. A fonte e a cadeia de verdade

A página **nunca decide**: ela sai de documentos do repositório, nesta ordem de força:

1. **As decisões do dono** em `docs/raw/produto/backlog-estrategico.md` (cada uma é uma seção `### D-nnn · título`).
2. **O registro de arquitetura** em `docs/raw/arquitetura/02-registro-de-decisoes.md` (`### ARQ-nnn`).
3. **A leitura do PO** em `docs/leitura/mfs/mf-nnn-*.md`: o texto de partida de cada página.
4. Se precisar: `05-v2.0-consolidada.md`, `06-versoes.md`, `07-mapa-de-objetivos-e-funcionalidades.md` e, em
   `docs/raw/arquitetura/`, os documentos 04, 05, 06, 07 e 08.

- **Só se lê esses arquivos; nunca se escreve neles.** A leitura está sendo editada por outra sessão: releia a fonte no
  momento de escrever.
- **Se duas fontes divergem,** vale a mais recente e específica (decisão do backlog > leitura). **Reporte a
  divergência**; o inventário se corrige na pendência `P-028`, e não na página.
- **Se a mf está "só no mapa",** a definição é mais fina: escreva só o que está decidido e declare o resto.

## 11. As regras de conteúdo (duras)

- **Só afirme o que as fontes dizem.** Regra em aberto não se inventa: vira o aviso "Ainda em definição" (seção 3), em
  linguagem de cliente, ou se omite quando for puramente técnica.
- **Nenhuma frase derivada.** Se a afirmação é conclusão sua (não está numa decisão nem na leitura), reescreva para o
  que está escrito ou tire. Nada de número, prazo, valor ou comparação sem fonte ("minutos contra dias", "em centavos").
- **Números de exemplo são ilustrativos** ("X%", "valor ilustrativo"). **Nunca** o nome de uma instituição real (um
  banco, um órgão público, um concorrente) junto de um número inventado. Marcas reais só quando são o próprio assunto
  (por exemplo, o Microsoft Teams na MF-122); no mais, "rede de lojas", "frota".
- **Sem códigos no texto:** `D-nnn`, `ARQ-nnn`, `P-nnn`, `I-nnn` e `A-nn` ficam **só** na tabela de fontes do
  `README.md`. Outra mf pode aparecer como "(MF-106)".
- **Nada de preço, margem nem composição de preço.** Pode dizer **quem** paga o quê, não **quanto**. Não diga que algo
  está "embutido no preço": isso fica só na MF-103.
- **Versão:** diga com clareza o que é da v2.0, o que é da v2.1 e o que está sem versão, quando a fonte disser.
- **Não repita o que outra página já explica** (assentos, IA da instância, avisos, convites, roles, fontes, modelos):
  aponte por link e acrescente só o que é novo da mf. Leia o que as páginas vizinhas dizem (`grep -n "MF-nnn"
  content/*.html`) e **não as contradiga**.
- **Dados pessoais (decisão do dono, `D-247`).** Se a página tocar em um destes dois pontos, a regra fica **como
  decidida** e entra o aviso "Na implantação": (1) o owner da organização lê as conversas de todos, sem aviso especial à
  pessoa; (2) quem é excluído tem os registros apagados junto. (O terceiro ponto, a Maind ver o nome de quem ocupa cada
  assento, saiu em 07/11/2026: a `D-274` tirou o nome do relatório.) **Não**
  escreva "o jurídico ainda confirma".
- **Convite do gestor (`D-248`).** O owner pode ligar, nas preferências da organização, a aprovação automática dos
  convites. Não diga como ela nasce.

## 12. Onde moram os arquivos e o que acompanha cada página

```
documentacao/
├── docx.json                ← a configuração: a entrada, as macros por versão, as seções e os diagramas
├── content/                 ← os fragmentos HTML, que são a fonte editável
│   ├── como-ler.html        ← o que é uma mf, como a página é organizada, o glossário
│   └── mf-101.html … mf-123.html   ← uma página por mf (v2.0 e v2.1)
├── diagramas/               ← a casca de cada diagrama; fontes/ guarda o JSON do Archify e os arquivos dos gates
├── README.md                ← a tabela de fontes de cada página, os pontos em aberto e as divergências
└── .gitignore               ← site/, *.archify.html e os recibos dos gates
```

A saída que o GitHub Pages serve é `../docs` (gerada, não se edita à mão). A marca vem de
`.claude/plugins-data/kbr-docs/docs-brand.yml`, na raiz do repositório.

A página não vive sozinha. Quem integra atualiza, **uma vez**, os arquivos compartilhados:

| Arquivo | O que entra |
| --- | --- |
| `docx.json`, `portal.macros` | O item da mf: `id`, `source`, `code`, `badge`, `title`, `summary` (uma frase) e, no máximo, dois `links` |
| `docx.json`, `diagrams` | A entrada do diagrama, se houver |
| `README.md`, "De onde veio o conteúdo" | A tabela da mf: `Assunto da página \| Fonte` (os `D-` e `ARQ-` e os arquivos); é onde os códigos moram |
| `README.md`, "Pontos em aberto" | Uma linha com o que a página declara como "Ainda em definição" |
| `README.md`, "Divergências nas fontes" | O que as fontes dizem de forma desencontrada, para a `P-028` |
| `content/como-ler.html` | Os termos novos do glossário |
| As páginas que citam a mf | O texto simples "Nome (MF-nnn)" vira link quando a página nova existe |

**Item da macro** (exemplo): `{"id":"mf-107","source":"content/mf-107.html","code":"MF-107","badge":"v2.0","title":"…",
"summary":"uma frase","links":[{"label":"…","href":"#mf-107-…"},{"label":"Perguntas frequentes","href":"#mf-107-faq"}]}`

## 13. Gerar e validar

Da pasta `documentacao/`, com o plugin DocX (`docx@maindtech`, 0.4.0 ou superior):

```bash
python "<plugin docx>/scripts/docx.py" gerar --config docx.json                  # teste, em site/ (o git ignora)
python "<plugin docx>/scripts/docx.py" validar --site site
python "<plugin docx>/scripts/docx.py" gerar --config docx.json --saida ../docs   # publicação (só com ordem do dono)
python "<plugin docx>/scripts/docx.py" validar --site ../docs
```

- Para **isolar a marca** de qualquer configuração do usuário, aponte `CLAUDE_USER_HOME` para uma pasta vazia.
- O gerador valida links e ids antes de gravar. Saída com edição manual é recusada (não apague o manifesto para
  contornar).
- Quem escreve **uma** página sem tocar nos arquivos compartilhados valida numa **cópia** do `docx.json` e do
  `content/`, registrando ali a própria macro e o próprio diagrama. O aviso de logo/placeholder da cópia é esperado. Se
  a validação reclamar de âncora de uma página que ainda não existe, registre uma página provisória na cópia ou tire o
  link.

## 14. As conferências antes de entregar

**Automáticas:**
1. `validar` com saída 0; ids únicos; nenhum link quebrado.
2. **Sem código no texto:** nenhum `D-nnn`, `ARQ-nnn`, `P-nnn`, `I-nnn` nem `A-nn` fora do `README.md`.
3. Nenhum `<b>` dentro de `<li>`; nenhum `badge--neutral`; nenhum `h1`/`h2` no fragmento.
4. **Seis** perguntas no FAQ, a primeira aberta.
5. Nenhuma palavra de preço ("embutido no preço", valores em reais) e nenhum nome de instituição real ao lado de número.
6. Nenhum estouro horizontal no celular; a busca acha texto de outras páginas.
7. O aviso "Na implantação" está nas páginas que tocam os dois pontos de dados pessoais (hoje: MF-102, 107, 110,
   111, 116 e 117).

**Visuais:** abra por HTTP local (o Playwright não abre `file:`) e veja desktop e celular, os temas claro e escuro, a
busca, o menu e a impressão. **Em cada diagrama:** clique numa caixa, use a roda do mouse e abra "Tela cheia". 🪤 O
Archify vive em iframe aninhado: para provar que o desenho carregou, conte o `svg` no quadro **neto**.

**De conteúdo:** um link válido não prova que a afirmação é verdadeira. Releia cada afirmação contra a decisão que a
sustenta.

## 15. Publicação e armadilhas

- **Gerar não é publicar.** Publicar só quando o dono mandar, com `--saida ../docs`, que **substitui o site** do Pages.
  O repositório é **público**: antes, varra o que vai subir (caminho local, segredo, e-mail, IP). Commit **nomeando os
  caminhos**, conferido com `git status --short`; nunca `git add -A`.
- 🪤 **Não rode `ferramentas/montar_fontes.py`** nem o `fontes/` antigo com `--saida docs`: recriam o portal antigo por
  cima.
- 🪤 O DocX 0.4.0 põe um "v" na frente de `project.version`: escreva "2.0 e 2.1 em desenho", sem "v" na frente do número.
- 🪤 O `descobrir.py` do `kbr-docs` sugere o nome da **pasta** como nome do projeto e "uso interno" no rodapé: corrija à
  mão no `docs-brand.yml`.
- 🪤 Uma falha `requestfailed` de `media/diagramas/*.html?embutido=1` no teste de celular é o quadro abortado pela
  navegação do próprio teste, e não um defeito.
- 🪤 `site/`, os `*.archify.html` e as pastas `*-review-*` ficam fora do git (`.gitignore`).

## 16. Pronto quando

- [ ] a página segue o molde (abertura, aviso de versão, assuntos, bastidores, limites, ligadas, FAQ) e o tamanho da
  seção 2;
- [ ] cada afirmação tem fonte, e nenhum código de decisão, preço ou marca real ao lado de número aparece no texto;
- [ ] o aviso "Ainda em definição" e o "Na implantação" estão onde as fontes pedem;
- [ ] são seis perguntas no FAQ, e todos os links apontam para ids que existem;
- [ ] o diagrama, se houver, passou no `finalize` e abre em tela cheia; se não houver, o relatório diz por quê;
- [ ] o `docx.json`, o `README.md` (fontes, pontos em aberto, divergências) e o glossário foram atualizados;
- [ ] a página foi gerada, validada e aberta no navegador;
- [ ] nada foi commitado nem publicado sem ordem do dono.

## 17. O manual irmão

Cada mf tem **dois** documentos, e cada um tem o seu manual: o **MF-xxx** (a explicação do produto), que é o deste
arquivo, e o **ARQ-xxx** (a arquitetura, para o time técnico), que tem o [manual dos documentos
ARQ-xxx](manual-geracao-doc-arq.md). Os dois são sites separados e têm regras de escrita diferentes: aqui **não entram**
códigos de decisão, e lá eles são obrigatórios. **Não copie uma regra de um para o outro.**
