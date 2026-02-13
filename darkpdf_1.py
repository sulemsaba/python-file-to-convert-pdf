import fitz  # Make sure you install PyMuPDF
import os
import sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def apply_dark_mode(input_path, output_path):
    """
    Apply dark mode effect to a PDF file using a reliable method.
    
    Args:
        input_path (str): Path to the input PDF file
        output_path (str): Path to save the modified PDF file
    """
    try:
        # Open the input PDF
        doc = fitz.open(input_path)
        total_pages = len(doc)
        
        print(f"Processing {total_pages} pages...")
        
        # Process each page
        for page_num, page in enumerate(doc):
            rect = page.rect
            
            # Add a white background underlay to ensure consistent inversion
            page.draw_rect(rect, color=None, fill=(1, 1, 1), overlay=False)
            
            # Add an annotation for color inversion using blend mode 'Difference'
            # Use fill color (0.9, 0.9, 0.9) to achieve dark gray background (~0.1)
            annot = page.add_rect_annot(rect)
            annot.set_colors(fill=(0.9, 0.9, 0.9))
            annot.set_border(width=0)
            annot.set_blendmode('Difference')
            annot.update()
            
            if (page_num + 1) % 10 == 0 or (page_num + 1) == total_pages:
                print(f"Processed page {page_num + 1}/{total_pages}")
        
        # Save the modified PDF
        doc.save(output_path, garbage=4, deflate=True)
        doc.close()
        
        print(f"Successfully saved dark mode PDF to: {output_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

def get_file_paths():
    """
    Get input and output file paths using a file dialog
    """
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()
    
    print("Please select the input PDF file:")
    input_path = askopenfilename(
        title="Select Input PDF",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )
    
    if not input_path:
        print("No input file selected. Exiting.")
        sys.exit(0)
    
    print("Please select where to save the output PDF file:")
    output_path = asksaveasfilename(
        title="Save Output PDF As",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
    )
    
    if not output_path:
        print("No output file selected. Exiting.")
        sys.exit(0)
    
    return input_path, output_path

def main():
    """
    Main function to run the PDF Dark Mode application
    """
    print("=" * 50)
    print("PDF Dark Mode Converter — Enhanced Edition")
    print("=" * 50)
    print("This program will apply a dark mode effect to your PDF file.")
    print("The resulting PDF will have a dark background with readable content.")
    print()
    
    # Get file paths from your device
    input_path, output_path = get_file_paths()
    
    print()
    print(f"Input file: {input_path}")
    print(f"Output file: {output_path}")
    print()
    
    # Check if input file exists
    if not os.path.exists(input_path):
        print(f"Error: The file '{input_path}' does not exist.")
        sys.exit(1)
    
    # Apply dark mode effect
    apply_dark_mode(input_path, output_path)
    
    # Show file size information
    input_size = os.path.getsize(input_path) / (1024 * 1024)  # MB 
    output_size = os.path.getsize(output_path) / (1024 * 1024)  # MB
    
    print()
    print("Conversion complete!")
    print(f"Original file size: {input_size:.2f} MB")
    print(f"New file size: {output_size:.2f} MB")

if __name__ == "__main__":

    main()

