
import sys
import requests
import datetime

def error_message():
    print("--- Script Error ---")
    print("* Script needs at least one file argument")
    print("* File should contain one domain at each line")
    exit()

def write_to_file(filename,listOne, listTwo):
    filename.write("--- Found Domains ---\n")
    while listOne:
        filename.write(listOne[-1])
        listOne.pop()
    filename.write("\n--- Not Resolved Domains ---\n")
    while listTwo:
        filename.write(listTwo[-1])
        listTwo.pop()

#Checks if argument file is provided, if not 
try:
    input_One= sys.argv[1]
except:
    error_message()
x = datetime.datetime.now()

#creating output file, with todays date
output_file_name = "output_resolution" + "_" + str(x.year) + "_" + str(x.month) + "_" + str(x.day)+ ".txt"
resolution_file = open(output_file_name, "w+")
#Opening input file if argument is given
input_file = open(input_One, "r")
lister = input_file.readlines()
found = []
not_found = []
http_entry = "http://"
# Go through each domain (line) in argument file
for item in lister:
    domain_name = str(http_entry + item.strip('\n'))
    try:
        response = requests.get(domain_name)
        results = str(domain_name) + ", status_code: " + str(response.status_code) + '\n'
        found.append(results)
        
    except:
        results = str(domain_name) + " is NOT resolved" + '\n'
        not_found.append(results)

write_to_file(resolution_file,found,not_found)
#set parameter back to the beginning of the file
resolution_file.seek(0)
reader = resolution_file.read()
print(reader)
input_file.close()
resolution_file.close()
        
