from data import *
from assets import *

# Set overall app cosmetics.
gui.set_appearance_mode('system')
gui.set_default_color_theme('green')

# Create an app object.
pressCheck: CTk = gui.CTk()

# Get details on primary monitor.
def get_geometry() -> str:
    primary_mon: Monitor = get_monitors()[0]
    screen_size_mult: float = .9
    width: int = int(primary_mon.width * screen_size_mult)
    height: int = int(primary_mon.height * screen_size_mult)
    x: int = int(primary_mon.x + (primary_mon.width - (width)) // 2)
    y: int = int(primary_mon.y + (primary_mon.height - (height)) // 2)
    return f"{width}x{height}+{x}+{y}"

# Get app details from .json file.
app_info: dict = {}
with open(VERSION_INFO, 'r') as file:
    app_info = load(file)

# Setup the main window of PressCheck and add logo to window header.
pressCheck.geometry(get_geometry())
pressCheck.title(f"{app_info['name']} | {app_info['version']}")
pressCheck.iconbitmap(ICO_LOGO)

# Change the logo of the app in the taskbar.
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("presscheck")

# Run the app mainloop.
pressCheck.mainloop()