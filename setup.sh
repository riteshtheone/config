#!/data/data/com.termux/files/usr/bin/bash

termux-change-repo
pkg update && yes N | pkg upgrade -y
curl -LO https://raw.githubusercontent.com/riteshtheone/config/refs/heads/main/setup.py
