import os
import PyPDF2
from tkinter import messagebox
from pdf2image import convert_from_path


# PDF slicing logic
def slice_pdf(input_pdf, start_page, end_page, output_pdf):
    try:
        # Check if output file exists and ask to overwrite
        if os.path.exists(output_pdf):
            overwrite = messagebox.askyesno("Overwrite File", "The output file already exists. Do you want to overwrite it?")
            if not overwrite:
                return

        # Open the input PDF
        with open(input_pdf, 'rb') as infile:
            reader = PyPDF2.PdfReader(infile)
            total_pages = len(reader.pages)
            
            # Validate page range
            if start_page <= 0 or end_page <= 0 or start_page > end_page or start_page > total_pages:
                messagebox.showerror("Invalid Input", "Please enter a valid page range.")
                return

            # Create a writer object to save the new PDF
            writer = PyPDF2.PdfWriter()

            # Loop through the selected range of pages
            for page_num in range(start_page - 1, end_page):  # Pages are 0-indexed
                writer.add_page(reader.pages[page_num])

            # Write the selected pages to the output PDF
            with open(output_pdf, 'wb') as outfile:
                writer.write(outfile)

        messagebox.showinfo("Success", f"PDF sliced successfully! Saved as {output_pdf}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Get total page count of a PDF
def get_pdf_page_count(pdf_path):
    try:
        with open(pdf_path, 'rb') as infile:
            reader = PyPDF2.PdfReader(infile)
            return len(reader.pages)
    except Exception as e:
        messagebox.showerror("Error", f"Could not retrieve page count: {str(e)}")
        return 0


# Function for previewing pages (using pdf2image)
def preview_pages(pdf_path, start_page, end_page):
    try:
        pages = convert_from_path(pdf_path, first_page=start_page, last_page=end_page)
        for page in pages:
            page.show()  # Opens the page in the default image viewer
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during preview: {str(e)}")
