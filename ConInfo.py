"""
Class ContactInfor: store the contact student information including:
+ attributes: Nation, Province, District, Phone, Email
+ methods: input, output, get-set
"""


class ConInfo:
    #initialization function with parameter
    def __init__(self, nation, province, district, phone, email):
        self.Nation = nation
        self.Province = province
        self.District = district
        self.Phone = phone
        self.Email = email


    #initialization function without parameter
    def __init__(self):
        self.Nation = ""
        self.Province = ""
        self.District = ""
        self.Phone = ""
        self.Email = ""

    #input function
    def ConInfoInput(self):
        self.Nation = input ("Enter Nation: ")
        self.Province = input ("Enter Province: ")
        self.District = input ("Enter District: ")
        self.Phone = input ("Enter Phone: ")
        self.Email = input("Enter Email: ")

    def ConInfoDisplay(self):
        print ("{:<15}{:<15}{:<15}{:<15}{:<15}".format("Nation", "Province", "District", "Phone", "Email"))
        print ("{:<15}{:<15}{:<15}{:<15}{:<15}".format(self.Nation, self.Province, self.District, self.Phone, self.Email))



# if __name__ == "__main__":
#     temp = ConInfo()
#     temp.ConInfoInput()
#     temp.ConInfoDisplay()