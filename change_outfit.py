from openai import OpenAI, api_key
import cv2

with open("API_KEY.txt", "r") as API_file:
    API_KEY = API_file.read()

client = OpenAI(api_key=API_KEY)


def change_outfit(model_img: str, outfit_img: str):
    img_rbg = cv2.imread(model_img)
    img_gray = cv2.cvtColor(img_rbg, cv2.COLOR_BGR2GRAY)

    # response = client.images.generate(
    #     image=model_img,
    #     mask=outfit_img,
    #     size="1024x1024",
    #     quality="standard",
    #     n=1,
    # )

    output_img_url = response.data[0].url
    print(output_img_url)


change_outfit("da", "Ddada")
