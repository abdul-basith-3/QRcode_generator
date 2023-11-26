import qrcode
feature = qrcode.QRCode(version=1,box_size=40,border=3)
feature.add_data(input("enter the url\n"))
feature.make(fit=True)
gen_image = feature.make_image(fill_color="black",back_color="white")
gen_image.save("image.png")