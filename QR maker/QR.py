import qrcode as qr
ip=input("Enter the link")
img=qr.make(ip)

img.save("vpa_baba.png")