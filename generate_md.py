import os.path
import airium


entries = [
    ("church.svg", ["church"]),
    ("mosque.svg", ["mosque"]),
    ("stupa.svg", ["stupa", "stup"]),
    ("bridge.svg", ["bridge"]),
    ("fez.svg", ["fez"]),
    ("pail.svg", ["pail", "vase"]),
    ("flake.svg", ["flake", "snow"]),
    ("horn.svg", ["horn", "claw"]),
    ("moon.svg", ["moon"]),
    ("tree.svg", ["tree"]),
    ("shroom.svg", ["shroom"]),
    ("stair.svg", ["stair"]),
    ("fang.svg", ["fang", "tooth", "keel"]),
    ("wave.svg", ["wave"]),
    ("leaf.svg", ["leaf", "maple"]),
    ("rook.svg", ["rook"]),
    ("knight.svg", ["knight", "horse"]),
    ("pawn.svg", ["pawn"]),
    ("meeple.svg", ["meeple", "dude", "gal", "guy"]),
]
sizes = [200] + list(reversed(range(5, 11)))


def write_entry(f, entry):
    title = ", ".join(entry[1])
    f.write(f"# `{title}`\n\n")
    for size in sizes:
        f.write(f'<img src="svgs/{entry[0]}" width={size} height={size}/>\n')
    f.write(f"\n\n")


def generate_md():
    output_file = os.path.join(os.path.dirname(__file__), "preview.md")

    with open(output_file, "w", encoding="utf-8") as f:
        for entry in entries:
            write_entry(f, entry)


def style(kvs):
    return ";".join([f"{k}:{v}" for k, v in kvs.items()])


def generate_html():
    output_file = os.path.join(os.path.dirname(__file__), "preview.html")
    a = airium.Airium()
    a("<!DOCTYPE html>")
    with a.head():
        a.meta(charset="utf-8")
    with a.body():
        with a.div(style=style({"display": "flex", "flex-wrap": "wrap"})):
            for entry in entries:
                with a.div(
                    style=style({"border": "2px solid black", "padding": "10px"})
                ):
                    with a.div(style=style({})):
                        with a.div():
                            with a.tt(style=style({"font-size": "1.5em"})):
                                a(", ".join(entry[1]))
                        a.img(
                            style=style(
                                {"height": f"{sizes[0]}px"},
                            ),
                            src=f"svgs/{entry[0]}",
                        )
                        with a.div(
                            style=style(
                                {
                                    "display": "flex",
                                    "margin": "10px",
                                    "margin-top": "30px",
                                    "justify-content": "space-between",
                                }
                            )
                        ):
                            for size in sizes[1:]:
                                a.img(
                                    style=style(
                                        {
                                            "object-fit": "contain",
                                            "width": "100%",
                                            "height": f"{size}px",
                                        },
                                    ),
                                    src=f"svgs/{entry[0]}",
                                )
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(str(a))


def main():
    generate_md()
    generate_html()


if __name__ == "__main__":
    main()
