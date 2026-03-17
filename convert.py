from PIL import Image
import os

def convert_webp(input_path, output_path, output_format="png"):

    img = Image.open(input_path)

    if output_format == "jpg":
        img = img.convert("RGB")

    img.save(output_path)

    return output_path