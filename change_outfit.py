from openai import OpenAI
from base64 import b64decode
import json

with open("API_KEY.txt", "r") as API_file:
    API_KEY = API_file.read()

client = OpenAI(api_key=API_KEY)


def change_outfit(model_str: str, outfit_str: str):
    response = client.images.edit(
        image=open(model_str, "rb"),
        mask=open(outfit_str, "rb"),
        prompt="Add red t-shirt",
        size="1024x1024",
        n=1,
        response_format="b64_json",
    )
    file_name = "output-manekin.json"

    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(response.model_dump(), file)

    with open(file_name, mode="r", encoding="utf-8") as file:
        response_file = json.load(file)

    for index, image_dict in enumerate(response_file["data"]):
        image_data = b64decode(image_dict["b64_json"])
        image_file = "output-manekin.png"
        with open(image_file, mode="wb") as png:
            png.write(image_data)


change_outfit("test-manekin.png", "edited-manekin.png")
