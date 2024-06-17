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
today = dt.now()
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? :"),
}

add_pixel = requests.post(
    url=f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs/{graph_params["id"]}",
    json=pixel_params,
    headers=headers,
)
print(add_pixel.text)

# UPDATE A PIXEL
# update_params = {
#     "quantity": input(f"Update Data: How many hours did you actually code on {today.strftime("%Y-%m-%d")}? :")
# }
# update_pixel = requests.put(
#     url=f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs/{graph_params["id"]}/"
#         f"{today.strftime("%Y%m%d")}",
#     json=update_params,
#     headers=headers
# )

# DELETE A PIXEL
# delete_pixel = requests.delete(
#     url=f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs/{graph_params["id"]}/"
#         f"{input('On which date you want delete the data (YYYYMMDD) :')}",
#     headers=headers,
# )
# print(delete_pixel.text)
