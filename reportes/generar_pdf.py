from xhtml2pdf import pisa
from flask import render_template
from io import BytesIO

def render_pdf(template_name, context):
    html = render_template(template_name, **context)
    result = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=result)
    if pisa_status.err:
        return None
    return result.getvalue()
