import numpy as np
from PIL import Image

image=Image.open(".\\image.png")

imageArray=np.asarray(image)
width,height=image.size
image=image.convert("RGB")
final="["

for y in range(height):
    for x in range(width):
        r,g,b=image.getpixel((x,y))
        final+=(f"({r},{g},{b})")
        if x <= width-1 and x*y!=(height-1)*(width-1):
            final+=","
    

final+="]"
print(final)