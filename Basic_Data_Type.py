#Basic Data Type
'''
Các kiểu dữ liệu co bản trong Python: bool, None, int, float, str
'''

'''
topic #0: bool & None
'''
# [] bool: True & False
var_bool = True

# [] type(): Dynamic typed
# print(type(var_bool))

# Numerically, they're evaluated as integers with value 1(true) 0(false)
a=1+True
# print(a)

b=False
# if b==0:
#     print("B is zoro")

# [] None: phần tử không

# email_address = None
email_address = "hieu123@gmail.com"
# if email_address:
#     print(f"Email deress is {email_address}")
# else:
#     print(f"Email address is empty or {email_address}")

'''
Topic #1: Number (int & float)
'''
# print(type(1)) #int
# print(type(0))
# print(type(-10))

# print(type(0.0)) #float
# print(type(2.3)) 
# print(type(4E2)) #4*10(^2)

# [] Arithmetic: Cac phep toan: + - * /     **  / // %
# print(10+3) #13
# print(10-3) #7
# print(10*3) #30 
# print(10**3) #10^3 =10*10*10 =1000 
# print(10/3) #3.33333333333333335
# print(10//3) #3
# print(10%3) #du 1

# [] Basic Funtion (ham co ban) 
# print(pow(10,3)) #10^3
# print(abs(-6.9)) #6.9
# print(round(6.69)) #7
# print(round(5.468,2)) #5.47 -> round to nth digit
# print(bin(512)) #0b1010101010101010101010
# print(hex(512)) #0xc0ffee