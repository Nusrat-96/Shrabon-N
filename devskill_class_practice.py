#Python OOP related 

from multipledispatch import dispatch    #used for method overloading

#class diclaration 
class motor_bike:
    bike_name=""
    speed_hour = 0

    """---------------constructor----------------------------------------------------------------
    The __init__() method is called the constructor and is always called when an object is created.
    It can be used in three types - Parameterized, Non-Parameterized, Default Constructor
    No need to use return in constructor, it is always None
    -------------------------------------------------------------------------------------------"""
    
    def __init__(self, information="") -> None:
        self.information = information
        print("Give information about {}".format(self.information))


    """A function defined inside a class is called a method"""
    @dispatch(object)
    def bike_type(self, color):                               
        return "{}".format(color)


    @dispatch(object, object)
    def bike_type(self, type, color):                 #method overloading                           
        return "This is  a {} and its color is  {}".format(type,color)

    def calculate_speed_minute(self, speed_in_hour):
        print("Speed in hour: {}".format(self.speed_hour))
        speed_in_minute = float(speed_in_hour/60)
        if speed_in_minute>30:
            return "Fabulous speed, speed is {:.3f} per minute".format(speed_in_minute)
        else:
            return "The speed of the bike is {:.3f}, less than 30km per minute".format(speed_in_minute)



class biker_informatin_1(motor_bike):    
   pass                             #do not want to add any other properties or methods to the class


class biker_informatin_2(motor_bike): 

    #if weadd the __init__() function, the child class will no longer inherit the parent's __init__() function.
    def __init__(self,information="", Biker_name="", bike_name="") -> None:   
        self.information = information
        print("Give information about {} from the biker informatin class".format(self.information))
        self.biker_name =  Biker_name
        self.bike_name = bike_name
    
    def Congratulation(self):
        print("Congratulatin {} for win , your bike name is {}".format(self.biker_name, self.bike_name))




#create object from  the class :  object_name = ClassName()
#we can create multiple object for a class
scotter = motor_bike("The scotter")


# #Access and modify class attribute using (.)
scotter_color = scotter.bike_type("Red") 
scotter.bike_name= "ScotterG1"
scotter.speed_hour = int(input("Give speed you need: "))
scotter_speed = scotter.speed_hour

print("*****Call bike_type method with one argument*****")
print(f"Name:{scotter.bike_name},  Color:{scotter_color}")
print(scotter.calculate_speed_minute(scotter_speed), end='\n')
print("\n")


#create another object
monkey_bikes = motor_bike("The Monkey Bike")



"""      ----------method overloading ----------
Two or more methods have the same name but different numbers 
of parameters or different types of parameters, or both"""
print("---------Overloading---------- ")
print("*****Call bike_type method with two argument******")
print(monkey_bikes.bike_type("Monkey24", "Black"))



"""                    ------Inheritance----
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class."""
print("\n---------Inheritance and overriding---------- ")
hero_hunda = biker_informatin_1("Hunda")
print("\n\n",hero_hunda.bike_type("HeroHunda","Green"))


"""        -------method overriding--------
In Python method overriding occurs simply defining in the child class 
a method with the same name of a method in the parent class
"""
suzuki_bike = biker_informatin_2("The winner", "Mr Jian", "suzuki123")
suzuki_bike.Congratulation()


