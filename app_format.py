from flask import Flask, json
import csv

class format_class:
    def __init__(self,dictionary_list, tid):
        self.dictionary_list = dictionary_list
        self.tid = tid
    
    def write_to_txt(self): 
        file_type = ".txt"
        output_file = open("output" + "_" + self.tid + file_type, 'w+')
        output_file.write("--- Output Of Response ---\n")
        for item in self.dictionary_list:
            try:
                output_file.write(str(item['name']) + "," + "http: " +str(item['http_response']) + "," + str(item['result_date'])+ "," + str(item['resolution_url']) + "\n")
            except:
                output_file.write(str(item['name']) + "," + "https: " + str(item['https_response']) + "," + str(item['result_date'])+ "," + str(item['resolution_url']) +"\n")
        output_file.close()

    def write_to_json(self):
        try:
            outcome_list = self.dictionary_list
            with open('domains.json', 'w') as f:
                json.dump(outcome_list, f, indent=2)
        except:
            print("Error occured to convert list to JSON (except in function)")
        json_string = json.dumps(outcome_list, indent=2)
        return json_string

    def write_to_csv(self):
        file_type = ".csv" 
        count = len(self.dictionary_list)

        with open('output_'+ self.tid + file_type, 'w', newline='') as f:
            csv_output = csv.writer(f)
            csv_output.writerow(['Domain','http_response','Date', 'Resolution URL' ])
            for item in self.dictionary_list:
                csv_output.writerow([str(item['name']), str(item['http_response']), str(item['result_date']), str(item['resolution_url'])])
            csv_output.writerow(["Results: " + str(count) ])
