from PIL import Image
import numpy as np

# Characters arranged from darkest to lightest
ascii_chars = "@%#*+=-:. "

def image_to_ascii(path, new_width=100):
    # Load and convert to grayscale
    img = Image.open(path).convert('L')

    # Resize image to new width
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)  # adjust for terminal height distortion
    img = img.resize((new_width, new_height))

    # Convert image to numpy array
    pixels = np.array(img)

    # Map each pixel to an ASCII character
    ascii_img = []
    for row in pixels:
        ascii_row = [ascii_chars[pixel * len(ascii_chars) // 256] for pixel in row]
        ascii_img.append("".join(ascii_row))

    return "\n".join(ascii_img)

# Run
ascii_art = image_to_ascii("bird.jpg", new_width=80)
print(ascii_art)
