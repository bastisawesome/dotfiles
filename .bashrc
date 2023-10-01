export TERM='xterm-256color'

HISTCONTROL=ignoredups:erasedups

export EDITOR='nvim'
export VISUAL='emacsclient -a "nvim" -c'

# Fix bug with Bat
export MANROFFOPT="-c"
export MANPAGER='sh -c "col -bx | bat -l man -p"'

[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
alias ping='ping -c 20 $@'
alias genpass='python -c "import uuid; print(uuid.uuid4().hex)"'
alias java8='/usr/lib/jvm/java-8-jdk/bin/java'
alias pyc='python -m compileall'

alias cp='cp -i'
alias rm='rm -i'
alias mv='mv -i'

alias emacs='emacsclient -a "nvim" -c'
alias vim='nvim'

alias df='df -h'
alias free='free -h'
alias psa='ps auxf'
alias psgrep='ps aux | grep -v grep | grep -i -e VSZ -e'
alias psmem='ps auxf | sort -nr -k 4'
alias pscpu='ps auxf | sort -nr -k 3'

# source /usr/share/git/completion/git-prompt.sh
# GIT_PROMPT_ENABLED=true

if ! hash starship 2>/dev/null; then
    if ! GIT_PROMPT_ENABLED; then
        export PS1="\[\e[96m\]\W\[\e[m\] \[\e[92m\]\\$\[\e[m\] \[\e[m\]\[\e[1;34m\]"
    else
        export PS1='\[\e[0;96m\]\W\[\e[0;38;5;46m\]$(__git_ps1 " %s") \[\e[0;94m\]\$ \[\e[0m\]'
    fi

else
    eval "$(starship init bash)"
fi

export PATH=$PATH:/home/bast/local/bin:/home/bast/local/opt/bin:/home/bast/.local/bin

if [ -d "$HOME/.config/emacs/bin" ]; then
	PATH="$PATH:$HOME/.config/emacs/bin"
fi

if [ -d "$HOME/.local/bin" ]; then
    PATH="$HOME/.local/bin:$PATH"
fi

if [ -d "$HOME/local/bin" ]; then
    PATH="$HOME/local/bin:$PATH"
fi

#export WORKON_HOME=~/.virtualenvs
#source /usr/bin/virtualenvwrapper.sh

if [[ -f ~/.config/.pythonrc.py ]]; then
    export PYTHONSTARTUP=~/.config/.pythonrc.py
fi

if hash pipenv 2>/dev/null; then
    eval  "$(_PIPENV_COMPLETE=bash_source pipenv)"
fi

shopt -s autocd
shopt -s cdspell
shopt -s cmdhist
shopt -s dotglob
shopt -s histappend
shopt -s expand_aliases
shopt -s checkwinsize

# Usage: ex <file>
ex() {
    if [ -f "$1" ]; then
        case $1 in
            *.tar.bz2)  tar xjf $1      ;;
            *.tar.gz)   tar xzf $1      ;;
            *.bz2)      bunzip2 $1      ;;
            *.rar)      unrar x $1      ;;
            *.gz)       gunzip $1       ;;
            *.tar)      tar xf $1       ;;
            *.tbz2)     tar xjf $1      ;;
            *.tgz)      tar xzf $1      ;;
            *.zip)      unzip $1        ;;
            *.Z)        uncompress $1   ;;
            *.7z)       7z x $1         ;;
            *.deb)      ar x $1         ;;
            *.tar.xz)   tar xf $1       ;;
            *.tar.zst)  unzstd $1       ;;
            *)          echo "'$1' cannot be extracted via ex()";;
        esac
    else
        echo "'$1' is not a valid file"
    fi
}

export DOTBARE_DIR=dotfiles
source ~/dotfiles/dotbarsource ~/dotfiles/dotbare.sh
