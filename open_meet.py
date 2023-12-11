from plyer import notification
import time

timings = []

while True:
    curr_time = str(time.strftime("%H:%M", time.localtime()))
    
    if curr_time in timings:        
        notification.notify(
            title = "Meeting now!",
            message = "Enter message details",
            app_icon = "logo.ico",
            timeout = 10
        )

        time.sleep(10)
