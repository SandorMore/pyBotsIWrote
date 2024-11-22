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
    """
    Brings the specified window to the foreground if it exists.
    
    :param window_title: The title of the window to bring to the foreground
    """
    try:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

            win32gui.SetForegroundWindow(hwnd)

    except Exception as e:
        print(f"Error bringing window to foreground: {e}")
enter()
keyboard.write("Hi i'm a bot made by the player using me! He is probably AFK right now peeing or some shit so dont even bother swapping he will be back in a minute! I will ban cait for him in the meanwhile! FUCK CAITLYN FUCK CAITLYN FUCK CAITLYN FUCK CAITLYN FUCK CAITLYN FUCK CAITLYN FUCK CAITLYN FUCK CAITLYN FUCK CAITLYN")
enter()
