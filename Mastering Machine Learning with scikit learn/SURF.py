import mahotas as mh##Image processing Libray for python
from mahotas.features import surf

image = mh.imread('lena.jpg', as_grey=True)
print('The first SURF descriptor:\n', surf.surf(image)[0])
print('Extracted %s SURF descriptors'%len(surf.surf(image)))
