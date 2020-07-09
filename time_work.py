import time                                         # import time library

t = time.localtime()                               #now,we extract the current date and time by using localtime() func which falls in time libraries
                                                    #and save in one variables
y = t.tm_year                                      #extracting the year and save it
m = t.tm_mon                                       #extracting the month and save it
d = t.tm_mday                                      #extracting the day and save it
h = t.tm_hour                                      #extracting the current hour and save it
min = t.tm_min                                     #extracting the minutes and save it

print("{} / {} / {}".format(d,m,y))                #format date,month and year in general view
print("{} : {}".format(h,min))                     #format time in general view too

#We also show date and time by using ctime() func which falls in time library too
print(time.ctime())

#----------------------------------------

#There is another library by which we can work on date and time i.e datetime
from datetime import *                       # import all func from datetime libraries

t = datetime.today()                         #save current date in variable by using today() func
print(t.month)                               #thats how we can work on month ,date or year
print(t.year)                                #we also save it in a variable and use in future
print(t.day)
string=t.strftime("%a,%b,%Y")                #extracting day,month and year by using argument in this function
print(string)

#EXAMPLE OF USING DATETIME BY USING LIST COMPREHENSIONS

from datetime import *                                      #import library

y,m,d= [int(i) for i in input("Enter date:  ").split()]     #using list comprehension,first we take input  in y/m/d format and then we split it and save them in different variables
d1=  date(y,m,d)                                            #now,convert it into date formate
print(d1.strftime("this is %j day of the year"))            #now,by using %j argument in strftime func ,we can tell that the date is which day pf the year
