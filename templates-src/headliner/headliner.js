// Headliner template demo: colour switcher, gallery photo viewer, print button and one-page resume.
(function () {
  'use strict';
  var root = document.documentElement;

  // Colour switcher: shows visitors the same template in another palette
  var PALETTES = [
    { id: 'sky', name: 'Sky', short: 'Sky', colours: ['#f4f6f9', '#e1e9f2', '#24477a'] },
    { id: 'charcoal', name: 'Charcoal', short: 'Charcoal', colours: ['#131518', '#93b0e6', '#eceef1'] },
    { id: 'garnet', name: 'Garnet', short: 'Garnet', colours: ['#ffffff', '#ececee', '#8c1c2b'] },
  ];
  var bar = document.createElement('div');
  bar.className = 'palette-switch';
  bar.setAttribute('role', 'group');
  bar.setAttribute('aria-label', 'Try a colour palette');
  var label = document.createElement('span');
  label.className = 'label';
  label.textContent = 'Colours';
  bar.appendChild(label);
  var buttons = PALETTES.map(function (p) {
    var b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('data-palette-choice', p.id);
    var sw = document.createElement('span');
    sw.className = 'swatch';
    sw.setAttribute('aria-hidden', 'true');
    p.colours.forEach(function (c) { var i = document.createElement('i'); i.style.background = c; sw.appendChild(i); });
    b.appendChild(sw);
    var full = document.createElement('span'); full.className = 'full'; full.textContent = p.name;
    var short = document.createElement('span'); short.className = 'short'; short.textContent = p.short;
    b.appendChild(full);
    b.appendChild(short);
    b.addEventListener('click', function () { setPalette(p.id); });
    bar.appendChild(b);
    return b;
  });
  document.body.appendChild(bar);

  function setPalette(id) {
    root.setAttribute('data-palette', id);
    try { localStorage.setItem('headliner-palette', id); } catch (e) {}
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-palette-choice') === id ? 'true' : 'false'); });
    // Keep the choice when moving between pages, even if storage is blocked
    document.querySelectorAll('a[href$=".html"], a[href*=".html?"]').forEach(function (a) {
      var href = a.getAttribute('href');
      if (/^https?:/.test(href) || /^images\//.test(href)) return;
      href = href.replace(/\?palette=[a-z-]+$/, '');
      a.setAttribute('href', id === 'sky' ? href : href + '?palette=' + id);
    });
  }
  setPalette(root.getAttribute('data-palette') || 'sky');

  // Print and PDF buttons on the resume page (choose "Save as PDF" in the print window)
  document.querySelectorAll('a[href="#print"], a[href="#pdf"]').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); window.print(); });
  });

  // Gallery: click a photo to see it larger (Escape, the close button or a click outside closes it)
  var opener = null;
  function closeBox() {
    var box = document.querySelector('.lightbox');
    if (!box) return;
    box.remove();
    document.removeEventListener('keydown', onKey);
    if (opener) opener.focus();
  }
  function onKey(e) { if (e.key === 'Escape') closeBox(); }
  document.querySelectorAll('[data-lightbox]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      if (e.metaKey || e.ctrlKey || e.shiftKey) return;
      e.preventDefault();
      opener = a;
      var box = document.createElement('div');
      box.className = 'lightbox';
      box.setAttribute('role', 'dialog');
      box.setAttribute('aria-modal', 'true');
      box.setAttribute('aria-label', a.getAttribute('aria-label') || 'Photo');
      var img = document.createElement('img');
      img.src = a.getAttribute('href');
      img.alt = '';
      var close = document.createElement('button');
      close.type = 'button';
      close.setAttribute('aria-label', 'Close');
      close.textContent = '×';
      close.addEventListener('click', closeBox);
      box.addEventListener('click', function (ev) { if (ev.target === box) closeBox(); });
      box.appendChild(img);
      box.appendChild(close);
      document.body.appendChild(box);
      document.addEventListener('keydown', onKey);
      close.focus();
    });
  });

  // Resume: keep the sheet on one page. If more credits are added than fit, the text shrinks a little at a time.
  var sheet = document.querySelector('.resume-sheet');
  var baseSize = sheet ? sheet.style.fontSize || getComputedStyle(sheet).fontSize : '';
  var baseRatio = sheet ? sheet.style.aspectRatio : '';
  var printing = false;
  function fitSheet() {
    if (!sheet) return;
    sheet.style.fontSize = baseSize;
    if (!printing && window.matchMedia('(max-width: 760px)').matches) return; // small screens let the sheet grow
    var size = parseFloat(getComputedStyle(sheet).fontSize);
    var min = size * 0.72;
    var target = sheet.offsetWidth * 11 / 8.5; // one letter page at the sheet's width
    sheet.style.setProperty('aspect-ratio', 'auto', 'important');
    sheet.style.setProperty('height', 'auto', 'important');
    while (sheet.scrollHeight > target + 1 && size > min) {
      size -= 0.25;
      sheet.style.fontSize = size + 'px';
    }
    sheet.style.removeProperty('height');
    sheet.style.removeProperty('aspect-ratio');
    sheet.style.aspectRatio = baseRatio;
  }
  if (sheet) {
    fitSheet();
    window.addEventListener('resize', fitSheet);
    window.addEventListener('beforeprint', function () { printing = true; sheet.style.width = '8.5in'; fitSheet(); });
    window.addEventListener('afterprint', function () { printing = false; sheet.style.width = ''; fitSheet(); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitSheet);
  }
})();
