if status is-interactive
    fish_add_path /home/denis/.local/bin
    fish_add_path /home/denis/code/spark-3.5.6-bin-hadoop3/bin
    
    # Commands to run in interactive sessions can go here
    set -U fish_user_paths $fish_user_paths ~/.local/bin ~/code/espanso/target/release/
    set -U XDG_CONFIG_HOME $HOME/.config
    set -x SPARK_LOCAL_IP 127.0.0.1
    set -x JAVA_HOME /usr/lib/jvm/openjdk17

    abbr --add cat bat
    abbr --add cdw 'cd $HOME/code/website/_posts'
    abbr --add dcb 'docker-compose build'
    abbr --add dcbn 'docker-compose build --no-cache'
    abbr --add dcd 'docker-compose down'
    abbr --add dci 'docker rmi -f (docker images -qf dangling=true)'
    abbr --add dcu 'docker-compose up'
    abbr --add dcuf 'docker-compose up --force-recreate'
    abbr --add de 'docker exec -it'
    abbr --add dps 'docker ps'
    abbr --add ga 'git add'
    abbr --add gl "git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
    abbr --add gb 'git branch'
    abbr --add gc 'git commit -m'
    abbr --add gca 'git commit --amend'
    abbr --add gch 'git checkout'
    abbr --add gcr 'git commit --rebase'
    abbr --add gd 'git diff'
    abbr --add gp 'git push'
    abbr --add gpr 'git pull --rebase'
    abbr --add gs 'git status'
    abbr --add v 'nvim .'
    abbr --add w 'nvim . -c "Goyo" -c "Limelight" -c "set wrap"'
    abbr --add ya 'yadm add'
    abbr --add yc 'yadm commit -m'
    abbr --add yp 'yadm push'
    abbr --add ypr 'yadm pull --rebase'
    abbr --add ys 'yadm status'
    abbr --add yd 'yadm diff'
    abbr --add yl "yadm log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
    abbr --add quaderno '$HOME/.local/bin/dptrp1 --addr 192.168.178.56'
    abbr --add reboot 'loginctl reboot'
    abbr --add poweroff 'loginctl poweroff'
end

fish_vi_key_bindings


function fish_user_key_bindings
    for mode in insert default visual
        bind -M $mode \cf forward-char
    end
end

# suppress greeting
set fish_greeting

# >>> coursier install directory >>>
set -gx PATH "$PATH:/home/denis/.local/share/coursier/bin"
# <<< coursier install directory <<<
