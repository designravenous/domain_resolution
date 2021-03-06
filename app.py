import sys
import requests

class domain_list_handling:
    
    def __init__(self, lista, tid):
        self.lista = lista
        self.tid = tid
      
   
    def http_requests(self):
        domain_info_item = {
            "name":"test",
            "http_response":0,
            "resolution_url":"",
            "result_date":""
        }
        http_var = 'http://'
        results = {
            'Domains':[],
            'Searches':0,
            'Response':True
        }
        for item in self.lista:
            http_address = http_var + str(item.strip('\n'))
            try:
                response_http = requests.get(http_address)
                domain_info_item['name'] = str(item.strip('\n'))
                domain_info_item['http_response'] = response_http.status_code
                domain_info_item['result_date'] = self.tid
                domain_info_item['resolution_url'] = str(response_http.url)
                results['Domains'].append(domain_info_item.copy())
        
            except:
                print("Failed Resolution: ", item)
                domain_info_item['name'] = str(item.strip('\n'))
                domain_info_item['http_response'] = None
                domain_info_item['result_date'] = self.tid
                domain_info_item['resolution_url'] = "N/A"
                results['Domains'].append(domain_info_item.copy())
                pass
        count = int(len(self.lista))
        results['Searches'] = count
        if count >= 0:
            results['Response'] = True
        else:
            results['Response'] = False
        return results
