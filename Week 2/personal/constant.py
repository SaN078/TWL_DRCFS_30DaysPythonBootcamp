import requests

response =  requests.get("http://www.google.com")
print(response.text)

#look into PEP8 for python styling

#writing variable name in caps for constant
STUDENT_COUNT = 55
CURRENT_MENTOR_COUNT = 6

