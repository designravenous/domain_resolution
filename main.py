import sys
import app
import app_format

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

#Calling method in class to do requests of the listitems
p1 = app.domain_list_handling(domains)
result_http = p1.http_requests()

#To call for the https methods
#result_https = p1.https_requests()

#Writing To TXT file
file_action = app_format.format_class(result_http)
file_action.write_to_txt()

#Writing to CSV file
file_action.write_to_csv()

#Writeing TO JSON
file_action.write_to_json()
