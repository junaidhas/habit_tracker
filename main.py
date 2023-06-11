import requests
import datetime as dt
import os

#saved username and password saved as environment variables for security

TOKEN = os.environ.get("password")
USERNAME = os.environ.get("username")

# ----------------------------1. Creating a new PIXELA user--------------------#

PIXELA_URL_ENDPOINT = "https://pixe.la/v1/users"

PIXELA_PARMETERS ={
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

response = requests.post(url=PIXELA_URL_ENDPOINT,json=PIXELA_PARMETERS)
print(response.text)

#---------------------2. Creating a new graph for daily measuring daly coding hours----------#
GRAPH_ENDPOINT = f"{PIXELA_URL_ENDPOINT}/{USERNAME}/graphs"

GRAPH_PARAMETERS = {
    "id":"graph2",
    "name":"Daily coding graph",
    "unit":"hours",
    "type":"float",
    "color":"momiji"
}

HEADERS ={
    "X-USER-TOKEN":TOKEN
}


graph_response = requests.post(url=GRAPH_ENDPOINT,json=GRAPH_PARAMETERS,headers=HEADERS)
print(graph_response.text)

post_pixel_endpoint = f"{PIXELA_URL_ENDPOINT}/{USERNAME}/graphs/graph2"

today = dt.datetime(year=2023,month=6,day=9)
# print(today.strftime('%Y''%m''%d'))

#--------------------------3. Creating a new pixel in the graph --------------------------#

create_pixel_parameters ={
    "date":f"{today.strftime('%Y''%m''%d')}",
    "quantity":"0.5"
}

create_pixel_response = requests.post(url=post_pixel_endpoint,
                                      json=create_pixel_parameters,
                                      headers=HEADERS)
print(create_pixel_response.text)


#----------------------------4. UPDATING A PIXEL ------------------------------------#
# this will update the quantity of the existing pixel or if the pixel didnt exist it will create a new one
update_pixel_endpoint = f"{PIXELA_URL_ENDPOINT}/{USERNAME}/graphs/graph2/20230609"
update_pixel_parameters = {
    "quantity":"0.5"
}

update_pixel_response = requests.put(url=update_pixel_endpoint,
                                     json=update_pixel_parameters,
                                     headers = HEADERS)

print(update_pixel_response.text)

#---------------------------5. DELETE PIXEL -----------------------------#
delete_pixel_endpoint = f"{PIXELA_URL_ENDPOINT}/{USERNAME}/graphs/graph2/20230609"


delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers = HEADERS )
print(delete_pixel_response.text)
