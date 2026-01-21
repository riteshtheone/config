from shutil import which
from subprocess import run


def main():
    if which("curl"):
        run(["echo", "hello curl!"], check=True)
