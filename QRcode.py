import qrcode

data = input("Enter text or URL to generate QR code :")

qr = qrcode.make(data)

qr.save("QR-code.png")
qr.show()


print("QR code generated successfully!")
print("Save as : QR-code.png")
