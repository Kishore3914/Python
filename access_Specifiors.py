class access_specifiers:

    """ public, protected and private variables """
    Public_name = "Kishore"
    _protected_name = "Arun"
    __Private_name = "Pranesh"

    """ Public method """
    def Public_method(self):
        print(self.Public_name, "Accessed public variable inside public method inside class")
        print(self._protected_name, "Accessed protected variable inside public method inside class")
        print(self.__Private_name, "Accessed private variable inside public method inside class")

    """ Protected method """
    def _Protected_method(self):
        print(self.Public_name, "Accessed public variable inside Protected method inside class")
        print(self._protected_name, "Accessed protected variable inside Protected method inside class")
        print(self.__Private_name, "Accessed private variable inside Protected method inside class")

    """ Private method """
    def __Private_method(self):
        print(self.Public_name, "Accessed public variable inside Private method inside class")
        print(self._protected_name, "Accessed protected variable inside Private method inside class")
        print(self.__Private_name, "Accessed private variable inside Private method inside class")


class access_specifiors_inherit(access_specifiers):
    pass

if __name__ == '__main__':

    obj = access_specifiers() # parent class object creation

    """ accessing public,protected and private variables of access_specifiers class in main using parent obj""" 

    print(obj.Public_name)
    
    print(obj._protected_name)
    
    # print(obj.__Private_name, "From main") # NOT ACCESSIBLE 

    """ accessing public,protected and private methods of access_specifiers class in main using parent obj"""
    
    obj.Public_method()
    
    obj._Protected_method()
    
    # obj.__Private_method() # NOT ACCESSIBLE


    child_obj = access_specifiors_inherit() # child class object creation

    """ accessing public,protected and private variables of access_specifiers class in main using child obj""" 

    print(child_obj.Public_name)

    print(child_obj._protected_name)

    # print(child_obj.__Private_name) # NOT ACCESSIBLE

    """ accessing public,protected and private methods of access_specifiers class in main using child obj"""

    child_obj.Public_method()

    child_obj._Protected_method()

    # child_obj.__Private_method() # NOT ACCESSIBLE
