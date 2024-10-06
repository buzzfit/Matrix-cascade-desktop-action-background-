import pygame
import random
import sys
import ctypes
from ctypes import wintypes
import win32gui
import win32con
import win32api
import time

# Initialize Pygame
pygame.init()

# Get screen dimensions
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Set up the display without borders
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

# Retrieve the window handle for the Pygame window
hwnd = pygame.display.get_wm_info()['window']

# Get the Progman window
progman = win32gui.FindWindow('Progman', None)

# Send a message to Progman to spawn a WorkerW window behind desktop icons
# This is a workaround to "fool" the Windows desktop setup, making our Pygame window appear as part of the desktop background
SendMessageTimeoutW = ctypes.windll.user32.SendMessageTimeoutW
SendMessageTimeoutW.argtypes = [
    wintypes.HWND,   # hWnd
    wintypes.UINT,   # Msg
    wintypes.WPARAM, # wParam
    wintypes.LPARAM, # lParam
    wintypes.UINT,   # fuFlags
    wintypes.UINT,   # uTimeout
    ctypes.POINTER(ctypes.c_ulong)  # lpdwResult
]

# Define LRESULT
LRESULT = ctypes.c_ssize_t
SendMessageTimeoutW.restype = LRESULT

# Send message to Progman to create WorkerW
result = ctypes.c_ulong()
SendMessageTimeoutW(progman, 0x052C, 0, 0, win32con.SMTO_NORMAL, 1000, ctypes.byref(result))

# Wait for the WorkerW window to be created
time.sleep(0.1)

# Enumerate all top-level windows to find the WorkerW window
# The WorkerW window is created behind the desktop icons, which is why we need to find it
# This allows us to "attach" our Pygame window to it, giving the illusion that it's part of the desktop

def enum_windows_callback(hwnd, lParam):
    if win32gui.GetClassName(hwnd) == 'WorkerW':
        hShellViewWin = win32gui.FindWindowEx(hwnd, 0, 'SHELLDLL_DefView', None)
        if hShellViewWin != 0:
            lParam.append(hwnd)
    return True

workerws = []
win32gui.EnumWindows(enum_windows_callback, workerws)

if len(workerws) > 0:
    # Found the correct WorkerW window
    workerw = workerws[0]
else:
    print("Could not find WorkerW window.")
    sys.exit()

# Set the Pygame window as a child of the WorkerW window
win32gui.SetParent(hwnd, workerw)

# Adjust the window styles to make it a child window and ensure it's visible
win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, win32con.WS_CHILD | win32con.WS_VISIBLE)

# Move and resize the window to cover the entire screen
win32gui.SetWindowPos(hwnd, win32con.HWND_BOTTOM, 0, 0, screen_width, screen_height, win32con.SWP_NOACTIVATE)

# Hide the Pygame window from the taskbar
ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
ex_style |= win32con.WS_EX_TOOLWINDOW
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)

# Define the characters to use for the cascade effect
chars = ['0', '1']

# Set font size and create font
font_size = 20
font = pygame.font.SysFont('Consolas', font_size)

# Calculate the number of columns based on screen width and font size
columns = int(screen_width / font_size)
drops = [random.randint(-50, 0) for _ in range(columns)]

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create a semi-transparent surface for the fading effect
    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 28))  # Adjust alpha for fade effect
    screen.blit(overlay, (0, 0))

    # Draw characters
    for i in range(len(drops)):
        char = random.choice(chars)
        char_surface = font.render(char, True, (0, 255, 0))
        x = i * font_size
        y = drops[i] * font_size

        screen.blit(char_surface, (x, y))

        # Reset drop position if it goes off screen
        if y > screen_height and random.random() > 0.975:
            drops[i] = 0
        drops[i] += 1

    # Update display
    pygame.display.flip()
    clock.tick(30)

# Clean up
pygame.quit()
sys.exit()