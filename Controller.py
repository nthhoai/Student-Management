"""
Controller Class: aim to to navigate functions and displays
--ATTRIBUTES: 
1. Education Program Management
2. Student Information Management
3. Academic Result Management
"""
#from Edu_Program_Management import EduPrograms
import Student_Info_Management as Stu
import Academic_Result_Management as Aca
import Edu_Program_Management as Edu

class MainController:
    Edu_Program_Management = Edu.EduPrograms()
    Student_Info_Management = Stu.Student_Infomation_Management()  
    #Academic_Result_Management = Aca.AcadResults(ListSub = Edu_Program_Management)

    def __init__(self):
        print ("Pass")

    #The view for Education Program Management module
    def View_Edu_Program_Management(self):
        while True: 
            print ("========== EDUCATION PROGRAM MANAGEMENT =========")
            print ("           1.  Enter the education program")
            print ("           2.  Show the education program")
            print ("           3.  Update the education program")
            print ("           4.  Remove the subject in the education program")
            print ("           0.  Cancel!")
            choice = int (input ("           Enter choice: "))
            if (choice == 1):
                self.Edu_Program_Management.EduProgramInput()
            if (choice == 2):
                self.Edu_Program_Management.EduProgramDisplay()
            if (choice == 3):
                Keyword = input ("           Enter code of subject: ")
                self.Edu_Program_Management.Update(Keyword)
            if (choice == 4):
                Keyword = input ("           Enter code of the subject which you want to remove: ")
                self.Edu_Program_Management.Remove(Keyword)
            if (choice == 0):
                break
                
    #The view for Detail Student Information Module
    def View_Detail_Student_Info(self):
        while True:
            print ("           1.  Contact student information")
            print ("           2.  Course student information")   
            print ("           0.  Cancel!")          
            choice = int ( input ("           Enter choice: "))
            if (choice == 1):
                Keyword = input ("Enter the ID student: ")
                self.Student_Info_Management.Student_Contact_Information_Management_Display(Keyword)
            if (choice == 2):
                Keyword = input ("Enter the ID student: ")
                self.Student_Info_Management.Student_Course_Information_Management_Display(Keyword) 
            if (choice == 0):
                break

    #The view for Student Information Management module
    def View_Student_Info_Management(self):
        while True:
            print ("========== STUDENT INFORMATION MANAGEMENT =========")
            print ("           1.  Enter the student information")
            print ("           2.  Show the student information") 
            print ("           3.  Update the student information")
            print ("           0.  Cancel!") 
            choice = int (input ("Enter choice: "))
            if (choice == 1):
                self.Student_Info_Management.Student_Infomation_Management_Input()
            if (choice == 2):
                self.Student_Info_Management.Student_Basic_Information_Mangement_Display()
                self.View_Detail_Student_Info()
            if (choice == 3):
                Keyword = input ("           Enter ID student who you want to update the information: ")
                self.Student_Info_Management.Update(Keyword)
            if (choice == 0):
                break
            
    


    #The view for Academic Result Management module
    def View_Academic_Result_Managment (self):
        self.Academic_Result_Management = Aca.AcadResults()
        while True:
            print ("========== ACADEMIC RESULT MANAGEMENT =========")
            print ("           1.  Enter the learning result information for student")
            print ("           2.  Show the learning result information by student ")  
            print ("           0.  Cancel!") 
            Choice = int (input ("           Enter choice: "))
            if (Choice == 1):
                self.Academic_Result_Management.AcadResultsInput(self.Edu_Program_Management, self.Student_Info_Management)
            if (Choice == 2):
                self.Academic_Result_Management.AcadResultsOverrallDisplay(self.Edu_Program_Management, self.Student_Info_Management)
            if (Choice == 0):
                break;

    
    #The controller: To direct
    def Main_Controller(self):
        while True:
            print ("========== EDUCATION SYSTEM MANAGEMENT =========")
            print ("           1.  Education Program Management")
            print ("           2.  Student Information Management")  
            print ("           3.  Academic Result Management")  
            print ("           0.  Exist!")
            Choice = int (input ("           Enter choice: "))
            if (Choice == 1):
                self.View_Edu_Program_Management()
            if (Choice == 2):
                self.View_Student_Info_Management()
            if (Choice == 3):
                self.View_Academic_Result_Managment()  
            if (Choice == 0):
                break                          
        
    
if __name__ == "__main__":
    temp = MainController()
    temp.Main_Controller()

            #Miss Manh Anh help me, so later I will consider. Grateful 
            # match choice:
            #     case 1: 
            #         self.Edu_Program_Management.EduProgramInput()
            #     case 2: 
            #         self.Edu_Program_Management.EduProgramDisplay()
