# Running

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
make serve
```

Then visit [localhost:8000/preview.html](localhost:8000/preview.html) to see the different hats and how they look at different scales.

# Installing into cursorless

Assuming your `.venv` already has been installed and activated:

```
# replace with the path to the cursorless git clone
export CURSORLESS_DIR=../cursorless
make install
```

This will preprocess the svgs, copy them to the appropriate directory in the cursorless repo, run the cursorless preprocess step on them, then finally build and install a local version of the cursorless vsix package.

The following files in the cursorless repo need to be edited to make use of the new hats:

```
.vscode/settings.json
cursorless-talon/src/marks/mark.py
packages/common/src/types/command/legacy/CommandV0V1.types.ts
packages/common/src/types/command/legacy/PartialTargetDescriptorV3.types.ts
packages/common/src/types/command/legacy/targetDescriptorV2.types.ts
packages/cursorless-vscode/package.json
packages/cursorless-vscode/src/ide/vscode/hatStyles.types.ts
packages/cursorless-vscode/src/ide/vscode/hats/shapeAdjustments.ts
```

Some of the files need to be edited in multiple places. Find the places where the hats are specified (by searching for `bolt` for instance) and make the appropriate additions.

Also, be sure to create a symlink from your `.talon/user/cursorless-talon` to the local version:

```
`ln -s $CURSORLESS_DIR/cursorless-talon ~/.talon/user/cursorless-talon
```
