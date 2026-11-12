// Picks the colour palette before the page paints (no flash of the wrong colours).
// Order: ?palette=sea (or popcorn) in the address, then the visitor's last choice, then blue.
(function () {
  var p = null;
  try {
    var m = location.search.match(/[?&]palette=([a-z-]+)/);
    p = m ? m[1] : localStorage.getItem('luminous-palette');
  } catch (e) {}
  if (p !== 'sea' && p !== 'popcorn') p = 'blue';
  document.documentElement.setAttribute('data-palette', p);
})();
