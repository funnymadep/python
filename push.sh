#!/bin/bash

if [ -n $1 ];then
  git add .
  git commit -m $1 
  git push 
fi

