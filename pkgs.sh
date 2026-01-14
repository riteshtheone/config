#!/bin/sh

echo "Installing packages on Void Linux..."

# list of packages we want
pkgs="
fish-shell
eza
helix
yazi
tmux
git
neovim
clang
clang-tools-extra
base-devel
cmake
ninja
fuzzypkg
ncdu
7zip
github-cli
"

for p in $pkgs
do
   # check if package is already installed
   if xbps-query -p pkgver "$p" >/dev/null 2>&1
   then
      echo "$p is already installed"
   else
      echo "Installing $p..."
      sudo xbps-install -y "$p"
   fi
done

echo "Done!"
