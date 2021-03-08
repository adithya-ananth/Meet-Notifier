from win10toast import ToastNotifier
import time

timings = ["08:00", "08:50", "09:40", "10:30", "11:30", "12:20"]

while True:
    curr_time = str(time.strftime("%H:%M", time.localtime()))
    
    if curr_time in timings:
        toast = ToastNotifier()
        toast.show_toast("Time for Class!", "You have a google meet class now", duration=3000, icon_path='logo.ico')