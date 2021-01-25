import argparse

import cv2


parser = argparse.ArgumentParser(description='Image manipulation on PNG and JPEG formats')
parser.add_argument(
    'first_image_path',
    metavar='first_image_path',
    help='Path to the image.'
)
parser.add_argument(
    'second_image_path',
    metavar='second_image_path',
    help='Path to the image.'
)
args = parser.parse_args()
first_image = cv2.imread(args.first_image_path)
second_image = cv2.imread(args.second_image_path)
first_image = cv2.resize(first_image, (300, 300))
second_image = cv2.resize(second_image, (300, 300))
# Split the first image into B, G, R channels
first_im_b_channel, first_im_g_channel, first_im_r_channel = cv2.split(
    first_image
)
# Split the second image into B, G, R channels
second_im_b_channel, second_im_g_channel, second_im_r_channel = cv2.split(
    second_image
)
# Get the difference of Blue channel between the two images
diff_b_channel = first_im_b_channel - second_im_b_channel
# Get the difference of Green channel between the two images
diff_g_channel = first_im_g_channel - second_im_g_channel
# Get the difference of Red channel between the two images
diff_r_channel = first_im_r_channel - second_im_r_channel
cv2.imwrite('../images/blue_channel_difference.jpg', diff_b_channel)
cv2.imwrite('../images/green_channel_difference.jpg', diff_g_channel)
cv2.imwrite('../images/red_channel_difference.jpg', diff_r_channel)
cv2.imshow('Blue Channel difference', diff_b_channel)
cv2.waitKey()
cv2.imshow('Green Channel difference', diff_g_channel)
cv2.waitKey()
cv2.imshow('Red Channel difference', diff_r_channel)
cv2.waitKey()
cv2.destroyAllWindows()
