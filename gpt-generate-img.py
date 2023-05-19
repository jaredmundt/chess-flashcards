from PIL import Image, ImageDraw, ImageFont

# Constants for board size and square size
BOARD_SIZE = 400
SQUARE_SIZE = BOARD_SIZE // 8

# Function to generate flashcards
def generate_flashcards():
    # Create an empty list to store flashcards
    flashcards = []

    # Iterate over each square on the board
    for row in range(8):
        for col in range(8):
            # Create a new blank image for each flashcard
            card = Image.new('RGB', (BOARD_SIZE, BOARD_SIZE), 'white')
            draw = ImageDraw.Draw(card)

            # Draw the square on the board
            square_pos = (col * SQUARE_SIZE, row * SQUARE_SIZE)
            square = (square_pos[0], square_pos[1], square_pos[0] + SQUARE_SIZE, square_pos[1] + SQUARE_SIZE)
            draw.rectangle(square, outline='black', width=2)

            # Add the coordinate text on the other side of the card
            font = ImageFont.truetype('arial.ttf', 30)
            text_width, text_height = draw.textsize(get_coordinate(col, row), font=font)
            text_pos = ((BOARD_SIZE - text_width) // 2, (BOARD_SIZE - text_height) // 2)
            draw.text(text_pos, get_coordinate(col, row), font=font, fill='black')

            # Add the flashcard to the list
            flashcards.append(card)

    return flashcards

# Function to get the chess coordinate for a given square
def get_coordinate(col, row):
    letter = chr(col + 97)  # 'a' is ASCII code 97
    number = str(8 - row)
    return letter + number

# Generate the flashcards for white's perspective
white_flashcards = generate_flashcards()

# Flip the board and generate the flashcards for black's perspective
black_flashcards = [card.transpose(Image.FLIP_TOP_BOTTOM) for card in white_flashcards]

# Combine both sets of flashcards
all_flashcards = white_flashcards + black_flashcards

# Save the flashcards to image files
for i, card in enumerate(all_flashcards):
    card.save(f'flashcard_{i+1}.png')

