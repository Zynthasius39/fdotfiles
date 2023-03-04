#!/bin/sh
if [ $(bluetoothctl show | grep "Powered: yes" | wc -c) -eq 0 ]
then
  echo "%{T2}%{F#A290D5}󰂲"
else
  if [ $(echo info | bluetoothctl | grep 'Device' | wc -c) -eq 0 ]
  then 
    echo "%{T2}%{F#608BCF}󰂯"
  fi
  echo "%{T2}%{F#608BCF}󰂱"
fi

