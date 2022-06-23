'''
# Wap to code a function where it will not take any parameter and not
#return any value
r = float(input("Enter Radius:  "))

def ar_circle():
    ar = 3.14 *r*r
    print("Area of circle:  " , ar)
    
ar_circle()
'''
'''




# Wap to code a function where it will  take any parameter and not
#return any value
r = float(input("Enter Radius:  "))

def ar_circle(radius): # formal variable  # function defination ,
                      #r is a parameter
    ar = 3.14 *radius*radius
    print("Area of circle:  " , ar)
    
ar_circle(r)  #Actual variable# function calling  , r is parameter
'''

# Wap to code a function where it will  take any parameter and 
#return specific value
'''
r = int(input("Enter Radius:  "))

def ar_circle(radius): # formal variable  # function defination ,
                      #r is a parameter
    ar = 3.14 *radius*radius
    return ar
  
    
#print(ar_circle(r))  #Actual variable# function calling  ,
                       #r is parameter
s = ar_circle(r)
#print("ans: " , int(s))
print(s)
'''
'''
# wap to return the multiple values with the
# define function name it to_calc()

def to_calc(x,y):
    return x+y , x-y , x*y , x/y

p = int(input("Enter p:  "))
q = int(input("Enter q:  "))

add , sub , mul , div= to_calc(p , q)
print("add:  " , add , "  sub: " , sub)
print("mul:  " ,mul , "  div: " , div)
'''

'''
# wap to calculate the sum of three numbers
# and pass the sum into another function which
#will return the average of returned value

def func1(x , y , z):
    return x+y+z

def func2_average(q):
    return q/3

t = func1(10 , 30 , 20)
print("Sum of number:  " , t)

m = func2_average(t)
print("Average of number:  " , m)
'''
'''
def func(sanjana):  # formal
    print("before defination statement: " ,num )
   
    sanjana = sanjana+1       # a , num  scope :  local , 
    print("inside function: " , sanjana) #5

num=4
print("before calling " , num)
func(num)  # actual    # num scope: global
print("after calling " , sanjana)'''

'''
john=None
def greet():
    john=223.5655
    print("Hello" , john) # noscope is define of john

greet()
print(john)

'''

# scope of functions


def greet():  # scope of defination global
    print("I am Happy ")
    def bye():   # defination local
        print("Hmm bye byee:  ")
        
        
    bye() # scope local


greet()  # scope of function calling is global
#bye()    # scope global but not able to access
             # bcz deination available in another function




























































    