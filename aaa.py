# import  matplotlib as plt
import matplotlib.pyplot as plt
import numpy as np
f = open("C:/Users/SHRISH/Downloads/Tensile Data 50 Deg C.txt", "r")


f.readline()
f.readline()

for i in range(60):
    f.readline()
l = []
for x in f:
    p = []
    s = ""
    for i in x:
        if i!=" " :
            s = s +i
        elif s!="" :
            s = s.rstrip("\n")
            p.append(float(s))
            s = ""
    if s!="":
        s = s.rstrip("\n")
        p.append(float(s))
        s =""

    l.append(p)

x = []
y = []
area = 28.27433388
length = 28
for i in l:
    x.append(i[1]/length)
    y.append((i[2]*1000)/area)

t = []
for i in x:
    t.append(583.692)
plt.plot(x,y, color = "black",linewidth = 1.5, label = 'At - 50 Degree Celcius')
# plt.plot(x,t)
plt.xlabel("strain(mm/mm)", size = 15)

plt.ylabel("stress(mega pascal)", size = 15)
plt.title("Engineering Stress-Strain Curve" , size  = 15)
temp = []

ymax = max(y)
xpos = y.index(ymax)
xmax = x[xpos]
# slope calculation using x1 = 0.011522, y1 = 252.244 , x2 = 0.01400 , y2 = 310.660

G = 26453.84988

for i in x:
    temp.append(G*(i-0.003))

plt.plot(x, temp, linestyle = "dashed" , color = "blue", label = "0.2% offset line"
         )

a = str(xmax)
b = str(ymax)
S = "UTS \n" + "x = " + a[:8] +"   \n" + "y = " + b[:8]
plt.annotate(S, xy=(xmax, ymax), xytext=(xmax, ymax-100),
            arrowprops=dict(facecolor='blue', shrink=0.05),
            )
S = "    Yield stress\n" + "    x = 0.0192" + "\n" + "    y = 448.05"
plt.annotate(S, xy=(0.019, 443.05), xytext=(0.0192, 443.05-100),
            arrowprops=dict(facecolor='blue', shrink=0.05),
            )
k  = str(max(x))
S = "  fracture  point\n" + "  x = " + k[:7]  + "\n" + "  y = 400.824"
plt.annotate(S, xy=(max(x), 400.824), xytext=(max(x), 400.824-100),
            arrowprops=dict(facecolor='blue', shrink=0.05),
            )
a = [733.1000, 733.1086]
b = [0,xmax]
plt.plot(b,a, color = "green" ,linestyle = "dashed", linewidth= 2 ,label = "uniform strain region" )

a = [0, max(x)]
b = [400.824,400.824]

plt.plot(a,b, color = "orange" ,linestyle = "dashed", linewidth= 2 ,label = "total strain region" )



plt.ylim(30,750)
plt.xlim(0.0018,max(x)+.02)
plt.legend()
plt.show()


# print(l)
###
