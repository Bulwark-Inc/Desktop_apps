import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
from logic import slice_pdf, preview_pages
import os

# Function to select input file
def select_input_file(input_entry):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)


# Function to select output file
def select_output_file(output_entry):
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)


# Function to handle slice action (with threading)
def slice_pdf_action(input_entry, output_entry, start_page_entry, end_page_entry, window):
    input_file = input_entry.get()
    output_file = output_entry.get()

    try:
        start = int(start_page_entry.get())
        end = int(end_page_entry.get())
        # Run slicing in a separate thread to avoid freezing the GUI
        threading.Thread(target=process_pdf_slicing, args=(input_file, start, end, output_file, window)).start()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid page numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Background processing for slicing (to prevent GUI freeze)
def process_pdf_slicing(input_file, start, end, output_file, window):
    try:
        slice_pdf(input_file, start, end, output_file)
        messagebox.showinfo("Success", f"PDF sliced successfully! Saved as {output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Function to show PDF preview (with threading)
def show_preview(input_entry, start_page_entry, end_page_entry):
    input_file = input_entry.get()
    try:
        start = int(start_page_entry.get())
        end = int(end_page_entry.get())
        # Run preview in a separate thread to prevent freezing the GUI
        threading.Thread(target=process_preview, args=(input_file, start, end)).start()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid page numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Background processing for preview (to prevent GUI freeze)
def process_preview(input_file, start, end):
    try:
        preview_pages(input_file, start, end)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during preview: {str(e)}")


# Function to create the GUI window
def create_gui():
    window = tk.Tk()  # Standard Tk window, no tkinterdnd
    window.title("PDF Slicer")

    window.geometry("500x450")
    window.resizable(False, False)

    # Dark theme with light accents
    window.tk_setPalette(background="#2C3E50", foreground="#FFFFFF")

    # Header Label
    header_label = tk.Label(window, text="PDF Slicer", font=("Helvetica", 18, "bold"), fg="#ECF0F1", bg="#2C3E50")
    header_label.pack(pady=20)

    # Input and Output PDF file selection
    input_entry = tk.Entry(window, width=40, font=("Arial", 12), bg="#34495E", fg="#ECF0F1", insertbackground='white')
    input_entry.pack(pady=5)
    tk.Button(window, text="Select Input File", font=("Arial", 12), bg="#2980B9", fg="#ECF0F1", command=lambda: select_input_file(input_entry)).pack(pady=5)

    output_entry = tk.Entry(window, width=40, font=("Arial", 12), bg="#34495E", fg="#ECF0F1", insertbackground='white')
    output_entry.pack(pady=5)
    tk.Button(window, text="Select Output File", font=("Arial", 12), bg="#2980B9", fg="#ECF0F1", command=lambda: select_output_file(output_entry)).pack(pady=5)

    # Page range input
    tk.Label(window, text="Start Page:", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").pack(pady=5)
    start_page_entry = tk.Entry(window, font=("Arial", 12), bg="#34495E", fg="#ECF0F1", insertbackground='white')
    start_page_entry.pack(pady=5)

    tk.Label(window, text="End Page:", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").pack(pady=5)
    end_page_entry = tk.Entry(window, font=("Arial", 12), bg="#34495E", fg="#ECF0F1", insertbackground='white')
    end_page_entry.pack(pady=5)

    # Slice PDF button
    tk.Button(window, text="Slice PDF", font=("Arial", 14), bg="#27AE60", fg="#ECF0F1", command=lambda: slice_pdf_action(input_entry, output_entry, start_page_entry, end_page_entry, window)).pack(pady=20)

    # Preview button
    tk.Button(window, text="Preview Pages", font=("Arial", 12), bg="#F39C12", fg="#ECF0F1", command=lambda: show_preview(input_entry, start_page_entry, end_page_entry)).pack(pady=10)

    # Start the GUI loop
    window.mainloop()
