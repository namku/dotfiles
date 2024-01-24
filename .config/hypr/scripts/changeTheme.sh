#!/bin/sh

#chosen=$(printf "Power Off\nRestart" | wofi --conf ~/.config/hypr/wofi/config --style ~/.config/hypr/wofi/style.    css --color ~/.config/hypr/wofi/colors -dmenu -i)
#

chosen=$(printf "Retro\nPink" | wofi -dmen -i --conf ~/.config/hypr/wofi/config --style ~/.config/hypr/wofi/style.css --color ~/.config/hypr/wofi/colors)

case "$chosen" in
  "Retro") 
    killall swaybg && swaybg --output '*' --mode fill --image ~/.config/hypr/wallpapers/retro.jpg
    sed -i 's/col.active_border.*$/col.active_border = rgba(33ccffee) rgba(00ff99ee) 45deg/g' /home/nham/.config/hypr/hyprland.conf
    ;;
  "Pink") 
    killall swaybg && swaybg --output '*' --mode fill --image ~/.config/hypr/wallpapers/wallpaper.png
    sed -i 's/col.active_border.*$/col.active_border = rgba(f5f5dcee) rgba(626258ee) 45deg/g' /home/nham/.config/hypr/hyprland.conf
    ;;
  *) exit 1
    ;;
esac
