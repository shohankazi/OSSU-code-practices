""" 
This video covers object-oriented programming in Python, discussing classes, inheritance, information hiding, and class variables. It also provides several examples, including creating objects that mimic real-life objects and adding functionality to child classes. Lastly, it explains how to use class variables to keep track of instances of a class.
"""
# Detailed Summary for [9. Python Classes and Inheritance](https://www.youtube.com/watch?v=FlGjISF3l78&ab_channel=MITOpenCourseWare) 
""" 
[00:00](https://www.youtube.com/watch?v=FlGjISF3l78&ab_channel=MITOpenCourseWare&t=0) The lecture is a recap of object-oriented programming and introduces new concepts like information hiding, class variables, and inheritance.
- Last lecture was about object-oriented programming and abstract data types implemented through Python classes
- Today's lecture will cover more examples and nuances of classes, information hiding, class variables, and inheritance
- Object-oriented programming can simulate real-life inheritance and the lecture will introduce this concept.
    
[05:56](https://www.youtube.com/watch?v=FlGjISF3l78&ab_channel=MITOpenCourseWare&t=356.95) Object-oriented programming allows creating objects that mimic real-life with data and procedural attributes.
- Each object can have different data and methods assigned to them.
- Objects can be grouped together based on their attributes.
- Data attributes define what the object is and it's up to the programmer to decide how to represent it.
    
[11:53](https://www.youtube.com/watch?v=FlGjISF3l78&ab_channel=MITOpenCourseWare&t=713.37) Getters and setters should be implemented for classes to prevent bugs from occurring later on
- Getters and setters are used to set data attributes to whatever is passed in
- The __str__ method is used to tell Python how to print an object of a certain type
- Accessing data attributes directly is not recommended, and getters and setters should be used instead
    
[17:48](https://www.youtube.com/watch?v=FlGjISF3l78&ab_channel=MITOpenCourseWare&t=1068.38) Default arguments can be passed into methods as formal parameters and if no parameter is passed, the default argument is used.
- Default arguments are used with formal parameters in methods.
- If no parameter is passed, the default argument is used.
- If a parameter is passed, it overrides the default argument.
    
[23:44](https://www.youtube.com/watch?v=FlGjISF3l78&ab_channel=MITOpenCourseWare&t=1424.75) Child classes can add more information and behavior than their parent classes, and can also override behavior.
- Child classes can have additional attributes and methods.
- Child classes can override methods from their parent classes.
- An example of a subclass, "Cat," is shown inheriting from the parent class "Animal."
    
[29:41](https://www.youtube.com/watch?v=FlGjISF3l78&ab_channel=MITOpenCourseWare&t=1781.26) The video explains how to create a Person class with a list of friends and methods to get age difference, print hello, and override the __str__ method.
- In the __init__ method, a list of friends is created for Person.
- The speak() method prints "hello" to the screen.
- The get_friends() method returns the list of friends.
- The get_age_diff() method calculates the age difference between two people.
    
[35:37](https://www.youtube.com/watch?v=FlGjISF3l78&ab_channel=MITOpenCourseWare&t=2137.8) The instructor discusses the concept of class variables and illustrates it using a subclass called Rabbit.
- Class variables are shared among all instances of a class.
- Class variables are typically defined inside the class but outside the __init__ method.
- The instructor initializes a class variable called "tag" to 1 inside the Rabbit class.
    
[41:31](https://www.youtube.com/watch?v=FlGjISF3l78&ab_channel=MITOpenCourseWare&t=2491.79) The section explains how instance variables work in Python classes and how to implement the __init__ and __add__ methods.
- Instance variables are specific to each instance of a class.
- The __init__ method initializes the instance variables of a class.
- The __add__ method is used to define the behavior of the plus operator between two instances of a class.
- The zfill() method is used to pad a number with zeros to a fixed length.
"""