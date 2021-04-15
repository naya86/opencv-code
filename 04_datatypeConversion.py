import cv2
import numpy as np

source = cv2.imread('data/images/sample.jpg', 1)  # 컬러

scalingFactor = 1 / 255.0

# Conver unsigned int (8bit) to float

source = np.float32(source)
source = source * scalingFactor
print(source)


# Conver back to unsigned int   (8bit)

source = source * ( 1.0 / scalingFactor)
source = np.uint8(source)
print(source)