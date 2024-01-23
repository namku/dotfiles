#!/bin/sh

#chosen=$(printf "Power Off\nRestart" | wofi --conf ~/.config/hypr/wofi/config --style ~/.config/hypr/wofi/style.    css --color ~/.config/hypr/wofi/colors -dmenu -i)
#

chosen=$(printf "Power Off\nRestart" | wofi -dmen -i --conf ~/.config/hypr/wofi/config --style ~/.config/hypr/wofi/style.css --color ~/.config/hypr/wofi/colors)

case "$chosen" in
  "Power Off") powefoff ;;
  "Restart") reboot ;;
  *) exit 1 ;;
esac
