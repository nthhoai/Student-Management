"""
Class PersonalInfor: store the student information including:
+ attributes: ID, fullname, gender, CID, StuClass
+ methods: input, output, get-set
"""

class PerInfo:
    #initialization function with parameter
    def __init__(self, ID, fullname, gender, CID, stuclass):
        self.ID = ID
        self.Fullname = fullname
        self.Gender = gender
        self.CID = CID
        self.StuClass = stuclass


    #initialization function without parameter
    def __init__(self):
        self.ID = ""
        self.Fullname = ""
        self.Gender = ""
        self.CID = ""
        self.StuClass = ""    

    #input function
    def PerInfoInput(self):
        self.ID = input ("Enter ID: ")
        self.Fullname = input ("Enter Fullname: ")
        self.Gender = input ("Enter Gender: ")
        self.CID = input ("Enter CID: ")
        self.StuClass = input("Enter Student class: ")

    def PerInfoDisplay(self):
        #print ("{:<15}{:<15}{:<15}{:<15}{:<15}".format("ID", "Fullname", "Gender", "CID", "Student Class"))
        print ("{:<15}{:<15}{:<15}{:<15}{:<15}".format(self.ID, self.Fullname, self.Gender, self.CID, self.StuClass))
        # print ("ID: ", self.ID)
        # print ("Fullname: ", self.Fullname)
        # print ("Gender: ", self.Gender)
        # print ("CID: ", self.CID)
        # print ("Student class: ", self.StuClass)


# if __name__ == "__main__":
#     temp = PerInfo()
#     temp.PerInfoInput()
#     temp.PerInfoDisplay()