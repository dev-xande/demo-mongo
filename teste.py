from uuid import uuid4
import json

# a = str(uuid4())

# print(type(uuid4))
# print(type(a))
# print(a)

from bson.objectid import ObjectId
b = ObjectId()
print(b)
print(type(b))
s = json.loads(b)
print(s)
print(type(s))