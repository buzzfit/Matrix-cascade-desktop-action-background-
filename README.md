# Matrix Cascade Desktop Background

## Description
This project transforms your desktop background to mimic the iconic Matrix cascade
of green 1's and 0's, while allowing you to maintain any chosen wallpaper as the
background. It creates an interactive desktop where icons remain functional but hidden
unless hovered over, offering a unique way to 'hide' icons within the cascade area.

## Key Features
- **Matrix Cascade Effect**: Enjoy a dynamic background of cascading green numbers
  over your existing desktop wallpaper.
- **Flexible Background Compatibility**: Works seamlessly with any background picture,
  adapting the cascade effect to overlay whatever wallpaper you have set.
- **Interactive Hidden Icons**: Desktop icons are best positioned in the reverse 'L'
  shaped area along the bottom and far right of the screen to remain visible. Icons
  placed elsewhere will be hidden behind the cascade, only flashing briefly when hovered over.

## Technical Approach
- The program uses a backdoor method to attach itself to the Windows desktop window,
  enabling the cascade effect to function as a moving background. This innovative approach
  allows the green Matrix numbers to animate over your static wallpaper, giving the illusion
  of dynamic interaction with your desktop environment.

## Setup Instructions
1. **Arrange Icons**: Before running the program, position your desktop icons within the
   reverse 'L' shaped area at the bottom and far right of your screen. This ensures they
   remain visible and accessible. Once the program is running, you can choose to hide icons
   by moving them outside this area, where they will be obscured by the cascade yet still functional.
2. **Download and Run**:
   - Download `matrix_cascade.exe` from this repository.
   - Place it in your Windows Startup folder. This ensures the cascade effect starts automatically
     each time you start your computer.
3. **Activate**: Restart your computer to activate the Matrix cascade effect. It will
   continue to initiate on every startup.

## Additional Information
This program was created using Python and Pygame, and packaged into an executable
using PyInstaller for easy use. Its unique icon-hiding feature,enhances the Matrix theme by adding an element of secrecy and personalization.

## How to Convert Python Script to Executable (For Developers)
If you wish to modify the script and create your own version of the executable:
1. Install PyInstaller via pip:
   ```bash
   pip install pyinstaller
Navigate to the script's directory and run:
bash
Copy code
pyinstaller --onefile --windowed matrix_cascade.py
This command generates a standalone executable in the dist directory.
