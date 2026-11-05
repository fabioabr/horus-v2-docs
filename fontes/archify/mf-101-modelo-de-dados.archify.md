# MF-101 · Administração da instância: o que o banco mestre guarda e onde cada dado mora {#mf-101-modelo-de-dados}

A MF-101 guarda **nove entidades no banco mestre** e nenhum conteúdo de organização. São a marca, os administradores, o registro das organizações, os assentos liberados, o aviso da instância e as cópias de ocupação e de uso, sempre em números.

- A Maind libera os assentos no mestre; a organização aplica o teto e é a verdade da ocupação (ARQ-088, D-076).
- Ocupação e uso diário são cópias agregadas, gravadas por um trabalho da fila, sem texto livre (D-091.1).
- O modelo não tem validade de assento, preço nem fatura (D-068, D-116).
- O dono respondeu as dúvidas de produto em 05/11/2026 (D-146 a D-152); restam duas perguntas pequenas desta modelagem, a Q13 e a Q14.

@answer scope="MF-101 · banco mestre · v2.0 · decisões de 05/11/2026"
@meta locale=pt-BR

## O que a MF-101 faz, e o que fica de fora? {#escopo}

| O que faz | Entrega | Decisão |
| --- | --- | --- |
| A marca: nome, logos claro e escuro e rodapé, válidos para todas as organizações | v2.0 | D-011 |
| Os administradores da instância, num papel só; só eles criam organizações | v2.0 | D-013, D-068.1, D-146, D-147 |
| O e-mail do produto: o ritmo de envio da instância | v2.0 | ARQ-046, D-128.3 |
| O painel de assentos: liberados e ocupados, por organização e por tipo | v2.0 | D-080, ARQ-017 |
| Liberar e cortar assentos, sem reduzir abaixo do ocupado e sem validade | v2.0 | D-067, D-068, D-075, D-076 |
| O uso e o custo de cada organização, em cards prontos e em um relatório para ver e baixar a qualquer momento | v2.0 | ARQ-017, ARQ-084, D-149, D-153 |
| O aviso de custo à Maind, com limiar por organização e sem corte | v2.0 | ARQ-017, ARQ-084 |
| O aviso da instância, escrito pelo administrador e mostrado na faixa de todas as pessoas | v2.0 | D-151, D-152 |
| A marca completa do contratante | v2.1 | D-121, ARQ-046 |
| O interruptor geral da segurança por pessoa | v2.1 | ARQ-090 |

@callout level=note title="Fora do modelo"
| Não entram no modelo: cobrar (preço, fatura e pagamento: D-116), consultar o rastro (MF-116) e escolher plano (há um só: D-115, D-117).
| Também ficam de fora os assentos on-premises (P-016, v2.1) e a faixa de avisos e números, com o aviso do owner da organização (MF-120).

## Onde cada dado da MF-101 mora? {#onde-mora}

A base se parte em duas (ARQ-010, ARQ-088). O **banco mestre** guarda o que é da instância ou cruza organizações; **um banco por organização** guarda tudo o que é dela. A MF-101 vive quase toda no mestre: o login lista as organizações de uma pessoa antes de abrir qualquer banco de organização.

@architecture id=onde-mora-dados title="Onde cada dado da MF-101 mora"
| painel | Painel da instância | frontend |
| api | API da plataforma | backend |
| mestre | Banco mestre | database |
| fila | Trabalho da fila | messagebus |
| banco-org | Banco da organização | database |
| painel > api | libera e edita |
| api > mestre | grava | emphasis |
| mestre > banco-org | copia o teto | dashed |
| banco-org > fila | ocupação e uso |
| fila > mestre | grava totais | emphasis |

