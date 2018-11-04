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
#p1 = app.domain_list_handling(domains)
#result_https = p1.https_requests()

#Writing To TXT file
some_var = app_format.format_class(result_http)
some_var.write_to_txt()

#Writeing TO JSON
writer = app_format.format_class(result_http)
json_result = writer.write_to_json()
print(json_result)
