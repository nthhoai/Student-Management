"""
Class DetailResults: store the details of subject scores including:
+ attributes: final score, attendance score, test score 1, test score 2, discussion score
+ methods: input, output, get-set
"""

class DetailResults:
    #initialization function with parameter
    def __init__(self, attendance, test1, test2, discussion, final):
        self.Attendance = attendance
        self.Test1 = test1
        self.Test2 = test2
        self.Dicussion = discussion
        self.Final = final

    #initialization function without parameter
    def __init__(self):
        self.Attendance = ""
        self.Test1 = ""
        self.Test2 = ""
        self.Dicussion = ""
        self.Final = ""

    #input function
    def DetailResultsInput(self):
        self.Attendance = float (input ("Enter Attendance score: "))
        self.Test1 = float (input ("Enter Test 1 score: "))
        self.Test2 = float (input ("Enter Test 2 score: "))
        self.Dicussion = float (input ("Enter Discussion Score: "))
        self.Final = float (input ("Enter Final Exam Score: "))

    def DetailResultsDisplay(self):
        #print ("{:<20}{:<20}{:<20}{:<20}{:<20}".format("Attendance score", "Test 1 score", "Test 2 score", "Discussion Score", "Final Exam Score"))
        print ("{:<20}{:<20}{:<20}{:<20}{:<20}".format(self.Attendance, self.Test1, self.Test2, self.Dicussion, self.Final))

    def GetAttendance(self):
        return self.Attendance
    
    def GetTest1(self):
        return self.Test1
    
    def GetTest2(self):
        return self.Test2
    
    def GetDiscussion (self):
        return self.Dicussion
    
    def GetFinal (self):
        return self.Final


if __name__ == "__main__":
    temp = DetailResults()
    temp.DetailResultsInput()
    temp.DetailResultsDisplay()