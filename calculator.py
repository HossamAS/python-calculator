import os
from math import *
from tkinter import *
state="d"
text=["_","_"]
text.pop()
text.pop()
cursor =0
operand1=0
operator="+"
first_equal=1
last_operator="_"
operand2=0
ans=0
clr1=0
operand=clr1
continue_=1
def to_bin():
    global state,text,cursor
    if ("".join(text)).isalnum():
      if state=="d":
         text=(str(bin(int("".join(text))))).replace("0b","") 
         print()
      elif state=="o":
         text=(str( bin(int("".join(text),8)))).replace("0b","")
         print()
      elif state=="h":
         text=(str( bin(int("".join(text),16)))).replace("0b","")
         print()
    else:
      text1,text2="".join(text).split('.')
      if state=="d":
         text1=(str(bin(int(text1)))).replace("0b","") 
         text2=(str(bin(int(text2)))).replace("0b","") 
         text="".join([text1,".",text2])
         print()
      elif state=="o":
          text1=(str(bin(int(text1,8)))).replace("0b","") 
          text2=(str(bin(int(text2,8)))).replace("0b","") 
          text="".join([text1,".",text2])
          print()
      elif state=="h":
          text1=(str(bin(int(text1,16)))).replace("0b","") 
          text2=(str(bin(int(text2,16)))).replace("0b","") 
          text="".join([text1,".",text2])
          print()
 
    state="b"
    


def to_hex():
    global state,text,cursor
    if ("".join(text)).isalnum():
      if state=="d":
         text=((str(  hex(int("".join(text))))).replace("0x","")).upper() 
         print()
      elif state=="o":
         text=((str( hex(int("".join(text),8)))).replace("0x","")).upper()
         print()
      elif state=="b":
         text=((str( hex(int("".join(text),2)))).replace("0x","")).upper()  
         print()
    else:
      text1,text2="".join(text).split('.')
      if state=="d":
         text1=(str(hex(int(text1)))).replace("0x","") 
         text2=(str(hex(int(text2)))).replace("0x","") 
         text="".join([text1,".",text2])
         print()
      elif state=="o":
          text1=(str(hex(int(text1,8)))).replace("0x","") 
          text2=(str(hex(int(text2,8)))).replace("0x","") 
          text="".join([text1,".",text2])
          print()
      elif state=="b":
          text1=(str(hex(int(text1,2)))).replace("0x","") 
          for i in range(1,len(text2)%4):
            text2.append("0")
          text2=(str(hex(int(text2,2)))).replace("0x","") 
          text="".join([text1,".",text2])
          print()
    lcd.config(text=text)
    text=list(text)
    cursor=len(text)    
    state="h"

def to_oct():
    global state,text,cursor
    if ("".join(text)).isalnum():
      if state=="d":
         text=(str( oct(int("".join(text))))).replace("0o","")
         print()
      elif state=="h":
         text=(str( oct(int("".join(text),16)))).replace("0o","")
         print()
      elif state=="b":
         text=(str( oct(int("".join(text),2)))).replace("0o","")
         print()
    else:
      text1,text2="".join(text).split('.')
      if state=="d":
          text1=(str(oct(int(text1)))).replace("0o","") 
          text2=(str(oct(int(text2)))).replace("0o","") 
          text="".join([text1,".",text2])
          print()
      elif state=="h":
          text1=(str(oct(int(text1,16)))).replace("0o","") 
          text2=(str(oct(int(text2,16)))).replace("0o","") 
          text="".join([text1,".",text2])
          print()
      elif state=="b":
          text1=(str(oct(int(text1,2)))).replace("0o","") 
          for i in range(1,len(text2)%3):
            text2.append("0")
          text2=(str(oct(int(text2,2)))).replace("0o","") 
          text="".join([text1,".",text2])
          print()
    state="o"

def to_dec():
    global state,text,cursor
    if ("".join(text)).isalnum():
      if state=="o":
         text=str( int("".join(text),8))
         print()
      elif state=="h":
         text=str(int("".join(text),16))
         print()
      elif state=="b":
         text=str(int("".join(text),2))
         print()
    else:
      
      text1,text2="".join(text).split('.')
      if state=="o":
          text1=(str(int(text1,8)))
          text2=(str(int(text2,8)))
          text="".join([text1,".",text2])
          print()
      elif state=="h":
          text1=(str(int(text1,16)))
          text2=(str(int(text2,16)))
          text="".join([text1,".",text2])
          print()
      elif state=="b":
          text1=(str(int(text1,2)))
          for i in range(1,len(text2)%4):
            text2.append("0")
          text2=(str(int(text2,2)))
          text="".join([text1,".",text2])
          print()
 
    state="d"

