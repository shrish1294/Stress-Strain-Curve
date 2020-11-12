import matplotlib.pyplot as plt
import numpy as np

f = open("C:/Users/SHRISH/Downloads/Tensile Data 196 Deg C.txt", "r")
f.readline()
f.readline()
x = []
y = []
f.readline()
s = ""
for i in f:
    if "E" in i:
      continue
    else:
        p = []
        for j in i:
            if j!=" " and j!="\t" and j!="\n":
                s = s+j
            elif s!="":
                s = s.rstrip("\n")
                s = s.rstrip("\t")
                p.append(float(s))
                s = ""
        if s != "":
            s = s.rstrip("\n")
            s = s.rstrip("\t")
            p.append(float(s))
            s = ""
        x.append(p[1])
        y.append(p[2])
print(len(x),"  ")
print(len(y))

area = 28.27433388
length = 28
X = []
Y = []
for i in x:
    X.append(i/length)
for i in y:
    Y.append((i*1000)/area)

# print(max(Y))
# print(max(X))
plt.plot(X,Y, label = "At - 196 degree celcius", color = "black")
# print(len(X),"   ")
# print(len(Y))
plt.xlabel("Strain(mm/mm)", size="15")
plt.ylabel("Stress (mega pascal)", size = "15")
plt.title("Engineering Stress Strain Curve", size = "16")
# plt.legend()
ymax = max(Y)
xpos = Y.index(ymax)
xmax = X[xpos]
A = [ymax, ymax]
B = [0,xmax]
# print(A)
plt.plot(B, A, label = "uniform strain region", linestyle = "dashed", color = "green")
#value substr
a = str(xmax)
b = str(ymax)
S = "UTS \n" + "x = " + a[:8] +"   \n" + "y = " + b[:8]
plt.annotate(S, xy=(xmax, ymax), xytext=(xmax, ymax-150),
            arrowprops=dict(facecolor='blue', shrink=0.05),
            )
temp = []
G = 12776.8213
for i in X:
    temp.append(G*(i-0.002))
plt.plot(X, temp, linestyle = "dashed", color = "blue" , label = "0.2 % offset line")
plt.xlim(0,max(X)+0.03)
plt.ylim(0, max(Y)+100)
A = [0 , max(X)]
k = X.index(max(X))
B = [Y[k-1], Y[k-1]]
# print(B)
plt.plot(A, B, label = "total strain region", linestyle = "dashed",  color = "orange")
m = str(X[k])
n = str(Y[k-1])
S = "  fracture point \n" +" x = " + m[:7] + " \n" + " y = " + n[:7]
plt.annotate(S, xy = (X[k], Y[k-1]) , xytext = (X[k], Y[k-1]-100) , arrowprops = dict(facecolor = "blue" , shrink = 0.05))
S = "    Yield stress\n" + "    x = 0.0859" + "\n" + "    y = 1073.34"
plt.annotate(S, xy=( 0.0859, 1073.34), xytext=( 0.0859, 1073.34-100),
            arrowprops=dict(facecolor='blue', shrink=0.05),
            )
plt.legend()
plt.show()