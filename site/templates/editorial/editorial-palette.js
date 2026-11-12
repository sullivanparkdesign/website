// Picks the colour palette before the page paints (no flash of the wrong colours).
// Order: ?palette=denim (or sage) in the address, then the visitor's last choice, then stone.
(function () {
  var p = null;
  try {
    var m = location.search.match(/[?&]palette=([a-z-]+)/);
    p = m ? m[1] : localStorage.getItem('editorial-palette');
  } catch (e) {}
  if (p !== 'denim' && p !== 'sage') p = 'stone';
  document.documentElement.setAttribute('data-palette', p);
})();
