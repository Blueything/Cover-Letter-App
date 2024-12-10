import streamlit as st
from fpdf import FPDF

# Your constant details
YOUR_NAME = "Hardik Ghori"
EMAIL = "hardikghori3@gmail.com"
LINKEDIN_URL = "https://linkedin.com/in/hardik-ghori99"
UNIVERSITY = "San Jose State University"
LOCATION = "San Jose, CA"
PHONE = "+1(669)288-1953"

def add_paragraph(pdf, text, bold=False):
    """Helper function to add a paragraph with proper margins."""
    if bold:
        pdf.set_font("Arial", size=11, style='B')
    else:
        pdf.set_font("Arial", size=11)

    # Use multi_cell to handle text wrapping within the page margins
    pdf.multi_cell(0, 6, text, align="L")

def generate_cover_letter(company_name, role_name, technologies):
    
    company_name = company_name.upper()
    role_name = role_name.title()
    technologies = technologies.title()
    
    # Generate PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.set_font("Arial", size=11)

    # Add header
    pdf.cell(0, 10, txt=YOUR_NAME, ln=True, align="L")
    pdf.ln(1.5)

    pdf.set_text_color(0, 0, 255)
    pdf.set_font("Arial", size=11, style='U')
    pdf.cell(16, 7, txt="LinkedIn", link=LINKEDIN_URL, align="L")
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial", size=11)
    pdf.cell(5, 7, txt=" | ", align="L")
    pdf.set_text_color(0, 0, 255)
    pdf.set_font("Arial", size=11, style='U')
    pdf.cell(0, 7, txt=EMAIL, link=f"mailto:{EMAIL}", align="L")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)

    pdf.set_font("Arial", size=11)
    pdf.cell(0, 6, txt=UNIVERSITY, ln=True, align="L")
    pdf.cell(0, 6, txt=LOCATION, ln=True, align="L")
    pdf.ln(7)

    # Add greeting
    pdf.cell(0, 6, txt="Dear Hiring Manager,", ln=True, align="L")
    pdf.ln(3)

    # Custom paragraph with bold terms
    add_paragraph(pdf, f"I am writing to express my interest in the {role_name}. With over two years of experience in software development and a Master's degree in Software Engineering from {UNIVERSITY}, I have a strong background in creating and optimizing software solutions, which I am eager to bring to your team.")

    pdf.ln(3)
    add_paragraph(pdf, f"Throughout my career, I have developed expertise in programming languages such as {technologies}, as well as hands-on experience with frameworks like React and Node.js. My work has involved building full-stack applications, improving backend performance, and utilizing cloud technologies like AWS to deploy scalable systems. I have also worked closely with teams to solve complex technical challenges, which has helped me develop strong problem-solving skills and adaptability in fast-paced environments.")

    pdf.ln(3)
    add_paragraph(pdf, f"I am particularly passionate about joining a company that is committed to innovation and cutting-edge technology, and I believe my skills and drive align well with the goals of a {role_name}. I am confident that my background in software engineering and enthusiasm for learning new technologies will allow me to make valuable contributions.")

    pdf.ln(3)
    add_paragraph(pdf, f"Thank you for considering my application. I look forward to the opportunity to discuss how my qualifications can meet your team's needs and contribute to {company_name}'s success.")

    # Add closing
    pdf.ln(7)
    pdf.cell(0, 7, txt="Sincerely,", ln=True, align="L")
    pdf.ln(3)
    pdf.cell(0, 6, txt=YOUR_NAME, ln=True, align="L")
    pdf.cell(0, 6, txt=PHONE, ln=True, align="L")

    # Add email and LinkedIn links at the end
    pdf.ln(3)
    pdf.set_text_color(0, 0, 255)
    pdf.set_font("Arial", size=11, style='U')
    pdf.cell(0, 6, txt=EMAIL, ln=True, align="L", link=f"mailto:{EMAIL}")
    pdf.cell(0, 6, txt="LinkedIn", ln=True, align="L", link=LINKEDIN_URL)
    pdf.set_text_color(0, 0, 0)

    # Save the PDF file only once
    pdf_filename = f"{YOUR_NAME}_{company_name}_Cover_Letter.pdf"
    pdf.output(pdf_filename)
    return pdf_filename

# Streamlit app interface
st.title("Cover Letter Generator")

company_name = st.text_input("Company Name")
role_name = st.selectbox("Role", ["Software Engineer", "Fullstack Engineer", "Data Engineer"])
technologies = st.text_input("Technologies")

if st.button("Generate Cover Letter"):
    if company_name and role_name and technologies:
        pdf_file = generate_cover_letter(company_name, role_name, technologies)
        with open(pdf_file, "rb") as file:
            st.download_button(label="Download Cover Letter", data=file, file_name=pdf_file, mime="application/pdf")
    else:
        st.error("Please fill in all the fields.")
