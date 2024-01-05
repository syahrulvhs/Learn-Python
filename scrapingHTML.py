import requests as req

respon = req.get('https://www.youtube.com/')
html = respon.text

print(html)
