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

def get_network_health():
    ticket = get_ticket()
    headers = {"X-Auth-Token": ticket}
    response = requests.get(base_url+"/assurance/health", headers=headers)
    health = response.json()
    network_health = health['response'][0]['networkDevices']['totalPercentage']
    return network_health

def get_network_issues():
	ticket = get_ticket()
	headers = {'Accept': 'application/json', 'X-Auth-Token': ticket}
	issues = requests.get(url = base_url +"/assurance/health-issues", headers=headers)
	issue_details = issues.json()
	devices = len(issue_details['response'])
	output = "Warning! There's an issue on "+ str(devices) +" details hardware:\n"
	output += "-"*60 +"\n"
	output += "No. | DEVICE | TIME | DESCRIPTION\n"
	output += "-"*60 +"\n"
	number=1
	for device in issue_details['response']:
		output += ""+ str(number) +". | "+ device['issueSource'] +" | "+ device['issueTimestamp'] +" | "+ device['issueDescription'] +"\n"
		number +=1
	return output

if __name__ == "__main__":
    network_health = get_network_health()
    if int(network_health) < 100:
        issues = get_network_issues()
        print(issues)
    else:
    	print("Percentage of Network Health : "+ network_health +"%")