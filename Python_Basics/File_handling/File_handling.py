#file1= open('textfile.txt','x') # 'x' for creating a file
# file1= open('textfile.txt','r') # r for read mode if r not mentioned by default it open in read mode
# data= file1.read()
# print(data)
# file1= open("textfile.txt","w") # open in over writing the file, if file does not existing it will create a new file
# file1.write("Karakootil dasan")
# file in r+ mode
#
# file1= open("textfile.txt","r+") # read and write mode if file does not exist it will give error. file handler will be in begenning of the file
# print(file1.tell())
# print(file1.read())
# print(file1.tell())
# file1.write(" yes iam-Karakootil dasan")
# print(file1.tell())
# file1.close()

# file in w+ mode
# file2= open("textfile.txt","w+")
# print(file2.tell())
# file2.write('Devarsh S Pillai')
# print(file2.tell())
# file2.write(' Rajappan Thengumude')
# print(file2.tell())
# file2.seek(0)
# data = file2.read()
# print(data)
# file2.close()

# File in a mode (append Mode)
# file3= open('textfile4.txt','a')
# file3.write(' I am the alfa and Omega')

# file in a+ mode
# file4= open ('textfile5.txt','a+')
# print(file4.tell())
# file4.seek(0)
# print(file4.read())
# file4.write(' Hellooooo')

# Reading binary files

f1= open('img1.jpg','rb')
print(f1.read())
# f2= open('img2.jpg','wb')
# for i in f1:
#     f2.write(i)

