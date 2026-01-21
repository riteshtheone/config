from pathlib import Path
from sys import argv, exit
from shutil import which
from subprocess import run, CalledProcessError


# -------------------------
# LOG TRACKING
# -------------------------
def track_log(action: str, pkgs: list[str], lines: list[str]):
    for pkg in pkgs:
        if action == "install" and pkg not in lines:
            lines.append(pkg)
            print(f"✅ added {pkg}")

        elif action == "remove" and pkg in lines:
            lines.remove(pkg)
            print(f"✅ removed {pkg}")

    lines.sort()


# -------------------------
# PACKAGE ACTION
# -------------------------
def run_pkg_action(action: str, pkgs: list[str], lines: list[str]):
    if which("nala"):
        pkg_manager = "nala"
    elif which("pkg"):
        pkg_manager = "pkg"
    else:
        print("No supported package manager found")
        exit(1)

    try:
        run([pkg_manager, action, "-y", *pkgs], check=True)

    except CalledProcessError:
        print("❌ Package manager failed, log not updated")
        exit(1)

    track_log(action, pkgs, lines)


def main():
    # -------------------------
    # CLI ARGUMENTS
    # -------------------------
    if len(argv) < 3 or argv[1] not in ("install", "remove"):
        print("❗ Usage: python main.py <install|remove> <package...>")
        exit(1)

    action = argv[1]
    pkgs = argv[2:]

    # -------------------------
    # LOG FILE SETUP
    # -------------------------
    log_file = Path().home() / ".local/pkgs.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    log_file.touch()

    lines = sorted(set({
        line.strip()
        for line in log_file.read_text().splitlines()
        if line.strip()
    }))

    # -------------------------
    # RUN
    # -------------------------
    run_pkg_action(action, pkgs, lines)
    log_file.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r\n⛔ Operation cancelled by user")
        exit(130)
