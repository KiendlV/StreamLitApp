from PIL import Image

def get_favicon():
    image_directory = "images/brain.webp"
    image = Image.open(image_directory)
    return image