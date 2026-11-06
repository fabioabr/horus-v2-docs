---
# Identificação da arquitetura de uma macro funcionalidade (mf). Copie este arquivo, preencha e apague os comentários.
# Nome do arquivo: mf-nnn-nome-da-mf.md, na pasta docs/raw/arquitetura/mfs/.
codigo: MF-000
nome: Nome da mf, como está no mapa do 04
entrega: v2.0                  # v2.0 · v2.1 (uma mf pertence a uma versão só) · ou "sem versão"
modulo: Plataforma             # o módulo da tabela 3.6 do documento 04 (Plataforma, Motor, Canais…)
objetivos: [O1]                # os objetivos do 07 que ela cumpre
situacao: rascunho             # rascunho · em revisão (há 🟡 com o dono) · fechada
complexidade: média            # baixa · média · alta, a mesma régua das páginas de leitura; é a estimativa do arquiteto
pontos_de_ataque: [4, 5, 8]    # os números dos assuntos da seção 0 que pedem decisão nesta mf
adrs: [ADR-000]                # as decisões de arquitetura registradas na seção 15 (várias por mf)
leitura: docs/leitura/mfs/mf-000-nome.md   # a página de leitura da mf, que é do PO
atualizado: AAAA-MM-DD
---

# Arquitetura da MF-000 · Nome da mf

> **Em uma frase:** como o Horus entrega esta mf por dentro, dito para quem não é da área técnica. Termo técnico vem
> traduzido na primeira vez ("caixa de saída: um recado gravado junto com a mudança, para nenhum aviso se perder").

**Complexidade (estimativa do arquiteto):** baixa · média · alta, em três frases: o que já existe e se reaproveita, o
que é novo, de quem mais depende. A página de leitura da mf copia este grau.

**O que este documento decide e o que não decide.** Ele decide **componentes** (as peças, a responsabilidade de cada uma
e a tecnologia que a faz) e **conexões** (quem fala com quem, por qual contrato, de forma imediata ou em segundo plano,
e o que trafega, em categorias). Ele **não decide código**: nada de esquema de tabela, rota, assinatura, classe ou passo
de implementação. Teste de bolso: se o trecho puder ser copiado para um editor e compilado, está baixo demais.

## Os assuntos a atacar

Toda mf passa pelos mesmos assuntos, na mesma ordem. Cada um responde a uma pergunta e **não repete** o documento de
tema de onde vem: se o tema já decide, a seção diz "segue o padrão (`ARQ-nnn`)" e para. O que pede decisão nova entra na
seção 0. Assunto que não vale para a mf se escreve "Não se aplica:" com o motivo, nunca se omite.

| Nº | Assunto | A pergunta que ele responde | Documento de tema | Quando entra |
| --- | --- | --- | --- | --- |
| 1 | O que a mf precisa garantir | O que do produto esta arquitetura não pode deixar de cumprir? | 05, 07 e o backlog | Sempre |
| 2 | Fronteira e dependências | Onde a mf começa e termina, e de quem ela precisa? | 04 (§3.6), 07 | Sempre |
| 3 | Componentes, contratos e fluxos | Que componentes entregam a mf e como se conectam? | 04 | Sempre |
| 4 | Dados e história | O que se guarda, onde mora, de quem é, por quanto tempo e como se reconstrói? | 06 | Sempre |
| 5 | Segurança, acesso e privacidade | Quem pode o quê, em nome de quem, e o que vaza se der errado? | 07 | Sempre |
| 6 | Integrações de fora | Que serviço de terceiro a mf usa, e o que acontece quando ele falha? | 08 | Se usar |
| 7 | O motor e a IA | Como a pergunta vira resposta aqui, e quem paga o modelo? | 05 | Se usar o motor |
| 8 | Concorrência, falha e recuperação | O que acontece quando duas coisas ocorrem juntas, quando algo cai no meio e quando é preciso voltar? | 04, 06 | Sempre |
| 9 | Desempenho, volume e custo | Qual o tamanho, qual a meta e quanto custa por organização? | 03, 13 | Sempre |
| 10 | Observabilidade e avisos | Como saberemos que funciona, e quem é avisado quando para? | 11 | Sempre |
| 11 | Ambientes, publicação e versões | O que muda ao publicar, e vale igual no SaaS e no on-premises? | 09, 10 | Sempre |
| 12 | Testes e provas | O que prova que funciona, sem chamar modelo pago? | 12 | Sempre |
| 13 | A tela | O que o front precisa, em qualquer dispositivo? | 04 (§3.5) | Se tiver tela |
| 14 | O que vem da v1.xx | O que se reaproveita, o que se reescreve e o que se descarta? | 01 (§5), 04 (§4) | Sempre |
| 15 | Registro de decisão de arquitetura (ADR-xxx) | Que decisões de arquitetura esta mf toma, e por quê? São várias por mf | 02 (as `ARQ-nnn` gerais) | Sempre |
| 16 | Riscos, o que falta decidir e o que volta ao PO | O que pode dar errado e o que não é do arquiteto? | 01 (§7 e §9), 14 | Sempre |
| 17 | Marcos e anexos | O que fica de pé em cada marco e o que vem depois deste documento? | 01 (§6) | Sempre |

