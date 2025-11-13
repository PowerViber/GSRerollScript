import pygetwindow as gw
import time
import sys

# --- Settings (you can adjust these) ---
# !!! IMPORTANT !!!
# Change this to the title of your game window.
# It can be a partial match (e.g., "BlueStacks" will find "BlueStacks App Player")
GAME_WINDOW_TITLE = "Grand Summoners - A" 

def find_emulator():
    """
    Scans for a window with a matching title and activates it.
    Returns True if found and activated, False otherwise.
    """
    print("--- Function: find_emulator() ---")
    print(f"Searching for window with title containing: '{GAME_WINDOW_TITLE}'")

    try:
        # Find all windows that contain the title
        windows = gw.getWindowsWithTitle(GAME_WINDOW_TITLE)
        
        if not windows:
            print(f"\n[FAILURE] No window found with title '{GAME_WINDOW_TITLE}'.")
            print("Please make sure the game is running and the title is correct.")
            return False # Failure

        # Get the first matching window
        window = windows[0]
        print(f"\n[SUCCESS] Found window: '{window.title}'")
        
        # If window is minimized, restore it
        if window.isMinimized:
            print("Window is minimized, restoring...")
            window.restore()
        
        # Activate the window (bring it to the front)
        print("Activating window...")
        window.activate()
        
        # Give a moment for the window to come into focus
        time.sleep(0.5) 
        
        return True # Success!

    except Exception as e:
        print(f"\nAn error occurred during window search: {e}")
        return False

# This 'if __name__ == "__main__":' block means
# this code will ONLY run if you execute 'python findEmu.py' directly.
# It will NOT run when 'init.py' imports it.
if __name__ == "__main__":
    print("Running findEmu.py directly for testing...")
    print(f"Looking for: {GAME_WINDOW_TITLE}")
    if find_emulator():
        print("Test successful: Found and activated window.")
    else:
        print("Test failed: Did not find window.")