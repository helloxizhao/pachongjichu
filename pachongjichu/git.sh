#!/bin/bash
git remote add git@github.com:helloxizhao/$1.git
git add ./*
git commit -m  "commit $1"
git push origin master
