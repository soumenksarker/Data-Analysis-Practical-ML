## 7. Practice - Splitting Elements in a List ##

g = open("crime_rates.csv",  "r")
f = g.read()
list = f.split("\n")
final_data = []
for i in list:
    t = i.split(',')
    final_data.append(t)
print(final_data[0:5])
    
