import plotext as plt
import numpy as np
import re

with open("output.txt") as file:
    lines = [line.rstrip() for line in file]

# remove header
lines = lines[10:]
print(lines[:5])
index=[]
time=[]
vout=[]
for line in lines:
    if line.strip():
        # two groups enclosed in separate ( and ) bracket
        result0 = re.search(r"\s(\d+)\t(\d\.\d+e[+\-]\d+)", line)
        result1 = re.search(r"\t(\d\.\d+e[+\-]\d+)", line)

        # Extract matching values of all groups
        try:
            #print("line = ", line)
            #print(result0.groups())
            #print("ind = ", result0.groups()[0], "time = ", float(result0.groups()[1]))
            index.append(result0.groups()[0])
            time.append(float(result0.groups()[1]))
        except:
            #print("line = ", line)
            #print(result1.groups())
            #print("vout = ", float(result1.groups()[0]))
            vout.append(float(result1.groups()[0]))


#y = plt.sin() # sinusoidal signal
plt.plot(time,vout)
plt.title("vout")
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.show()
