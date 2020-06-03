
import json

# Deserialize JSON to Python object (a str, bytes or bytearray instance
# containing a JSON document)

#  Sample JSON Single row
#userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

#  Sample JSON Multiple row
userJSON1='[{"id":1,"text":"Brijesh"},{"id":2,"text":"Raj"},{"id":3,"text":"Nav"}]'
items = json.loads(userJSON1)

# for in loop
for x in items:
    print(x)  # print first array and second array
    print(x['text'])  # print text

# if loop
if True:
    print(1)
else:
    print(2)

# try catch finally
...
try:
    print(1)
except expression as identifier:
    print(2)
else:
    print(3)
finally:
    print(4)
...
