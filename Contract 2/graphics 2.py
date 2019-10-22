from PIL import Image

from opensimplex import OpenSimplex
tmp = OpenSimplex(seed=1)
print (tmp.noise2d(x=10, y=10))
threshold=100



img=Image.new("RGB",(600,900))  #picked the size first
img_data = img.load()
for X in range(img.size[0]):
    for Y in range(img.size[1]):
        value = int(round((tmp.noise2d(X/50,Y/50) + 1) * 255 / 2))

        if value < threshold: #colors
            img_data[X, Y] = (139,69,19)
        else:
            img_data[X, Y] = (185,202,222)
img.show()
