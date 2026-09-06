'''Assignment 4: Hospital Patient Register'''

import re
class Patient :
  _patient_counter=0
  
  @staticmethod
  def validate_dob_format(dob_str):
    pattern=re.match(r"\d{4}-\d{2}-\d{2}",dob_str)
    if pattern:
      return True
    return False

  def __init__(self,name,dob):   
    global _patient_counter
    self.dob=dob
    self.name=name
    x=Patient.validate_dob_format(self.dob)
    if x==False:
      raise ValueError(f"Invalid date of birth format: '{self.dob}'. Expected YYYY-MM-DD.")
    else:
      Patient._patient_counter+=1
    y=1000+Patient._patient_counter
    self.patient_id="Pat-"+str(y)
  
  @classmethod
  def get_total_patients(cls):    
    return cls._patient_counter

def main():
  p1 = Patient("Arham Khan", "1999-05-15")
  print(p1.patient_id) # Output: PAT-1001
  try:
    p2 = Patient("Lisa", "12/08/1998")
  except ValueError as e:
    print(e)  # Output: Invalid date of birth format: '12/08/1998'. Expected YYYY-MM-DD.

  print(Patient.get_total_patients())  # Output: 1
  
main()