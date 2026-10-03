/* Progressive enhancement: native anchors and disclosures work without JavaScript. */
(() => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  const mobile = window.matchMedia('(max-width: 680px)');

  const closeMenu = (restoreFocus = false) => {
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Open navigation');
    toggle.querySelector('.menu-label').textContent = 'Menu';
    nav.classList.remove('is-open');
    if (restoreFocus) toggle.focus();
  };
  toggle.addEventListener('click', () => {
    if (toggle.getAttribute('aria-expanded') === 'true') return closeMenu();
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Close navigation');
    toggle.querySelector('.menu-label').textContent = 'Close';
    nav.classList.add('is-open');
  });
  nav.addEventListener('click', (event) => {
    const link = event.target.closest('a');
    if (!link || !mobile.matches) return;
    closeMenu();
    const href = link.getAttribute('href');
    if (href.startsWith('#')) {
      const target = document.querySelector(href);
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
      target.addEventListener('blur', () => target.removeAttribute('tabindex'), { once: true });
    } else {
      toggle.focus();
    }
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') closeMenu(true);
  });
  document.addEventListener('click', (event) => {
    if (!header.contains(event.target)) closeMenu();
  });
  header.addEventListener('focusout', (event) => {
    if (event.relatedTarget && !header.contains(event.relatedTarget)) closeMenu();
  });
  mobile.addEventListener('change', () => closeMenu());
  document.documentElement.classList.add('nav-ready');

  if ('IntersectionObserver' in window) {
    const links = [...nav.querySelectorAll('[data-nav]')];
    const visible = new Set();
    const observer = new IntersectionObserver((entries) => {
      for (const entry of entries) {
        if (entry.isIntersecting) visible.add(entry.target.id);
        else visible.delete(entry.target.id);
      }
      const active = links.find((link) => visible.has(link.hash.slice(1)));
      links.forEach((link) => {
        if (link === active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }, { rootMargin: '-15% 0px -55% 0px', threshold: 0 });
    links.forEach((link) => observer.observe(document.querySelector(link.hash)));
  }
})();
