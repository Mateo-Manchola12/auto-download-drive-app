# Icono cuadrado negro 512x512 px para macOS y Windows
import sys
from PIL import Image

img = Image.new('RGBA', (512, 512), (0, 0, 0, 255))
img.save('macos/icon.png')
img.save('macos/icon.ico')
