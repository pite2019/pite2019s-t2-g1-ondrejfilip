# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#
#Try to expand your implementation as best as you can.
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository.
#
#Delete these comments before commit!
#Good luck.
class student:

    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

student1 = student('John','Doe')
student2 = student('Franta','Lala')

class diary(student):

    def __init__(self, score, attendance):
        super().__init__(firstname, surname)
        self.score = score
        self.attendance = attendance

    def averageinclass(self):
        return sum(self.score) / len(self.score)

    def averagetotal(self):
        pass
