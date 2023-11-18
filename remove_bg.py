from rembg import remove
from PIL import Image


def remove_bg(img_source: str) -> Image:
    input_img = Image.open(img_source)
    output_img = remove(input_img)

    output_img.save(img_source.replace(".jpg", "_output.png"))

    # return output_img.save(img_source.removesuffix(".png").join("_output.png"))
    remove_bg("20231117_222909.jpg")
