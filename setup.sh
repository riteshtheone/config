#!/data/data/com.termux/files/usr/bin/bash

yes N | pkg update
termux-change-repo
# termux-setup-storage

pkg update && pkg upgrade -y
