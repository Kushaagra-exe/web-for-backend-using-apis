import json

# us = 'https://randomuser.me/api?nat=us'

# resp = (requests.get(us)).json()
# # print(resp.content)
# # a = resp.json()
# b= json.dumps(resp)
# json_data = json.loads(b)
# print(json_data)

st = '{"results":[{"gender":"male","name":{"title":"Mr","first":"Aiden","last":"Mendoza"},"location":{"street":{"number":7045,"name":"Country Club Rd"},"city":"Sioux Falls","state":"Pennsylvania","country":"United States","postcode":27385,"coordinates":{"latitude":"-77.6320","longitude":"-108.9480"},"timezone":{"offset":"+1:00","description":"Brussels, Copenhagen, Madrid, Paris"}},"email":"aiden.mendoza@example.com","login":{"uuid":"097b2db3-2a17-408b-adca-bd06641037be","username":"silverostrich738","password":"supra","salt":"iPgDdGSQ","md5":"1e48dbbe501c343d0d9a418f7bf19aac","sha1":"e204fa3fb3b4ef5e93dba9cfeb20ab5b3d03795c","sha256":"f79ac4d12e59bc4cdd7866ef776a903129ae5b096066da91ce2ea8ab9213eac5"},"dob":{"date":"1993-11-02T19:48:24.821Z","age":28},"registered":{"date":"2002-11-14T17:03:56.521Z","age":19},"phone":"(530) 224-6936","cell":"(969) 361-5353","id":{"name":"SSN","value":"280-24-9179"},"picture":{"large":"https://randomuser.me/api/portraits/men/42.jpg","medium":"https://randomuser.me/api/portraits/med/men/42.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/42.jpg"},"nat":"US"}],"info":{"seed":"853efa720370f707","results":1,"page":1,"version":"1.4"}}'
a= json.loads(st)
print(a)