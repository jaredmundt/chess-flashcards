import cv2

# Load the image
image = cv2.imread('temp-img/screenshot.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection
edges = cv2.Canny(gray, threshold1, threshold2)

# Find and draw contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Display the image with the detected edges
cv2.imshow('Edge Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
