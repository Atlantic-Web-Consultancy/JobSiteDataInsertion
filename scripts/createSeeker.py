import requests
import os
import time
import datetime
baseURL = open(os.getcwd() + '/../config/' + 'config').readlines()[0].replace('\n', '')
requestURL = 'http://' + baseURL + '/createSeeker'
f = open(os.getcwd() + '/../data/' + 'applicants.csv')
csvLines = f.readlines()
csvLines.pop(0)
for line in csvLines:
	id, username, first_name, last_name , address1, address2, city, state, country, zip, phone, email, dob, gender, password = line.split(',')
	data = {
		"username": username,
		"first_name": first_name,
		"last_name": last_name,
		"address1": address1,
		"address2": address2,
		"city": city,
		"state": state,
		"country": country,
		"zip": zip,
		"phone": phone,
		"email": email,
		"dob": int(time.mktime(datetime.datetime.strptime(dob, "%m/%d/%Y").timetuple())),
		"gender": gender,
		"password": password.replace('\n', '')
	}
	requests.post(requestURL, data=data)