# with open('dimensions.txt', 'r') as f:
#     width = int(f.readline().strip())
#     height = int(f.readline().strip())
#     background_color = tuple(map(int, f.readline().strip().split()))
#     line_color = tuple(map(int, f.readline().strip().split()))
from PIL import Image, ImageEnhance, ImageOps, ImageDraw
import numpy as np
import cv2


def image2lines(imageName, width, height, background_color, line_color):
    image = Image.open('media/images/' + imageName)
    image = image.resize((width, height))
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(3.0)
    image = ImageOps.grayscale(image)

    image_array = np.array(image)

    line_art_array = np.full((height, width, 3), background_color, dtype=np.uint8)

    num_vertical_lines = width // 12
    num_horizontal_segments = height // 3

    min_line_thickness = 1
    max_line_thickness = 9

    def calculate_thickness(intensity, max_intensity, min_thickness, max_thickness):
        normalized_intensity = intensity / 255
        inverted_intensity = 1 - normalized_intensity
        thickness = int(inverted_intensity * (max_thickness - min_thickness) + min_thickness)
        return thickness

    segment_height = height // num_horizontal_segments

    for i in range(num_horizontal_segments):
        segment_start_y = i * segment_height
        segment_end_y = (i + 1) * segment_height if i < num_horizontal_segments - 1 else height

        for j in range(num_vertical_lines):
            line_x = j * (width // num_vertical_lines)

            segment_slice = image_array[segment_start_y:segment_end_y, line_x:line_x + (width // num_vertical_lines)]

            average_intensity = np.mean(segment_slice)

            line_thickness = calculate_thickness(average_intensity, 255, min_line_thickness, max_line_thickness)

            cv2.line(line_art_array, (line_x, segment_start_y), (line_x, segment_end_y), line_color, line_thickness)

    line_art_image = Image.fromarray(line_art_array)
    output_path_lines = 'media/processed_images/' + 'lineRES' + imageName
    line_art_image.save('media/processed_images/' + 'lineRES' + imageName)

def getOutputPath_lines(imageName):
    return 'media/processed_images/' + 'lineRES' + imageName