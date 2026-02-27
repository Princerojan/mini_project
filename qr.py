import qrcode

qr = qrcode.make("https://princerojan.github.io/mini_project/")
qr.save("qrcode.png")

print("QR code saved!")