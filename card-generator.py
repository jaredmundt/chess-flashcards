from PIL import Image, ImageDraw
import os
import shutil

# Define the file paths of the base images
black_base_image_path = "img/starting-black.png"
white_base_image_path = "img/starting-white.png"

# Define the output directory to save the generated images
output_directory = "output/"
if os.path.exists(output_directory):
    shutil.rmtree(output_directory)
os.makedirs(output_directory)

# Define the size of the chessboard
board_size = 8

# Define the radius and outline color of the circle
circle_radius = 50
outline_color = "green"
outline_thickness = 12

# Load the base images
black_base_image = Image.open(black_base_image_path)
white_base_image = Image.open(white_base_image_path)

# Generate images with circled squares
for row in range(board_size):
    for col in range(board_size):
        # Create a copy of the base images for each square
        black_image = black_base_image.copy()
        white_image = white_base_image.copy()

        # Create a draw object for each image
        black_draw = ImageDraw.Draw(black_image)
        white_draw = ImageDraw.Draw(white_image)

        # Calculate the position of the square on the chessboard
        square_x = col * black_base_image.width // board_size
        square_y = row * black_base_image.height // board_size

        # Calculate the coordinates of the circle
        circle_x = square_x + black_base_image.width // (2 * board_size)
        circle_y = square_y + black_base_image.height // (2 * board_size)
        circle_coords = (
            circle_x - circle_radius,
            circle_y - circle_radius,
            circle_x + circle_radius,
            circle_y + circle_radius,
        )

        # Draw a thicker circle on the image for each square
        black_draw.ellipse(circle_coords, outline=outline_color, width=outline_thickness)
        white_draw.ellipse(circle_coords, outline=outline_color, width=outline_thickness)
        
        # Save the generated images
        letter = chr(ord('a') + row)
        black_image.save(f"{output_directory}black_{letter}{col}.png")
        white_image.save(f"{output_directory}white_{letter}{col}.png")

