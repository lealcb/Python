import pyqrcode 
link = pyqrcode.create('https://git-scm.com/download/win')
link.png('code.png', scale=10)
#add new