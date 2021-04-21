import pyqrcode

url = pyqrcode.create('https://www.dulzoltan.hu/')

export_folder = "export/"
export_filename = "dulzoltan-hu.svg"

url.svg(export_folder + export_filename, scale=8)