#!/bin/bash
objetivo=graficar.dat
python billiard.py > $objetivo
sed -i '{s/\[//g;s/\]//g}' $objetivo
