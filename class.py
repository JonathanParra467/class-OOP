"""
Assignment Steps:

Class Creation: Design a class named Person with the following data: name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read. You need to print out all the data for each. You can create a method that prints everything or call each get function one at a time.
"""
class Student:

    school_name = "McHenry County College"

    def __init__(self, first_name, last_name, student_id, grade_level="Freshman"):
        # Instance variables
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__grade_level = grade_level

    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
        
    def get_student_id(self):
        return self.__student_id
    
    def get_grade_level(self):
        return self.__grade_level

    def set_first_name(self, value):
        self.__first_name = value
    
    def set_last_name(self, value):
        self.__last_name = value

    def set_student_id(self, value):
        self.__student_id = value
    
    def set_grade_level(self, value):
        self.__grade_level = value

    def print_student_details(self):
        print("Student Details:", vars(self))
    
    def print_info(self):
        print(self.__first_name)
        print(self.__last_name)
        print(self.__student_id)
        print(self.__grade_level)

def main():
    
    student1 = Student("John", "Deven", "123456", "Sophomore")
    student2 = Student("serge", "Smith", "789012", "Freshman")
    student3 = Student("ivan", "andrew", "475612", "senior")

    print(student1.get_first_name())
    print(student1.get_last_name())
    print(student1.get_student_id())
    print(student1.get_grade_level())

    print(student2.get_first_name())
    print(student2.get_last_name())
    print(student2.get_student_id())
    print(student2.get_grade_level())
     
    print(student3.get_first_name())
    print(student3.get_last_name())
    print(student3.get_student_id())
    print(student3.get_grade_level())

main()