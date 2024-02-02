#!/bin/bash

atira="$1"
echo    "Plotting $atira. Please wait..."
echo -n "Combination: "


for i in {001..243}; do
    echo -n "$i ";
    csv="${atira}_${i}_N.csv";
    python3 csvEIPlot.py "$csv";
    python3 csvLogPlot.py "$csv";
    python3 csvNormalPlot.py "$csv";
done

echo "Done."
