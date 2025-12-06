#!/bin/bash
performance &
lxqt-config-monitor -l & #monitor-start
bluefilter & #blue-filter
xset s off -dpms & #hibernator
okr & 
picom &
BACKLIGHT=$(ls /sys/class/backlight/ | head -n1) && MAX=$(cat /sys/class/backlight/$BACKLIGHT/max_brightness) && echo $MAX | sudo tee /sys/class/backlight/$BACKLIGHT/brightness &
