#!/data/data/com.termux/files/usr/bin/bash

termux-change-repo
pkg update && yes | pkg upgrade -y

curl -LO "https://raw.githubusercontent.com/riteshtheone/config/refs/heads/main/dist/setup"

chmod +x setup
./setup

rm setup
