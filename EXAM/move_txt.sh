#!/bin/bash
# creates a folder ‘TXT’ in home directory;
# moves there all the *.txt files from your home directory (don’t go to subdirectories);
# prints on the screen: “<*> txt files moved”, where <*> is the number of files moved.

cd $HOME
mkdir TXT
count=0

for file in $HOME/*.txt; do
    if [ -f $file ]; then # Because directories can technically have extentions here
        mv $file /$HOME/TXT
        ((count++))
    fi
done

echo $count ".txt files moved"

# Conclusions:
# I had to remind myself of bash syntax using some of my previous homework
# I haven't used mv before but we discussed it