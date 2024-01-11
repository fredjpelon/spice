import plotext as plt
import numpy as np
import re

with open("npnout.txt") as file:
    lines = [line.rstrip() for line in file]

# remove header
lines = lines[11:]
print(lines[:5])
index=[]
time=[]
v1=[]
v2=[]
V1FLAG=1;
V2FLAG=0;
for line in lines:
    if line.strip():
        # two groups enclosed in separate ( and ) bracket
        result0 = re.search(r"\s(\d+)\t(\d\.\d+e[+\-]\d+)", line)
        result1 = re.search(r"\t(\d\.\d+e[+\-]\d+)", line)

        # Extract matching values of all groups
        try:
            index.append(result0.groups()[0])
            time.append(float(result0.groups()[1]))
        except:
            if V1FLAG == 1:
                v1.append(float(result1.groups()[0]))
                V1FLAG = 0
                V2FLAG = 1
            else:
                v2.append(float(result1.groups()[0]))
                V1FLAG = 1
                V2FLAG = 0


str = "v at BASE and v at COLLECTOR (mean removed), gain = -" + str(np.max(np.abs(v2))/np.max(np.abs(v1)))
plt.plot(time,v1-np.mean(v1))
plt.plot(time,v2-np.mean(v2))
plt.title(str)
plt.xlabel("Time (s)")
plt.ylabel("Voltage")
plt.show()
