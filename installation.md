# Python Project Installation Guide

Follow the steps below to download, install, and run this Python project from GitHub.

## 1. Install Git

First, make sure Git is installed on your computer.

### Debian / Ubuntu

```bash
sudo apt update
sudo apt install git
```

Check the installation:

```bash
git --version
```

## 2. Install Python

Make sure Python 3 is installed.

On Debian / Ubuntu:

```bash
sudo apt install python3 python3-pip python3-venv
```

Check the Python version:

```bash
python3 --version
```

## 3. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Replace the URL with the actual GitHub repository URL.

Then enter the project directory:

```bash
cd YOUR-REPOSITORY
```

## 4. Create a Virtual Environment

It is recommended to use a virtual environment for this project.

Run:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

After activation, you should see `(.venv)` at the beginning of your terminal prompt.

## 5. Upgrade pip

Run:

```bash
python -m pip install --upgrade pip
```

## 6. Install the Project

If this project uses `pyproject.toml`, install it with:

```bash
pip install .
```

For development/editable installation:

```bash
pip install -e .
```

If the project instead uses `requirements.txt`, install the dependencies with:

```bash
pip install -r requirements.txt
```

## 7. Run the Application

After installation, run the application using the project's command.

For example:

```bash
python main.py
```

If the project provides a command-line command, use that command instead.

## 8. Updating the Project

To download the latest changes from GitHub:

```bash
git pull
```

If the dependencies have changed, run the installation command again:

```bash
pip install -e .
```

or:

```bash
pip install -r requirements.txt
```

## 9. Deactivate the Virtual Environment

When you are finished using the application:

```bash
deactivate
```

To use the project again later, go to the project directory and activate the environment:

```bash
cd YOUR-REPOSITORY
source .venv/bin/activate
```

## Quick Installation

For a typical Linux installation, the process is:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
pip install .

python main.py
```

Replace `YOUR-USERNAME`, `YOUR-REPOSITORY`, and `python main.py` with the actual values for this project.

## Troubleshooting

### Git is not installed

Install Git:

```bash
sudo apt update
sudo apt install git
```

### Python is not installed

Install Python:

```bash
sudo apt install python3 python3-pip python3-venv
```

### `externally-managed-environment`

If Debian prevents pip from installing packages globally, use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install .
```

Avoid using:

```bash
sudo pip install ...
```

### Missing Python modules

Make sure the virtual environment is activated and install the project's dependencies again:

```bash
pip install .
```

or:

```bash
pip install -r requirements.txt
```

## Done!

The project should now be installed and ready to use.

If you encounter a problem during installation, check the error message in the terminal and refer to the project's GitHub Issues page for troubleshooting.
