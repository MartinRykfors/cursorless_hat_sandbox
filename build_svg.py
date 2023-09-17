#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil
import tempfile


if __name__ == "__main__":
    input_path = sys.argv[1]
    svg_filename = os.path.basename(input_path)
    with tempfile.TemporaryDirectory() as tmpdirname:
        print("created temporary directory", tmpdirname)
        shutil.copy(input_path, os.path.join(tmpdirname, svg_filename))

        print('applying transforms')
        subprocess.run(
            [
                "inkscape",
                "-o",
                os.path.join(tmpdirname, 'transformed.svg'),
                "--verb=com.klowner.filter.apply_transform",
                "-g",
                "--batch-process",
                os.path.join(tmpdirname, svg_filename),
            ]
        )

        print('scouring')
        subprocess.run(
            [
                "scour",
                "-i",
                os.path.join(tmpdirname, 'transformed.svg'),
                "-o",
                os.path.join(tmpdirname, "{}.2".format(svg_filename)),
                "--remove-metadata",
                "--strip-xml-prolog",
                "--enable-comment-stripping",
            ]
        )
        print('copying back')
        shutil.copy(
            os.path.join(tmpdirname, "{}.2".format(svg_filename)),
            os.path.join("build", svg_filename),
        )
