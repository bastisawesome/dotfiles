alias ls='ls --color=auto'
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'
alias ping='ping -c 20 $@'
alias genpass='python -c "import uuid; print(uuid.uuid4().hex)"'
alias java8='/usr/lib/jvm/java-8-jdk/bin/java'
alias pyc='python -m compileall'

# Safety features
alias cp='cp -i'
alias rm='rm -i'
alias mv='mv -i'
