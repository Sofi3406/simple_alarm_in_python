# alarm_clock
import time
import winsound  
alarm_time = input("Enter the alarm time (HH:MM, 24-hour format): ")

print(f"Waiting for alarm at {alarm_time}... ⏳")

while True:
    current_time = time.strftime("%H:%M")
    
    if current_time == alarm_time:
        print("Wake up, Wake up, Wake up! 🔔🔔🔔")
    
        for _ in range(3):
            winsound.Beep(1000, 1000) 
        break

    time.sleep(60)
