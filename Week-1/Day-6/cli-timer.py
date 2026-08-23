import time
from plyer import notification
from playsound import playsound

WORK_MIN = 1
BREAK_MIN = 5
LONG_BREAK_MIN = 15
CYCLES_BEFORE_LONG_BREAK = 4

def notify(title, message, sound_file=None):
    notification.notify(
        title=title,
        message=message,
        timeout=10  # seconds the notification stays visible
    )

    if sound_file:
        playsound(sound_file)

def countdown(minutes, label):
    print(f"{label} started for {minutes} minutes...")
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"\r{label}: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1
    print()

def pomodoro():
    cycle = 1
    while True:
        countdown(WORK_MIN, f"Work session {cycle}")
        notify("Pomodoro", f"Work session {cycle} done! Take a break.")

        if cycle % CYCLES_BEFORE_LONG_BREAK == 0:
            countdown(LONG_BREAK_MIN, "Long break")
            notify("Pomodoro", "Long break over. Back to work!")
        else:
            countdown(BREAK_MIN, "Short break")
            notify("Pomodoro", "Break over. Back to work!")

        cycle += 1

if __name__ == "__main__":
    try:
        pomodoro()
    except KeyboardInterrupt:
        print("\nPomodoro timer stopped.")