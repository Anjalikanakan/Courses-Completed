#!/usr/bin/env python3
"""
Convert PDF certificates to JPG format
Requires: pip install pdf2image pillow
"""

from pdf2image import convert_from_path
from PIL import Image
import os

def convert_pdf_to_jpg(pdf_path, output_path):
    """Convert a PDF file to JPG format"""
    try:
        # Convert PDF to images (one per page)
        images = convert_from_path(pdf_path, dpi=300)
        
        # Save the first page as JPG (certificates are typically single page)
        if images:
            jpg_filename = output_path
            images[0].convert('RGB').save(jpg_filename, 'JPEG', quality=95)
            print(f"✓ Successfully converted: {pdf_path} → {jpg_filename}")
            return True
    except Exception as e:
        print(f"✗ Error converting {pdf_path}: {str(e)}")
        return False

# Convert the certificate PDFs
pdf_files = [
    ("Claude code 101 Certificate.pdf", "Claude_code_101_Certificate.jpg"),
    ("Claude Code Certification .pdf", "Claude_Code_Certification.jpg"),
    ("Github Copilot Microsoft course completion certificate .pdf", "Github_Copilot_Microsoft_Certificate.jpg")
]

print("Starting PDF to JPG conversion...\n")
for pdf_file, jpg_file in pdf_files:
    if os.path.exists(pdf_file):
        convert_pdf_to_jpg(pdf_file, jpg_file)
    else:
        print(f"⚠ File not found: {pdf_file}")

print("\nConversion complete!")