## 0. Pontos de ataque

De três a seis assuntos da lista acima que **pedem decisão nova** nesta mf (os outros seguem o padrão). Para cada um: o
que o torna difícil aqui e quem decide.

| Assunto (nº) | Por que pede decisão aqui | Quem decide |
| --- | --- | --- |
| 4 · Dados e história | Uma frase: o que nesta mf foge do padrão | Arquiteto · dono · PO |

## 1. O que a mf precisa garantir

Escreva: as **exigências** numeradas (E1, E2…), cada uma com a decisão de produto (`D-nnn`) ou o objetivo que a pede e,
quando tocar, o invariante do produto (confiança, "quem pergunta vê só o que pode ver", definição do negócio pela
empresa, white label, qualquer dispositivo). Não reescreva o produto: aponte para a página de leitura.

## 2. Fronteira e dependências

Escreva: o que está **dentro** e **fora** (como o PO fixou, citando a `D-nnn`); de que mfs **depende** e de quais **é a
base**, e o que uma exige da outra em contrato (nome e responsabilidade); o que parece desta mf e não é.

## 3. Componentes, contratos e fluxos

Escreva: o **módulo** e os **componentes**, com a responsabilidade de cada um numa linha; o **papel do executável** que
os roda (atender ou trabalhar); os **contratos** com os outros módulos, pelo nome e pela responsabilidade; e os **dois a
quatro fluxos** que mandam, passo a passo entre componentes (um diagrama de sequência, se ajudar). Só o módulo dono
escreve a sua tabela.

## 4. Dados e história

Escreva: as **categorias** de dado (não as tabelas); **onde mora** cada uma (banco mestre, banco da organização ou banco
de log); **de quem é** (o módulo dono); o **isolamento** entre organizações e o que a mf **nunca lê** (conteúdo); a
**retenção e a exclusão** (e a guarda legal que colide com elas); a **história** que precisa ser reconstruída numa data;
e o **dado pessoal**. O esquema de tabelas é o modelo de dados, que sai como anexo (seção 17).

## 5. Segurança, acesso e privacidade

Escreva: as **ações novas** na matriz de permissões, por papel e por tipo de assento; o **em nome de quem** cada ação
roda; os **dados pessoais** e o que a LGPD pede (o que depende do jurídico vira pendência); os **segredos** (quem
guarda, quem lê); o que entra no **rastro** e o que a **telemetria nunca carrega**; e o **abuso**: o que alguém
mal-intencionado tentaria (ler dado de outra organização, adivinhar um identificador, reaproveitar um convite).

## 6. Integrações de fora

Escreva, para cada serviço de terceiro (e-mail, Meta e WhatsApp, provedor de IA, fonte de dados do cliente, login
corporativo): o **contrato** (nome e responsabilidade), o **limite** do serviço, o que acontece na **falha**
(retentativa, quem é avisado), **de quem é a credencial** e o **custo**. Se a mf não usa serviço de fora, "Não se
aplica:" e o motivo.

## 7. O motor e a IA

