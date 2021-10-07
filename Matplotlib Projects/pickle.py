import pickle
#the name of the file where we will store the object
shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot','latest','u have to be punished for mistakes' ]
#write to the file
f = open(shoplistfile, 'wb')
#Dump the object in a file
pickle.dump(shoplist, f)
f.close
#destroy the shoplist variable
del shoplist
#Read back from the storage
f = open(shoplistfile, 'rb')
#Load the object from the file
storedlist = pickle.load(f)
print(storedlist)
