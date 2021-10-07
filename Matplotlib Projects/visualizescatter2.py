import matplotlib.pyplot as plt
x = [1,3,5,5,6,7,8]
y = [2,4,6,3,4,2,3]

#population_age = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,112,115,112,80,75,65,54,44,43,42,48]
#ids = [x for x in range(len(population_age))]
#bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.scatter(x,y, label="Fuck", color='r', marker = '*',s=100)
#plt.bar(ids, population_age)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph')
plt.legend()
plt.show()