@steps id=onde-mora-passos
| s-painel | Painel da instância | A Maind edita a marca, libera assentos e consulta o uso; nenhuma tela lê conteúdo de organização (D-091.1). | onde-mora-dados | painel |
| s-mestre | Banco mestre | Guarda o que cruza organizações: marca, administradores, registro das organizações, assentos liberados, ocupação, uso, limiares e o aviso da instância. | onde-mora-dados | mestre |
| s-banco-org | Banco da organização | É a verdade da ocupação e do consumo bruto, e confere a reserva do assento na própria transação. | onde-mora-dados | banco-org |
| s-fila | Trabalho da fila | Soma os bancos e grava só os totais no mestre; por isso ocupação e uso chegam atrasados e o painel mostra a hora da leitura. | onde-mora-dados | fila |

## Quais são as entidades e o que cada uma guarda? {#entidades}

| Entidade | O que guarda | Regra que a define |
| --- | --- | --- |
| `instancia` | Nome, rodapé, TTL do cache de prompt e envios de e-mail por minuto, numa linha só | A chave fixa impede uma segunda linha (I1); host e senha do SMTP ficam fora do banco (ARQ-044) |
| `imagem_de_marca` | O logo claro ou escuro da instância ou de uma organização | Um dono por vez; PNG, JPEG ou WebP de até 600 KB, nunca SVG (I10) |
| `administrador_da_instancia` | Quem administra a instância, quem concedeu e quando | A instância nunca fica sem administrador (I2); há um papel só (D-147); o owner de uma organização não vira administrador por isso (D-013) |
| `organizacao` | O registro no mestre: nome, slug, situação, responsável e o provisionamento do banco | Slug único e imutável (I3); só o administrador a cria (D-146); nasce em configuração, com 1 assento de owner (D-148, D-123) |
| `assento_liberado` | A quantidade liberada por organização e por tipo | Sem coluna de validade (D-068); só reduz até ocupados + reservados (D-076) |
| `ocupacao_de_assento` | Ocupados e reservados por tipo, e a hora da leitura | Cópia derivada: nenhuma tela escreve nela |
| `uso_diario_da_organizacao` | Quantidade e custo por dia e por medida | Só números, nunca conteúdo (I8); fica enquanto a organização existir (D-150) |
| `limiar_de_custo` | Os limites que avisam a Maind; a linha sem organização é o padrão | Coluna nula herda o padrão; avisa e nunca corta (ARQ-017) |
| `aviso_da_instancia` | O texto do aviso, a data e a hora a que ele se refere e a janela em que aparece | Só o administrador escreve (I14, D-151); o aviso do owner da organização é da MF-120 e mora no banco dela |

@callout level=note title="Só como referência"
| `pessoa` e `vinculo_pessoa_organizacao` são da MF-102 e aparecem no MER apenas para fechar as chaves. O mestre guarda o vínculo só para dizer que ele existe (ARQ-088).

## Como as entidades se relacionam? {#relacoes}

O MER completo, com todas as colunas, os tipos e a opcionalidade de cada ponta, está na página `mer-mf-101.html`, na mesma pasta desta. A tabela resume as cardinalidades que o desenho não mostra por extenso.

| Relação | Cardinalidade | O que ela garante |
| --- | --- | --- |
| `instancia` ou `organizacao` com `imagem_de_marca` | 1 para 0..2 | No máximo uma imagem por tema; cada imagem tem exatamente um dono |
| `organizacao` com `assento_liberado` | 1 para 4 | Uma linha por tipo; a criação já grava `owner = 1` |
| `organizacao` com `ocupacao_de_assento` | 1 para 4 | Cópia derivada, reescrita pelo trabalho da fila |
| `organizacao` com `uso_diario_da_organizacao` | 1 para N | Uma linha por dia e por medida |
| `organizacao` com `limiar_de_custo` | 1 para 0..1 | A exceção da organização; sem linha, vale o padrão da instância |
| `organizacao` com `pessoa` (responsável) | N para 0..1 | Nulo até o convite do responsável ser aceito |
| `aviso_da_instancia` com `pessoa` (quem escreveu) | N para 1 | Só uma pessoa administradora escreve (I14) |

