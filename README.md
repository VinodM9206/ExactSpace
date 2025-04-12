This Python script reads the HAR file **(exactspace.har)** that was manually downloaded from the browser while visiting https://exactspace.co. 
It analyzes the HTTP responses and counts how many requests fall under each status code category (1XX, 2XX, etc.).
It then calculates the percentage of each category and saves the result in a file named network_summary.json.

**📁 Files included:**
har_parser.py – Python code to parse the HAR file

exactspace.har – HAR file exported from browser

network_summary.json – Final output in JSON format

Vinod_M_Resume.pdf – My resume

README.txt

**▶️ How to run it:**
Make sure exactspace.har is in the same folder as har_parser.py

Open terminal in VS code

Run the script using:

python har_parser.py
After running, it will generate network_summary.json.



