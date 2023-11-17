from openai import OpenAI, api_key
from PIL import Image

with open("API_KEY.txt", "r") as API_file:
    API_KEY = API_file.read()

client = OpenAI(api_key=API_KEY)


def change_outfit(model_img: str, outfit_img: str):
    model = Image.open(model_img)
    mask = Image.open(outfit_img)
    size = mask.size
    model = model.resize(size, Image.BILINEAR)
    model.save("model.png")

    response = client.images.edit(
        image=open("model.png", "rb"),
        mask=open(outfit_img, "rb"),
        prompt="boy has yellow dress",
        size="1024x1024",
        n=1,
    )

    output_img_url = response.data[0].url
    print(output_img_url)


change_outfit("mati123.png", "suknia.png")
