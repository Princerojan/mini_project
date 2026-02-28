import qrcode

# QR code for quotes page
qr1 = qrcode.make("https://princerojan.github.io/mini_project/")
qr1.save("qrcode.png")

# QR code for name page
qr2 = qrcode.make("https://princerojan.github.io/mini_project/name.html")
qr2.save("name_qrcode.png")

print("✅ Both QR codes generated!")