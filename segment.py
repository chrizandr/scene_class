import numpy as np

def segmentImage(img):
    if img.shape == (256,256):
        segments = list()
        for i in range(0,256,64):
            for j in range(0,256,64):
                segments.append(img[i:i+64,j:j+64])
        return segments
    else:
        return None
