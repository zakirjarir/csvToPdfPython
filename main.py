import pandas as pd
from tkinter import Tk, Label, Button, filedialog, Entry, StringVar, messagebox
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def csv_to_pdf(csv_file, pdf_file):
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)

        # Convert DataFrame to list for table
        data = [df.columns.tolist()] + df.values.tolist()

        # Create PDF
        pdf = SimpleDocTemplate(pdf_file, pagesize=landscape(A4))
        table = Table(data)

        # Table styling
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#4CAF50")),  # Header bg
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),                 # Header text color
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke),
        ])
        table.setStyle(style)

        elems = [table]
        pdf.build(elems)

        messagebox.showinfo("✅ Success", f"PDF file has been created:\n{pdf_file}")
    except Exception as e:
        messagebox.showerror("❌ Error", f"Failed to convert CSV to PDF.\nError: {e}")

def browse_csv():
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv")],
        title="Select a CSV File"
    )
    if file_path:
        csv_path.set(file_path)

def save_as_pdf():
    if not csv_path.get():
        messagebox.showwarning("⚠️ Warning", "Please select a CSV file first.")
        return
    
    output_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save PDF File As"
    )
    if output_path:
        csv_to_pdf(csv_path.get(), output_path)

# ----------------- GUI -----------------
root = Tk()
root.title("📊 CSV to PDF Converter")
root.geometry("600x250")
root.resizable(False, False)

csv_path = StringVar()

Label(root, text="CSV File Path:", font=("Arial", 12)).pack(pady=10)

Entry(root, textvariable=csv_path, width=50, font=("Arial", 11)).pack(pady=5)

Button(root, text="📂 Browse CSV", command=browse_csv, font=("Arial", 11), bg="#4CAF50", fg="white", width=20).pack(pady=10)

Button(root, text="📄 Convert to PDF", command=save_as_pdf, font=("Arial", 11), bg="#2196F3", fg="white", width=20).pack(pady=10)

Button(root, text="❌ Exit", command=root.quit, font=("Arial", 11), bg="#f44336", fg="white", width=20).pack(pady=10)

root.mainloop()
