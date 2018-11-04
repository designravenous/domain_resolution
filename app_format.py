import datetime
from flask import Flask, json

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
            jsonStr = json.dumps(outcome_list, indent=2)
            with open('domains.json', 'w+') as json_file:
                json.dump(jsonStr, json_file)
        
        except:
            print("Error occured to convert list to JSON (except in function)")
        
        return jsonStr




        
