import cv2

def crop_image_from_screenshot(screenshot_path, crop_area):
    # Load the screenshot
    screenshot = cv2.imread(screenshot_path)
    
    # Extract the crop area coordinates
    x, y, width, height = crop_area
    
    # Crop the image
    cropped_image = screenshot[y:y+height, x:x+width]
    
    return cropped_image

# Example usage
screenshot_path = 'temp-img/uncropped-white.png'
crop_area = (100, 100, 300, 200)  # Example coordinates: (x, y, width, height)

cropped_image = crop_image_from_screenshot(screenshot_path, crop_area)

# Save the cropped image
cv2.imwrite('temp-img/cropped_image.png', cropped_image)
