from PIL import Image
import numpy as np

img = np.array(Image.open("480-360-sample.bmp").reshape(480, 360, 3))
