# Just an ameteur coding, nothing to see here

LANG=$(setxkbmap -query | grep layout)

if [ "$LANG" = "layout:     us" ]; then
	setxkbmap az
elif [ "$LANG" = "layout:     az" ]; then
	setxkbmap ru
elif [ "$LANG" = "layout:     ru" ]; then
	setxkbmap us
else
	echo "lang crashed"
fi