## Como um assento é liberado, reduzido e cortado? {#assentos}

A Maind libera os assentos **tipo a tipo**, e a organização os ocupa. São quatro tipos: owner, gestor, membro full e membro leitor (D-069).

@facts
| Livres | liberados − ocupados − reservados; calculado, nunca gravado |
| Reserva | um convite aprovado e ainda pendente guarda o assento por N dias (D-071, D-078) |
| Quem acumula papéis | owner e gestor na mesma pessoa ocupam um assento só, o de owner (D-074) |
| Validade | não existe: nenhuma coluna de data de fim (D-068) |

Com 10 assentos liberados, 6 ocupados e 2 reservados, sobram 10 − 6 − 2 = 2 livres, e o menor valor que se pode liberar é 6 + 2 = 8. Os números são um exemplo, não dados de organização.

@steps id=reduzir-assento
| pedido | Pedir a redução | O administrador informa o tipo e a nova quantidade. |
| conferir | Conferir na organização | Sob trava, lê ocupados e reservados no banco da organização, que é a verdade; a cópia do mestre pode estar atrasada. |
| decidir | Recusar ou aceitar | Recusa a quantidade abaixo de ocupados + reservados; liberar mais é sempre permitido (D-076). |
| gravar | Gravar e copiar | Grava no mestre e copia o teto ao banco da organização, na mesma transação (ARQ-088). |

## Como uma organização nasce, é cortada e some? {#ciclo}

Duas colunas contam essa história: `banco_situacao`, que acompanha o provisionamento, e `situacao`, que o produto mostra. Criar a organização é um trabalho da fila, e não um passo instantâneo.

@workflow id=ciclo-da-organizacao title="Ciclo de uma organização"
| criar | Criar organização | frontend |
| pendente | Banco pendente | messagebus |
| pronto | Banco pronto | database |
| falhou | Banco falhou | external |
| config | Em configuração | backend |
| ativa | Ativa | backend |
| inativa | Inativa (corte) | security |
| removendo | Removendo | external |
| criar > pendente | |
| pendente > pronto | fila | emphasis |
| pendente > falhou | erro | dashed |
| pronto > config | |
| config > ativa | ativar |
| ativa > inativa | cortar | security |
| inativa > ativa | reativar |
| ativa > removendo | excluir |

@callout level=note title="Cortar não apaga nada"
| A situação `inativa` só muda `situacao`: não altera `assento_liberado`, os agentes pausam por evento e as rodadas perdidas não se refazem (D-075, I7). Reativar devolve tudo.
| Excluir apaga o banco, o login e as linhas da organização, nesta ordem: tira do mapa, apaga o banco, apaga o login (ARQ-037, I12). O uso dela some junto, e a Maind baixa o relatório da organização antes (D-149).

## O que o painel mostra de uso e quando a Maind é avisada? {#uso-e-custo}

O painel pede o mês; o aviso pede a semana e a execução. A menor granularidade útil é o dia, e o mês e a semana são soma.

| Medida | O que conta | Custo |
| --- | --- | --- |
| `pergunta-respondida` | Perguntas de análise respondidas | Sem custo atribuído |
| `execucao-de-agente` | Execuções de agente | Sem custo atribuído |
| `ia-conversa` | Chamadas de IA nas conversas | Em US$ |
| `ia-agente` | Chamadas de IA nas funções de agente | Em US$ |
| `whatsapp` | Mensagens enviadas | Em US$, pela conta da Maind |
| `email` | Envios | Nenhum: conta em número, não em dinheiro (ARQ-084) |

O custo fixo (máquinas, cópia e plantão) não entra (ARQ-084). Com 30 organizações, 6 medidas e 365 dias, são 30 × 6 × 365 = 65.700 linhas por ano, o que dispensa partição. O uso fica guardado **enquanto a organização existir**, sem prazo (D-150).

