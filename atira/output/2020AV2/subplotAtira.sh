#!/bin/bash

atira="$1"
forms="$2"
echo    "Plotting $atira. Please wait..."
echo -n "Combination: "


for i in {001..243}; do
    echo -n "$i ";
    csv="${atira}_${i}_N.csv";
    python3 subLogPlots.py "$csv" "$forms";
    python3 subNormalPlots.py "$csv" "$forms";
done

echo "Done."
