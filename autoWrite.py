import keyboard
import pyautogui
import pygetwindow as gw
import time
import threading
import win32gui
import win32con
import sys

def enter():
    keyboard.send("enter")
def bring_window_to_foreground(window_title):

    try:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

            win32gui.SetForegroundWindow(hwnd)
            print(f"Window '{window_title}' brought to the foreground.")
    except Exception as e:
        print(f"Error bringing window to foreground: {e}")
def monitor_and_click(target_window_title, x_offset=10, y_offset=10, check_interval=1, stop_event=None):

    print(f"Monitoring for window: '{target_window_title}'...")
    window_brought_to_foreground = False 

    while not stop_event.is_set():  
        try:

            hwnd = win32gui.FindWindow(None, target_window_title)

            if hwnd:
                if not window_brought_to_foreground:

                    bring_window_to_foreground(target_window_title)
                    window_brought_to_foreground = True

                foreground_hwnd = win32gui.GetForegroundWindow()
                if hwnd == foreground_hwnd:

                    rect = win32gui.GetWindowRect(hwnd)
                    x = rect[0] + x_offset
                    y = rect[1] + y_offset



                    pyautogui.moveTo(x, y, duration=0.5)  
                    pyautogui.click()
                    time.sleep(10)
                    enter()
                    keyboard.write("Hi im a bot made by the player using me! He is away at the  moment but will be back for selection of champs if you want to swap dont bother i wont accept it! I will ban caitlyn for him!")
                    enter()
                else:
                    print(f"Window '{target_window_title}' is not in the foreground. Skipping click.")
            else:

                window_brought_to_foreground = False

            time.sleep(check_interval)
        except Exception as e:
            print(f"Error during monitoring: {e}")

def is_window_in_foreground(window_title):

    try:
        hwnd = win32gui.FindWindow(None, window_title)
        foreground_hwnd = win32gui.GetForegroundWindow()
        return hwnd == foreground_hwnd
    except Exception as e:
        print(f"Error checking foreground window: {e}")
        return False


if __name__ == "__main__":

    target_window_title = "League of Legends"

    x_offset = 450
    y_offset = 430

    check_interval = 1  

    stop_event = threading.Event()

    bot_thread = threading.Thread(target=monitor_and_click, args=(target_window_title, x_offset, y_offset, check_interval, stop_event))
    bot_thread.start()

    print("Bot is running in the background. Press Ctrl+C to stop.")

    try:
        while bot_thread.is_alive():  
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping the bot...")
        stop_event.set() 
        bot_thread.join()  
        print("Bot stopped. Exiting program.")
        sys.exit(0)
