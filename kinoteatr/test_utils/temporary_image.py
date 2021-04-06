from PIL import Image
from io import BytesIO


def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new('RGBA', size, color)
    image.save(temp_file, 'png')
    return temp_file


def get_temporary_bytes_io_image():
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new('RGBA', size, color)
    temp_bytes = BytesIO()
    image.save(temp_bytes, 'png')
    temp_bytes.seek(0)
    return temp_bytes
