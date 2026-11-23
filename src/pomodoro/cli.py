"""Command-line entry point for the ``pomodoro`` command."""

import sys


def run():
    # tkinter pip দিয়ে ইন্সটল হয় না; সিস্টেম প্যাকেজ লাগে। না থাকলে পরিষ্কার মেসেজ দেখাই।
    try:
        import tkinter  # noqa: F401
    except ImportError:
        sys.exit(
            "Error: tkinter পাওয়া যায়নি।\n"
            "Debian/Ubuntu:  sudo apt install python3-tk\n"
            "Fedora:         sudo dnf install python3-tkinter\n"
            "Arch:           sudo pacman -S tk"
        )

    from .main import main

    main()
