// Picks the colour palette before the page paints (no flash of the wrong colours).
// Order: ?palette=sage (or plum) in the address, then the visitor's last choice, then blue.
(function () {
  var p = null;
  try {
    var m = location.search.match(/[?&]palette=([a-z-]+)/);
    p = m ? m[1] : localStorage.getItem('luminous-palette');
  } catch (e) {}
  if (p !== 'sage' && p !== 'plum') p = 'blue';
  document.documentElement.setAttribute('data-palette', p);
})();
