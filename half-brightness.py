from PIL import Image

# Open the input image
img = Image.open("img/starting-board.png")

# Convert the image to RGB format (if it's not already)
img = img.convert("RGB")

# Get the image size
width, height = img.size

# Create a new image with the same size and mode
new_img = Image.new(img.mode, (width, height))

# Loop over each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the pixel at this position
        pixel = img.getpixel((x, y))

        # Divide each color channel by 2 to reduce brightness
        new_pixel = (pixel[0] // 2, pixel[1] // 2, pixel[2] // 2)

        # Set the pixel in the new image
        new_img.putpixel((x, y), new_pixel)

# Save the new image to a file
new_img.save("img/output_image.jpg")
