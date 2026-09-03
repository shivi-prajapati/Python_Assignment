'''Assignment 6: Server Log Analyzer & Traffic Classifier (Advanced RegEx)
Scenario
An automated server monitor analyzes web traffic logs to detect security issues. 
The monitor extracts HTTP details from log strings and filters out requests originating 
from local network IP addresses.'''

import re 
def analyze_server_logs(logs_text): 
    pattern = re.compile( 
        r'(?P<ip>\S+) - - ' 
        r'\[(?P<time>[^\]]+)\] ' 
        r'"(?P<method>GET|POST|PUT|DELETE) ' 
        r'(?P<resource>\S+) HTTP/\d\.\d" ' 
        r'(?P<status>\d+) ' 
        r'(?P<bytes>\d+)' ) 
    result = [] 
    for line in logs_text.split("\n"): 
        match = pattern.search(line) 
        if match is None: 
            print(f"Warning: Could not parse line: '{line}'. Skipping.") 
            continue 
        ip = match.group("ip") 
        time = match.group("time") 
        method = match.group("method") 
        resource = match.group("resource") 
        status = int(match.group("status")) 
        bytes_sent = int(match.group("bytes")) 
         
        if ip.startswith("192.168.") or ip.startswith("10."):
            continue 

        log = { 
            "ip": ip, 
            "time": time, 
            "method": method, 
            "resource": resource, 
            "status": status, 
            "bytes": bytes_sent 
            } 
        result.append(log) 
    return result
def main():
    log_data = """192.168.1.5 - - [28/Aug/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1024
    8.8.8.8 - - [28/Aug/2026:10:10:00] "GET /api/v1/users HTTP/1.1" 200 4096
Corrupted log entry here
10.0.0.12 - - [28/Aug/2026:10:15:00] "POST /submit_data HTTP/1.1" 403 512
172.16.0.4 - - [28/Aug/2026:10:20:00] "POST /login HTTP/1.1" 401 256"""
    print(analyze_server_logs(log_data))
main()