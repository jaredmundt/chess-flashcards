from PIL import Image, ImageDraw

# Load the starting board image
base_img = Image.open("img/starting-board.png")

# Define the size of a single square on the board
square_size = base_img.width // 8

# Define the colors for the highlighted squares
white_highlight_color = (255, 255, 0, 128)
black_highlight_color = (0, 0, 255, 128)

# Loop through all 64 squares on the board
for rank in range(8):
    for file in range(8):
        # Create a new image with the same size and mode as the base image
        new_img = Image.new("RGBA", base_img.size)

        # Copy the base image onto the new image
        new_img.paste(base_img)

        # Determine the position of the square to highlight
        x1 = file * square_size
        y1 = rank * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size

        # Create a new ImageDraw object for the new image
        draw = ImageDraw.Draw(new_img)

        # Highlight the square with the appropriate color based on its position
        if (rank + file) % 2 == 0:
            draw.rectangle((x1, y1, x2, y2), fill=white_highlight_color)
        else:
            draw.rectangle((x1, y1, x2, y2), fill=black_highlight_color)

        # Save the new image with a filename that indicates the highlighted square
        filename = f"img/highlighted-square-r{rank+1}-f{file+1}.png"
        new_img.save(filename)

# Flip the board and repeat the process for the black pieces on bottom
flipped_base_img = base_img.transpose(method=Image.FLIP_TOP_BOTTOM)

for rank in range(8):
    for file in range(8):
        new_img = Image.new("RGBA", flipped_base_img.size)
        new_img.paste(flipped_base_img)
        x1 = file * square_size
        y1 = rank * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        draw = ImageDraw.Draw(new_img)
        if (rank + file) % 2 == 0:
            draw.rectangle((x1, y1, x2, y2), fill=black_highlight_color)
        else:
            draw.rectangle((x1, y1, x2, y2), fill=white_highlight_color)
        filename = f"img/highlighted-square-flipped-r{rank+1}-f{file+1}.png"
        new_img.save(filename)
