import argparse
import sys
from gui import create_gui
from logic import slice_pdf

# Command-line interface logic
def cli():
    parser = argparse.ArgumentParser(description="Slice a PDF")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("start_page", type=int, help="Starting page")
    parser.add_argument("end_page", type=int, help="Ending page")
    parser.add_argument("output_pdf", help="Path to save the sliced PDF")
    args = parser.parse_args()

    slice_pdf(args.input_pdf, args.start_page, args.end_page, args.output_pdf)

# Main entry point
def main():
    if len(sys.argv) > 1:
        cli()  # If there are arguments, use CLI
    else:
        create_gui()  # Otherwise, start the GUI

if __name__ == "__main__":
    main()
