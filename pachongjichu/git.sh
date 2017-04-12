#!/bin/bash
if [ $# -eq  1 ];then
    git remote add origin git@github.com:helloxizhao/$1.git
    git add ./*
    git commit -m  "commit $1"
    git push origin master
else echo "Usage $(basename $0)" git_project_name
fi
