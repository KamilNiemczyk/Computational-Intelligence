
import os
import cv2

def count_birds(image):
    #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    closing = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    black_object_count = len(contours)
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 0, 255), 2)
    return black_object_count

folder = "bird_miniatures"
images = os.listdir(folder)

for image_name in images:
    image_path = os.path.join(folder, image_name)
    
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    bird_count = count_birds(image)

    print(f"Image: {image_name}, Bird count: {bird_count}")