#!/bin/python3
import sys

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
  
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        
    def calculate(self):
        mean_score = 0
        for i in range(len(self.scores)):
            mean_score += self.scores[i]
            
        mean_score = mean_score/len(self.scores)
        grade = ""
        if mean_score < 40:
            grade = "T"
        elif mean_score < 55:
            grade = "D"
        elif mean_score < 70:
            grade = "P"
        elif mean_score < 80:
            grade = "A"
        elif mean_score <90:
            grade = "E"
        else:
            grade = "O"  
        return grade
		
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())	 