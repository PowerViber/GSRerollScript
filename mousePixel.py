import pyautogui
import time
import sys

# ----------------------------------------------------------------
# PART 2: LIVE PIXEL TRACKER
# ----------------------------------------------------------------
try:
    while True:
        # 1. Get the current X, Y coordinates of the mouse
        x, y = pyautogui.position()

        # 2. Get the RGB color of the pixel at that location
        rgb_color = pyautogui.pixel(x, y)
        
        # 3. Format the output string
        output = f"  Mouse Position: (X: {x:4d}, Y: {y:4d}) | RGB Color: {str(rgb_color):15s}  "
        
        # 4. Print the output
        # We use \r to return to the start of the line (carriage return)
        # and end="" to prevent it from printing a new line each time.
        # sys.stdout.flush() ensures it prints immediately.
        sys.stdout.write('\r' + output)
        sys.stdout.flush()

        # Wait a very short time so we don't spam the CPU
        time.sleep(0.05) 

except KeyboardInterrupt:
    # This block runs when you press Ctrl+C
    print("\n\nScript stopped.")
except Exception as e:
    print(f"\nAn error occurred: {e}")