# Just an ameteur coding, nothing to see here

VOL=$(expr $(pamixer --get-volume) + $(($1)))
if [ $VOL -gt 150 ]; then
	echo "Max Volume reached"
	exit
fi
pactl -- set-sink-volume 0 $VOL%
