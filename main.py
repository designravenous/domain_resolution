import sys
import app
import app_format
import datetime
from flask import Flask

def error_message():
    print("--- Script Error ---")
    print("* Script needs at least one file argument")
    print("* File should contain one domain at each line")
    exit()

try:
    input_One= sys.argv[1]
except:
    error_message()

#Creating list from the file Items
input_file = open(input_One,'r')
domains = input_file.readlines()

#Creating dateString
time_var = datetime.datetime.now()
date_string =str(time_var.year) + "-" + str(time_var.month) + "-" + str(time_var.day)

#Calling method in class to do requests of the listitems
p1 = app.domain_list_handling(domains, date_string)
result_http = p1.http_requests()


#To call for the https methods
#result_https = p1.https_requests()

#Writing To TXT file
file_action = app_format.format_class(result_http['Domains'], date_string)
file_action.write_to_txt()

#Writing to CSV file
file_action.write_to_csv()

#Writing TO JSON, will return a json string that we can use as API
json_action = app_format.format_class(result_http, date_string)
json_string = json_action.write_to_json()


#Setup flask - REST -JSONAPI
app = Flask(__name__)
@app.route('/')
def api_rest():
    return json_string

if __name__ == '__main__':
    app.run()
