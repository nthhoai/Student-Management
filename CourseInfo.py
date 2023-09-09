"""
Class Course Infor: store the course information including:
+ attributes: Name, Training forms, Consultant, PhoneCons
+ methods: input, output, get-set
"""

class CourInfo:
    #initialization function with parameter
    def __init__(self, name, forms, consultant, phonecons):
        self.Name = name
        self.Forms = forms
        self.Consultant = consultant
        self.PhoneCons = phonecons


    #initialization function without parameter
    def __init__(self):
        self.Name = ""
        self.Forms = ""
        self.Consultant = ""
        self.PhoneCons = ""    

    #input function
    def CourInfoInput(self):
        self.Name = input ("Enter Course Name: ")
        self.Forms = input ("Enter Forms: ")
        self.Consultant = input ("Enter Consultant Name: ")
        self.PhoneCons = input ("Enter Phone consultant: ")

    #display function
    def CourInfoDisplay(self):
        print ("{:<20}{:<20}{:<20}{:<20}".format("Name", "Forms", "Consultant", "Phone Consultant"))
        print ("{:<20}{:<20}{:<20}{:<20}".format(self.Name, self.Forms, self.Consultant, self.PhoneCons))



# if __name__ == "__main__":
#     temp = CourInfo()
#     temp.CourInfoInput()
#     temp.CourInfoDisplay()