'''Assignment 3: Corporate Directory Search & Scraper
Scenario
You are writing a parser to extract formatted employee phone records from unstructured text files. Employee phone numbers are formatted in multiple ways across the directory.

Problem Description
Write a function scrape_directory_phones(directory_text) that extracts phone records from text and returns a structured list of dictionaries.

The function must detect phone numbers matching any of the following three formats:
AAA-PPP-LLLL (e.g., 123-456-7890)
(AAA) PPP-LLLL (e.g., (123) 456-7890)
AAAPPPLLLL (10 consecutive digits, e.g., 1234567890) where AAA represents the area code (3 digits), PPP represents the prefix (3 digits), and LLLL represents the line number (4 digits).
Design a single compiled RegEx pattern to parse all three formats using capture groups.
For each match found in directory_text, build a dictionary with the following keys:
"area_code": String containing the extracted 3 area code digits.
"prefix": String containing the extracted 3 prefix digits.
"line_number": String containing the extracted 4 line number digits.
"formatted": A normalized phone string in the format "(AAA) PPP-LLLL".
Return a list of these dictionaries. If no phone numbers are found, return an empty list.'''

import re
def scrape_directory_phones(directory_text):

    list=[]
    dict1={"area_code":0, "prefix":0, "line_number":0, "formatted":0}
    dict2={"area_code":0, "prefix":0, "line_number":0, "formatted":0}
    dict3={"area_code":0, "prefix":0, "line_number":0, "formatted":0}
    pattern=re.search(r"(\d{3})-(\d{3})-(\d{4})",directory_text)
    if pattern:
        dict1["area_code"]=pattern.group(1)
        dict1["prefix"]=pattern.group(2)
        dict1["line_number"]=pattern.group(3)
        dict1["formatted"]=f"({dict1['area_code']}) {dict1['prefix']}-{dict1['line_number']}"
        list.append(dict1)   
    pattern1 = re.search(r"(\(\d{3}\))\s*(\d{3})-(\d{4})", directory_text)
    if pattern1:
        dict2["area_code"]=pattern1.group(1)
        dict2["prefix"]=pattern1.group(2)
        dict2["line_number"]=pattern1.group(3)
        dict2["formatted"]=f"({dict2['area_code']}) {dict2['prefix']}-{dict2['line_number']}"
        list.append(dict2)
    pattern2=re.search(r"(\d{3})(\d{3})(\d{4})",directory_text)
    if pattern2:
        dict3["area_code"]=pattern2.group(1)
        dict3["prefix"]=pattern2.group(2)
        dict3["line_number"]=pattern2.group(3)
        dict3["formatted"]=f"({dict3['area_code']}) {dict3['prefix']}-{dict3['line_number']}"
        list.append(dict3)
    print(list)
    
def main():
    directory = "Contact HR at 123-456-7890 or the helpdesk at (987) 654-3210. Direct line is 5558881234."
    scrape_directory_phones(directory)
main()