Escreva, só para a mf que pergunta ao motor: o **nível de inferência**, o uso da **web**, o **modelo semântico**, a
**conexão de IA** de que a mf depende (da organização ou da instância) e quem paga, o **teto de tempo e de custo** por
execução, e o que o modelo **nunca recebe** (dado fora da permissão de quem perguntou).

## 8. Concorrência, falha e recuperação

Escreva: a **ordem das travas** quando duas pessoas mexem no mesmo dado; a **repetição segura** (o que acontece se a
fila entregar duas vezes); a **consistência entre bancos** (sem transação que atravessa dois bancos); o que **continua
funcionando** quando uma peça cai; como se **reprocessa** o que falhou; e como se **desfaz**.

## 9. Desempenho, volume e custo

Escreva: o **volume** esperado (por organização e por instância); a **meta de rapidez** (documento 03); o que é
**imediato** e o que vai para **segundo plano**; os **picos** e o **espalhamento** (um aviso que chega a todas as
pessoas); e o **custo por organização** (IA, WhatsApp, infraestrutura, armazenamento) e quem o paga.

## 10. Observabilidade e avisos

Escreva: o que a mf **mede** e **registra**; os **alertas** (plantão só para o que não pode esperar); **quem é avisado**
quando um serviço de que ela depende para (dono do serviço, administrador, autor); e o que a telemetria nunca leva.

## 11. Ambientes, publicação e versões

Escreva: a **migração** de esquema e de dados; os dados **semeados** (organizações de exemplo); a **configuração** que
muda por ambiente; se vale igual no **SaaS e no on-premises** e para **qualquer marca**; o que a mf **não pode quebrar**
ao publicar; e como se **volta** uma versão.

## 12. Testes e provas

Escreva: para cada exigência da seção 1, a **prova** que a cobre (unidade, integração com Postgres real, arquitetura,
corrida, ponta a ponta), tudo **sem chamar modelo pago**; o que só se prova em homologação; e o que fica **sem prova
automática**, com o motivo.

## 13. A tela

Escreva: as **páginas e os componentes** que a mf pede ao front; o **contrato com a API** (nome e responsabilidade, sem
rota nem campo); os **estados** vazio, de erro e de espera; e como se comporta em **computador, celular e tablet**.
Mudar um gesto ou o visual de algo que existe é decisão do dono.

## 14. O que vem da v1.xx

| Peça da v1.xx | Destino | Por quê |
| --- | --- | --- |
| `horus@318db52b:caminho` | ♻️ Fica · 🔧 Reescreve · ❌ Sai | A decisão ou a razão |

## 15. Registro de decisão de arquitetura (ADR-xxx)

Uma mf registra **várias** ADRs, uma por decisão. A ADR é a decisão de arquitetura **desta mf**: ela mora aqui, e fala
só de componentes e conexões, nunca de código. A decisão que vale para o sistema todo, ou para mais de uma mf, continua
sendo uma `ARQ-nnn` no registro geral (documento 02); a ADR a cita em "Aplica".

**Índice** (uma linha por ADR da mf):

| Nº | Decisão | Situação | Quem decide |
| --- | --- | --- | --- |
| `ADR-000` | Título curto | 🟡 · 🟢 · ✅ · ⚪ | Arquiteto · dono |

**Cada ADR, nesta forma:**

```markdown
### ADR-000 · Título curto: a decisão numa frase
Situação: 🟡 proposta ao dono | 🟢 decidida pelo arquiteto | ✅ confirmada pelo dono | ⚪ substituída por ADR-nnn · Data: dd/mm/aaaa · Alcance: MF-000
**Quem decide:** arquiteto (organização interna) | dono (infraestrutura, fornecedor, custo, segurança, retenção, ou o que muda o que alguém vê, faz, recebe ou paga)
**Contexto:** a exigência (E1…) e a `D-nnn` que forçam a decisão, em duas ou três frases.
**Decisão:** uma frase, em termos de componentes e conexões.
**Aplica:** as `ARQ-nnn` gerais em que ela se apoia.
**Alternativas:** as duas ou três melhores, com prós e contras; a escolhida primeiro.
**Por que esta:** o critério que decidiu e o que se abre mão.
**Consequências:** o que muda nos componentes e nas conexões desta mf e das outras.
**Reabrir quando:** a condição que justifica rever.
```

