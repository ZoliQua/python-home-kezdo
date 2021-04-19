from p5 import *

f = None
kaktusz = None
dino = None
x = 0
y_circle = 72
x_circle = 72

def setup():
	global kaktusz
	global dino
	global f

	f = create_font("Arial.ttf", 10)
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
	global x
	global y_circle
	global x_circle
	global f

	stroke(255, 153, 0)

	background(255)
	# no_stroke()

	if x < 400:
		x += 1
	else:
		x = -50

	image(kaktusz, x, 200)
	image(dino, x, 300)

	if 50 < x_circle < 350 and y_circle < 350:
		x_circle += 3
	else:
		if y_circle < 350 and x_circle > 350:
			y_circle += 3
		else:
			if x_circle > 50:
				x_circle -= 3
			else:
				y_circle -= 3
				if y_circle < 72:
					x_circle = 51
					y_circle = 72


	# bright red
	fill(255, 0, 0)
	circle((x_circle, y_circle), 58)

	# text

	text_font(f, 13)
	fill(0)
	y_tostring = "Y: " + str(y_circle)
	x_tostring = "X: " + str(x_circle)
	text(x_tostring, (x_circle-11, y_circle-11))
	text(y_tostring, (x_circle-11, y_circle+1))

	if mouse_is_pressed:
		stroke(255)
	else:
		stroke(0)

	line((mouse_x - 66, mouse_y), (mouse_x + 66, mouse_y))
	line((mouse_x, mouse_y - 66), (mouse_x, mouse_y + 66))


	# # dark red
	# fill(127, 0, 0)
	# circle((144, 72), 58)
	#
	# # Pink (pale red)
	# fill(255, 200, 200)
	# circle((216, 72), 58)


if __name__ == '__main__':
	run()