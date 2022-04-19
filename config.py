import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://cosmos-python-demo.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', '3dS511dkLygKOL2YRjw2JPpKiw850Y1w4NMjVW9EckbZsPAMu9slEidEMs7WpF4NQ82quhfVNn8g3d5IbLV5cA=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}

# settings = {
#     'host': os.environ.get('ACCOUNT_HOST', 'https://localhost:8081'),
#     'master_key': os.environ.get('ACCOUNT_KEY', 'C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw=='),
#     'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
#     'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
# }