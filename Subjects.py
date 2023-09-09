"""
Class Subjects: store the sucbject information including:
+ attributes: Code, Name, Credit, prerequisite courses code, department
+ methods: input, output, get-set
"""

class Subjects:
    #initialization function with parameter
    def __init__(self, code, name, credit, PreCourCode, Dep):
        self.Code = code
        self.Name = name
        self.Credit = credit
        self.PreCourCode = PreCourCode
        self.Dep = Dep

    #initialization function without parameter
    def __init__(self):
        self.Code = ""
        self.Name = ""
        self.Credit = ""
        self.PreCourCode = ""
        self.Dep = ""  

    #input function
    def SubjectInput(self):
        self.Code = input ("Enter Code: ")
        self.Name = input ("Enter Name: ")
        self.Credit = int (input ("Enter Number of credits: "))
        self.PreCourCode = input ("Enter Prerequisite course code: ")
        self.Dep = input ("Enter Department: ") 

    #Search the Subject function


    #Display function
    def SubjectDisplay(self):
        print ("{:<20}{:<20}{:<30}{:<30}{:<20}".format(self.Code, self.Name, self.Credit, self.PreCourCode, self.Dep))

    #Get Code Subject function
    def GetCode(self):
        return self.Code
    
    #Get Code Subject function
    def GetName(self):
        return self.Name
    
    #Get the number of Subject Credit 
    def GetCredit(self):
        return self.Credit


# if __name__ == "__main__":
#     temp = Subjects()
#     temp.SubjectInput()
#     temp.SubjectDisplay()
