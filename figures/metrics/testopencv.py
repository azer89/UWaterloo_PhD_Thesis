import cv2
import numpy as np

# read input
#img = cv2.imread('harambe.jpg')

# convert to YCbCr
#ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# use inRange thresholding
#thresh = cv2.inRange(ycrcb, np.array([0, 135, 85]), np.array([200, 200, 200]))
img = cv2.imread('star.jpg')
thresh = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# get outer contour
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
big_contour = max(cnts, key=cv2.contourArea)

# draw filled contour on black background
filled = np.zeros_like(thresh)
cv2.drawContours(filled, [big_contour], -1, (255), cv2.FILLED)

# get distance transform
result = filled.copy()
result = cv2.distanceTransform(result, distanceType=cv2.DIST_L2, maskSize=3, dstType=cv2.CV_8U)

# stretch to full dynamic range
result2 = cv2.normalize(result, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# save result
cv2.imwrite('dog_thresh.png', thresh)
cv2.imwrite('dog_filled_contour.png', filled)
cv2.imwrite('dog_distance.png', result)
cv2.imwrite('dog_distance_normalized.png', result2)

# show results
# note result image will look binary
cv2.imshow("thresh", thresh)
cv2.imshow("filled", filled)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()