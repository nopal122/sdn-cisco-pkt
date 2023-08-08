import requests

base_url = "http://192.168.1.254/api/v1"
user = "nopal"
password = "nopal122"

def get_ticket():
	headers = {"content-type": "application/json"}
	data = {"username": user, "password": password}
	
	response = requests.post(base_url+"/ticket", headers=headers, json=data)
	ticket = response.json()
	service_ticket = ticket["response"]["serviceTicket"]
	return service_ticket

if __name__ == "__main__":
	ticket = get_ticket()
	print("Service Ticket : ", ticket)