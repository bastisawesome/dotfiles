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

alias emacs="emacsclient -a 'nvim' -c"
alias vim='nvim'

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
	PATH=$PATH:$HOME/.config/emacs/bin
fi

HISTCONTROL=ignoredups:erasedups

#export WORKON_HOME=~/.virtualenvs
#source /usr/bin/virtualenvwrapper.sh

if [[ -f ~/.config/.pythonrc.py ]]; then
    export PYTHONSTARTUP=~/.config/.pythonrc.py
fi

if hash pipenv 2>/dev/null; then
    eval  "$(_PIPENV_COMPLETE=bash_source pipenv)"
fi

export DOTBARE_DIR=dotfiles
