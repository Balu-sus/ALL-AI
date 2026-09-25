import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf(summary_text: str, image_path: str, output_pdf: str = "final_output.pdf"):
    """Combines text summary and generated image into a clean PDF document."""
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Header Style
    title_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor("#1e293b"),
        spaceAfter=15
    )
    
    # Custom Body Style
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#334155")
    )

    story = []

    # 1. Add Title
    story.append(Paragraph("ALL-AI Generated Report", title_style))
    story.append(Spacer(1, 10))

    # 2. Add Email Summary Text
    formatted_summary = summary_text.replace('\n', '<br/>')
    story.append(Paragraph(f"<b>Summary & Action Items:</b><br/>{formatted_summary}", body_style))
    story.append(Spacer(1, 20))

    # 3. Add Generated Image (if file exists)
    if os.path.exists(image_path):
        story.append(Paragraph("<b>Generated Visual Context:</b>", body_style))
        story.append(Spacer(1, 10))
        img = Image(image_path, width=400, height=300)
        story.append(img)
    else:
        story.append(Paragraph("<i>Image file not found.</i>", body_style))

    # Build PDF
    doc.build(story)
    print(f"PDF successfully created: {output_pdf}")

if __name__ == "__main__":
    sample_summary = """• Key Summary: The team held a Q3 roadmap meeting to align on near-term deliverables.
• Action Items:
  - Sarah: Finalize API architecture docs by Friday, Oct 2.
  - Alex: Complete database migration script by Tuesday, Oct 6.
  - Everyone: Review project board and add estimates by EOD tomorrow."""
    
    # Combines sample summary and the image created from Module 2
    generate_pdf(sample_summary, "generated_image.png")
