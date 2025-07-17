import os
from tkinter import Tk, filedialog

if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    allowed_extensions = ['.py', '.c', '.cpp', '.cs']
    file_selected = filedialog.askdirectory(
        initialdir='C:\\',
        title="Select a folder count the lines in")

    if not file_selected:
        print("No folder selected. Exiting.")
        exit()

    total_lines = 0
    for dirpath, dirnames, filenames in os.walk(file_selected):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in allowed_extensions):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                        total_lines += len(lines)
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    print(f"From files with extensions: {allowed_extensions}")
    print(f"Total lines of code in selected folder: {total_lines}")