def print():
    global text,cursor
    lcd.config(text=text)
    text=list(text)
    cursor=len(text)  


calculator=Tk()
calculator.geometry("279x196")
calculator.resizable(0, 0)
lcd=Label(calculator,background="#B8E573",fg="#A4476E",font=("Times New Roman", 21, "bold"))
lcd.place(x=0,y=0)
def clear_screen():
    global text,cursor,operand1,operand2
    operand1=0
    operand2=0
    text=[""]
    lcd.config(text="")
    cursor=0
def Insert_1():
    global text
    global cursor
    clear_for_new()
    text.insert(cursor,"1")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_2():
    global state,text
    global cursor
    clear_for_new()
    if state=='b' :
       state='d'
    text.insert(cursor,"2")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_3():
    global state,text
    global cursor
    clear_for_new()
    if state=='b' :
       state='d'
    text.insert(cursor,"3")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_4():
    global state,text
    global cursor
    clear_for_new()
    if state=='b' :
       state='d'
    text.insert(cursor,"4")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_5():
    global state,text
    clear_for_new()
    global cursor
    if state=='b' :
       state='d'
    text.insert(cursor,"5")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_6():
    global cursor
    global state,text
    clear_for_new()
    if state=='b' :
       state='d'
    text.insert(cursor,"6")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_7():
    global cursor
    global state,text
    clear_for_new()
    if state=='b' :
       state='d'
    text.insert(cursor,"7")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_8():
    global cursor
    global state,text
    clear_for_new()
    if state=='b' or state=='o':
       state='d'
    text.insert(cursor,"8")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_9():
    global cursor
    global state,text
    clear_for_new()
    if state=='b' or state=='o':
       state='d'
    text.insert(cursor,"9")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_0():
    global cursor
    global state,text
    clear_for_new()
    text.insert(cursor,"0")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_A():
    global cursor
    global state,text
    clear_for_new()
    state='h'
    text.insert(cursor,"A")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_B():
    global cursor
    global state,text
    clear_for_new()
    state='h'
    text.insert(cursor,"B")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_D():
    global cursor
    global state,text
    clear_for_new()
    state='h'
    text.insert(cursor,"D")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_E():
    global cursor
    global state,text
    clear_for_new()
    state='h'
    text.insert(cursor,"E")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_F():
    global cursor
    global state,text
    clear_for_new()
    state='h'
    text.insert(cursor,"F")
    lcd.config(text="".join(text))
    cursor+=1
def Insert_C():
    global cursor
    global state,text
    clear_for_new()
    state='h'
    text.insert(cursor,"C")
    lcd.config(text="".join(text))
    cursor+=1

def Insert_dot():
    global cursor
    global state,text
    clear_for_new()
    text.insert(cursor,".")
    lcd.config(text="".join(text))
    cursor+=1

def clear_for_new():
    global operand,text,cursor
    if operand==clr1:
      operand=continue_
      text=[""]
      lcd.config(text="")
      cursor=0

def hex_or_dec():
    global text,state
    if(("".join(text)).isalnum()):
        if(("".join(text)).isdigit()):
            state='d'
        else :
            state='h'
    else :
        text1,text2="".join(text).split('.')
        if(("".join(text1)).isdigit() and ("".join(text2)).isdigit()):
            state='d'
        else :
            state='h'



def Insert_sin():
    global operator
    operator="sin"
    Insert_operand()
    
def Insert_cos():
    global operator
    operator="cos"
    Insert_operand()
    
def Insert_tan():
    global operator
    operator="tan"
    Insert_operand()
    

def Insert_asin():
    global operator
    operator="asin"
    Insert_operand()
    
def Insert_acos():
    global operator
    operator="acos"
    Insert_operand()
    
def Insert_atan():
    global operator
    operator="atan"
    Insert_operand()
    
def Insert_sum():
    global operator
    operator="+"
    Insert_operand()
    
def Insert_sub():
    global operator
    operator="-"
    Insert_operand()
    
def Insert_mul():
    global operator
    operator="x"
    Insert_operand()
    
def Insert_div():
    global operator
    operator="÷"
    Insert_operand()
    
def Insert_bitwise_or():
    global operator
    operator="|"
    Insert_operand()
    
def Insert_bitwise_and():
    global operator
    operator="&"
    Insert_operand()
    
