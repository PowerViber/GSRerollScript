import findEmu
import funcs
import time
import sys

def main():
    """
    Main function to run the automation.
    """
    print("===== Running init.py =====\n")
    
    game_window = findEmu.find_emulator()
    
    if not game_window:
        print("\nEmulator not found. Exiting script.")
        sys.exit(1) 

    print("\nEmulator found, proceeding to start game...")
    time.sleep(1) 
    
    if not funcs.goto_game():
        print("\nGame start sequence failed. Exiting script.")
        sys.exit(1)

    print("\nGame is running. Proceeding to main game logic...")    
    print("\n===== Script finished =====")


if __name__ == "__main__":
    main()