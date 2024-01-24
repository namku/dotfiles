#!/bin/sh

#chosen=$(printf "Power Off\nRestart" | wofi --conf ~/.config/hypr/wofi/config --style ~/.config/hypr/wofi/style.    css --color ~/.config/hypr/wofi/colors -dmenu -i)
#

chosen=$(printf "Orig\nTest" | wofi -dmen -i --conf ~/.config/hypr/wofi/config --style ~/.config/hypr/wofi/style.css --color ~/.config/hypr/wofi/colors)

case "$chosen" in
  "Orig") killall swaybg && swaybg --output '*' --mode fill --image ~/.config/hypr/wallpapers/01-wall.jpg ;;
  "Test") killall swaybg && swaybg --output '*' --mode fill --image ~/.config/hypr/wallpapers/wallpaper.png ;;
  *) exit 1 ;;
esac
