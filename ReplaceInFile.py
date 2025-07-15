from tkinter import filedialog
from tkinter import Tk


def replace_text_in_file(file_path, old_pattern, new_pattern):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace(old_pattern, new_pattern)

    with open(file_path, 'w') as file:
        file.write(content)


if __name__ == '__main__':
    root = Tk()
    root.withdraw()
    file_selected = filedialog.askopenfile(mode='r', title="Select a file to replace text in")
    if not file_selected:
        print("No file selected. Exiting.")
        exit()

    to_replace = input("Enter the text to replace: ")
    if not to_replace:
        print("No text to replace provided. Exiting.")
        exit()
    print(f"'{to_replace}' will be replaced.")

    replacement = input("Enter the replacement text: ")
    if not replacement:
        print("No replacement text provided. Exiting.")
        exit()

    accept = input(f"Do you want to replace '{to_replace}' with '{replacement}'? (yes/no): ").strip().lower()
    if accept == 'yes':
        print("Replacement confirmed.")
        replace_text_in_file(file_selected.name, to_replace, replacement)
