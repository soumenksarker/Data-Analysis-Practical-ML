import matplotlib.pyplot as plt
x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,12]
plt.plot(x,y,label ='First Line')
plt.plot(x2,y2, label='Second line')
plt.xlabel('Plot number')
plt.ylabel('Important variable')
plt.title('Interesting Graph\n Check it out')
plt.legend()
plt.show()
