import pyautogui
import pygetwindow as gw
import time

# Saved window center (x, y) for other modules to use. Set by goto_game().
WINDOW_CENTER = None

def goto_game():
    """
    Finds the active window and moves the mouse to the center.
    """
    print("\n--- Function: goto_game() ---")
    
    try:
        time.sleep(0.5)

        activeWindow = gw.getActiveWindow()
        if not activeWindow:
            print("[FAILURE] Could not find an active window.")
            return

        print(f"Found active window: '{activeWindow.title}'")
    except Exception as e:
        print(f"[ERROR] Exception occurred while getting active window: {e}")
        return
        
    # Move to the center of the active window and save it globally
    window_center_x, window_center_y = activeWindow.center
    print(f"Moving to window center at: ({window_center_x}, {window_center_y})")
    pyautogui.moveTo(window_center_x, window_center_y, duration=0.1)

    # Set module-level WINDOW_CENTER so other modules can reference it
    global WINDOW_CENTER
    WINDOW_CENTER = (window_center_x, window_center_y)
        
    print("[SUCCESS] Game start sequence complete.")
    
def click(target_x, target_y):
    pyautogui.click(target_x, target_y)
    

if __name__ == "__main__":
    print("Running gameStart.py directly for testing...")
    goto_game()
    print(f"Saved WINDOW_CENTER: {WINDOW_CENTER}")

def get_window_center():
    """
    Returns the last saved window center as a (x, y) tuple, or None if not set.
    """
    return WINDOW_CENTER