// Picks the colour palette before the page paints (no flash of the wrong colours).
// Order: ?palette=charcoal (or garnet) in the address, then the visitor's last choice, then sky.
(function () {
  var p = null;
  try {
    var m = location.search.match(/[?&]palette=([a-z-]+)/);
    p = m ? m[1] : localStorage.getItem('headliner-palette');
  } catch (e) {}
  if (p !== 'charcoal' && p !== 'garnet') p = 'sky';
  document.documentElement.setAttribute('data-palette', p);
})();
