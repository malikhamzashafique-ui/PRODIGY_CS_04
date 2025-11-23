Project Overview

This project implements a simple, educational keylogger using Python and the pynput library.
The keylogger captures keystrokes and stores them in a local text file (keylog.txt) for analysis.

Disclaimer:
This keylogger is strictly for educational and authorized testing purposes only.
Running a keylogger on any system without explicit permission is illegal and unethical.

Features

Real-time keystroke logging
Captures letters, numbers, and symbols as they are typed.

Special key handling
Properly logs keys such as Enter, Space, Tab, Shift, Backspace, etc.

Timestamp-based logging
Each keystroke entry is tagged with the current date and time.

Safe termination
Pressing the Esc key immediately stops the program and saves the log.

Technologies Used

Python 3.x

pynput library for keyboard event listening

datetime module for timestamping logs

To install dependencies:

pip install pynput

How It Works

The script initializes a global log file (keylog.txt).

A keyboard.Listener monitors every key press and release.

When a key is pressed:

Printable characters are recorded directly.

Special keys are converted to readable formats (e.g., [Key.shift], new lines, spaces).

Press Esc to stop the listener and safely close the program.

Usage Instructions

Install Python and required libraries.

Place the script in your desired folder.

Run the script:

python keylogger.py


Start typing—logs will be saved automatically.

Press Esc to stop the keylogger.

Open keylog.txt to view captured keystrokes.

Log File Format (keylog.txt)

Example output:

hello world
[Key.shift] H [Key.shift]
python   programming

Ethical and Legal Considerations

Keyloggers can collect sensitive information such as:

Passwords

Personal messages

Banking details

Therefore:

Use only with full permission from the system owner.

Do not deploy on public, shared, or unauthorized systems.

Violating these rules may result in legal action.

Support

If you need help understanding the code or improving it, feel free to ask.  