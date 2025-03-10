import qrcode
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path


base_url = "https://github.com/beeaqui/orderPDF_FactoryLab/raw/main/Round3/"

# List of PDF filenames
pdf_files = ["Order 1.1.pdf", "Order 2.1.pdf", "Order 2.2.pdf", "Order 3.1.pdf", "Order 3.2.pdf",
             "Order 3.3.pdf", "Order 4.1.pdf", "Order 4.2.pdf", "Order 5.1.pdf", "Order 5.2.pdf",
             "Order 6.1.pdf", "Order 7.1.pdf", "Order 8.1.pdf", "Order 8.2.pdf", "Order 9.1.pdf",
             "Order 9.2.pdf", "Order 10.1.pdf", "Order 11.1.pdf", "Order 11.2.pdf", "Order 12.1.pdf",
             "Order 12.2.pdf", "Order 13.1.pdf", "Order 13.2.pdf", "Order 13.3.pdf", "Order 14.1.pdf",
             "Order 15.1.pdf", "Order 16.1.pdf", "Order 16.2.pdf", "Order 17.1.pdf", "Order 17.2.pdf",
             "Order 18.1.pdf", "Order 18.2.pdf", "Order 18.3.pdf", "Order 19.1.pdf", "Order 20.1.pdf",
             "Order 20.2.pdf"]

# Directory to save the QR codes
output_dir = Path(r'C:\Users\anaba\OneDrive\Ambiente de Trabalho\Investigação\4. Factory Lab\1. Games_dynamics'
                  r'\1_Ordens_Producao_Ronda3\QR_codes')

output_dir.mkdir(parents=True, exist_ok=True)

# Paths to the logo images
factorylab_logo_path = Path(r"factorylab_logo.png")
uc_logo_path = Path(r"uc_logo.png")
font_path = Path(r"Roboto-Black.ttf")

factorylab_logo = Image.open(factorylab_logo_path)
uc_logo = Image.open(uc_logo_path)
font_size = 250
font = ImageFont.truetype(str(font_path), font_size)


def create_final_image(qr_code_img, order_number):
    # A6 size in pixels at 300 dpi (105 mm x 148 mm)
    width, height = 1240, 1748
    final_img = Image.new('RGB', (width, height), 'white')  # White background

    # Resize logos
    logo_width = int(width * 0.5)
    factorylab_logo_resized = factorylab_logo.resize((logo_width, int(logo_width * factorylab_logo.height /
                                                                      factorylab_logo.width)))
    uc_logo_aspect_ratio = uc_logo.width / uc_logo.height
    uc_logo_resized = uc_logo.resize((logo_width, int(logo_width / uc_logo_aspect_ratio)))

    # Paste the FactoryLab logo at the top
    final_img.paste(factorylab_logo_resized, ((width - logo_width) // 2, 30), factorylab_logo_resized)

    # Draw the order number
    draw = ImageDraw.Draw(final_img)
    text_bbox = draw.textbbox((0, 0), order_number, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    draw.text(((width - text_width) / 2, factorylab_logo_resized.height + 100), order_number, fill='black', font=font)

    # Resize and place QR code
    qr_size = int(height * 0.45)
    qr_code_resized = qr_code_img.resize((qr_size, qr_size))
    qr_y_position = factorylab_logo_resized.height + 100 + text_height + 100
    final_img.paste(qr_code_resized, ((width - qr_size) // 2, qr_y_position))

    # Paste UC logo
    uc_logo_y = qr_y_position + qr_size + 50
    final_img.paste(uc_logo_resized, ((width - uc_logo_resized.width) // 2, uc_logo_y), uc_logo_resized)

    return final_img


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
    qr_code_img = qr.make_image(fill='black', back_color='white')

    # Extract order number
    order_number = pdf.replace('.pdf', '').split(' ')[-1]

    # Create the final image
    final_img = create_final_image(qr_code_img, order_number)

    # Save the final image
    final_img.save(output_dir / f"{pdf.replace('.pdf', '')}_QR.png")

    print(f"QR code for {pdf} saved as {pdf.replace('.pdf', '')}_QR.png")
