import requests
from pathlib import Path
from tqdm import tqdm
import zipfile
# from shutil import rmtree


def download_file(name: str, url: str):
    r = requests.get(url, stream=True)
    total = int(r.headers.get("content-length", 0))

    path = Path(name)

    with path.open("wb") as f, tqdm(
        desc=name,
        total=total,
        unit="B",
        unit_scale=True,
    ) as bar:
        for chunk in r.iter_content(8192):
            f.write(chunk)
            bar.update(len(chunk))
    pass


def main():
    dir = "repo_main"
    file = f"{dir}.zip"
    url = "https://github.com/riteshtheone/config/archive/refs/heads/main.zip"

    zip_path = Path(file)
    repo_path = Path(dir)
    repo_path.mkdir(exist_ok=True)

    if not zip_path.exists():
        download_file(file, url)

    with zipfile.ZipFile(zip_path) as z:
        z.extractall(repo_path)

    print(f"Extracted {zip_path} -> {repo_path}")
    # zip_path.unlink()

    config_path = repo_path / "config"

    for p in config_path.iterdir():
        print(p)

    # home = Path().home()
    # bin = home / ".local/bin"
    # config = home / ".config"
    #
    # (home / ".local/bin").mkdir(exist_ok=True)
    # (config / "").mkdir(exist_ok=True)
    #
    pass


if __name__ == "__main__":
    main()
