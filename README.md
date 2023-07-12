To run:

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python generate_md.py
```

This generates `preview.md` and `preview.html`. Use a local live server on the `preview.html` file to see different zoom levels for the svgs in real time as you edit and save them.