class people:
   '''Represents a people with  details'''
   def __init__(self, name, age, contact,district, relation):
         self.name = name
         self.age = age
         self.contact = contact
         self.district = district
         self.relation = relation
         print ('(Initialized the people : {} )'. format(self.name))

   def tell(self):
        '''Tell my details'''
        print('Name : "{}"  Age : "{}" Contact : "{:d}" district : "{}" Relation : "{}"'.format(self.name, self.age, self.contact, self.district, self.relation))

class friend(people):
    '''Represent  a friend with details'''
    def __init__(self, name, age, contact, district, relation, charecter):
         self.name = name
         self.age =  age
         self.contact = contact
         self.district = district  
         self.relation = relation
         self.charecter = charecter
         print ('(Initialized the friend :{})'.format(self.name))

    def tell(self):
         people.tell(self)
         print('Charecter : "{}"'.format(self.charecter))
class relative(people):
    '''Represents a relative with details'''
    def __init__(self, name, age, contact, district, relation, mail_address):
         self.name = name
         self.age =  age
         self.contact = contact
         self.district = district  
         self.relation = relation
         self.mail_address = mail_address
         print('(Initialized the relative : {})'.format(self.name))
    def tell(self):
         people.tell(self)
         print('mail_address : "{}"'.format(self.mail_address))
class Spam(people):
    '''Represents a bad guy with details'''
    def __init__(self,name,age,contact, district,relation,danger_level):
         self.name = name
         self.age = age
         self.contact = contact
         self.district = district
         self.relation = relation
         self.danger_level = danger_level
         print ('(Initialized the Bad guy : {})'.format(self.name))
    def tell(self):
        people.tell(self)
        print ('Danger_Level : "{}"'.format(self.danger_level))

e = friend('masud', 21, 1795776460, 'khulna', 'good', 'simply a good guy & friendly')
f = friend('toriqul', 20, 1792956569, 'Bogra', 'good', 'very fast')
r = relative('taposhi di', 30, 17822, 'bogra', 'better', 'i dont know may be she has not')
s = Spam('Rabbi', 21, 17988, 'kushtia', 'bad', 'have some but i dont care')
print()
     #print A blank line
members = [e, f, r, s]
for member in members:
     member.tell() 
