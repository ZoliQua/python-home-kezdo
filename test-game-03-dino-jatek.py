from processing import *

def setup():
	size(400, 300)
	kaktusz = loadImage("images/pngImageDir/jatek-kaktusz.png")
	image(kaktusz, 100, 200)
	dino = loadImage("images/pngImageDir/jatek-dino.png")
	image(dino, 20, 200)

run()