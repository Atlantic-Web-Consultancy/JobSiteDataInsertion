import requests
import os
import time
import datetime
baseURL = open(os.getcwd() + '/../config/' + 'config').readlines()[0].replace('\n', '')
requestURL = 'http://' + baseURL + '/createSeeker'
f = open(os.getcwd() + '/../data/' + 'employers.csv')
csvLines = f.readlines()
csvLines.pop(0)
for line in csvLines:
	id, username, first_name, last_name , email, phone, organization, password = line.split(',')
	data = {
		"username": username,
		"first_name": first_name,
		"last_name": last_name,
		"phone": phone,
		"email": email,
		"password": password.replace('\n', ''),
		"organization": organization
	}
	requests.post(requestURL, data=data)