O administrador da instância vê e baixa um **relatório da organização** a qualquer momento (D-149). Ele só tem números e mostra os assentos como estão hoje, sem histórico mês a mês. O relatório sai destas mesmas tabelas e não pede tabela nova. Os números viram cards prontos da categoria Instance Cards (D-153, proposta); a montagem do painel é da MF-120.

| Sinal do aviso | Valor padrão proposto | Quando avisa |
| --- | --- | --- |
| Mês | US$ 30 por assento que pergunta | O custo do mês passa do limite; contam owner, gestor e membro full |
| Semana | Fator 2 e piso de US$ 20 | A semana passa do dobro da média das quatro anteriores e do piso |
| Execução | US$ 2 | Uma execução de agente passa do valor; é avaliada na origem, no fim da execução |

@callout level=open-question title="Valores a calibrar"
| Os valores do limiar são hipótese e se calibram com a primeira medição (documento 13, seção 3.12). Avisar não corta nada: quem decide é a Maind, caso a caso.

## Quais regras de integridade o modelo garante? {#integridade}

| # | Regra | Garantia |
| --- | --- | --- |
| I1 | Existe uma só `instancia` | Chave fixa |
| I2 | A instância nunca fica sem administrador | Transação com trava |
| I3 | `slug` único e imutável; `banco_identificador` único e opaco | Índice único e nenhum `UPDATE` do slug |
| I4 | Toda organização tem as 4 linhas de `assento_liberado` e `owner ≥ 1` desde a criação | Gravadas na mesma transação da organização |
| I5 | Reduzir nunca deixa a quantidade abaixo de ocupados + reservados | Conferido no banco da organização, sob trava (D-076) |
| I6 | Não existe validade de assento | Nenhuma coluna de data de fim (D-068) |
| I7 | Cortar não apaga, não altera `assento_liberado` e é reversível | Só muda `situacao`; agentes pausam por evento (D-075) |
| I8 | O mestre não tem conteúdo de organização | Nenhuma coluna de texto livre nas cópias; teste de arquitetura (ARQ-018) |
| I9 | Só o módulo dono escreve a sua tabela | A Plataforma escreve; a Fundação entra pela fachada (ARQ-018) |
| I10 | Imagem em PNG, JPEG ou WebP, até 600 KB, nunca SVG; uma por dono e tema | Validação na borda e índice único |
| I11 | Provisionar é idempotente e retomável | `banco_situacao` só avança de `pendente` para `pronto` ou `falhou` |
| I12 | Excluir apaga banco, login e linhas, nesta ordem | Exclusão com `banco_situacao = removendo` (ARQ-037) |
| I13 | Só o administrador da instância cria organizações | Permissão da Plataforma (D-146) |
| I14 | Só o administrador da instância escreve o aviso da instância | Permissão da Plataforma (D-151) |

## O que muda no backend de 05/11? {#backend}

O backend de organizações criado em 05/11 usa um banco só e assentos como um número. O modelo pede mais, e o maior desvio são os assentos.

| Hoje | No modelo | Impacto |
| --- | --- | --- |
| `Orgs.SeatsTotal`, um inteiro | `assento_liberado` por 4 tipos e `ocupacao_de_assento` | O maior desvio: tela e API falam de um número, a MF-101 fala de quatro tipos |
| Nome, logos e rodapé só no `localStorage` do front | `instancia` e `imagem_de_marca` | A tela de administração ainda não persiste no servidor |
| `Users.IsAdmin`, um booleano | `administrador_da_instancia` | Ganha origem: quem concedeu e quando |
| Logo na própria linha da organização | `imagem_de_marca` | Acaba a leitura dos bytes em toda listagem |
| `Orgs.Status` com `setup`, `active` e `inactive` | `organizacao.situacao` | Mesmo domínio; "em configuração" confirmada pelo dono (D-148) |
| `PrimaryOwnerUserId` | `responsavel_id` e o nome e e-mail indicados | O responsável pendente precisa de nome e e-mail no mestre |
| Um banco com `Orgs`, `OrgMembers` e `OrgInvites` | Mestre mais um banco por organização | Membros e convites migram para o banco da organização (ARQ-088) |
| Sem uso nem custo | `uso_diario_da_organizacao` e `limiar_de_custo` | Novo, e depende da fila da Fundação (ARQ-005) |
| Sem aviso da instância | `aviso_da_instancia` | Novo (D-151); a faixa que o mostra é da MF-120 |
| Já só o administrador cria organização | Igual (I13) | Já alinhado (D-146) |

