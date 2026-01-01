#!/bin/bash

# Rename original images
cd ~/Desktop/Gameshow/images/original
counter=1
ls -1 *.png 2>/dev/null | sort | while IFS= read -r file; do
    mv "$file" "${counter}.png"
    counter=$((counter + 1))
done

# Rename altered images
cd ~/Desktop/Gameshow/images/altered
counter=1
ls -1 *.png 2>/dev/null | sort | while IFS= read -r file; do
    mv "$file" "${counter}.png"
    counter=$((counter + 1))
done

echo "Images renamed successfully!"
