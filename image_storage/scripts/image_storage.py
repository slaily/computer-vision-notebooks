import argparse
import cv2

from numpy import (
    all,
    average
)


parser = argparse.ArgumentParser(description='Process PGM and PPM files')
parser.add_argument(
    'image_path',
    metavar='image_path',
    help='Path to the image.'
)
args = parser.parse_args()
image = cv2.imread(args.image_path)
image_extension = args.image_path[-3:]

if image_extension == 'pgm':
    cv2.imshow('Input Image PGM', image)
    cv2.waitKey()
    # Image inversion operation
    # Alternative image inversion:
    #   * image_inverted = ~image
    #   * image_inverted = cv2.bitwise_not(image)
    image_inverted = (255 - image)
    cv2.imwrite('../images/grayscale_inverted.ppm', image_inverted)
    cv2.imshow('Output Image Inverted PGM', image_inverted)
    cv2.waitKey()
    cv2.destroyAllWindows()
elif image_extension == 'ppm':
    cv2.imshow('Input Image PPM', image)
    cv2.waitKey()
    color_image = image.copy()
    # Define Blue color
    blue_color  = [255, 0, 0]
    # Define Green color
    green_color = [0, 255, 0]
    # Define Red color
    red_color   = [0, 0, 255]
    # Create a Mask of all Blue color pixels
    blue_color_pixels_mask = all(color_image == blue_color, axis=-1)
    # Create a Mask of all Green color pixels
    green_color_pixels_mask = all(color_image == green_color, axis=-1)
    # Create a Mask of all Red color pixels
    red_color_pixels_mask = all(color_image == red_color, axis=-1)
    # Change all Blue color pixels to Green color pixels
    color_image[blue_color_pixels_mask] = green_color
    # Change all Green color pixels to Red color pixels
    color_image[green_color_pixels_mask] = red_color
    # Change all Red color pixels to Blue color pixels
    color_image[red_color_pixels_mask] = blue_color
    # Save the transformed image
    cv2.imwrite('../images/rgb_colours_transformed.ppm', color_image)
    cv2.imshow('Output Color Image PPM', color_image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    # TODO - Convert the color image to grayscale
    # https://web.stanford.edu/class/cs101/image-6-grayscale-adva.html
    # avg_color_per_row = average(color_image, axis=0)
    # avg_color = average(avg_color_per_row, axis=0)
else:
    print(
        (
        f'[INFO] - Image with extension `{image_extension}` '
        'is not supported for processing.')
    )