def Insert_comp():
    global operator
    operator="~"
    Insert_operand()
def Insert_log_or():
    global operator
    operator="||"
    Insert_operand()
    
def Insert_log_and():
    global operator
    operator="&&"
    Insert_operand()
    
def Insert_not():
    global operator
    operator="!"
    Insert_operand()
def Insert_pow():
    global operator
    operator="pow"
    Insert_operand()
    
def Insert_root():
    global operator
    operator="root"
    Insert_operand()
    
def Insert_log():
    global operator
    operator="log"
    Insert_operand()
    
def Insert_mod():
    global operator
    operator="%"
    Insert_operand()
    
def Insert_bitwise_xor():
    global operator
    operator="^"
    Insert_operand()
  
    

def Insert_operand():
    global operand1,operand,operand2,operand2_state,operand1_state,first_equal
    first_equal=1
    operand=clr1
    operand1=save_operand()

         
def save_operand():
    global state,text
    if ("".join(text)).isalnum():
            if state=="h":
               oper=int("".join(text),16)
            elif state=="o":
               oper=int("".join(text),8) 
            elif state=="b":
                oper=int("".join(text),2) 
            else:
                oper=int("".join(text))
    else:
                oper=float("".join(text))

    return  oper


def Insert_eq():
   
      global operator,operand,operand2,last_operator,operand2_state,first_equal
      operand=clr1
      if(first_equal==1):
        first_equal=0
        operand2=save_operand()
      Insert_operation()
      
      
      

def Insert_operation():
      global operand1,operand2,text,operator,ans,operand,cursor,state
      if operator=="+":
         
         ans=operand1+operand2

      elif operator=="-":
         
         ans=operand1-operand2

      elif operator=="x":
         
         ans=operand1*operand2

      elif operator=="÷":
         
         ans=operand1/operand2


      elif operator=="|":
     
         ans=operand1|operand2


      elif operator=="&":
   
         ans=operand1 & operand2


      elif operator=="~":
         ans=~operand1


      elif operator=="||":
    
         ans=operand1 or operand2


      elif operator=="&&":
     
         ans=operand1 and operand2


      elif operator=="!":
         ans=not operand1


      elif operator=="sin":
         ans=sin(operand1*pi/180)


      elif operator=="cos":
         ans=cos(operand1*pi/180)


      elif operator=="tan":
         ans=tan(operand1*pi/180)


      elif operator=="asin":
         ans=asin(operand1)*180/pi


      elif operator=="acos":
         ans=acos(operand1)*180/pi


      elif operator=="atan":
         ans=atan(operand1)*180/pi


      elif operator=="pow":

         ans=pow(operand1,operand2)
         operand=2

      elif operator=="root":
 
         ans=pow(operand1,1/operand2)


      elif operator=="log":

         ans=log(operand1,operand2)
 

      elif operator=="%":
 
         ans=operand1%operand2
  

      elif operator=="^":
         
         ans=operand1^operand2
 
      operand1=ans
      text=list(str(ans))
      if state=='h':
        state='d'
        to_hex()
      elif state=='o':
        state='d'
        to_oct()
      elif state=='b':
        state='d'
        to_bin()
      lcd.config(text="".join(text))
      cursor=len(text)

def Delete():
    global cursor,text
    if len(text)>=1:
      text.pop()
      lcd.config(text=''.join(text))
      cursor-=1
    else:
      text=[""]
      lcd.config(text="")

