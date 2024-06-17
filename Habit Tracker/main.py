import requests
import os
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()
# user_params = {
#     "token": os.environ["PIXELA_AUTHENTICATION_TOKEN"],
#     "username": os.environ["PIXELA_USERNAME"],
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# create_user = requests.post(url="https://pixe.la/v1/users", json=user_params)

# CREATE A GRAPH
graph_params = {
    "id": "anand-code",
    "name": "Daily Code Time",
    "unit": "hours",
    "type": "int",
    "color": "shibafu",
    "timezone": "Asia/Kolkata",
}

headers = {
    "X-USER-TOKEN": os.environ["PIXELA_AUTHENTICATION_TOKEN"]
}
#
# create_graph = requests.post(
#     url=f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs",
#     json=graph_params,
#     headers=headers,
# )

# ADDING PIXEL
today_date = ""
for part in str(dt.now().date()).split("-"):
    today_date += part

pixel_params = {
    "date": today_date,
    "quantity": "8",
}

add_pixel = requests.post(
    url=f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs/{graph_params["id"]}",
    json=pixel_params,
    headers=headers,
)
print(add_pixel.text)
