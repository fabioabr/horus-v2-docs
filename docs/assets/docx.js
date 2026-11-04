/* DocX · o que é do DocX sobre o KbDoc: a busca pelo índice embutido, o atalho "/", a memória do tema e o imprimir. */
(() => {
  'use strict';
  const normalize = value => String(value).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  function search(items, query) {
    const words = normalize(query).trim().split(/\s+/).filter(Boolean);
    if (!words.length) return [];
    return items.map(item => {
      const title = normalize(item.title);
      const text = normalize(`${item.title} ${item.summary} ${item.text}`);
      return { item, score: words.every(word => text.includes(word)) ? 1 + words.filter(word => title.includes(word)).length * 5 : 0 };
    }).filter(result => result.score).sort((a, b) => b.score - a.score).map(result => result.item);
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = { normalize, search };
  if (typeof document === 'undefined') return;
  const $ = (selector, parent = document) => parent.querySelector(selector);
  const $$ = (selector, parent = document) => [...parent.querySelectorAll(selector)];

  /* Busca: o mesmo índice em todas as páginas (assets/busca.js); até 20 resultados, com teclado. */
  const input = $('[data-search-input]');
  const results = $('[data-search-results]');
  const status = $('[data-search-status]');
  const index = Array.isArray(window.DX_BUSCA) ? window.DX_BUSCA : null;
  if (input && results && index) {
    const close = () => { results.hidden = true; };
    const render = () => {
      const query = input.value.trim();
      const matches = search(index, query);
      results.replaceChildren();
      results.hidden = !query;
      if (!query) { if (status) status.textContent = ''; return; }
      if (status) status.textContent = `${matches.length} ${matches.length === 1 ? 'resultado' : 'resultados'}.`;
      const count = document.createElement('p');
      count.className = 'dx-search-count';
      count.textContent = matches.length ? `${matches.length} ${matches.length === 1 ? 'resultado' : 'resultados'}` : 'Nenhum resultado. Tente outro termo.';
      results.append(count);
      matches.slice(0, 20).forEach(item => {
        const link = document.createElement('a');
        link.href = item.url;
        const icon = document.createElement('i');
        icon.className = 'icon_document_alt';
        icon.setAttribute('aria-hidden', 'true');
        const text = document.createElement('span');
        const title = document.createElement('strong');
        title.textContent = item.title;
        const summary = document.createElement('small');
        summary.textContent = item.summary;
        text.append(title, summary);
        link.append(icon, text);
        results.append(link);
      });
    };
    input.addEventListener('input', render);
    input.addEventListener('focus', () => { if (input.value.trim()) render(); });
    input.addEventListener('keydown', event => {
      if (event.key === 'Escape') { close(); return; }
      if (event.key === 'ArrowDown' && $('a', results)) { event.preventDefault(); $('a', results).focus(); }
    });
    results.addEventListener('keydown', event => {
      const links = $$('a', results);
      const current = links.indexOf(document.activeElement);
      if (event.key === 'Escape') { close(); input.focus(); }
      if (['ArrowDown', 'ArrowUp'].includes(event.key)) {
        event.preventDefault();
        const next = current + (event.key === 'ArrowDown' ? 1 : -1);
        if (next < 0) input.focus(); else links[Math.min(next, links.length - 1)]?.focus();
      }
    });
    results.addEventListener('click', event => { if (event.target.closest('a')) close(); });
    const form = input.closest('form');
    if (form) form.addEventListener('submit', event => {
      event.preventDefault();
      const first = $('a', results);
      if (first) first.click(); else render();
    });
    document.addEventListener('click', event => { if (!event.target.closest('[data-search-form]')) close(); });
    document.addEventListener('keydown', event => {
      const typing = /^(input|textarea|select)$/i.test(document.activeElement?.tagName || '') || document.activeElement?.isContentEditable;
      if (event.key === '/' && !typing) { event.preventDefault(); input.focus(); }
    });
  }

  /* Menu lateral: o body do Onepage prende o scrollspy do Bootstrap à barra do topo (data-target=".navbar"), e o menu
     de tópicos nunca acende. Criado aqui, antes do onpage-menu.js e do data-api, ele acompanha o menu, descontando a
     barra fixa. */
  if ($('.doc-sidebar') && window.jQuery && window.jQuery.fn.scrollspy) {
    const bar = $('.menu_one');
    window.jQuery(document.body).scrollspy({ target: '.doc-sidebar', offset: (bar ? bar.offsetHeight : 0) + 30 });
  }

  /* Tema: o KbDoc guarda a escolha num cookie, que o navegador não grava em file://; o DocX guarda no localStorage. */
  const switcher = $('#something');
  if (switcher) {
    let saved = null;
    try { saved = localStorage.getItem('docx-theme'); } catch (_) { /* Sem armazenamento, vale a escolha do KbDoc. */ }
    if (saved === 'dark' || saved === 'light') {
      document.body.classList.toggle('body_dark', saved === 'dark');
      switcher.checked = saved === 'dark';
    }
    switcher.addEventListener('change', () => {
      try { localStorage.setItem('docx-theme', switcher.checked ? 'dark' : 'light'); } catch (_) { /* O tema vale nesta página. */ }
    });
  }

  /* Imprimir: um botão, e não um link javascript:. */
  $$('[data-print]').forEach(button => button.addEventListener('click', () => window.print()));
})();
