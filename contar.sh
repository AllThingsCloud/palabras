#!/bin/bash

file="palex.out"
count=0
current_word=""
found_definitions=false

while IFS= read -r line
do
    # Check if line contains only letters (a word)
    if [[ "$line" =~ ^[[:alpha:]]+$ ]]; then
        if [[ -z "$current_word" ]]; then
            # First occurrence of a word
            current_word="$line"
        elif [[ "$line" == "$current_word" ]]; then
            # Second occurrence of the same word - pattern found!
            ((count++))
            current_word=""
        else
            # Different word - reset
            current_word="$line"
        fi
    fi
done < "$file"

echo "Number of word-definitions-word patterns: $count"
