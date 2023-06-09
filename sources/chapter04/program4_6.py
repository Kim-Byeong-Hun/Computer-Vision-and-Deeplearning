# 정규화 절단 알고리즘으로 영역 분할하기
import skimage
import numpy as np
import cv2 as cv
import time

coffee = skimage.data.coffee()

start = time.time()
slic = skimage.segmentation.slic(coffee, compactness=20, n_segments=600, start_label=1)
g = skimage.graph.rag_mean_color(coffee, slic, mode = 'similarity')
ncut = skimage.graph.cut_normalized(slic, g)
print(coffee.shape, 'Coffee영상을 분할하는데 ', time.time()-start, '초 소요')

marking = skimage.segmentation.mark_boundaries(coffee, ncut)
ncut_coffee = np.uint8(marking*255.0)

cv.imshow('Nomalized cut', cv.cvtColor(ncut_coffee, cv.COLOR_RGB2BGR))

cv.waitKey()
cv.destroyAllWindows()

np.unique(ncut).size
