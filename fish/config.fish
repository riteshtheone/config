if status is-interactive
    set -g fish_greeting
    function fish_prompt
        set_color --bold green
        echo -n (whoami)

        set_color --bold white
        echo -n '@'

        set_color --bold yellow
        echo -n 'linux'

        set_color --bold white
        echo -n ':'

        set_color --bold blue
        echo -n (prompt_pwd)
        echo -n ' $ '
        set_color normal
    end

    set -Ux EDITOR hx
    fish_add_path $HOME/.local/bin

    alias c='clear'
    alias e='exit'
    alias t='tmux'
    alias y='yazi'

    alias get_idf='. $HOME/.local/opt/esp-idf/export.fish'

    alias l='eza -l --icons --group-directories-first'
    alias la='eza -la --icons --group-directories-first'
    alias lt='eza --tree --icons --group-directories-first'
end
