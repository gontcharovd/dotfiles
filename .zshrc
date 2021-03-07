export LANG=en_US.UTF-8
export LC_MESSAGES="C"

export TERM=xterm-kitty

# editor used by cron
export VISUAL=vim

# tmuxp
export DISABLE_AUTO_TITLE='true'

alias python=python3.8

export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="risto"
HIST_STAMPS="dd.mm.yyyy"
plugins=(git)
source $ZSH/oh-my-zsh.sh

alias v="vim ."

alias gs="git status"
alias ga="git add"
alias gsa="git submodule add"
alias gc="git commit -m"
alias gca="git commit --amend"
alias gd="git diff"
alias gl="git log --graph --all --pretty=format:'%C(yellow)%h -%C(auto)%d %C(bold cyan)%s %C(bold white)(%cr)%Creset %C(dim white)<%an>'"  
alias gpr="git pull --rebase"
alias gp="git push"
alias gch="git checkout"

alias dps="docker ps"
alias dcu="docker-compose up"
alias dcuf="docker-compose up --force-recreate"
alias dcd="docker-compose down"
alias dcb="sudo docker-compose build"
alias dcbn="sudo docker-compose build --no-cache"

di() {
    docker inspect $1
}

de() {
    docker exec -it "$1" "$2"
}

PATH=$PATH:~/.local/bin
PATH=$PATH:~/.gem/ruby/2.7.0/bin

# switch keyboard layouts
setxkbmap -model hhk -layout us,de -option grp:lalt_lshift_toggle

# kitty
autoload -Uz compinit
compinit
kitty + complete setup zsh | source /dev/stdin

cd $HOME
clear
