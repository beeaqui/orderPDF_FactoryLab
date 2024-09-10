import qrcode
from pathlib import Path


# GitHub base URL for raw files
base_url = "https://raw.githubusercontent.com/beeaqui/orderPDF_FactoryLab/96bc726d33b1c6eb84107e57f5b8421a305c6fd8/"

# List of PDF filenames
pdf_files = ["Order 1.pdf", "Order 2.pdf", "Order 3.pdf", "Order 4.pdf", "Order 5.pdf",
             "Order 6.pdf", "Order 7.pdf", "Order 8.pdf", "Order 9.pdf", "Order 10.pdf",
             "Order 11.pdf", "Order 12.pdf", "Order 13.pdf", "Order 14.pdf", "Order 15.pdf",
             "Order 16.pdf", "Order 17.pdf", "Order 18.pdf", "Order 19.pdf", "Order 20.pdf"]

# Directory to save the QR codes
output_dir = Path(r"C:\Users\anaba\OneDrive\Ambiente de Trabalho\Investigação\Games and dynamics\1. Folha de "
                  r"Encomenda\1. QR_codes\QR_codes_png")
output_dir.mkdir(parents=True, exist_ok=True)

# Generate a QR code for each PDF
for pdf in pdf_files:
    # Full URL to the PDF
    url = f"{base_url}{pdf}"

    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Save the QR code as an image file
    img = qr.make_image(fill='black', back_color='white')
    img.save(output_dir / f"{pdf.replace('.pdf', '')}_QR.png")

    print(f"QR code for {pdf} saved as {pdf.replace('.pdf', '')}_QR.png")
    