import cv2
import numpy as np

background_color = [248,240,232]
dots_color = [16,16,16]

max_dots = 250

org_image = cv2.imread('bp.JPG', 0)

org_image_height, org_image_width = org_image.shape

if org_image_height == max(org_image_height, org_image_width):
    downsize_image = cv2.resize(org_image,(int(org_image_height*(max_dots/org_image_width)),max_dots))
else:
    downsize_image = cv2.resize(org_image,(int(org_image_height*(max_dots/org_image_width))))

downsize_image_height, downsize_image_width = downsize_image.shape

multiplier = 100

blank_img_height = downsize_image_height * multiplier
blank_img_width = downsize_image_width * multiplier

padding = int(multiplier/2)

blank_image = np.full(((blank_img_height), (blank_img_width), 3), background_color, dtype=np.uint8)

for y in range(0, downsize_image_height):
    for x in range(0, downsize_image_width):
        cv2.circle(blank_image, (((x * multiplier) + padding),((y*multiplier)+padding)), int((0.6 * multiplier) * ((255-downsize_image[y][x])/255)), dots_color, -1)

    cv2.imwrite('bp.JPG', blank_image)