import requests

#TOKEN = 'KEY'
USERNAME = 'renato5650'
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
GRAPH_ID = 'graph1'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor': 'yes'
}
url_user = 'https://pixe.la/v1/users'
#create_user = requests.post(url=url_user, json=user_params)
#print(create_user.text)

headers = {
    'X-USER-TOKEN': TOKEN
}
graphs_params = {
    'id': 'graph1',
    'name': 'renatoEfforts',
    'unit': 'Km',
    'type': 'float',
    'color': 'momiji'
}
url_graphs = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
#create_graph = requests.post(url_graphs, json=graphs_params, headers=headers)
#print(create_graph.text)

post_pixel_params = {
    'date': '20250914',
    'quantity': '40.5'
}
url_pixel_post = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'
create_pixel_post = requests.post(url=url_pixel_post, json=post_pixel_params, headers=headers)
print(create_pixel_post.text)