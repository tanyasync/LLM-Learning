import requests

if requests:
	response = requests.get("https://api.github.com/")
	response.raise_for_status()
	print("Status Code:", response.status_code)
	data = response.json()
	print(data.get("current_user_url"))


#post --call
payload = {"prompt":"Hello","max_tokens":50, "temp":.2}
headers = {"Authorization":"Bearer fake-key"}



post = requests.post(
    "http://httpbin.org/post",
    json=payload,
    headers=headers,
    timeout=10

)

post.raise_for_status()
echoed_data =post.json()
print(echoed_data)