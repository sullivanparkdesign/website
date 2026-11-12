// Picks the colour palette before the page paints (no flash of the wrong colours).
// Order: ?palette=heather (or forest) in the address, then the visitor's last choice, then denim.
(function () {
  var p = null;
  try {
    var m = location.search.match(/[?&]palette=([a-z-]+)/);
    p = m ? m[1] : localStorage.getItem('editorial-palette');
  } catch (e) {}
  if (p !== 'heather' && p !== 'forest') p = 'denim';
  document.documentElement.setAttribute('data-palette', p);
})();
