"""
Class Education Program Management (is parent class of Subjects class): store the education programs information including:
+ attributes: Subject(many subjects depend on specialized traning.) 
+ methods: input, display, get-set, search, remove and update 
"""
#import when files are in the same folder
from Subjects import *

class EduPrograms:

    def __init__(self, number, ID,listparam):
        self.Number = number
        self.ID = ID
        self.ListSubjects = listparam    

    #initialization function without parameter
    def __init__(self):
        self.Number = 0
        self.ListSubjects = []  

    #input function
    def EduProgramInput(self):
        self.ID = input ("Enter the ID of education program: ")
        self.Number = int (input ("Enter Number of Subjects: "))
        for i in range (0, self.Number):
            #declare Subject object
            self.Subject = Subjects()
            self.Subject.SubjectInput()
            self.ListSubjects.append(self.Subject)

    def EduProgramDisplay(self):
        print ("{:<20}{:<20}{:<30}{:<30}{:<20}".format("Code", "Name", "Num of Credits", "Prerequisite course code", "Department"))
        for self.Subject in self.ListSubjects:
            self.Subject.SubjectDisplay()

    #Search the subject in Education program
    def Search(self, Keyword):
        for index in range (0, self.Number):
            self.Subject = self.ListSubjects[index]
            if (Keyword == self.Subject.Code):
                return [index, self.Subject]
        return False   
    
    #The update function: To update Subject in Education Program: Search by code of the subject and then update information
    def Update(self, Keyword):
        Check = self.Search(Keyword)
        if (Check == False):
            print ("A Subject code is not appropriate!")
        else:
            Check[1].SubjectInput()
            index = Check[0] # Get index of subject which need to update
            self.ListSubjects[index] = Check[1]
            print ("Update successfully the Subject in Education program!")

    #The remove function: To remore from current education program: Search by code of the subject and then remove
    def Remove(self, Keyword):
        Check = self.Search(Keyword)
        if (Check == False):
            print ("A Subject code is not appropriate!")
        else:
            index = Check[0] # Get index of subject which need to update
            self.ListSubjects.pop(index)
            print ("Remove successfully the Subject in Education program!")


# if __name__ == "__main__":
#     temp = EduPrograms()
#     temp.EduProgramInput()
#     temp.EduProgramDisplay()
#     FindByID = input ("Enter ID student who want to update: ")
#     temp.Update(FindByID)
#     print ("After updating: ")
#     temp.EduProgramDisplay()
#     FindByID = input ("Enter ID student who want to remove: ")
#     temp.Remove(FindByID)
#     temp.EduProgramDisplay()