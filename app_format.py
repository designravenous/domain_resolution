import datetime
from flask import Flask, json
import csv

class format_class:
    def __init__(self,dictionary_list):
        self.dictionary_list = dictionary_list
    
    def write_to_txt(self): 
        time_var = datetime.datetime.now()
        current_date =str(time_var.year) + "_" + str(time_var.month) + "_" + str(time_var.day)
        file_type = ".txt"

        output_file = open("output" + "_" + current_date + file_type, 'w+')
        output_file.write("--- Output Of Response ---\n")
        for item in self.dictionary_list:
            try:
                output_file.write(str(item['name']) + "," + "http: " +str(item['http_response']) + "," + str(item['result_date'])+"\n")
            except:
                output_file.write(str(item['name']) + "," + "https: " + str(item['https_response']) + "," + str(item['result_date'])+"\n")
        output_file.close()

    def write_to_json(self):
        try:
            outcome_list = self.dictionary_list
            count_of_search = len(outcome_list)
            outcome_list.append({"count":int(count_of_search)})
            with open('domains.json', 'w') as f:
                json.dump(outcome_list, f, indent=2)
        except:
            print("Error occured to convert list to JSON (except in function)")

    def write_to_csv(self):
        time_var = datetime.datetime.now()
        current_date =str(time_var.year) + "_" + str(time_var.month) + "_" + str(time_var.day)
        file_type = ".csv" 
        count = len(self.dictionary_list)

        with open('output_'+ current_date + file_type, 'w', newline='') as f:
            csv_output = csv.writer(f)
            csv_output.writerow(['Domain','http_response','date' ])
            for item in self.dictionary_list:
                csv_output.writerow([str(item['name']), str(item['http_response']), str(item['result_date'])])
            csv_output.writerow(["Results: " + str(count) ])
