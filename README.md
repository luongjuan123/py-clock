# Clock & Stopwatch

## Description
This project is a Python-based graphical clock with a built-in stopwatch. It features an analog clock displaying the current time with hour, minute, and second hands, along with a stopwatch that includes start, stop, and reset functionalities. A ticking sound is played every second while the stopwatch is running, enhancing the user experience.

## Overview
This Python program creates a graphical clock with an analog display and a stopwatch feature using Tkinter. The clock shows the current time with hour, minute, and second hands, while the stopwatch includes start, stop, and reset functions. Additionally, the stopwatch produces a ticking sound every second when running.

## Features
- **Analog Clock**: Displays current time with hour, minute, and second hands.
- **Numbered Clock Face**: Shows numbers 1-12 for better readability.
- **Stopwatch**: Start, stop, and reset functionality.
- **Ticking Sound**: Plays a beep sound every second when the stopwatch is running.

## Requirements
- Python 3.x
- Tkinter (built-in with Python)
- `winsound` module (for Windows sound effects)

## Installation
1. Ensure you have Python installed on your system.
2. Copy the script into a Python file (e.g., `clock.py`).
3. Run the script using:
   ```sh
   python clock.py
   ```

## Usage
- The program starts with an analog clock displaying the current time.
- Use the **Start** button to begin the stopwatch.
- Use the **Stop** button to pause the stopwatch.
- Use the **Reset** button to reset the stopwatch to `00:00:00`.

## Notes
- The `winsound.Beep` function is used for the ticking sound and works only on Windows. On other operating systems, you may need to replace it with a different sound library.

## License
This project is open-source and free to use.

