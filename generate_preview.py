import os.path
import airium


entries = [
    ("bridge.svg", ["bridge", "rail", "bone"]),
    ("church.svg", ["church"]),
    ("gate.svg", ["gate"]),
    ("fang.svg", ["fang", "tooth", "keel"]),
    ("cone.svg", ["cone", "hat", "fez"]),
    ("gem.svg", ["gem"]),
    ("horn.svg", ["horn", "claw", "smile"]),
    ("knight.svg", ["knight", "horse"]),
    ("leaf.svg", ["leaf", "spade"]),
    ("meeple.svg", ["meeple", "dude", "gal", "guy"]),
    ("moon.svg", ["moon", "lune", "luna"]),
    ("mosque.svg", ["mosque"]),
    ("pail.svg", ["pail", "vase", "urn"]),
    ("rook.svg", ["rook"]),
    ("shroom.svg", ["shroom", "tree", "boom", "fret"]),
    ("singer.svg", ["singer", "sew"]),
    ("stair.svg", ["stair", "step"]),
    ("star.svg", ["star", "astro", "astri"]),
    ("stupa.svg", ["stupa", "stup"]),
    ("wave.svg", ["wave"]),
    ("wrench.svg", ["wrench"]),
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
