import matplotlib.pyplot as plt
x=[10,20,30,40]
y=[50,60,70,80]
plt.plot(x,y,'r--')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.savefig("sample.png")
plt.show()
