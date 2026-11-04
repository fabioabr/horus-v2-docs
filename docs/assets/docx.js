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

  /* O painel do menu rola por conta própria: quando o scrollspy muda o tópico ativo, a lista leva o item à vista, sem mexer
     na rolagem da página (por isso não é scrollIntoView). */
  const rolagem = $('.dx-menu-rolagem');
  if (rolagem) {
    let agendado = false;
    const mostrarAtivo = () => {
      agendado = false;
      /* O .active fica no <li> e vale também para o grupo que contém o item: o que interessa é o mais interno. */
      const marcados = Array.from(rolagem.querySelectorAll('.nav-item.active, .nav-link.active'));
      const interno = marcados.filter(el => !marcados.some(outro => outro !== el && el.contains(outro))).pop();
      const ativo = interno && (interno.querySelector(':scope > .nav-link') || interno);
      if (!ativo) return;
      const area = rolagem.getBoundingClientRect();
      const item = ativo.getBoundingClientRect();
      const folga = 8;
      if (item.top < area.top + folga) rolagem.scrollTop -= area.top + folga - item.top;
      else if (item.bottom > area.bottom - folga) rolagem.scrollTop += item.bottom - (area.bottom - folga);
    };
    new MutationObserver(() => { if (!agendado) { agendado = true; requestAnimationFrame(mostrarAtivo); } })
      .observe(rolagem, { attributes: true, attributeFilter: ['class'], subtree: true });
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

  /* Divisor entre o menu de tópicos e o conteúdo: arrastar (ou ← →, Home, End) muda a largura do menu; duplo clique volta
     à padrão. A largura fica no localStorage, e as outras páginas e abas abertas a recebem pelo evento "storage"; o <head>
     da página a aplica antes da primeira pintura, para o menu não saltar ao trocar de página. */
  const divisor = $('.dx-divisor');
  const coluna = $('.doc-sidebar');
  if (divisor && coluna) {
    const CHAVE = 'docx-menu-largura';
    const MIN = 200;
    const raiz = document.documentElement;
    const maximo = () => Math.max(MIN, Math.min(640, Math.round(window.innerWidth / 2)));
    const limitar = px => Math.min(maximo(), Math.max(MIN, Math.round(px)));
    const guardada = () => {
      try { const valor = parseInt(localStorage.getItem(CHAVE), 10); return Number.isFinite(valor) ? valor : null; } catch (_) { return null; }
    };
    const guardar = px => {
      try { if (px === null) localStorage.removeItem(CHAVE); else localStorage.setItem(CHAVE, String(px)); } catch (_) { /* A largura vale nesta página. */ }
    };
    const aplicar = px => {
      if (px === null) raiz.style.removeProperty('--dx-menu-largura');
      else raiz.style.setProperty('--dx-menu-largura', limitar(px) + 'px');
      divisor.setAttribute('aria-valuenow', String(Math.round(coluna.getBoundingClientRect().width)));
    };
    divisor.setAttribute('aria-valuemin', String(MIN));
    divisor.setAttribute('aria-valuemax', String(maximo()));
    const mudar = px => { const valor = limitar(px); aplicar(valor); guardar(valor); };
    aplicar(guardada());

    divisor.addEventListener('pointerdown', event => {
      if (event.button !== 0) return;
      event.preventDefault();
      divisor.setPointerCapture(event.pointerId);
      divisor.classList.add('arrastando');
      raiz.classList.add('dx-arrastando');
    });
    divisor.addEventListener('pointermove', event => {
      if (divisor.hasPointerCapture(event.pointerId)) mudar(event.clientX - coluna.getBoundingClientRect().left);
    });
    const soltar = () => { divisor.classList.remove('arrastando'); raiz.classList.remove('dx-arrastando'); };
    divisor.addEventListener('pointerup', soltar);
    divisor.addEventListener('pointercancel', soltar);
    divisor.addEventListener('dblclick', () => { guardar(null); aplicar(null); });
    divisor.addEventListener('keydown', event => {
      const largura = coluna.getBoundingClientRect().width;
      const passo = event.shiftKey ? 64 : 16;
      const destino = { ArrowLeft: largura - passo, ArrowRight: largura + passo, Home: MIN, End: maximo() }[event.key];
      if (destino === undefined) return;
      event.preventDefault();
      mudar(destino);
    });
    window.addEventListener('storage', event => { if (event.key === CHAVE || event.key === null) aplicar(guardada()); });
    window.addEventListener('resize', () => { divisor.setAttribute('aria-valuemax', String(maximo())); aplicar(guardada()); });
  }

  /* Imprimir: um botão, e não um link javascript:. */
  $$('[data-print]').forEach(button => button.addEventListener('click', () => window.print()));
})();
