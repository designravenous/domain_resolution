import sys
import requests
import datetime

class domain_list_handling:
    
    def __init__(self, lista):
        self.lista = lista
      
   
    def http_requests(self):
        domain_info_item = {
            "name":"test",
            "http_response":0,
            "result_date":""
        }
        http_var = 'http://'
        results = []
        time_var = datetime.datetime.now()
        current_date =str(time_var.year) + "-" + str(time_var.month) + "-" + str(time_var.day)
        for item in self.lista:
            http_address = http_var + str(item.strip('\n'))
            try:
                response_http = requests.get(http_address)
                domain_info_item['name'] = str(item.strip('\n'))
                domain_info_item['http_response'] = response_http.status_code
                domain_info_item['result_date'] = current_date
                results.append(domain_info_item.copy())
        
            except:
                print("Failed Resolution: ", item)
                domain_info_item['name'] = str(item.strip('\n'))
                domain_info_item['http_response'] = None
                domain_info_item['result_date'] = current_date
                results.append(domain_info_item.copy())
                pass
        return results

    def https_requests(self):
        domain_info_item = {
            "name":"test",
            "https_response":0,
            "result_date":""
        }
        https_var = 'https://'
        results = []
        time_var = datetime.datetime.now()
        current_date =str(time_var.year) + "-" + str(time_var.month) + "-" + str(time_var.day)
        for item in self.lista:
            https_address = https_var + str(item.strip('\n'))
            try:
                response_https = requests.get(https_address)
                domain_info_item['name'] = str(item.strip('\n'))
                domain_info_item['https_response'] = response_https.status_code
                domain_info_item['result_date'] = current_date
                results.append(domain_info_item.copy())
        
            except:
                print("Failed Resolution: ", item)
                domain_info_item['name'] = str(item.strip('\n'))
                domain_info_item['https_response'] = None
                domain_info_item['result_date'] = current_date
                results.append(domain_info_item.copy())
                pass
        return results
