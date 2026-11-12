// Picks the colour palette before the page paints (no flash of the wrong colours).
// Order: ?palette=light (or mono) in the address, then the visitor's last choice, then charcoal.
(function () {
  var p = null;
  try {
    var m = location.search.match(/[?&]palette=([a-z-]+)/);
    p = m ? m[1] : localStorage.getItem('feature-palette');
  } catch (e) {}
  if (p !== 'light' && p !== 'mono') p = 'charcoal';
  document.documentElement.setAttribute('data-palette', p);
})();
