import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox

# Function to create a zip archive
def create_zip_archive(zip_name, files_to_zip):
    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files_to_zip:
                if os.path.exists(file):
                    zipf.write(file, os.path.basename(file))
                else:
                    print(f"Error: {file} not found.")
        messagebox.showinfo("Success", f"Archive {zip_name} created successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to extract a zip archive
def extract_zip_archive(zip_name, extract_to_folder):
    try:
        if not extract_to_folder:
            # If no folder is specified, extract to the current directory where the script is located
            extract_to_folder = os.path.dirname(os.path.abspath(__file__))
        
        if not os.path.exists(extract_to_folder):
            os.makedirs(extract_to_folder)
        
        with zipfile.ZipFile(zip_name, 'r') as zipf:
            zipf.extractall(extract_to_folder)
        messagebox.showinfo("Success", f"Files extracted to {extract_to_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to browse and select files for compression
def browse_files_to_zip():
    files = filedialog.askopenfilenames(title="Select files to compress")
    if files:
        file_list.set("\n".join(files))  # Display selected files in the text area

# Function to create the zip file
def create_archive():
    files = file_list.get().splitlines()
    if files:
        zip_name = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")], title="Save ZIP file as")
        if zip_name:
            create_zip_archive(zip_name, files)

# Function to browse and select zip file for extraction
def browse_zip_file():
    zip_file = filedialog.askopenfilename(filetypes=[("ZIP files", "*.zip")], title="Select a ZIP file to extract")
    if zip_file:
        zip_file_path.set(zip_file)  # Set the selected zip file path

# Function to extract the selected zip file
def extract_archive():
    zip_file = zip_file_path.get()
    if zip_file:
        extract_to_folder = folder_entry.get() or None
        extract_zip_archive(zip_file, extract_to_folder)

# Initialize the GUI window
root = tk.Tk()
root.title("Simple ZIP Compressor/Decompressor")
root.geometry("500x500")
root.configure(bg="#2e2e2e")  # Dark background color

# Define custom colors
bg_color = "#2e2e2e"
fg_color = "#ffffff"
button_color = "#444444"
entry_color = "#555555"
highlight_color = "#1e90ff"

# Frame for file compression section
compression_frame = tk.Frame(root, bg=bg_color)
compression_frame.pack(pady=20, padx=20, fill="x")

compression_label = tk.Label(compression_frame, text="Files to Compress:", fg=fg_color, bg=bg_color, font=("Arial", 12))
compression_label.pack(anchor="w")

file_list = tk.StringVar()
file_list_display = tk.Label(compression_frame, textvariable=file_list, fg=fg_color, bg=entry_color, width=60, height=5, relief="sunken", anchor="nw", justify="left", padx=10, pady=5)
file_list_display.pack(pady=10)

browse_button = tk.Button(compression_frame, text="Browse Files", command=browse_files_to_zip, fg=fg_color, bg=button_color, relief="flat", width=20)
browse_button.pack(pady=5)

create_button = tk.Button(compression_frame, text="Create Archive", command=create_archive, fg=fg_color, bg=highlight_color, relief="flat", width=20)
create_button.pack(pady=5)

# Frame for file extraction section
extraction_frame = tk.Frame(root, bg=bg_color)
extraction_frame.pack(pady=20, padx=20, fill="x")

extraction_label = tk.Label(extraction_frame, text="Select ZIP file to Extract:", fg=fg_color, bg=bg_color, font=("Arial", 12))
extraction_label.pack(anchor="w")

zip_file_path = tk.StringVar()
zip_file_path_display = tk.Entry(extraction_frame, textvariable=zip_file_path, fg=fg_color, bg=entry_color, width=50)
zip_file_path_display.pack(pady=10)

browse_zip_button = tk.Button(extraction_frame, text="Browse ZIP File", command=browse_zip_file, fg=fg_color, bg=button_color, relief="flat", width=20)
browse_zip_button.pack(pady=5)

folder_label = tk.Label(extraction_frame, text="Extract to Folder (leave empty for current folder):", fg=fg_color, bg=bg_color, font=("Arial", 12))
folder_label.pack(anchor="w", pady=5)

folder_entry = tk.Entry(extraction_frame, fg=fg_color, bg=entry_color, width=50)
folder_entry.pack(pady=10)

extract_button = tk.Button(extraction_frame, text="Extract Archive", command=extract_archive, fg=fg_color, bg=highlight_color, relief="flat", width=20)
extract_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
