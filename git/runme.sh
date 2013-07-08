#!/bin/bash

txts=('what-is-git.txt' 'why-use-git.txt' 'commit-hash.txt' 'why-branch.txt' 'gitignore.txt' '../.gitignore')

length=${#txts[@]}
i=0

while read -e -p "> " input; do
    if [ -z "$input" ]; then
        if [[ $i -lt $length ]]; then
            cat ${txts[$i]}
            echo ""
            i=$((i+1))
        fi
    else
        $input
    fi
done

commands=('init.sh' 'config.sh' 'add.sh' 'status.sh' 'commit.sh' 'remote.sh' 'push.sh' 'clone.sh' 'log.sh' 'branch.sh' 'checkout.sh' 'fetch.sh' 'merge.sh' 'rm.sh' 'pull.sh' 'diff.sh' 'whatchanged.sh' 'blame.sh' 'stash.sh' 'reset.sh')

length=${#commands[@]}
i=0

while read -e -p "> " input; do
    if [ -z "$input" ]; then
        if [[ $i -lt $length ]]; then
            ./${commands[$i]}
            echo ""
            i=$((i+1))
        else
            exit
        fi
    else
        $input
    fi
done
