print("Dictionaries in python")

phone_number= {
   'Subin' : 9910247855,
    'Rajamma': 8368315928,
    'Kannan': 9633468540,
    'Subin': 9744268824
}

phone_numbers= dict({'Subin' : 9910247855,
    'Rajamma': 8368315928,
    'Kannan': 9633468540
})
# priting dictionery keys
print("Dictionery key",phone_numbers.keys())

# printing dictionery values

print("Dictionery values",phone_numbers.values())

#printing dictioney

print("Dictionery items",phone_numbers.items())

print(phone_numbers)
print(phone_numbers['Subin'])

# Values are mutable
phone_numbers['Subin']= 9768468458
print(phone_numbers)
# can add any type of data as values

phone_numbers['Subin']={1234567890, 395547885} # list

print(phone_numbers)

phone_numbers['Subin']={'Subin_Home': 5655874 , 'Subin_Office': 89547855} # dictionary
print(phone_numbers)

print(phone_numbers['Subin']['Subin_Home']) # Accessing Dictionery in dictionery

# using Get method
print(phone_numbers.get('Subin'))
# deleting a Key
#del phone_numbers['Subin']
#print(phone_numbers)
phone_numbers.pop('Rajamma')
print(phone_numbers)
print(phone_numbers.popitem())
# clearing the entire dictionery
phone_numbers.clear()
print(phone_numbers)