Regras: o número é fixo, de uma sequência única para todas as mfs (`ADR-001`, `ADR-002`…), e nunca se reaproveita; o
índice geral e o próximo número ficam em `mfs/README.md`. A ADR não se reescreve: a nova substitui a antiga, que passa a
⚪. Para saber de quem é, use o teste de bolso: se alguém de fora do time técnico perceberia a diferença, a decisão não é
só do arquiteto.

## 16. Riscos, o que falta decidir e o que volta ao PO

| Risco | Por quê | O que se faz |
| --- | --- | --- |
| Uma frase | A causa | A resposta |

**Fila do dono** (só o título): as ADRs 🟡 desta mf. **O que volta ao PO:** cada `P-nnn` ou `I-nnn` aberto no backlog
estratégico, com origem `ADR-nnn`.

## 17. Marcos e anexos

Escreva: o que fica **de pé** ao fim de cada marco que toca a mf, e do que ele depende (nunca a lista de tarefas).
Depois, os **anexos** que vêm depois deste documento, cada um com o seu link: o modelo de dados (MER), o contrato da API
e os diagramas de sequência. São artefatos de desenvolvimento, e não parte da arquitetura.

<!--
O objetivo do documento: o arquiteto, o dono e quem for construir saberem COMO a mf é entregue, no nível do componente,
da tecnologia, do padrão e do contrato, e o que ainda falta decidir. Nada de esquema de tabela, rota, assinatura de
código ou passo de implementação.

Regras (as mesmas em todos os documentos de mf):
  - A lista de assuntos é fixa, na mesma ordem. Assunto que não vale: "Não se aplica:" e o motivo. Nenhum some em
    silêncio.
  - A seção 0 nomeia de três a seis assuntos que pedem decisão. Mais de seis é sinal de que a mf está grande demais;
    volte ao PO.
  - Não repita o documento de tema. Se ele decide, escreva "segue o padrão (`ARQ-nnn`)". Repetir cria duas verdades.
  - Cada afirmação sobre o produto cita a `D-nnn`; cada decisão desta mf é uma `ADR-nnn` (seção 15) e cita as `ARQ-nnn`
    gerais em que se apoia. Confira os números contra o backlog e o registro antes de entregar, o número e o conteúdo.
  - Nunca altere uma `D-nnn`. Se a arquitetura não comporta uma decisão de produto, abra uma `P-nnn` ou um `I-nnn` no
    backlog estratégico e siga com o resto.
  - Quem decide: o que muda o que alguém vê, faz, recebe ou paga, infraestrutura, fornecedor, custo, segurança e
    retenção são do dono (🟡). A organização interna do sistema é do arquiteto (🟢).
  - Marcas: ✅ confirmada pelo dono · 🟢 decidida pelo arquiteto · 🟡 proposta ao dono · 🔎 hipótese · ⚪ substituída ·
    ♻️ fica · 🔧 reescreve · ❌ sai.
  - Código da v1.xx se cita como `horus@318db52b:<caminho>`.
  - Português do Brasil com acentuação. UTF-8, LF, sem BOM. Prosa a 120 colunas.

Pronto quando:
  [ ] os 17 assuntos estão preenchidos, com "segue o padrão" ou "Não se aplica:" onde couber;
  [ ] a seção 0 tem de três a seis pontos, cada um com quem decide;
  [ ] toda `D-nnn`, `ARQ-nnn` e `ADR-nnn` citadas foram conferidas;
  [ ] toda decisão desta mf é uma ADR no formato da seção 15, e toda 🟡 está na fila do dono;
  [ ] a decisão que vale para mais de uma mf subiu para o registro geral (02) como `ARQ-nnn`;
  [ ] o texto fala de componentes e conexões, sem código nem esquema;
  [ ] tudo o que é do produto virou `P-nnn` ou `I-nnn` no backlog;
  [ ] a complexidade do cabeçalho confere com a da página de leitura.
-->
