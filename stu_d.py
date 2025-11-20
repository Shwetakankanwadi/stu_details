import sys
if len(sys.argv)==3:
  script_name = sys.argv[0]
  name = sys.argv[1]
  rollno = sys.argv[2]
  print("user provided input values:")
else:
  script_name = sys.argv[0]
  name = "ritika"
  rollno = "156"
  print("no input given --using default values:")

print("scrip name:",script_name)
print("Student name:",name)
print("Roll number:",rollno)
