print("Arbitrary key word arguments")

def info_person(**persons_data):
    for key, value in persons_data.items():
        print(key,value)

info_person(name='subin', age='33', department='Commerce')
info_person(name='Rajappan',department='Commerce')
