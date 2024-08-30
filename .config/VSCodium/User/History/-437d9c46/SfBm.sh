wallDIR="$HOME/Pictures/wallpapers"
SCRIPTSDIR="$HOME/.config/hypr/scripts"

# variables
focused_monitor=$(hyprctl monitors | awk '/^Monitor/{name=$2} /focused: yes/{print name}')
# swww transition config
FPS=60
TYPE="any"
@@ -40,8 +39,9 @@ menu() {

  for pic_path in "${sorted_options[@]}"; do
    pic_name=$(basename "$pic_path")

    # Displaying .gif to indicate animated images
    if [[ ! "$pic_name" =~ \.gif$ ]]; then
      printf "%s\x00icon\x1f%s\n" "$(echo "$pic_name" | cut -d. -f1)" "$pic_path"
    else
      printf "%s\n" "$pic_name"
@@ -54,15 +54,25 @@ swww query || swww-daemon --format xrgb

# Choice of wallpapers
main() {
  choice=$(menu | $rofi_command)

  # Trim any potential whitespace or hidden characters
  choice=$(echo "$choice" | xargs)
  RANDOM_PIC_NAME=$(echo "$RANDOM_PIC_NAME" | xargs)

  # No choice case
  if [[ -z "$choice" ]]; then
    echo "No choice selected. Exiting."
    exit 0
  fi

  # Random choice case
  if [[ "$choice" == "$RANDOM_PIC_NAME" ]]; then
	swww img -o "$focused_monitor" "$RANDOM_PIC" $SWWW_PARAMS;
    sleep 0.5
    "$SCRIPTSDIR/WallustSwww.sh"
    sleep 0.2
    "$SCRIPTSDIR/Refresh.sh"
    exit 0
  fi

@@ -77,7 +87,7 @@ main() {
  done

  if [[ $pic_index -ne -1 ]]; then
    swww img -o "$focused_monitor" "${PICS[$pic_index]}" $SWWW_PARAMS
  else
    echo "Image not found."
    exit 1
@@ -87,12 +97,14 @@ main() {
# Check if rofi is already running
if pidof rofi > /dev/null; then
  pkill rofi
  sleep 1  # Allow some time for rofi to close
fi

main

sleep 0.5
"$SCRIPTSDIR/WallustSwww.sh"

sleep 0.2
"$SCRIPTSDIR/Refresh.sh"