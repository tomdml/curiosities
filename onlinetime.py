import requests

url = "http://api.timezonedb.com/v2.1/get-time-zone"
params = {
	'key':'YUNQYR5SK7Z7',
	'format':'json',
	'fields':'timestamp',
	'by':'zone',
	'zone':'Europe/London'
}

r = requests.get(url = url, params=params)

print(f"Server returned status code {r.status_code}")

webTime = r.json()['timestamp']

print(f"Time from Web is {webTime}")