import json
import mysql.connector
from datetime import datetime

cnx = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="root",
        password="root",
        database="test_selenium"
    )
cursor = cnx.cursor(dictionary=True)

f = open('test.json')

data = json.load(f)

created_at = data['report']['created_at']
passed = data['report']['summary']['passed'] if 'passed' in data['report']['summary'] else 0
failed = data['report']['summary']['failed'] if 'failed' in data['report']['summary'] else 0
error = data['report']['summary']['error'] if 'error' in data['report']['summary'] else 0
skipped = data['report']['summary']['skipped'] if 'skipped' in data['report']['summary'] else 0
xfailed = data['report']['summary']['xfailed'] if 'xfailed' in data['report']['summary'] else 0
xpassed = data['report']['summary']['xpassed'] if 'xpassed' in data['report']['summary'] else 0
num_tests = data['report']['summary']['num_tests']
duration = data['report']['summary']['duration']

tests = data['report']['tests']
nameSenario = '-'
if len(tests) > 0:
    test = data['report']['tests'][0]
    nameParts = test['name'].split("::")
    nameSenario = nameParts[0]
created_at_datetime = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f').strftime('%Y-%m-%d %H:%M:%S')
sql = "SELECT * FROM senario WHERE name = '" + nameSenario + "' AND created_at = '" + created_at_datetime + "'"
cursor.execute(sql)
existingSenario = cursor.fetchone()

if existingSenario == None:
    # insert senario

    sql = "INSERT INTO senario (name, passed, failed, error, skipped, xfailed, xpassed, num_tests, duration, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nameSenario, passed, failed, error, skipped, xfailed, xpassed, num_tests, duration, created_at)
    cursor.execute(sql, val)

    senario_id = cursor.lastrowid

    for test in tests:
        nameParts = test['name'].split("::")
        name = nameParts[2]
        duration = test['duration']
        outcome = test['outcome']
        sql = "INSERT INTO test (name, outcome, duration, senario_id) VALUES (%s, %s, %s, %s)"
        val = (name, outcome, duration, senario_id)
        cursor.execute(sql, val)

    cnx.commit()

cnx.close()
f.close()
