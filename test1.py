import requests

# Sends a GET request:param url: URL for the new Request object.

# this will results 1 item
# response = requests.get('https://randomuser.me/api')

# json(**kwargs) Returns the json-encoded content of a response, if any.
#: param ** kwargs: Optional arguments that json.loads takes.

# data = response.json()

# this will results 10 item
response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()

# Since data contains the results array
for x in data['results']:
    print(x['name']['first'], x['name']['last'])

# AutoDocString
    def greet(greeting, name):
        """Return a greeting
        Arguments:
        greeting {string} -- A greet word
        name {string} -- A person name

        Returns
        string -- A greeting with name
        """
        return f'{greeting} {name}'

    print(greet('hello', 'world'))
