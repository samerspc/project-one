# with open('dimensions.txt', 'r') as f:
#     width = int(f.readline().strip())
#     height = int(f.readline().strip())
#     background_color = tuple(map(int, f.readline().strip().split()))
#     line_color = tuple(map(int, f.readline().strip().split()))
from PIL import Image, ImageEnhance, ImageOps, ImageDraw
import numpy as np
import random
import cv2
def image2dots(imageName, width, height, background_color, line_color):
    image = Image.open('media/images/' + imageName)
    image = image.resize((width, height))
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(3.0)
    image = ImageOps.grayscale(image)

    num_points = width // 12
    points = num_points**2
    points_per_side = int(np.sqrt(points))
    section_width = width // points_per_side
    section_height = height // points_per_side

    processed_image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(processed_image)

    max_radius = min(section_width, section_height) // 2 + 1

    for x in range(0, width, section_width):
        for y in range(0, height, section_height):
            section = image.crop((x, y, x + section_width, y + section_height))
            mean = np.mean(section)
            radius = (255 - mean) / 255 * max_radius
            ellipse_x0 = x + section_width / 2 - radius
            ellipse_y0 = y + section_height / 2 - radius
            ellipse_x1 = x + section_width / 2 + radius
            ellipse_y1 = y + section_height / 2 + radius
            draw.ellipse((ellipse_x0, ellipse_y0, ellipse_x1, ellipse_y1), fill=line_color)

    output_path_dots = 'media/processed_images/' + 'dotRES' + str(random.randint(0, 100000)) + imageName
    processed_image.save(output_path_dots)
    return output_path_dots

# def getOutputPath_dots(imageName):
#     return 'media/processed_images/' + 'dotRES' + imageName