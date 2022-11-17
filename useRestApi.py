import requests

response = requests.get("http://127.0.0.1:8000/students")
print(response.json())

newStudent = {
  "first_name": "Hellen",
  "last_name": "Xi",
  "gender": "M",
  "date_of_birth": "2012-11-15",
  "major": "MA"
}
response2 = requests.post("http://127.0.0.1:8000/students", json = newStudent)
print(response2.text)
