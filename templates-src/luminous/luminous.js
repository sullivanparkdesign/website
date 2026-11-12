// Luminous template demo: colour switcher, headshot filters, print button and demo-only forms.
(function () {
  'use strict';
  var root = document.documentElement;

  // Colour switcher: shows visitors the same template in another palette
  var PALETTES = [
    { id: 'blue', name: 'Blue & gold', short: 'Blue', colours: ['#1c2b45', '#e4ecf3', '#c2a060'] },
    { id: 'sage', name: 'Sage & slate', short: 'Sage', colours: ['#5c757a', '#c7cdbf', '#e9e2d8'] },
    { id: 'plum', name: 'Plum & champagne', short: 'Plum', colours: ['#2a1a26', '#c9a66b', '#f2e8dc'] },
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
    try { localStorage.setItem('luminous-palette', id); } catch (e) {}
    buttons.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-palette-choice') === id ? 'true' : 'false'); });
    // Keep the choice when moving between pages, even if storage is blocked
    document.querySelectorAll('a[href$=".html"], a[href*=".html?"]').forEach(function (a) {
      var href = a.getAttribute('href');
      if (/^https?:/.test(href) || /^images\//.test(href)) return;
      href = href.replace(/\?palette=[a-z-]+$/, '');
      a.setAttribute('href', id === 'blue' ? href : href + '?palette=' + id);
    });
  }
  setPalette(root.getAttribute('data-palette') || 'blue');

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
        b.style.color = on ? 'var(--paper)' : 'var(--ink)';
        b.style.borderColor = on ? 'var(--ink)' : 'var(--accent)';
      });
      shots.forEach(function (s) {
        s.style.display = f === 'all' || s.getAttribute('data-cat') === f ? '' : 'none';
      });
    });
  });

  // Print button on the resume page
  document.querySelectorAll('a[href="#print"]').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); window.print(); });
  });

  // Forms are for show in the template demo
  document.querySelectorAll('[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.querySelector('.demo-note')) return;
      var p = document.createElement('p');
      p.className = 'demo-note';
      p.setAttribute('role', 'status');
      p.textContent = 'This is a template preview, so messages are not sent. On a live site this form goes straight to the actor or their parent.';
      form.appendChild(p);
    });
  });
})();
