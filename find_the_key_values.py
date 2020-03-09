def find_the_key_values(dict1 = None, Keyname1 = None):
    ''' to list the values of given key 
    in a nested dictionory or list containig dictionory'''

    values = []

    if Keyname1 == None:
        return None

    if isinstance(dict1,(list,tuple)):
        for index in range(len(dict1)):
            if isinstance(dict1[index] , (list,dict,tuple)):
                values += find_the_key_values(dict1[index] , Keyname1)
    elif isinstance(dict1,dict):
        for key in dict1:
            if isinstance(dict1[key],(list,dict,tuple)):
                values += find_the_key_values(dict1[key],Keyname1)
            elif key == Keyname1:
                values.append(dict1[Keyname1])
    return values


dt1 = {1:[{1:'1'}] , 2:[{},{1:'2'}] , 3:{1:'abc'} , 4:({1:'xyz'},2)}
dt3 = [{1:'abc' , 2:'3'} , [{2:'gh'}]]
dic2 = {1:'abc'}

print(find_the_key_values(dt3,2))


