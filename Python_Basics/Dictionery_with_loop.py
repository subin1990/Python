phonumbers = {'Subin': 9910247855, 'Achu': 8368315928, 'Kannan': 9633468540}
for i in phonumbers:

    print(i)
    print(phonumbers[i])
for i in phonumbers.items():
    print(i)

print("Copy to another dictionery")

phonumbers2 =phonumbers.copy()
print(phonumbers2)