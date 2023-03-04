# Just an ameteur coding, nothing to see here
import sys, subprocess

def trybr(brin):
    if brin > 1 or brin < 0.1:
        print("Input Out of Range")
        exit()

if len(sys.argv) < 3:
    print("Not enough arguments")
    exit()

def check_arg():
    if (sys.argv[1] != "+") and (sys.argv[1] != "-") and (sys.argv[1] != "="):
        print("Operation not found")
        exit()
    try:
        float(sys.argv[2])
    except ValueError:
        print("Argument format is incorrect")
        exit()

check_arg()
br = round(float(sys.argv[2]), 1)
brold = float(subprocess.check_output("xrandr --verbose| grep -m 1 -i brightness | cut -f2 -d ' '", shell=True).decode("utf-8").replace("\n",""))

if sys.argv[1] == "+":
    brnew=brold+br
    trybr(brnew)
    subprocess.run("xrandr --output eDP-1 --brightness "+str(brnew) , shell=True)
elif sys.argv[1] == "-":
    brnew=brold-br
    trybr(brnew)
    subprocess.run("xrandr --output eDP-1 --brightness "+str(brnew) , shell=True)
elif sys.argv[1] == "=":
    trybr(br)
    subprocess.run("xrandr --output eDP-1 --brightness "+str(br) , shell=True)
else:
    print("Syntax error")

