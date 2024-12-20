import qrcode

# Taking UPI ID and payment amount as input
upi_id = input('Enter your UPI ID: ')
amount = input('Enter the amount: ')
message = input('Enter a message (optional): ')

# Defining the payment URL based on the UPI ID
payment_url = f'upi://pay?pa={upi_id}&pn=YourName&mc=YourMerchantCode&tid=YourTransactionId&am={amount}&cu=INR&url=https://yoururl.com'

if message:
    payment_url += f'&tn={message}'

# Generating the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(payment_url)
qr.make(fit=True)

# Creating an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")

# Saving the QR code image
img.save("upi_payment_qr.png")

print("QR Code generated and saved as 'upi_payment_qr.png'.")
