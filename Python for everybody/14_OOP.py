# Object Oriented Programming
""" 
1. A program is made up of many cooperating objects
2. Instead of being the "whole program" - each object is a little "island" within the program and cooperatively working with other objects.
3. A program is made up of one or more objects working together - objects make use of each other's capabilities
"""

# Object 
""" 
1. An object is a bit of self-contained code and data.
2. A key aspect of the object approach is to break the problem into smaller understandable parts(divide and conquer)
3. Objects have boundaries that allow us to ignore un-needed detail
4. We have been using objects all along: String objects, integer objects, dictionary objects, list objects
5. Objects hide detail - they allow us to ignore the detail of the "rest of the program"
5. Objects hide detail - they allow they allow the "rest of the program" to ignore the detail about "us"
"""
# Definitions

""" 
1. Class - a template - Dog
2. Method or Message - A defined capability of a class - bark()
3. Field or attribute - A bit of data in a class - length
4. Object or instance - A particular instance of a class - Lassie
"""
# Terminology - Class

""" 
Defines the abstract characteristics of a thing (object), including the thing's characteristics (its attributes, fields or properties) and the thing's behaviors (the things it can do, or methods, operations or features). One might say that a class is a blueprint or factory that describes the nature of something. For example, the class dog would consist of traits shared by all dogs, such as breed and fur color(characteristics), and the ability to bark and sit(behaviors).

A pattern (exemplar) of a class. The class of dog defines all possible dogs by listing the characteristics and behaviors they can have; the object Lassie is one of the characteristics. A dog has fur; Lassie has brown-and-white fur.
"""
# Terminology - Instance
""" 
One can have an instance of a class or a particular object. The instance is the actual object created at runtime. In programmer Jargon, the Lassie object is an instance of the Dog class. The set of values of the attributes of a particular object is called its state. The object consists of state and the behavior that's defined in the object's class.
====>> Object and instance are often used interchangeably
"""
# Terminology - Method
""" An object's abilities. In language, methods are verbs. Lassie, being a Dog, has the ability to bark. So bark() is one of Lassie's methods. She may have other methods as well, for example sit() or eat() or walk() or save_timmy(). Within the program, using a method usually affects only one particular object; all Dogs can bark, but you need only one particular dog to do the barking 
====>> Method and Message are often used interchangeably. 
"""
# This is the template for making PartyAnimal objects

class PartyAnimal:
    x = 0 #Each PartyAnimal object has a bit of data.
    def party(self):
        self.x = self.x + 1
        print("So far",self.x)
an = PartyAnimal() #Construct a PartyAnimal object and store in an
an.party() #PartyAnimal.party(an)
# an.party()
# an.party()
print("Type", type(an))
print("Dir",dir(an)) # We can use dir to find the "capabilities" of our newly created class.

# A nerdy way to find Capabilities
""" 
1. The dir() command lists capabilities
2. Ignore the ones with underscores - these are used by python itself
3. The rest are real operations that the object can perform
4. It is like type() - it tells us something "about" a variable 
"""
y = 'Hello there' 
# print(dir(y))