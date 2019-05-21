#!/bin/bash

# git
git config --global user.name "yumemo"
git config --global user.email "hogehoge@gmail.com"
git config --global core.editor 'vim -c "set fenc=utf-8"'
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto
git config --global alias.st status
git config --global alias.ct commit
git config --global alias.co checkout
git config --global alias.reh "reset --hard HEAD^"

# bash
cat ./bash_alias.txt >> ~/.bashrc
