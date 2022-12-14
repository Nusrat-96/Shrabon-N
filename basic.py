#way to print mutiple variable in python

''' pthon commenting 
multiple line'''

# keyboard shortcut key to comment multiple line at a time is (ctrl + c+k)
# to run (ctrl+alt+n)

print ("enter name (string) class (int)")
Name = str (input())
Classname= int(input())

print (Name, "is in class",Classname)
print ("%s is in class %s"  %(Name, Classname))                        #using % formating
print ("%(na)s is in calss %(cl)s " %{'na': Name, 'cl':Classname})     #pass as dictionay 
print ("{} in in class {}".format(Name, Classname))      # The new style of string formatting using the format() method
print ("{0} is in class {1} and {0} is a good boy".format (Name, Classname ))
print ("{v1} , {v2}".format (v1=Name, v2=Classname))
print (Name + ",,,,," + str(Classname))
#printing with comma separator 
print (Name, Classname, sep=', ')



#taking multiple inputs at a time 
x, y, z = input ("Enter three values: ").split()
x1,x2, x3 = input ("Enter three values, separated with comma : ").split(",")
print(x,y,z) 
print(x1,x2, x3 ) 


#taking list input
l = list(map(int, input("Please enter List values: ").split()))
l1 = [int (i) for i in input("list value: ").split()]
print ("Give List value: ")
print (l)


#documentation 1
#number 
print ("operators work, reminder , division, floor devision, power ")
a= 5%3          #provide reminder 
b=5/3
c= 5//3         # provide Floor value 
d= 5**3            #also can use pow(x,y) function 
e= complex (5, d)           #complex(real, imaginary)
print (a,b, c,d,e, sep='\n')

print (e.conjugate())


#string 
