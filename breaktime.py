import time
import webbrowser

total_breaks = 3
break_count =0

print("This program started on"+ time.ctime())
while (break_count<=total_breaks):
    time.sleep(10)
    webbrowser.open_new("https://www.youtube.com/watch?v=1tVL11ULjYY")
    break_count = break_count + 1
