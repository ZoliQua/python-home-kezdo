# SOURCE https://python.plainenglish.io/how-to-create-a-cli-app-in-python-aea606509332

import typer
import os
from PIL import Image

cli = typer.Typer()


@cli.command()
def stats(filename: str):
	'''
	Show image info for FILENAME
	'''
	img = Image.open(filename)

	# Print properties
	typer.echo(f' Format:\t {img.format}')
	typer.echo(f'   Mode:\t {img.mode}')
	typer.echo(f'   Size:\t {img.size[0]} x {img.size[1]}')
	typer.echo(f'Palette:\t {img.palette}')
	typer.echo(f'Information:\t {img.info}')

@cli.command()
def statsdir(dirname: str):
	'''
	Show image info for a DIRECTORY
	'''

	images = os.listdir(dirname)

	# iterate images array

	for image in images:
		img = Image.open(f'{dirname}/{image}')
		cleaned_name = os.path.splitext(image)[0]

		# Print properties
		typer.echo(f'{dirname}/{image} PROPERTIES')
		typer.echo('=' * 20)
		typer.echo(f' Format:\t {img.format}')
		typer.echo(f'   Mode:\t {img.mode}')
		typer.echo(f'   Size:\t {img.size[0]} x {img.size[1]}')
		typer.echo(f'Palette:\t {img.palette}')
		typer.echo(f'Information:\t {img.info}')
		# Print end spacer
		typer.echo('=' * 20)

@cli.command()
def statsdirls(dirname: str):
	'''
	Show image info for a DIRECTORY
	'''

	extensions = ['png', 'jpg', 'jpeg', 'bmp', 'gif']

	images = os.listdir(dirname)

	# iterate images array

	typer.echo(f'Folder Name: {dirname}')
	typer.echo(f'IMAGE\t\tFORMAT\tSIZE')

	for image in images:
		img = Image.open(f'{dirname}/{image}')

		extension = os.path.splitext(image)[1][1:]
		if extension not in extensions:
			continue

		# Print properties
		typer.echo(f'{image}\t{img.format}\t{img.size[0]} x {img.size[1]}')


@cli.command()
def resize(filename: str, width: int, heigth: int, out: str = 'out.jpg'):
	'''
	Resize FILENAME with new WIDTH and HEIGHT.

	The output filename will be "out.jpg" if not specified by --out.
	'''
	img = Image.open(filename)
	resized = img.resize((width, heigth), Image.LANCZOS)
	resized.save(out)
	typer.echo(f'New image saved {out} with size {width}x{heigth}')


if __name__ == '__main__':
	cli()
