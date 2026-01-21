import requests
from pathlib import Path
from tqdm import tqdm
from zipfile import ZipFile
from shutil import rmtree


def download_file(file: str, url: str):
    r = requests.get(url, stream=True)
    total = int(r.headers.get("content-length", 0))

    path = Path(file)

    with path.open("wb") as f, tqdm(
        desc=file,
        total=total,
        unit="B",
        unit_scale=True,
    ) as bar:
        for chunk in r.iter_content(8192):
            f.write(chunk)
            bar.update(len(chunk))


def main():
    repo = "config-main"
    file = f"{repo}.zip"
    url = "https://github.com/riteshtheone/config/archive/refs/heads/main.zip"

    file_path = Path(file)
    repo_path = Path(repo)

    if not file_path.exists():
        download_file(file, url)

    with ZipFile(file_path) as z:
        z.extractall()

    home = Path().home()
    dest = home / ".config"
    config = repo_path / "config"

    green, yellow, reset = "\033[92m", "\033[33m", "\033[0m"

    for p in config.rglob("*"):
        if p.is_file():
            dest_path = dest / p.relative_to(config)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            p.replace(dest_path)
            print(f"{green}{p.name} {yellow}-> {green}{dest_path}{reset}")

    local_bin = home / ".local/bin"
    local_bin.mkdir(exist_ok=True)
    (repo_path / "dist/pkgs").replace(local_bin / "pkgs")
    print(f"{green}pkgs {yellow}-> {green}{local_bin / "pkgs"}{reset}")

    file_path.unlink()
    rmtree(repo_path)


if __name__ == "__main__":
    main()
