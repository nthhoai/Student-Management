"""
Class Academic Results: store the academic result information including:
+ attributes: school year, semester, the code of subject, list of student who learn this subject, 10-point scale, 4-point scale,  letter grading scale
+ methods: input, output, get-set
"""
import math
from Edu_Program_Management import *
from DetailResults import * 
from Student_Info_Management import *

ListSub = EduPrograms()
ListStudents = Student_Infomation_Management()

class AcadResults:

    #ListSub = EduPrograms()
    #ListSub.EduProgramInput()
    DetailResults =   DetailResults()
    #initialization function with parameter
    #code, name, credit, PreCourCode, Dep
    def __init__(self, SchoYear, semester, ListSub, TenPointScale, FourPointScale, LetterGScale):
        self.SchoYear = SchoYear
        self.Semester = semester
        self.EduPrograms = ListSub
        self.TenPointScale = TenPointScale
        self.FourPointScale = FourPointScale


    #initialization function without parameter
    def __init__(self):
        self.SchoYear = ""
        self.Semester = ""
        self.Subject = Subjects()
        self.EduPrograms = EduPrograms()
        self.TenPointScale = ""
        self.FourPointScale = ""
        self.LetterGScale = ""


    #input function
    def AcadResultsInput(self, ListSub, ListStudents):
        self.SchoYear = input ("Enter School year: ")
        self.Semester = input ("Enter Semester: ")
        keyword = input ("Enter the code of subject: ")
        #Check the code of subject
        self.check = ListSub.Search(keyword)
        while (self.check == False):
            keyword = input ("Enter the Code of Subject Again: ")
            check = ListSub.Search(keyword)
        for index in range (0, len(ListStudents.ListPer)):
            print ("Enter the score for student: (ID)", ListStudents.ListPer[index].ID)
            self.DetailResults.DetailResultsInput()
            self.Calculate_Ten_Point_Scale()
            self.Calculate_Four_Point_Scale()                


    #Caculate the 10 point scale
    def Calculate_Ten_Point_Scale(self):
        if (self.check[1].GetCredit() == 2):
            self.TenPointScale = self.DetailResults.GetAttendance() * 0.1 + (self.DetailResults.GetTest1() + self.DetailResults.GetDiscussion() * 2) / 3 * 0.3 + self.DetailResults.GetFinal() * 0.6
        else: 
            self.TenPointScale = self.DetailResults.GetAttendance() * 0.1 + (self.DetailResults.GetTest1() + self.DetailResults.GetTest2() + self.DetailResults.GetDiscussion() * 2) / 4 * 0.3 + self.DetailResults.GetFinal() * 0.6


    #Caculate the 4 point scale
    def Calculate_Four_Point_Scale(self):
        if (self.TenPointScale > 8.5):
            self.FourPointScale = 4
            self.LetterGScale = "A"

        if (self.TenPointScale > 7.5):
            self.FourPointScale = 3.5
            self.LetterGScale = "B"

        if (self.TenPointScale > 6.5):
            self.FourPointScale = 3
            self.LetterGScale = "C"

        if (self.TenPointScale > 5):
            self.FourPointScale = 2.5
            self.LetterGScale = "D"


        else:
            self.FourPointScale = 2
            self.LetterGScale = "F"




    #Display the Results 
    def AcadResultsOverrallDisplay(self, ListSub, ListStudents):
        print ("            School Year: ", self.SchoYear)
        print ("            School Year: ", self.Semester)
        print ("            The code of subject: ", self.check[1].GetCode())
        print ("            The Subject name: ", self.check[1].GetName())
        for index in range (0, len (ListStudents.ListPer)): 
            print ("{:<20}{:<20}{:<20}{:<20}".format("ID Student", "10-point scale", "4-point scale",  "letter grading scale"))
            print ("{:<20}{:<20}{:<20}{:<20}".format(ListStudents.ListPer[index].ID, self.TenPointScale, self.FourPointScale, self.LetterGScale))


    def AcadResultsDetailDisplay(self):
        print ("Show detail score: ")
        self.DetailResults.DetailResultsDisplay()

    

  


#if __name__ == "__main__":
    # ListSub = EduPrograms()
    # ListSub.EduProgramInput()
    # temp = AcadResults()
    # temp.AcadResultsInput()
    # temp.Calculate_Ten_Point_Scale()
    # temp.Calculate_Four_Point_Scale()
    # choice = int (input("Do you want to show detail score, Please enter 1!"))
    # if (choice == 1):
    #     temp.DetailResults.DetailResultsDisplay()
    # else:
    #     print ("NO")
    # temp.AcadResultsOverrallDisplay()
    # print ("The number of accumulated credit: ", temp.AccumulatedCredit)
    # print ("The number of accumulated GPA: ", temp.FourPointScale)
