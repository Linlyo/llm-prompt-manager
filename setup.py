"""
Turn the script into a standalone app
"""

from setuptools import setup

APP = ['app.py']
APP_NAME = "PromptTool"

DATA_FILES = ['prompts.txt'] # prompts file
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'MyIcon.icns',
    'plist': {
        'CFBundleName': APP_NAME,
        'CFBundleDisplayName': APP_NAME,
        'CFBundleGetInfoString': "PromptTool App",
        'CFBundleIdentifier': "com.linly.prompttool",
        'CFBundleVersion': "0.1.0",
        'CFBundleShortVersionString': "0.1.0",
        'NSHumanReadableCopyright': "Copyright © 2024 Linly, All Rights Reserved.",
        'LSUIElement': True, # This makes it a menu bar app without a dock icon
    },
    'packages': ['rumps', 'pyperclip', 'subprocess'], # Explicitly include necessary packages
    'includes': ['rumps', 'pyperclip', 'subprocess'], # Also useful for finding hidden imports
    'site_packages': True, # Ensure site-packages are included
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
