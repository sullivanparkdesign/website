// Feature template demo: colour switcher, headshot filters and print button.
(function () {
  'use strict';
  var root = document.documentElement;

  // Colour switcher: shows visitors the same template in another palette
  var PALETTES = [
    { id: 'charcoal', name: 'Charcoal & cornflower', short: 'Charcoal', colours: ['#131518', '#93b0e6', '#eceef1'] },
    { id: 'light', name: 'Navy & sky', short: 'Navy', colours: ['#f4f6f9', '#e1e9f2', '#24477a'] },
    { id: 'mono', name: 'Black & white', short: 'B&W', colours: ['#0b0b0b', '#7a7a7a', '#ffffff'] },
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
    try { localStorage.setItem('feature-palette', id); } catch (e) {}
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-palette-choice') === id ? 'true' : 'false'); });
    // Keep the choice when moving between pages, even if storage is blocked
    document.querySelectorAll('a[href$=".html"], a[href*=".html?"]').forEach(function (a) {
      var href = a.getAttribute('href');
      if (/^https?:/.test(href) || /^images\//.test(href)) return;
      href = href.replace(/\?palette=[a-z-]+$/, '');
      a.setAttribute('href', id === 'charcoal' ? href : href + '?palette=' + id);
    });
  }
  setPalette(root.getAttribute('data-palette') || 'charcoal');

  // Headshot filters (headshots page)
  var filters = Array.prototype.slice.call(document.querySelectorAll('[data-filter]'));
  var shots = Array.prototype.slice.call(document.querySelectorAll('[data-cat]'));
  filters.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = btn.getAttribute('data-filter');
      filters.forEach(function (b) {
        var on = b === btn;
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
        b.style.background = on ? 'var(--ink)' : 'transparent';
        b.style.color = on ? 'var(--bg)' : 'var(--ink)';
        b.style.borderColor = on ? 'var(--ink)' : 'var(--rule)';
      });
      shots.forEach(function (s) {
        s.style.display = f === 'all' || s.getAttribute('data-cat') === f ? '' : 'none';
      });
    });
  });

  // Print and PDF buttons on the resume page (choose "Save as PDF" in the print window)
  document.querySelectorAll('a[href="#print"], a[href="#pdf"]').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); window.print(); });
  });

})();
