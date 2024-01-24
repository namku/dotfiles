#!/bin/sh

chosen=$(printf "Retro\nPink" | wofi -dmen -i --conf ~/.config/hypr/wofi/config --style ~/.config/hypr/wofi/style.css --color ~/.config/hypr/wofi/colors)

case "$chosen" in
  "Retro") 
    cp /home/nham/.config/hypr/waybar/style_retro.css /home/nham/.config/hypr/waybar/style.css
    killall -9 waybar && /home/nham/.config/hypr/scripts/statusbar &
    sed -i 's/col.active_border.*$/col.active_border = rgba(f5f5dcee) rgba(626258ee) 45deg/g' /home/nham/.config/hypr/hyprland.conf
    sed -i 's/swaybg.*$/swaybg --output "*" --mode fill --image ~\/.config\/hypr\/wallpapers\/sheet.jpg \&/g' /home/nham/.config/hypr/scripts/startup
    killall swaybg && swaybg --output '*' --mode fill --image ~/.config/hypr/wallpapers/sheet.jpg
    ;;
  "Pink") 
    cp /home/nham/.config/hypr/waybar/style_pink.css /home/nham/.config/hypr/waybar/style.css
    killall -9 waybar && /home/nham/.config/hypr/scripts/statusbar &
    sed -i 's/col.active_border.*$/col.active_border = rgba(33ccffee) rgba(00ff99ee) 45deg/g' /home/nham/.config/hypr/hyprland.conf
    sed -i 's/swaybg.*$/swaybg --output "*" --mode fill --image ~\/.config\/hypr\/wallpapers\/wallpaper.png \&/g' /home/nham/.config/hypr/scripts/startup
    killall swaybg && swaybg --output '*' --mode fill --image ~/.config/hypr/wallpapers/wallpaper.png 
    ;;
  *) exit 1
    ;;
esac