but_dot = Button(calculator,text=".",background="#DACA00",command=Insert_dot,foreground="#630C3B",height=1,width=3)
but_dot.place(x=186,y=170)      
but_A = Button(calculator,text="A",background="#DACA00",command=Insert_A,foreground="#630C3B",height=1,width=3)
but_A.place(x=155,y=170)
but_B = Button(calculator,text="B",background="#DACA00",command=Insert_B,foreground="#630C3B",height=1,width=3)
but_B.place(x=124,y=170)
but_C = Button(calculator,text="C",background="#DACA00",command=Insert_C,foreground="#630C3B",height=1,width=3)
but_C.place(x=93,y=170)
but_D = Button(calculator,text="D",background="#DACA00",command=Insert_D,foreground="#630C3B",height=1,width=3)
but_D.place(x=62,y=170)
but_E = Button(calculator,text="E",background="#DACA00",command=Insert_E,foreground="#630C3B",height=1,width=3)
but_E.place(x=31,y=170)
but_F = Button(calculator,text="F",background="#DACA00",command=Insert_F,foreground="#630C3B",height=1,width=3)
but_F.place(x=0,y=170)
but_clr_screen = Button(calculator,text="C",background="#DACA00",command=clear_screen,foreground="#630C3B",height=1,width=19)
but_clr_screen.place(x=140,y=144)
but_back = Button(calculator,text="CE",background="#DACA00",command=Delete,foreground="#630C3B",height=1,width=19)
but_back.place(x=0,y=144)
but_oct = Button(calculator,text="oct",background="#DACA00",command=to_oct,foreground="#630C3B",height=1,width=3)
but_oct.place(x=248,y=40)
but_hex = Button(calculator,text="hex",background="#DACA00",command=to_hex,foreground="#630C3B",height=1,width=3)
but_hex.place(x=248,y=66)
but_dec = Button(calculator,text="dec",background="#DACA00",command=to_dec,foreground="#630C3B",height=1,width=3)
but_dec.place(x=248,y=92)
but_bin = Button(calculator,text="bin",background="#DACA00",command=to_bin,foreground="#630C3B",height=1,width=3)
but_bin.place(x=248,y=118)
but_asin = Button(calculator,text="asin",background="#DACA00",command=Insert_asin,foreground="#630C3B",height=1,width=3)
but_asin.place(x=217,y=66)
but_acos = Button(calculator,text="acos",background="#DACA00",command=Insert_acos,foreground="#630C3B",height=1,width=3)
but_acos.place(x=217,y=92)
but_atan = Button(calculator,text="atan",background="#DACA00",command=Insert_atan,foreground="#630C3B",height=1,width=3)
but_atan.place(x=217,y=118)
but_log = Button(calculator,text="log",background="#DACA00",command=Insert_log,foreground="#630C3B",height=1,width=3)
but_log.place(x=217,y=40)
but_root = Button(calculator,text="root",background="#DACA00",command=Insert_root,foreground="#630C3B",height=1,width=3)
but_root.place(x=186,y=40)
but_sin = Button(calculator,text="sin",background="#DACA00",command=Insert_sin,foreground="#630C3B",height=1,width=3)
but_sin.place(x=186,y=66)
but_cos = Button(calculator,text="cos",background="#DACA00",command=Insert_cos,foreground="#630C3B",height=1,width=3)
but_cos.place(x=186,y=92)
but_tan = Button(calculator,text="tan",background="#DACA00",command=Insert_tan,foreground="#630C3B",height=1,width=3)
but_tan.place(x=186,y=118)
but_log_and = Button(calculator,text="&&",background="#DACA00",command=Insert_log_and,foreground="#630C3B",height=1,width=3)
but_log_and.place(x=155,y=118)
but_bit_or = Button(calculator,text="||",background="#DACA00",command=Insert_log_or,foreground="#630C3B",height=1,width=3)
but_bit_or.place(x=155,y=92)
but_bit_not = Button(calculator,text="!",background="#DACA00",command=Insert_not,foreground="#630C3B",height=1,width=3)
but_bit_not.place(x=155,y=66)
but_pow = Button(calculator,text="pow",background="#DACA00",command=Insert_pow,foreground="#630C3B",height=1,width=3)
but_pow.place(x=155,y=40)
but_bit_and = Button(calculator,text="&",background="#DACA00",command=Insert_bitwise_and,foreground="#630C3B",height=1,width=3)
but_bit_and.place(x=124,y=118)
but_bit_or = Button(calculator,text="|",background="#DACA00",command=Insert_bitwise_or,foreground="#630C3B",height=1,width=3)
but_bit_or.place(x=124,y=92)
but_bit_xor = Button(calculator,text="^",background="#DACA00",command=Insert_bitwise_xor,foreground="#630C3B",height=1,width=3)
but_bit_xor.place(x=124,y=66)
but_bit_comp = Button(calculator,text="~",background="#DACA00",command=Insert_comp,foreground="#630C3B",height=1,width=3)
but_bit_comp.place(x=124,y=40)
but_mul = Button(calculator,text="x",background="#DACA00",command=Insert_mul,foreground="#630C3B",height=1,width=3)
but_mul.place(x=93,y=118)
but_div = Button(calculator,text="÷",background="#DACA00",command=Insert_div,foreground="#630C3B",height=1,width=3)
but_div.place(x=93,y=92)
but_sum = Button(calculator,text="+",background="#DACA00",command=Insert_sum,foreground="#630C3B",height=1,width=3)
but_sum.place(x=93,y=66)
but_sub = Button(calculator,text="-",background="#DACA00",command=Insert_sub,foreground="#630C3B",height=1,width=3)
but_sub.place(x=93,y=40)
but_eq = Button(calculator,text="=",background="#DACA00",command=Insert_eq,foreground="#630C3B",height=1,width=3)
but_eq.place(x=62,y=118)
but_0 = Button(calculator,text="0",background="#DACA00",command=Insert_0,foreground="#630C3B",height=1,width=3)
but_0.place(x=31,y=118)
but_mod = Button(calculator,text="%",background="#DACA00",command=Insert_mod,foreground="#630C3B",height=1,width=3)
but_mod.place(x=0,y=118)
but_1 = Button(calculator,text="1",background="#DACA00",command=Insert_1,foreground="#630C3B",height=1,width=3)
but_1.place(x=62,y=92)
but_2 = Button(calculator,text="2",background="#DACA00",command=Insert_2,foreground="#630C3B",height=1,width=3)
but_2.place(x=31,y=92)
but_3 = Button(calculator,text="3",background="#DACA00",command=Insert_3,foreground="#630C3B",height=1,width=3)
but_3.place(x=0,y=92)
but_4 = Button(calculator,text="4",background="#DACA00",command=Insert_4,foreground="#630C3B",height=1,width=3)
but_4.place(x=62,y=66)
but_5 = Button(calculator,text="5",background="#DACA00",command=Insert_5,foreground="#630C3B",height=1,width=3)
but_5.place(x=31,y=66)
but_6 = Button(calculator,text="6",background="#DACA00",command=Insert_6,foreground="#630C3B",height=1,width=3)
but_6.place(x=0,y=66)
but_7 = Button(calculator,text="7",background="#DACA00",command=Insert_7,foreground="#630C3B",height=1,width=3)
but_7.place(x=62,y=40)
but_8 = Button(calculator,text="8",background="#DACA00",command=Insert_8,foreground="#630C3B",height=1,width=3)
but_8.place(x=31,y=40)
but_9 = Button(calculator,text="9",background="#DACA00",command=Insert_9,foreground="#630C3B",height=1,width=3)
but_9.place(x=0,y=40)


 

