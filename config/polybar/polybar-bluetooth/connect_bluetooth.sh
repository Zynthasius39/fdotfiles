bluetoothctl connect $(bluetoothctl devices Trusted | grep -o -E '([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}')
