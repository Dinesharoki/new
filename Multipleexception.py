

#First code with string data:
d1={"CH1":"AMUL","CH2":"DAIRYMILK","CH3":"FIVESTAR","CH3":"KITKAT","CH4":"MENTHOS"}
try:
  value=d1["CH1"]
  print(d1["CH1"])
except KeyError:
  print("Key not found in the dictionary")
try:
   value=d1["CH2"]
except NameError:
  print("NAME ERROR")
try:
  z=d1["CH1"]/d1["CH2"]
except TypeError:
  print("This is a type error")
else:
  print("Nil error")
finally:
  print("Multiple Exception handling Exercise done")

#Second code with numeric data:
d1={"CH1":5,"CH2":6,"CH3":7,"CH3":1,"CH4":8}
try:
  value=d1["CH1"]
  print(d1["CH1"])
except KeyError:
  print("Key not found in the dictionary")
try:
   value=d1["CH2"]
except NameError:
  print("NAME ERROR")
try:
  z=d1["CH1"]/d1["CH2"]
except TypeError:
  print("This is a type error")
else:
  print("Nil error")
finally:
  print("Multiple Exception handling Exercise done")





   
   
  
