import cv2
import numpy as np


lena_image = cv2.imread('../images/lena.jpg')
cv2.imshow('Lena', lena_image)
# Convert image to YUV color space.
ycrcb_image = cv2.cvtColor(lena_image, cv2.COLOR_BGR2YCR_CB)
cv2.imshow('Lena YUV', ycrcb_image)
# Split the image into separate color planes
y, cr, cb = cv2.split(ycrcb_image)
# Allocates a matrix of the specified size and type
noise = np.zeros(lena_image.shape, dtype=np.uint8)
# Fills the matrix with normally distributed random values;
cv2.randn(noise, (128, 128, 128), (20, 20, 20))
cv2.imshow('Noise', noise)
# Blur the noise a bit, kernel size is 3x3 and both sigma's are set to 0.5
noise_blurred = cv2.GaussianBlur(noise, (3, 3), 0.5, 0.5)
cv2.imshow('Noise blurred', noise_blurred)
noise_blurred_first_color_channel, _, _ = cv2.split(noise_blurred)
brightness_gain = 0
contrast_gain = 1.7
cv2.addWeighted(
    y,
    contrast_gain,
    noise_blurred_first_color_channel,
    1,
    -128 + brightness_gain,
     y
)
color_scale = 0.5
# Scale and add values to plane[1];
cv2.convertScaleAbs(cr, cr, color_scale, 128 * (1 - color_scale))
# TODO: Apply Element-wise multiplication to 'y' matrix
# y *= 1. / 255
# Now merge the results back
ycrcb_merged = cv2.merge((y, cr, cb))
# Produce the output RGB image
lena_image_with_grain = cv2.cvtColor(ycrcb_merged, cv2.COLOR_YCrCb2RGB)
cv2.imshow('Lena with grain', lena_image_with_grain)
cv2.waitKey()
cv2.destroyAllWindows()
