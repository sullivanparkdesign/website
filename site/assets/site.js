// Sullivan Park Design: small, dependency-free behaviours for the static site.
// Mirrors the design canvas logic: sticky header, phone menu, dropdown Escape, back-to-top,
// FAQ toggles, hero video, before/after slider and the contact form.
(function () {
  var doc = document, win = window;
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || doc).querySelectorAll(sel)); };
  var reduce = win.matchMedia && win.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- header ----------
  var header = doc.querySelector('[data-header]');
  var nav = header && header.querySelector('.sp-nav');
  var mnav = doc.querySelector('[data-mnav]');
  var fabs = $$('.sp-fab');
  var menuOpen = false, deep = false;

  function setFab() { fabs.forEach(function (f) { f.setAttribute('data-show', deep && !menuOpen ? 'true' : 'false'); }); }
  function sync() {
    var y = win.pageYOffset || doc.documentElement.scrollTop || 0;
    if (header) header.setAttribute('data-scrolled', y > 24 ? 'true' : 'false');
    var d = y > 640;
    if (d !== deep) { deep = d; setFab(); }
  }
  win.addEventListener('scroll', sync, { passive: true });
  sync();

  function setMenu(open, focusBtn) {
    menuOpen = open;
    if (mnav) { if (open) mnav.removeAttribute('hidden'); else mnav.setAttribute('hidden', ''); }
    $$('[data-menu-toggle]').forEach(function (b) { b.setAttribute('aria-expanded', open ? 'true' : 'false'); });
    if (header) header.setAttribute('data-menu', open ? 'true' : 'false');
    setFab();
    if (!open && focusBtn) { var b = doc.querySelector('[data-menu-toggle]'); if (b) b.focus(); }
  }
  $$('[data-menu-toggle]').forEach(function (b) { b.addEventListener('click', function () { setMenu(!menuOpen); }); });
  doc.addEventListener('click', function (e) {
    var t = e.target.closest && e.target.closest('[data-menu-close]');
    if (t) setMenu(false);
  });

  doc.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape' && e.key !== 'Esc') return;
    var active = doc.activeElement;
    var inHeader = !!(header && active && header.contains(active));
    if (menuOpen) { setMenu(false, inHeader); return; }
    if (inHeader && active.closest && active.closest('.sp-dd-panel')) {
      var dd = active.closest('.sp-dd'); var top = dd && dd.querySelector('.sp-navlink');
      if (top) top.focus();
    }
    if (nav) nav.setAttribute('data-hush', 'true');
  });
  if (nav) {
    var unhush = function () { nav.setAttribute('data-hush', 'false'); };
    nav.addEventListener('pointerleave', unhush);
    nav.addEventListener('focusout', unhush);
  }

  // ---------- FAQ toggles (each opens independently, like the design) ----------
  $$('[data-faq-btn]').forEach(function (btn) {
    var n = btn.getAttribute('data-faq-btn');
    btn.addEventListener('click', function () {
      var panel = doc.querySelector('[data-faq-panel="' + n + '"]');
      if (!panel) return;
      var opening = panel.hasAttribute('hidden');
      if (opening) panel.removeAttribute('hidden'); else panel.setAttribute('hidden', '');
      btn.setAttribute('aria-expanded', opening ? 'true' : 'false');
    });
  });

  // ---------- hero video ----------
  var video = doc.querySelector('[data-hero-video]');
  var vtoggle = doc.querySelector('[data-video-toggle]');
  var setVideoUi = function (paused) {
    if (!vtoggle) return;
    var label = paused ? 'Play background video' : 'Pause background video';
    vtoggle.setAttribute('aria-label', label); vtoggle.setAttribute('title', label);
    $$('[data-video-icon]', vtoggle).forEach(function (s) {
      var show = (s.getAttribute('data-video-icon') === 'paused') === paused;
      if (show) s.removeAttribute('hidden'); else s.setAttribute('hidden', '');
    });
  };
  if (video) {
    video.muted = true; video.defaultMuted = true; video.loop = true; video.playsInline = true;
    var conn = navigator.connection;
    var saveData = !!(conn && (conn.saveData || /(^|-)2g$/.test(conn.effectiveType || '')));
    if (reduce || saveData) {
      video.removeAttribute('autoplay'); video.preload = 'none'; try { video.pause(); } catch (e) {}
      setVideoUi(true);
    } else {
      var p = video.play(); if (p && p.catch) p.catch(function () { setVideoUi(true); });
    }
    if (vtoggle) vtoggle.addEventListener('click', function () {
      if (video.paused) { var q = video.play(); if (q && q.catch) q.catch(function () {}); setVideoUi(false); }
      else { video.pause(); setVideoUi(true); }
    });
  }

  // ---------- before / after slider ----------
  $$('[data-ba]').forEach(function (el) {
    var input = el.querySelector('.rd-ba-range');
    if (!input) return;
    var move = function () { el.style.setProperty('--pos', (input.value || 50) + '%'); };
    input.addEventListener('input', move); input.addEventListener('change', move);
  });

  // ---------- contact form ----------
  var form = doc.querySelector('[data-form]');
  if (form) {
    var endpoint = form.getAttribute('data-endpoint') || '';
    var views = {};
    $$('[data-form-view]').forEach(function (v) { views[v.getAttribute('data-form-view')] = v; });
    var show = function (el, on) { if (!el) return; if (on) el.removeAttribute('hidden'); else el.setAttribute('hidden', ''); };
    var submit = form.querySelector('[data-form-submit]');
    var label = submit ? submit.getAttribute('data-label') || submit.textContent : '';
    var sending = false;
    var field = function (n) { var el = form.elements.namedItem(n); return el && typeof el.value === 'string' ? el.value.trim() : ''; };
    var setError = function (n, on, text) {
      var box = form.querySelector('[data-error="' + n + '"]');
      var input = form.elements.namedItem(n);
      show(box, on);
      if (text && box) { var t = box.querySelector('[data-error-text]'); if (t) t.textContent = text; }
      if (input) {
        input.setAttribute('aria-invalid', on ? 'true' : 'false');
        if (on) input.setAttribute('aria-describedby', 'f-' + n + '-error'); else input.removeAttribute('aria-describedby');
      }
    };
    var finish = function (ok) {
      sending = false;
      if (submit) { submit.textContent = label; submit.setAttribute('aria-disabled', 'false'); }
      if (ok) { show(views.form, false); show(views.sent, true); var s = views.sent && views.sent.querySelector('p'); if (s) { s.setAttribute('tabindex', '-1'); s.focus(); } }
      else show(views.failed, true);
    };
    var send = function () {
      if (sending) return;
      var name = field('name'), email = field('email'), message = field('message');
      var errs = { name: !name, email: !email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email), message: !message };
      setError('name', errs.name);
      setError('email', errs.email, !email ? 'Please enter your email address.' : 'Please enter a valid email address.');
      setError('message', errs.message);
      show(views.failed, false);
      var first = ['name', 'email', 'message'].filter(function (k) { return errs[k]; })[0];
      if (first) { var el = form.elements.namedItem(first); if (el) el.focus(); return; }
      if (!endpoint) {
        // Not connected to a form service yet: hand the message to the visitor's email app.
        var body = 'Name: ' + name + '\nEmail: ' + email + '\nWebsite: ' + field('website') + '\nService: ' + field('service') + '\n\n' + message;
        var alertBox = views.failed && views.failed.querySelector('[role="alert"]');
        if (alertBox && alertBox.getAttribute('data-mailto-note')) alertBox.innerHTML = alertBox.getAttribute('data-mailto-note');
        show(views.failed, true);
        win.location.href = 'mailto:hello@sullivanparkdesign.com?subject=' + encodeURIComponent('Website enquiry from ' + name) + '&body=' + encodeURIComponent(body);
        return;
      }
      sending = true;
      var subject = form.querySelector('[name="_subject"]');
      if (subject) subject.value = 'Website enquiry from ' + name;
      if (submit) { submit.textContent = 'Sending…'; submit.setAttribute('aria-disabled', 'true'); }
      try {
        fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
          .then(function (res) { finish(res && res.ok); })
          .catch(function () { finish(false); });
      } catch (e) { finish(false); }
    };
    // Arriving from the Actor Websites page (/contact?service=actor-websites): that service is chosen
    // for the visitor, who can still pick another. Its hint shows whenever it's the chosen service.
    var serviceSelect = form.elements.namedItem('service');
    var serviceHint = doc.getElementById('f-service-hint');
    var SERVICES = { 'actor-websites': 'Actor Websites' };
    var updateHint = function () {
      if (!serviceSelect || !serviceHint) return;
      var on = serviceSelect.value === 'Actor Websites';
      show(serviceHint, on);
      if (on) serviceSelect.setAttribute('aria-describedby', 'f-service-hint'); else serviceSelect.removeAttribute('aria-describedby');
    };
    try {
      var wanted = SERVICES[new URLSearchParams(win.location.search).get('service') || ''];
      if (wanted && serviceSelect) serviceSelect.value = wanted;
    } catch (e) {}
    if (serviceSelect) serviceSelect.addEventListener('change', updateHint);
    updateHint();
    if (submit) submit.addEventListener('click', send);
    form.addEventListener('submit', function (e) { e.preventDefault(); send(); });
    $$('[data-form-reset]').forEach(function (b) {
      b.addEventListener('click', function () {
        form.reset(); updateHint(); ['name', 'email', 'message'].forEach(function (n) { setError(n, false); });
        show(views.sent, false); show(views.failed, false); show(views.form, true);
        var f = form.elements.namedItem('name'); if (f) f.focus();
      });
    });
  }
  // ---------- actor website intake form (hidden page /services/actor-websites/intake) ----------
  var ik = doc.querySelector('form[data-intake]');
  if (ik) {
    var ikEndpoint = ik.getAttribute('data-endpoint') || '';
    var ikSubmit = ik.querySelector('[data-intake-submit]');
    var ikLabel = ikSubmit ? ikSubmit.textContent : '';
    var ikErr = ik.querySelector('[data-intake-error]'), ikFail = ik.querySelector('[data-intake-failed]');
    var ikSent = doc.querySelector('[data-intake-sent]');
    var ikBusy = false, ikDirty = false, ikDone = false;
    var picked = function (key) { var on = ik.querySelector('input[data-key="' + key + '"]:checked'); return on ? on.value : ''; };
    var stillsBox = ik.elements.namedItem('Stills folder');
    // conditions that show questions or make them required
    var conds = function () {
      return {
        contact: /form|Email link/.test(picked('contact')),
        minor: picked('minor') === 'Yes',
        nopdf: /^No/.test(picked('resume')),
        stills: !!(stillsBox && stillsBox.value.trim())
      };
    };
    var ikSync = function () {
      var c = conds();
      $$('[data-show-if]', ik).forEach(function (el) { if (c[el.getAttribute('data-show-if')]) el.removeAttribute('hidden'); else el.setAttribute('hidden', ''); });
    };
    $$('.ik-err', ik).forEach(function (e) { e.setAttribute('data-default', e.textContent); });
    var boxOf = function (el) { return el.closest('.ik-field'); };
    var mark = function (box, bad, msg) {
      if (!box) return;
      box.setAttribute('aria-invalid', bad ? 'true' : 'false');
      var e = box.querySelector('.ik-err');
      if (!e) return;
      e.textContent = msg || e.getAttribute('data-default');
      if (bad) e.removeAttribute('hidden'); else e.setAttribute('hidden', '');
    };
    var empty = function (el) { return el.type === 'checkbox' ? !el.checked : !el.value.trim(); };
    var validate = function () {
      var c = conds(), first = null;
      $$('.ik-field', ik).forEach(function (b) { mark(b, false); });
      var fail = function (box, el, msg) { mark(box, true, msg); if (!first) first = el; };
      $$('input[data-req], textarea[data-req]', ik).forEach(function (el) { if (empty(el)) fail(boxOf(el), el); });
      $$('fieldset[data-req]', ik).forEach(function (fs) { if (!fs.querySelector('input:checked')) fail(fs, fs.querySelector('input')); });
      $$('[data-req-if]', ik).forEach(function (el) { var k = el.getAttribute('data-req-if'); if (k !== 'bio' && c[k] && empty(el)) fail(boxOf(el), el); });
      var bio = $$('[data-req-if="bio"]', ik);
      if (bio.length && bio.every(empty)) bio.forEach(function (el) { fail(boxOf(el), el, 'Please fill in your bio or your notes for one.'); });
      $$('input[type=email]', ik).forEach(function (el) {
        var v = el.value.trim();
        if (v && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v) && !el.closest('[hidden]')) fail(boxOf(el), el, 'Please enter a valid email address.');
      });
      return first;
    };
    var ikSend = function (e) {
      if (e) e.preventDefault();
      if (ikBusy) return;
      if (ikFail) ikFail.setAttribute('hidden', '');
      var first = validate();
      if (first) {
        if (ikErr) ikErr.removeAttribute('hidden');
        first.scrollIntoView({ block: 'center', behavior: reduce ? 'auto' : 'smooth' });
        first.focus({ preventScroll: true });
        return;
      }
      if (ikErr) ikErr.setAttribute('hidden', '');
      // questions in page order, ticked boxes joined, questions that don't apply left out
      var data = new FormData(), seen = {};
      Array.prototype.forEach.call(ik.elements, function (el) {
        if (!el.name || el.type === 'submit' || el.type === 'button' || el.closest('[hidden]')) return;
        if (el.type === 'radio' || el.type === 'checkbox') {
          if (!el.checked) return;
          if (seen[el.name] !== undefined) { seen[el.name] += ', ' + el.value; data.set(el.name, seen[el.name]); return; }
          seen[el.name] = el.value; data.append(el.name, el.value); return;
        }
        data.append(el.name, el.value.trim());
      });
      var who = ik.elements.namedItem('Name on website');
      data.set('_subject', 'Actor website details: ' + (who ? who.value.trim() : ''));
      if (!ikEndpoint) { if (ikFail) ikFail.removeAttribute('hidden'); return; }
      ikBusy = true;
      if (ikSubmit) { ikSubmit.textContent = 'Sending…'; ikSubmit.setAttribute('aria-disabled', 'true'); }
      var done = function (ok) {
        ikBusy = false;
        if (ikSubmit) { ikSubmit.textContent = ikLabel; ikSubmit.setAttribute('aria-disabled', 'false'); }
        if (ok) {
          ikDone = true;
          ik.setAttribute('hidden', '');
          if (ikSent) { ikSent.removeAttribute('hidden'); ikSent.scrollIntoView({ block: 'center' }); var h = ikSent.querySelector('h2'); if (h) h.focus({ preventScroll: true }); }
        } else if (ikFail) ikFail.removeAttribute('hidden');
      };
      try {
        fetch(ikEndpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
          .then(function (res) { done(res && res.ok); }, function () { done(false); });
      } catch (err) { done(false); }
    };
    ik.addEventListener('submit', ikSend);
    ik.addEventListener('change', function () { ikDirty = true; ikSync(); });
    ik.addEventListener('input', function (e) {
      ikDirty = true;
      var b = e.target.closest && e.target.closest('.ik-field');
      if (b && b.getAttribute('aria-invalid') === 'true') mark(b, false);
      if (e.target === stillsBox) ikSync();
    });
    // a long form: warn before leaving with answers that haven't been sent
    win.addEventListener('beforeunload', function (e) { if (ikDirty && !ikDone) { e.preventDefault(); e.returnValue = ''; } });
    ikSync();
  }
})();
