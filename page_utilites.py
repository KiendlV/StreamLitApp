import PIL

def get_favicon():
    image_directory = "images/brain.webp"
    image = PIL.Image.open(image_directory)
    return image