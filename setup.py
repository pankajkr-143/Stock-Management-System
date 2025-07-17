from cx_Freeze import setup, Executable
import sys
import os

# Dependencies are automatically detected, but some modules need manual configuration
build_exe_options = {
    "packages": [],
    "include_files": [
        ("sms.db", "sms.db"),
        ("Images", "Images"),
        ("bill", "bill"),
    ],
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for GUI apps to hide the console

setup(
    name="StockManagementSystem",
    version="1.0",
    description="Stock Management System Login",
    options={"build_exe": build_exe_options},
    executables=[Executable("login.py", base=base)],
)