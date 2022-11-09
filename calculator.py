import os
import math
while 1:
  os.system("cls")
  mode=input("to scientific mode press 1 \n to programmer mode press 0 :")
  if mode.isdigit():
    if int(mode):
      terminate_flag=1
      while terminate_flag: 
        os.system("cls")
        operator=input("the following is the type of operations\n\
        \nsummation\
        \nsubtraction\
        \nremender\
        \nmultiplication\
        \ndivision\
        \npower\
        \nroot\
        \nsin\
        \ncos\
        \ntan\
        \nsin_inv\
        \ncos_inv\
        \ntan_inv\
        \nlog\
        \nexit\
        \n\nEnter one the operation : ")
  
        if operator=="summation" or operator=="subtraction"or operator=="remender" or operator=="multiplication"or operator=="division"or operator=="power" or operator=="root" :
          x=input("Enter Two Values separated by one space or one value :").split(' ')
          x[0] =int(x[0])
          x[1] =int(x[1])
          if operator=="summation":
            print(x[0]+x[1])
          elif  operator=="subtraction":
            print(x[0]-x[1])
          elif  operator=="remender":
            print(x[0]%x[1])
          elif  operator=="multiplication":
            print(x[0]*x[1])
          elif  operator=="division":
            print(x[0]/x[1])
          elif  operator=="power" :
            print(x[0]**x[1])
          elif  operator=="root":
            print(x[0]**(1/x[1]))
        
        elif  operator=="sin" or operator=="cos" or operator=="tan" or operator=="sin_inv" or operator=="cos_inv" or operator=="tan_inv" or operator=="log" :
          x=int(input("Enter one Value : ")) 
          if operator=="sin":
            print(math.sin(x))
          elif  operator=="cos":
            print(math.cos(x))
          elif  operator=="tan":
            print(math.tan(x))
          elif  operator=="sin_inv":
            print(math.asin(x))
          elif  operator=="cos_inv":
            print(math.acos(x))
          elif  operator=="tan_inv" :
            print(math.atan(x))
          elif  operator=="log":
            print(math.log(x))
        elif "exit":
          terminate_flag=0
        else:
            print("undefined operation")
        input()
    else:
      terminate_flag=1
      while terminate_flag:
        operator=input("the following is the type of operations\n\
        \nlogical_and\
        \nlogical_or\
        \nbitwise_and\
        \nbitwise_or\
        \nbitwise_xor\
        \nlogical_not\
        \nbitwise_not\
        \nhexadecimal_to_binary\
        \nhexadecimal_to_decimal\
        \nhexadecimal_to_octal\
        \nhexadecimal_to_all_systems\
        \ndecimal_to_binary\
        \ndecimal_to_hexadecimal\
        \ndecimal_to_octal\
        \ndecimal_to_all_systems\
        \noctal_to_binary\
        \noctal_to_hexadecimal\
        \noctal_to_decimal\
        \noctal_to_all_systems\
        \nbinary_to_hexadecimal\
        \nbinary_to_decimal\
        \nbinary_to_octal\
        \nbinary_to_all_systems\
        \nexit\
        \n\nEnter one the operation : ")
    
        if operator=="logical_and" or operator=="logical_or"or operator=="bitwise_and" or operator=="bitwise_or"or operator=="bitwise_xor" :
            x=input("Enter Two Values separated by one space or one value :").split(' ')
            x[0] =int(x[0])
            x[1] =int(x[1])
            if operator=="logical_and":
              print(bool(x[0] and x[1]))
            elif  operator=="logical_or":
              print(bool(x[0] or x[1]))
            elif  operator=="bitwise_and":
              print(x[0]&x[1])
            elif  operator=="bitwise_or":
              print(x[0]|x[1])
            elif  operator=="bitwise_xor":
              print(x[0]^x[1])
            else:
              print("undefined operation")
        elif  operator=="logical_not" or operator=="bitwise_not" or       operator=="hexadecimal_to_binary" or operator=="hexadecimal_to_decimal"       or operator=="hexadecimal_to_octal" or operator=="hexadecimal_to_all_systems"       or operator=="decimal_to_binary"or operator=="decimal_to_hexadecimal" or        operator=="decimal_to_octal" or operator=="decimal_to_all_systems" or        operator=="octal_to_binary"or operator=="octal_to_hexadecimal" or        operator=="octal_to_decimal" or operator=="octal_to_all_systems" or         operator=="binary_to_hexadecimal"or operator=="binary_to_decimal"or          operator=="binary_to_octal"or operator=="binary_to_all_systems":
            x=input("Enter one Value : ") 
            if operator=="logical_not":
              print(bool(not int(x)))
            elif  operator=="bitwise_not":
              print(~int(x))
            elif  operator=="hexadecimal_to_binary":
              print(bin(int(x),16))
            elif  operator=="hexadecimal_to_decimal":
              print(int(int(x,16)))
            elif  operator=="hexadecimal_to_octal":
              print(oct(int(x,16)))
            elif  operator=="hexadecimal_to_all_systems" :
              print("binary :",bin(int(x,16)))
              print("decimal :",int(x,16))
              print("binary :",oct(int(x,16)))

            elif  operator=="decimal_to_binary":
              print(bin(int(x)))
            elif  operator=="decimal_to_hexadecimal":
              print(hex(int(x)))
            elif  operator=="decimal_to_octal":
              print(oct(int(x)))
            elif  operator=="decimal_to_all_systems":
              print("binary :",bin(int(x)))
              print("octal :",oct(int(x)))
              print("hexadecimal :",hex(int(x)))
            elif  operator=="octal_to_binary":
              print(bin(int(x,8)))
            elif  operator=="octal_to_hexadecimal" :
              print(hex(int(x,8)))
            elif  operator=="octal_to_decimal":
              print(int(int(x,8)))
            elif  operator=="octal_to_all_systems":
              print("binary",bin(int(x,8)))
              print("hexadecimal",hex(int(x,8)))
              print("decimal",int(int(x,8)))
            elif  operator=="binary_to_hexadecimal":
              print(hex(int(x,2)))
            elif  operator=="binary_to_decimal" :
              print(int(int(x,2)))
            elif  operator=="binary_to_octal":
              print(oct(int(x,2)))
            elif  operator=="binary_to_all_systems":
              print("octal",oct(int(x,2)))
              print("hexadecimal",hex(int(x,2)))
              print("decimal",int(int(x,2)))
        elif "exit":
            terminate_flag=0
        else:
          print("undefined operation")
        input() 
