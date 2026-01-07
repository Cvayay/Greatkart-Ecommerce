import io
import os
from markdown import markdown
from xhtml2pdf import pisa

def md_to_pdf(md_path, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md = f.read()

    html_body = markdown(md)
    html = f"<html><head><meta charset='utf-8'></head><body>{html_body}</body></html>"

    with open(pdf_path, 'wb') as out:
        pisa_status = pisa.CreatePDF(io.BytesIO(html.encode('utf-8')), dest=out)
    return pisa_status.err

if __name__ == '__main__':
    root = os.path.dirname(os.path.dirname(__file__))
    md = os.path.join(root, 'PROJECT_OVERVIEW.md')
    pdf = os.path.join(root, 'PROJECT_OVERVIEW.pdf')
    err = md_to_pdf(md, pdf)
    if err:
        print('PDF generation failed (xhtml2pdf returned error).')
    else:
        print(f'PDF created: {pdf}')
