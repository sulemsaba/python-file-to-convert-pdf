PDF Dark Mode Converter

I made this little Python tool because I read a lot of PDFs at night, and the bright white pages were hurting my eyes.
So this script converts any normal PDF into a dark mode version — darker background, lighter text, and much easier to read.

It’s free, clean, and super simple to use.

What it does
Turns a regular PDF into a dark-mode styled one
Keeps the text readable instead of fully inverting everything
Shows progress as it converts each page
Lets you pick your files with a normal Windows file dialog
Works on most PDFs without any trouble

Requirements
You only need Python and PyMuPDF:
-------------------
pip install PyMuPDF
-------------------
That’s it.

How to use it
Run the script:
python convert_pdf_dark_mode.py
Choose the PDF you want to convert.
Choose where you want the dark-mode version saved.
Wait a bit while it processes.
Done — enjoy your new dark PDF.

How it works
The script goes page-by-page and applies a blend effect that flips the brightness in a cleaner way than the usual “invert colors” trick.
The result is a dark theme with good contrast and readable text.

A few notes
Works best on digital PDFs, though scanned ones still work

Larger PDFs will take longer
Output size may be slightly different from the original

Why I made it
Honestly, just for personal use.
I wanted something lightweight and trustworthy, with no ads, no “Pro version,” and definitely no malware.
If it helps someone else, even better.
