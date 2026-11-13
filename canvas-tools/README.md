# Canvas tools

The scripts that generate the design pages on the Claude Design canvas (the `.dc.html` files in `design-source/`).
They were run from a scratchpad with this layout:

```
canvas/project/      the canvas files (same as design-source/ plus canvas.json)
build/               these scripts
callum/ laura/ ...   image id maps for each case study (blobs.json)
mobile/              test renders (build2.py turns .dc.html into plain HTML, ed-shot.js screenshots it)
```

Typical run: `python3 build/build_actor.py canvas/project`, then `python3 build/nav_upgrade.py canvas/project`
(nav_upgrade refreshes the header, menus and footer on every page). Then publish the canvas and copy the
changed files into `design-source/` before running `build/build.mjs`.

Not every page has a generator: the Services page and parts of others were edited directly.
`services_actor.py` is not in use (actor websites stay off the Services page).