## O que o dono decidiu e o que ainda falta? {#abertas}

O dono respondeu as dúvidas de produto em 05/11/2026 e elas estão no backlog estratégico. Restam duas perguntas pequenas desta modelagem e as propostas que aguardam a confirmação dele.

| # | Pergunta | Resposta | Registro |
| --- | --- | --- | --- |
| Q1 | O produto distingue owner da instância de administrador da instância? | Um papel só, `administrador`; "owner da instância" é o nome comercial; não há coluna `papel` | ✅ D-147 |
| Q2 | O relatório mostra o histórico dos assentos? | Não: só a situação de hoje; sem tabela de histórico | ✅ D-149 |
| Q3 | "Em configuração" é situação do produto? O corte é a organização `inativa` inteira? | Sim para as duas | ✅ D-148 |
| Q4 | `EmailContato` e `Copyright` da v1 seguem? | Não migram; `rodape` cobre o fecho | 🟡 D-156 |
| Q5 | Desempenho e envio de e-mail continuam na administração? | Sim, os dois parâmetros em `instancia` | 🟡 D-155 |
| Q6 | Quem cria organização no SaaS? | Só o administrador da instância (SaaS: a Maind; on-premises: o administrador do contratante) | ✅ D-146 |
| Q7 | Fuso do dia e retenção do uso diário | Dia em Brasília (técnico); fica enquanto a organização existir, sem prazo | ✅ D-150 |
| Q8 | O painel marca qual assento é o grátis? | Não: o produto só garante `owner ≥ 1` | 🟡 D-156 |
| Q9 | Excluir a organização apaga os totais de uso dela? | Apaga; a Maind tem um relatório da organização para ver e baixar a qualquer momento | ✅ D-149 |
| Q10 | A aparência do protótipo é da instância ou da pessoa? | Fora da v2.0 | 🟡 D-156 |
| Q11 | A administração publica um aviso a todas as pessoas? | Sim, na faixa contínua abaixo do cabeçalho, só pela faixa; tabela `aviso_da_instancia` | ✅ D-151 |
| Q12 | Como se conta "pergunta respondida"? | Como na medida de autonomia da MF-117 | 🟡 D-156 |
| Q13 | Quando o aviso sai da faixa: pelo horário (`exibir_ate`) ou quando o administrador o retira? | Aberta | ❓ dono |
| Q14 | Em que formato se baixa o relatório da organização: planilha, PDF ou os dois? | Aberta | ❓ dono |

@callout level=note title="O que é proposta desta modelagem"
| As colunas de `aviso_da_instancia` (`mensagem`, `ocorre_em`, `exibir_de`, `exibir_ate`) são proposta: a D-151 diz só "texto, data e hora". A Q13 e a Q14 mudam o que a pessoa vê ou baixa, por isso são do dono. Os cards de uso (D-153) são proposta do PO.

## Quais são os próximos passos até o EF Core? {#antes-do-ef}

@list id=proximos-passos ordered=true
| Responder a Q13 e a Q14 (o aviso sai pelo horário ou à mão; o formato do relatório).
| Confirmar com o dono as propostas D-153 a D-156.
| Planejar o retrabalho dos assentos: de um número para os quatro tipos (D-069, D-080).
| Só então separar mestre e organização no backend, trocar `SeatsTotal` por `assento_liberado` e criar `instancia`, `imagem_de_marca`, `administrador_da_instancia` e `aviso_da_instancia`.
