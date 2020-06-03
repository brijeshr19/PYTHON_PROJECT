#What is JSON?
#JSON: JavaScript Object Notation
#JSON is commonly used with data APIS
#JSON is a syntax for storing and exchanging data
#JSON is a light weight data - interchange format
#JSON is "self-describing" and easy to understand
#JSON is language independent *
#JSON uses JavaScript syntax, but the JSON format is text only

#JSON to JavaScript?
#var myJSON = '{"name":"John", "age":31, "city":"New York"}';
#var myObj = JSON.parse(myJSON);

#JavaScript to JSON
#var myObj = {name: "John", age: 31, city: "New York"};
#var myJSON = JSON.stringify(myObj);

#JSON in Python?
# Parse JSON into a Python dictionary and vice versa

import json

# JSON to Python Conversion
#  Sample JSON
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dictionary Object
userPythondictObj = json.loads(userJSON)

print(userPythondictObj)#{'first_name': 'John', 'last_name': 'Doe', 'age': 30}. Note this is disctionary Object
print(userPythondictObj['first_name'])#John

# Python dictionary Object to JSON Conversion

#dictionary Object
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

#JSON Object
carJSONObj = json.dumps(car)
print(carJSONObj)#{"make": "Ford", "model": "Mustang", "year": 1970}. This is JSON format