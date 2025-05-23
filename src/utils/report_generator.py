from fpdf import FPDF
import datetime

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Malware Scan Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def generate_pdf_report(filename, infected_files):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.cell(0, 10, f"Date: {date_str}", ln=True)
    pdf.ln(5)

    if not infected_files:
        pdf.cell(0, 10, "No malware detected during the scan.", ln=True)
    else:
        for file in infected_files:
            path = file.get("file")
            rules = ", ".join(file.get("matched_rules", []))
            hash_val = file.get("hash", "N/A")
            pdf.multi_cell(0, 10, f"File: {path}\nMatched Rules: {rules}\nSHA-256: {hash_val}")
            pdf.ln(3)

    pdf.output(filename)
