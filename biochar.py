import qrcode
import os

data_values = """
99598b6a-a846-4d77-a868-4fa5f22101ca
"""

data_values = data_values.split()

output_directory = "biochar"

os.makedirs(output_directory, exist_ok=True)

for i, data in enumerate(data_values, start=1):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image with a unique filename
    filename = f"{i:03d}_biochar.png"  # Format the filename with a leading zero
    img.save(os.path.join(output_directory, filename))
