#!/data/data/com.termux/files/usr/bin/bash

# termux-setup-storage
termux-change-repo
yes N | pkg update && yes N | pkg upgrade -y
echo "Hello Bash Script!"
