# domain_resolution
Python Script to get resolution inforamtion from domains http-response code, resolution url, name and date of search.

This Script can export the results in txt, csv and JSON. main script also include Flask webserver, to host REST-API.

Steps:
- Make sure that all modules needed are installed
- Include a .txt file with domains in seperate rows

  example:
  python main.py text_file.txt

- after the script have gone through requests for each items of the text file a Flask app will be running.
- Verify this on 'http://localhost:5000/'
- on a seperate bash tab, run the 