calculator.mainloop()

















#while 1:
#  os.system("cls")
#  mode=input("to scientific mode press 1 \n to programmer mode press 0 :")
#  if mode.isdigit():
#    if int(mode):
#      terminate_flag=1
#      while terminate_flag: 
#        os.system("cls")
#        operator=input("the following is the type of operations\n\
#        \nsummation\
#        \nsubtraction\
#        \nremender\
#        \nmultiplication\
#        \ndivision\
#        \npower\
#        \nroot\
#        \nsin\
#        \ncos\
#        \ntan\
#        \nsin_inv\
#        \ncos_inv\
#        \ntan_inv\
#        \nlog\
#        \nexit\
#        \n\nEnter one the operation : ")
#  
#        if operator=="summation" or operator=="subtraction"or operator=="remender" or operator=="multiplication"or operator=="division"or operator=="power" or operator=="root" :
#          x=input("Enter Two Values separated by one space or one value :").split(' ')
#          x[0] =int(x[0])
#          x[1] =int(x[1])
#          if operator=="summation":
#            print(x[0]+x[1])
#          elif  operator=="subtraction":
#            print(x[0]-x[1])
#          elif  operator=="remender":
#            print(x[0]%x[1])
#          elif  operator=="multiplication":
#            print(x[0]*x[1])
#          elif  operator=="division":
#            print(x[0]/x[1])
#          elif  operator=="power" :
#            print(x[0]**x[1])
#          elif  operator=="root":
#            print(x[0]**(1/x[1]))
#        
#        elif  operator=="sin" or operator=="cos" or operator=="tan" or operator=="sin_inv" or operator=="cos_inv" or operator=="tan_inv" or operator=="log" :
#          x=int(input("Enter one Value : ")) 
#          if operator=="sin":
#            print(math.sin(x))
#          elif  operator=="cos":
#            print(math.cos(x))
#          elif  operator=="tan":
#            print(math.tan(x))
#          elif  operator=="sin_inv":
#            print(math.asin(x))
#          elif  operator=="cos_inv":
#            print(math.acos(x))
#          elif  operator=="tan_inv" :
#            print(math.atan(x))
#          elif  operator=="log":
#            print(math.log(x))
#        elif "exit":
#          terminate_flag=0
#        else:
#            print("undefined operation")
#        input()
#    else:
#      terminate_flag=1
#      while terminate_flag:
#        operator=input("the following is the type of operations\n\
#        \nlogical_and\
#        \nlogical_or\
#        \nbitwise_and\
#        \nbitwise_or\
#        \nbitwise_xor\
#        \nlogical_not\
#        \nbitwise_not\
#        \nhexadecimal_to_binary\
#        \nhexadecimal_to_decimal\
#        \nhexadecimal_to_octal\
#        \nhexadecimal_to_all_systems\
#        \ndecimal_to_binary\
#        \ndecimal_to_hexadecimal\
#        \ndecimal_to_octal\
#        \ndecimal_to_all_systems\
#        \noctal_to_binary\
#        \noctal_to_hexadecimal\
#        \noctal_to_decimal\
#        \noctal_to_all_systems\
#        \nbinary_to_hexadecimal\
#        \nbinary_to_decimal\
#        \nbinary_to_octal\
#        \nbinary_to_all_systems\
#        \nexit\
#        \n\nEnter one the operation : ")
#    
#        if operator=="logical_and" or operator=="logical_or"or operator=="bitwise_and" or operator=="bitwise_or"or operator=="bitwise_xor" :
#            x=input("Enter Two Values separated by one space or one value :").split(' ')
#            x[0] =int(x[0])
#            x[1] =int(x[1])
#            if operator=="logical_and":
#              print(bool(x[0] and x[1]))
#            elif  operator=="logical_or":
#              print(bool(x[0] or x[1]))
#            elif  operator=="bitwise_and":
#              print(x[0]&x[1])
#            elif  operator=="bitwise_or":
#              print(x[0]|x[1])
#            elif  operator=="bitwise_xor":
#              print(x[0]^x[1])
#            else:
#              print("undefined operation")
#        elif  operator=="logical_not" or operator=="bitwise_not" or       operator=="hexadecimal_to_binary" or operator=="hexadecimal_to_decimal"       or operator=="hexadecimal_to_octal" or operator=="hexadecimal_to_all_systems"       or operator=="decimal_to_binary"or operator=="decimal_to_hexadecimal" or        operator=="decimal_to_octal" or operator=="decimal_to_all_systems" or        operator=="octal_to_binary"or operator=="octal_to_hexadecimal" or        operator=="octal_to_decimal" or operator=="octal_to_all_systems" or         operator=="binary_to_hexadecimal"or operator=="binary_to_decimal"or          operator=="binary_to_octal"or operator=="binary_to_all_systems":
#            x=input("Enter one Value : ") 
#            if operator=="logical_not":
#              print(bool(not int(x)))
#            elif  operator=="bitwise_not":
#              print(~int(x))
#            elif  operator=="hexadecimal_to_binary":
#              print(bin(int(x),16))
#            elif  operator=="hexadecimal_to_decimal":
#              print(int(int(x,16)))
#            elif  operator=="hexadecimal_to_octal":
#              print(oct(int(x,16)))
#            elif  operator=="hexadecimal_to_all_systems" :
#              print("binary :",bin(int(x,16)))
#              print("decimal :",int(x,16))
#              print("binary :",oct(int(x,16)))
#
#            elif  operator=="decimal_to_binary":
#              print(bin(int(x)))
#            elif  operator=="decimal_to_hexadecimal":
#              print(hex(int(x)))
#            elif  operator=="decimal_to_octal":
#              print(oct(int(x)))
#            elif  operator=="decimal_to_all_systems":
#              print("binary :",bin(int(x)))
#              print("octal :",oct(int(x)))
#              print("hexadecimal :",hex(int(x)))
#            elif  operator=="octal_to_binary":
#              print(bin(int(x,8)))
#            elif  operator=="octal_to_hexadecimal" :
#              print(hex(int(x,8)))
#            elif  operator=="octal_to_decimal":
#              print(int(int(x,8)))
#            elif  operator=="octal_to_all_systems":
#              print("binary",bin(int(x,8)))
#              print("hexadecimal",hex(int(x,8)))
#              print("decimal",int(int(x,8)))
#            elif  operator=="binary_to_hexadecimal":
#              print(hex(int(x,2)))
#            elif  operator=="binary_to_decimal" :
#              print(int(int(x,2)))
#            elif  operator=="binary_to_octal":
#              print(oct(int(x,2)))
#            elif  operator=="binary_to_all_systems":
#              print("octal",oct(int(x,2)))
#              print("hexadecimal",hex(int(x,2)))
#              print("decimal",int(int(x,2)))
#        elif "exit":
#            terminate_flag=0
#        else:
#          print("undefined operation")
#        input() 