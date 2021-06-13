import requests

question_data = []
response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
if response.raise_for_status() is None:
    data = response.json()
    question_data = data["results"]
