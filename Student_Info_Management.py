"""
Student Information Management Class:
1. Personal Information: 
2. Contact information
3. Learning outcomes
"""


import PersonalInfo as Per
import ConInfo as Con
import CourseInfo as Cour

class Student_Infomation_Management:
    ListPer = []
    ListCont = []
    ListCourse = []


    #initiallization with the parameter
    def __init__ (self):
        self.Number = 0

    #The input function
    def Student_Infomation_Management_Input(self):
        self.Number = int (input ("Enter the number of student: "))
        for i in range (0, self.Number):
            #Personal Information
            PersonalInfo = Per.PerInfo()
            PersonalInfo.PerInfoInput()            
            self.ListPer.append(PersonalInfo)

            #Contact Information
            ContInfo = Con.ConInfo()
            ContInfo.ConInfoInput()
            self.ListCont.append(ContInfo)

            #Course Information
            CourInfo = Cour.CourInfo()
            CourInfo.CourInfoInput()
            self.ListCourse.append(CourInfo)
            
    # The search function: To find personal student information by ID
    def search(self, Keyword):
        for index in range (0, self.Number):
            self.PersonalInfo = self.ListPer[index]
            if (Keyword == self.PersonalInfo.ID):
                return [index, self.PersonalInfo]
        return False                
    
    #The basic display function of students: To display the basic student information
    def Student_Basic_Information_Mangement_Display(self):
        print ("=========== THE LIST OF STUDENT INFORMATION =========== ")
        print ("            1. To show Basic Information")
        print ("{:<15}{:<15}{:<15}{:<15}{:<15}".format("ID", "Fullname", "Gender", "CID", "Student Class"))
        for index in range (0, self.Number):
            self.ListPer[index].PerInfoDisplay()

    #The contact display function: To display the contact student information
    def Student_Contact_Information_Management_Display(self, Keyword):
        Check = self.search(Keyword)
        if (Check == False):
            print ("ID is not appropriate!")
        else:
            index = Check[0]
            self.ContInfo = self.ListCont[index]
            self.ContInfo.ConInfoDisplay()

    #The Course display function: To display the course student information
    def Student_Course_Information_Management_Display(self, Keyword):
        Check = self.search(Keyword)
        if (Check == False):
            print ("ID is not appropriate!")
        else:
            index =  Check[0]
            self.CourInfo = self.ListCourse[index]
            print (self.CourInfo)            
            self.CourInfo.CourInfoDisplay()            


    # The update function: To update personal student information: Find student by ID --> UPDATE
    def Update(self, Keyword):
        Check = self.search(Keyword)
        if (Check == False):
            print ("ID is not appropriate!")  
        else:
            Check[1].PerInfoInput()
            self.ContInfo.ConInfoInput()
            self.CourInfo.CourInfoInput()
            Verify = int (input ("Enter 1 to update successully: "))
            if (Verify == 1):
                # get index of the element finded
                index = Check[0] 
                self.ListPer[index] = Check[1]
                self.ListCont[index] = self.ContInfo
                self.ListCourse[index] = self.CourInfo
                print ("Update Successfully!")
            else:
                print ("Do not update information!")

# if __name__ == "__main__":
#     SIM = Student_Infomation_Management()
#     SIM.Student_Infomation_Management_Input()
#     SIM.Student_Information_Mangement_Display()
#     FindByID = input ("Enter ID student who want to search: ")
#     SIM.Update(FindByID)
#     print ("========== After updating ============")
#     SIM.Student_Information_Mangement_Display()

        




        

        

    






