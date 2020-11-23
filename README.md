# Raspi Control Panel
A basic tool to control specific features on your Raspberry Pi. Designed from the ground up in Python and PyQt5.

## Building Python files from Qt Designer
If you are using Qt Designer to create UIs and resource files, you'll need to convert them to Python files before they can be used in the program. 

To convert .ui files to Python:
```bash
pyuic5 <ui file> -o <output.py>
```

To convert .qrc resource files to Python:
```bash
pyrcc5 <qrc file> -o <output.py>
```