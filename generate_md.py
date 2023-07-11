import os.path


entries = [
    ("bridge.svg", ["bridge"]),
    ("church.svg", ["church", "mosque"]),
    ("fang.svg", ["fang", "tooth"]),
    ("fez.svg", ["fez"]),
    ("flake.svg", ["flake"]),
    ("gem.svg", ["gem"]),
    ("horn.svg", ["horn", "claw"]),
    ("knight.svg", ["knight", "horse"]),
    ("moon.svg", ["moon"]),
    ("rook.svg", ["rook"]),
    ("shield.svg", ["shield", "badge"]),
    ("shroom.svg", ["shroom"]),
    ("stair.svg", ["stair"]),
    ("stupa.svg", ["stupa", "stup"]),
    ("wave.svg", ["wave"]),
]
sizes = [200, 10, 9, 6]


def write_entry(f, entry):
    title = ", ".join(entry[1])
    f.write(f"# `{title}`\n\n")
    for size in sizes:
        f.write(f'<img src="svgs/{entry[0]}" width={size} height={size}/>\n')
    f.write(f"\n\n")


def main():
    output_file = os.path.join(os.path.dirname(__file__), "preview.md")
    print(output_file)

    with open(output_file, "w", encoding="utf-8") as f:
        for entry in entries:
            write_entry(f, entry)


if __name__ == "__main__":
    main()
