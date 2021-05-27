from barnum import gen_data
import csv
import os
import requests
import random
baseURL = open(os.getcwd() + '/../config/' + 'config').readlines()[0].replace('\n', '')
requestURL = 'http://' + baseURL + '/'
employmentTypes = ['Part-Time','Full-Time', 'Temporary']
experienceLevels = ['3+ Years', '2+ Years', '1 Year', '5+ Years', '10+ Years']
workTypes = ['Remote', 'Onsite']
employerDict = {}
with open (os.getcwd() + '/../data/' + 'employers.csv') as employerCSV:
    employers = csv.reader(employerCSV, delimiter=',')
    for row in employers:
      if (row[0] != 'id'):
        employerDict[int(row[0])] = {
          'username': row[1],
          'password': row[7]
        }
for i in range (0, 3500):
  randomizedData = {
  'title' : gen_data.create_job_title(),
  'description' : gen_data.create_paragraphs(),
  'employment_type' : random.choice(employmentTypes),
  'experience_level' : random.choice(experienceLevels),
  'salary' : random.randint(10000,1000000),
  'type_work' : random.choice(workTypes),
  'location' : gen_data.create_city_state_zip()[0]
  }
  employer_id = random.randint(1001, 2000)
  authReq = requests.post(requestURL + 'login', data = employerDict[employer_id])
  authCookie = { 'jobsite': authReq.headers['Set-Cookie'].split(';')[0].split('jobsite=', 1)[1]}
  requests.post(requestURL + 'jobs/create', data = randomizedData, cookies = authCookie)
  requests.get(requestURL + 'logout', cookies = authCookie)