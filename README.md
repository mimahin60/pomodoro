# pomodoro

A timer for study based on the Pomodoro technique (25 min focus / 5 min break).

## Install (Linux)

`tkinter` is a system package — pip cannot install it:

```bash
# Debian / Ubuntu
sudo apt install python3-tk python3-venv
```

Then, inside the project folder:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

## Run

```bash
pomodoro
# or
python -m pomodoro
```

## Uninstall

```bash
pip uninstall pomodoro
```

## Development

```bash
pip install -e .
```
