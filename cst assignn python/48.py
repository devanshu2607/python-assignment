##48.	Create a program that utilizes a hashtable to store and retrieve key-value pairs.
hashtable={}

def add_pair(key,value):
     hashtable[key] = value

     def get_value(key):
          return hashtable.get(key,"not not found")
     
add_pair("name","devanshu")
add_pair("age",19)
add_pair("city","indore")
add_pair("country:","india")

print("name:", get_value("name"))
print("age:", get_value("age"))
print("city:",get_value("city"))
print("country:",get_value("country"))