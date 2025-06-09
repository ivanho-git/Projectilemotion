from turtle import *
import math
import matplotlib.pyplot as plt


setworldcoordinates(0,0,800,600)
shape("circle")
color("red")
velocity=int(input("enter projection velocity  "))
angle=int(input("enter angle of projection "))
angr=math.radians(angle)

totalrange=((velocity**2)*math.sin(2*angr))/10


penup()
goto(0,0)
pendown()
speed(1000)
scale=200

for i in range(0,int(totalrange)+1):
    
    y=i*math.tan(angr)-(10*(i**2))/(2*(velocity*math.cos(angr))**2)
    goto(i,y)
    
done()

m=20
#for the graph
time1=[]
kineticenergy=[]
time=round(2*(velocity*math.sin(angr)/10))
print(time)
x=round(velocity*math.cos(angr))
y1=round(velocity*math.sin(angr))
for i in range(0,time+1):
    time1.append(i)
    if i>time/2:
        y=-(y1-(10*i))
        net=(x**2+y**2)**1/2
        ke=1/2*(m*(y**2))
        kineticenergy.append(ke)
        print(y)
    elif i<=time/2:
        y=y1-(10*i)
        net=(x**2+y**2)**1/2
        ke=1/2*(m*(y**2))
        print(y)
        kineticenergy.append(ke)
print(time1)
print(kineticenergy)
plt.grid()
plt.title("KINETIC ENERGY VS TIME")
plt.plot(time1,kineticenergy)
plt.xlabel("TIME")
plt.ylabel("KINETIC ENERGY")
plt.show()
