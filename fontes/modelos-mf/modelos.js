/* Propostas locais: todos os destinos vêm do índice real da MF-102. */
(() => {
  'use strict';
  const topics = window.HORUS_MF_102;
  const models = {
    cartoes: '01 · Cartões — assuntos em destaque e todas as referências visíveis, agrupadas por origem.',
    compacto: '02 · Compacto — atalhos menores e grupos de referências que você abre quando precisar.',
    contextual: '03 · Contextual — selecione um assunto para ver suas fontes logo abaixo.',
    lateral: '04 · Menu lateral — assuntos à esquerda, resumo à direita e referências abaixo do conjunto.'
  };
  const params = new URLSearchParams(location.search);
  let currentModel = Object.hasOwn(models, params.get('modelo')) ? params.get('modelo') : 'cartoes';
  let selectedTopic = 0;
  const content = document.getElementById('model-content');
  const preview = document.getElementById('preview');
  const total = topics.reduce((sum, topic) => sum + topic.sources.length, 0);
  const icon = name => `<i class="fas fa-${name}" aria-hidden="true"></i>`;
  const escape = value => String(value).replace(/[&<>"']/g, char => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[char]));
  const destination = hash => `../site/mf-102.html${hash}`;
  const link = (href, label, className = '') => `<a class="${className}" href="${escape(href)}" target="_blank" rel="noopener">${label}</a>`;
  const countText = topic => topic.sources.length ? `${topic.sources.length} ${topic.sources.length === 1 ? 'referência' : 'referências'}` : 'Outras citações';
  const sourceLink = source => link(destination(source.href), `<span>${escape(source.label)}</span>${icon('arrow-up')}`, 'source-link');
  const empty = '<p class="empty-sources">Nenhuma referência listada no índice.</p>';
  const sourcesHeading = () => `<div class="sources-heading"><div><div class="sources-title">${icon('link')}<h3>De onde vem</h3></div><p class="sources-subtitle">Referências que fundamentam esta funcionalidade</p></div><span class="source-count">${total} referências</span></div>`;
  const sourceCards = () => `<div class="sources-grid">${topics.map(topic => `<section class="source-card"><h4 class="source-card-head">${icon(topic.icon)}<span>${escape(topic.label)}</span><small>${topic.sources.length || '—'}</small></h4>${topic.sources.length ? topic.sources.map(sourceLink).join('') : empty}</section>`).join('')}</div>`;
  const readingPreview = () => `<section class="reading-preview"><h3>O que é</h3><h4>Definição macro · D-114</h4><p class="reading-source">No ${link('../site/produto-backlog.html#d-114', 'Backlog estratégico, D-114')}:</p><p>O owner liga e desliga, por role, tudo o que a conversa oferece, botão a botão. O que a pessoa vê dos dados continua com a MF-106: Segurança dos dados por pessoa.</p>${link(destination(topics[0].href), `Continuar a leitura ${icon('arrow-right')}`, 'read-link')}</section>`;
  function navTiles() {
    return `<div class="section-label"><h3>Explore os assuntos</h3><span class="section-count">8 seções</span></div><nav class="nav-grid" aria-label="Assuntos desta página">${topics.map(topic => link(destination(topic.href), `<span class="topic-symbol">${icon(topic.icon)}</span><span class="topic-copy"><strong>${escape(topic.label)}</strong><small>${countText(topic)}</small></span>${icon('arrow-right')}`, 'topic-tile')).join('')}</nav>`;
  }
  function compact() {
    return `<div class="section-label"><h3>Navegue pelo conteúdo</h3></div><nav class="compact-nav" aria-label="Assuntos desta página">${topics.map(topic => link(destination(topic.href), `${icon(topic.icon)}<span>${escape(topic.label)}</span>`, 'compact-link')).join('')}</nav><section class="compact-sources">${sourcesHeading()}<div class="accordion-list">${topics.map((topic, index) => `<details class="source-accordion"${index === 0 ? ' open' : ''}><summary>${icon(topic.icon)}<span>${escape(topic.label)}</span><small>${topic.sources.length}</small>${icon('chevron-down')}</summary><div class="accordion-links">${topic.sources.length ? topic.sources.map(sourceLink).join('') : empty}</div></details>`).join('')}</div></section>${readingPreview()}`;
  }
  function selector(lateral = false) {
    return `<div class="${lateral ? 'lateral-nav' : 'context-nav'}" role="tablist" aria-label="Selecionar assunto"${lateral ? ' aria-orientation="vertical"' : ''}>${lateral ? '<h3>Nesta página</h3>' : ''}${topics.map((topic, index) => `<button class="${lateral ? 'lateral-tab' : 'context-tab'}" id="topic-${index}" role="tab" type="button" aria-selected="${index === selectedTopic}" aria-controls="topic-panel" tabindex="${index === selectedTopic ? '0' : '-1'}" data-topic="${index}">${icon(topic.icon)}<span>${escape(topic.label)}</span><small>${topic.sources.length || '—'}</small></button>`).join('')}</div>`;
  }
  function contextualPanel() {
    const topic = topics[selectedTopic];
    return `<section class="context-panel" role="tabpanel" id="topic-panel" aria-labelledby="topic-${selectedTopic}"><div class="context-panel-top"><div><span class="context-kicker">DE ONDE VEM</span><h3>${escape(topic.label)}</h3></div>${link(destination(topic.href), `Ler este assunto ${icon('arrow-right')}`, 'section-button')}</div><div class="context-list">${topic.sources.length ? topic.sources.map(source => link(destination(source.href), `<span class="source-file-icon">${icon('file-alt')}</span><span><strong>${escape(source.label)}</strong><small>${escape(topic.label)} · MF-102</small></span>${icon('arrow-right')}`, 'context-source')).join('') : empty}</div><p class="context-foot">${countText(topic)} neste assunto · ${total} referências na página</p></section>`;
  }
  function lateralPanel() {
    const topic = topics[selectedTopic];
    return `<section class="lateral-article" role="tabpanel" id="topic-panel" aria-labelledby="topic-${selectedTopic}"><p class="eyebrow">MF-102 / ${String(selectedTopic + 1).padStart(2, '0')}</p><h3>${escape(topic.label)}</h3><p>${escape(topic.summary)}</p>${link(destination(topic.href), `Abrir seção completa ${icon('arrow-right')}`, 'section-button')}<p class="selection-meta">${icon('link')}<span>${countText(topic)}${topic.sources.length ? ' neste assunto. As fontes estão reunidas abaixo.' : '. Consulte a seção completa na documentação.'}</span></p></section>`;
  }
  function selectTopic(index, focus = false) {
    selectedTopic = index;
    document.querySelectorAll('[data-topic]').forEach(button => {
      const selected = Number(button.dataset.topic) === selectedTopic;
      button.setAttribute('aria-selected', String(selected));
      button.tabIndex = selected ? 0 : -1;
    });
    document.getElementById('topic-panel').outerHTML = currentModel === 'lateral' ? lateralPanel() : contextualPanel();
    if (focus) document.getElementById(`topic-${selectedTopic}`).focus();
  }
  function renderModel() {
    document.querySelectorAll('[data-model]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.model === currentModel)));
    document.getElementById('model-description').textContent = models[currentModel];
    document.getElementById('isolated-link').href = `?modelo=${currentModel}&isolado=1`;
    if (currentModel === 'cartoes') content.innerHTML = `${navTiles()}<section class="sources-section">${sourcesHeading()}${sourceCards()}</section>${readingPreview()}`;
    if (currentModel === 'compacto') content.innerHTML = compact();
    if (currentModel === 'contextual') content.innerHTML = `<div class="section-label"><h3>Explore por assunto</h3><span class="section-count">Selecione para ver as fontes</span></div>${selector()}${contextualPanel()}${readingPreview()}`;
    if (currentModel === 'lateral') content.innerHTML = `<div class="lateral-layout">${selector(true)}${lateralPanel()}</div><section class="sources-section lateral-sources">${sourcesHeading()}${sourceCards()}</section>`;
    const url = new URL(location.href);
    url.searchParams.set('modelo', currentModel);
    try { history.replaceState(null, '', url); } catch (_) { /* A prévia também funciona em navegadores com file: restrito. */ }
  }
  document.querySelectorAll('[data-model]').forEach(button => button.addEventListener('click', () => { currentModel = button.dataset.model; renderModel(); }));
  document.querySelectorAll('[data-size]').forEach(button => {
    if (button.tagName !== 'BUTTON') return;
    button.addEventListener('click', () => {
      preview.dataset.size = button.dataset.size;
      document.querySelectorAll('button[data-size]').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    });
  });
  content.addEventListener('click', event => {
    const button = event.target.closest('[data-topic]');
    if (button) selectTopic(Number(button.dataset.topic));
  });
  content.addEventListener('keydown', event => {
    const button = event.target.closest('[data-topic]');
    if (!button) return;
    let index = Number(button.dataset.topic);
    if (['ArrowRight', 'ArrowDown'].includes(event.key)) index = (index + 1) % topics.length;
    else if (['ArrowLeft', 'ArrowUp'].includes(event.key)) index = (index - 1 + topics.length) % topics.length;
    else if (event.key === 'Home') index = 0;
    else if (event.key === 'End') index = topics.length - 1;
    else return;
    event.preventDefault();
    selectTopic(index, true);
  });
  if (params.get('isolado') === '1') document.body.classList.add('isolated');
  renderModel();
})();
