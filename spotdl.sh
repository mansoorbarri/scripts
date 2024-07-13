#!/bin/bash

if [ -z "$1" ]
then
    echo "Usage:" $0 "[URL]"
    exit 1
fi

spotdl $1 

song=$(ls *.mp3)

mv "$song" ~/Music/anar/mujik/

exit