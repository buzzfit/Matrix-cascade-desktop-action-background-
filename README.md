# Matrix Cascade Desktop Background

## Description
This project transforms your desktop background to mimic the iconic Matrix cascade
of green 1's and 0's, while allowing you to maintain any chosen wallpaper as the
background. It creates an interactive desktop where icons remain
functional but hidden unless hovered over, offering a unique way to 'hide' icons
within the cascade area.

## Key Features
- **Matrix Cascade Effect**: Enjoy a dynamic background of cascading green numbers
  over your existing desktop wallpaper.
- **Flexible Background Compatibility**: Works seamlessly with any background picture,
  adapting the cascade effect to overlay whatever wallpaper you have set.
- **Interactive Hidden Icons**: Desktop icons are best positioned in the reverse 'L'
  shaped area along the bottom and far right of the screen to remain visible. Icons
  placed elsewhere will be hidden behind the cascade, only flashing briefly when hovered over.

## Technical Approach
- The program utilizes a backdoor within the windows desktop setup to attach the pygame window to the Windows desktop window,
  enabling the cascade effect to function as a moving background. The pygame window is then hidden from the task bar. This innovative approach
  allows the green Matrix numbers to animate over your static wallpaper, giving the illusion
  of dynamic interaction with your desktop environment.

## Setup Instructions
1. **Arrange Icons**: Before running the program, position your desktop icons within the
   reverse 'L' shaped area at the bottom and far right of your screen. This ensures they
   remain visible and accessible. Once the program is running, you can choose to hide icons
   by moving them outside this area, where they will be obscured by the cascade yet still functional.
2. **Run the Script or Convert to Executable**:
   - Ensure you have Python and Pygame installed:
     ```bash
     pip install pygame
     ```
   - Download `matrix_cascade.py` from this repository and run it directly or convert it into
     an executable using the instructions below.

## How to Convert Python Script to Executable
If you prefer to run the script as an executable, follow these steps to create it and set it to run at startup:
1. Install PyInstaller via pip:
   ```bash
   pip install pyinstaller
Convert the script to an executable:
pyinstaller --onefile --windowed matrix_cascade.py
This command generates a standalone executable in the dist directory.
Place the Executable in the Windows Startup Folder:
Find the matrix_cascade.exe in the dist folder.
Copy this file to your Windows Startup folder. This setup ensures that the cascade effect starts automatically each time you start your computer.
Additional Information
This program was created using Python and Pygame, and leverages Windows-specific APIs to manipulate the desktop environment. The unique icon-hiding feature enhances the Matrix theme by adding an element of secrecy and personalization.
