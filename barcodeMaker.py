import qrcode

img = qrcode.make('https://sijaone.website')
img.save('sijaWEB.png')
img.show()
