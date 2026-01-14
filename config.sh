mkdir -p $HOME/.config/fish
mkdir -p $HOME/.config/helix
mkdir -p $HOME/.config/yazi
mkdir -p $HOME/.config/tmux

echo "✅ Config directories ensured"

cp ./fish/config.fish $HOME/.config/fish
cp ./helix/config.toml $HOME/.config/helix
cp ./helix/languages.toml $HOME/.config/helix
cp ./yazi/yazi.toml $HOME/.config/yazi
cp ./tmux/tmux.conf $HOME/.config/tmux

echo "🎉 All done!"
