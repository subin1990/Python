import math

print("Exercise 21 How manu cane required for paint the wall ")

def Cane_Qty(Height,Width):
    Sq_meter= Height*Width
    # 1 cane can use to pain 7.sq meter
    Qty=math.ceil(Sq_meter/7)
    print(f"{Qty} cane is required to paint the wall")

Height= int(input("Enter the Height in Meter"))
Width= int(input("Enter the Width in Meter"))
Cane_Qty(Height=Height, Width=Width)
