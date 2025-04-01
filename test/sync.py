#!/usr/bin/env python

import markdown

# Create a simple markdown text
md_text = "# Hello, World!"

# Convert markdown text to HTML
html = markdown.markdown(md_text)

print("Markdown text:")
print(md_text)
print("\nConverted HTML:")
print(html)