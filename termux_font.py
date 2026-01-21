import requests
from pathlib import Path
from tqdm import tqdm
from subprocess import run


def main():
    fonts = {
        "font.ttf": "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/JetBrainsMono/NoLigatures/Regular/JetBrainsMonoNLNerdFont-Regular.ttf",
        "font-italic.ttf": "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/JetBrainsMono/NoLigatures/Italic/JetBrainsMonoNLNerdFont-Italic.ttf",
        "font-bold.ttf": "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/JetBrainsMono/NoLigatures/Bold/JetBrainsMonoNLNerdFont-Bold.ttf",
        "font-bold-italic.ttf": "https://raw.githubusercontent.com/ryanoasis/nerd-fonts/master/patched-fonts/JetBrainsMono/NoLigatures/BoldItalic/JetBrainsMonoNLNerdFont-BoldItalic.ttf",
    }

    downloaded_fonts = []

    for name, url in fonts.items():
        r = requests.get(url, stream=True)
        total = int(r.headers.get("content-length", 0))

        path = Path(name)
        downloaded_fonts.append(path)

        with path.open("wb") as f, tqdm(
            desc=name,
            total=total,
            unit="B",
            unit_scale=True,
        ) as bar:
            for chunk in r.iter_content(8192):
                f.write(chunk)
                bar.update(len(chunk))

    fonts_dir = Path().home() / ".termux"
    fonts_dir.mkdir(exist_ok=True)

    green, yellow, reset = "\033[92m", "\033[33m", "\033[0m"
    for path in downloaded_fonts:
        dest = fonts_dir / path.name
        path.replace(dest)
        print(f"{green}{path.name} {yellow}-> {green}{dest}{reset}")

    run(["termux-reload-settings"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\r\n⛔ Operation cancelled by user")
        exit(130)
