from p5 import *

kaktusz = None
dino = None

def setup():
	global kaktusz
	global dino

	size(400, 400)
	line(1, 3,100,200)
	kaktusz = load_image("images/pngImageDir/jatek-kaktusz.png")
	dino = load_image("images/pngImageDir/jatek-dino.png")
	y = 0

# def draw():
# 	# background(0) # Clear the screen with a black background
# 	rect_mode(CENTER)
# 	rect((100, 100), 20, 100)
# 	ellipse((100, 70), 60, 60)
# 	ellipse((81, 70), 16, 32)
# 	ellipse((119, 70), 16, 32)
# 	line((90, 150), (80, 160))
# 	line((110, 150), (120, 160))


def draw():
	background(255)
	no_stroke()
	image(kaktusz, 100, 200)
	image(dino, 200, 300)

	# # bright red
	# fill(255, 0, 0)
	# circle((72, 72), 58)
	#
	# # dark red
	# fill(127, 0, 0)
	# circle((144, 72), 58)
	#
	# # Pink (pale red)
	# fill(255, 200, 200)
	# circle((216, 72), 58)


if __name__ == '__main__':
	run()