print(" Calculating average height in list")
height = input()

h = height.split()

count = 0
for number in h:
    count= count+1

#print(count)

for t in range(0,count):
    h[t]= int (h[t])


total = sum(h)
average = round (total/count)
print("Average Height is ",average)
# my method print(" Calculating average height in list")
# height = input()
#
# h = height.split()
# hight_list = list(h)
#
# print(hight_list)
#
# i = 0
# count = 0
# total = 0
# for i in hight_list:
#     total= total+int(i)
#     count=count+1
#
# #print(total)
# #print(count)
# average = round(total/count)
# print(average)