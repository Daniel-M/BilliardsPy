#!/bin/bash
target=trayecto.gif
ffmpeg -i $target $target.mp4
rename 's/.gif.mp4/.mp4/' *.mp4
