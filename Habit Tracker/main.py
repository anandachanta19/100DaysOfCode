import requests
import os
from dotenv import load_dotenv

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

create_graph = requests.post(
    url=f"https://pixe.la/v1/users/{os.environ["PIXELA_USERNAME"]}/graphs",
    json=graph_params,
    headers=headers,
)
