import markdown
from xhtml2pdf import pisa
import os

def convert_markdown_to_pdf(source_file, output_file):
    """
    Converts a Markdown file into a PDF document.
    Requires libraries: markdown, xhtml2pdf
    """
    if not os.path.exists(source_file):
        print(f"Error: {source_file} not found.")
        return

    try:
        with open(source_file, 'r', encoding='utf-8') as f:
            md_text = f.read()

        # Convert Markdown to HTML
        html_content = """
        <html>
        <head><style>body { font-family: Helvetica, Arial, sans-serif; }</style></head>
        <body>
        """ + markdown.markdown(md_text) + """
        </body>
        </html>
        """

        # Generate PDF from HTML content
        with open(output_file, "wb") as pdf_out:
            pisa_status = pisa.CreatePDF(html_content, dest=pdf_out)

        if not pisa_status.err:
            print(f"Success: {output_file} has been created.")
        else:
            print("Error: Could not generate PDF.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage for testing
    test_md = "README.md"
    if not os.path.exists(test_md):
        with open(test_md, "w") as f:
            f.write("# Sample Document\n\nThis is an automated conversion test.")
    
    convert_markdown_to_pdf(test_md, "output_document.pdf")