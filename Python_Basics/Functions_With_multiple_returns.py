import statistics
print("Functions with multiples returs")

def mean_median_mode(list1):

    #return statistics.mean(list1), statistics.median(list1),statistics.mode(list1) # return in the form of tuples
    return [statistics.mean(list1), statistics.median(list1), statistics.mode(list1)] # return in the form of list




print(mean_median_mode([18, 16, 19, 48, 65, 83, 96]))
resulst = [mean_median_mode([18,16, 19, 48,65, 83, 96])]
print(resulst)
a, b,c =mean_median_mode([18,16,19,48,65,83,96])
print(f"Mean {a} medaian {b} and mode {c}")
def fullname(Fname, Lname):
    if Fname=='' and Lname== '':
        return "You have entered nothing"
    else:
        Fullname= Fname.title()+ " "+ Lname.title()
        return Fullname

first_name =str(input("Enter the first name: "))
Last_name= str(input("Enter the second name: "))
fullName= fullname(first_name,Last_name)
print(fullName)