# Running

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
make serve
```

Then visit [localhost:8000/preview.html](localhost:8000/preview.html) to see the different hats and how they look at different scales.

# Building

The svgs must be cleared of any editor specific-properties before they can be used by cursorless.

Run:
```
make build
```

This creates optimized svgs that can be copied to `$CURSORLESS_ROOT/images/hats`. Run the cursorless package script

```
pnpm -F @cursorless/cursorless-vscode preprocess-svg-hats
```

to ensure they are scaled and colored according to what cursorless expects.
