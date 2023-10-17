from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

class MyGUI:

    def __init__(self):
        self.mainWindow = Tk()
        self.windowWidth = 700
        self.windowHeight = 220 # variable to resize window height
        self.mainWindow.geometry(f"700x{self.windowHeight}+720+50")
        self.mainWindow.title("GPA Calculator")
        self.gradeValue = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
        self.frame1 = Frame(self.mainWindow, width=520, height=30, bg="#d2302c")
        self.frame1.place(x=20, y=30)
        self.frame2Height = 100 # variable to resize frame2 height
        self.frame2 = Frame(self.mainWindow, width=520, height=self.frame2Height, bg="#f4a896")
        self.frame2.place(x=20, y=60)
        self.frame3 = Frame(self.mainWindow, width=100, height=180)
        self.frame3.place(x=560, y=30)
    
        self.courseLabel = Label(self.frame1, text="Course", font=14, fg="white", bg="#d2302c")
        self.courseLabel.place(x=10, y=5)
        self.gradeLabel = Label(self.frame1, text="Grade", font=14, fg="white", bg="#d2302c")
        self.gradeLabel.place(x=113, y=5)
        self.includeLabel = Label(self.frame1, text="Included", font=14, fg="white", bg="#d2302c")
        self.includeLabel.place(x=180, y=5)
        self.courseLabel2 = Label(self.frame1, text="Course", font=14, fg="white", bg="#d2302c")
        self.courseLabel2.place(x=280, y=5)
        self.gradeLabel2 = Label(self.frame1, text="Grade", font=14, fg="white", bg="#d2302c")
        self.gradeLabel2.place(x=383, y=5)
        self.includeLabel2 = Label(self.frame1, text="Included", font=14, fg="white", bg="#d2302c")
        self.includeLabel2.place(x=450, y=5)
        
        self.choice=StringVar()
        self.choice.set("RED")
        
        self.rb1=Radiobutton(self.frame3, text="Red", font=14, variable=self.choice, value="RED", command=self.changeBgr)
        self.rb1.place(x=10, y=70)
        self.rb2=Radiobutton(self.frame3, text="Green", font=14, variable=self.choice, value="GREEN", command=self.changeBgg)
        self.rb2.place(x=10, y=100)
        self.rb3=Radiobutton(self.frame3, text="Blue", font=14, variable=self.choice, value="BLUE", command=self.changeBgb)
        self.rb3.place(x=10, y=130)

        
        
        self.course = Entry(self.frame2, width=10, bg="#f4a896", fg="black")
        self.course.place(x=10, y=5)
        self.grade = ttk.Combobox(self.frame2, values=self.gradeValue, width=3)
        self.grade.place(x=113, y=5)
        self.grade.set(self.gradeValue[0])
        self.include=IntVar()
        self.include.set(1)
        self.cb = Checkbutton(self.frame2, width=3, variable=self.include, font=14, bg="#f4a896")
        self.cb.place(x=195, y=5)
        
        '''self.course2 = Entry(self.frame2, width=10, bg="#f4a896", fg="black")
        self.course2.place(x=280, y=5)
        self.grade2 = ttk.Combobox(self.frame2, values=self.gradeValue, width=3)
        self.grade2.place(x=383, y=5)
        self.grade2.set(self.gradeValue[0])
        self.include2=IntVar()
        self.include2.set(1)
        self.cb2 = Checkbutton(self.frame2, width=3, variable=self.include, font=14, bg="#f4a896")
        self.cb2.place(x=470, y=5)'''
        
        

        
        self.addCourseButton = Button(self.frame3, text="Add Course", font=("Arial", 14), width=7, command=self.addCourse)
        self.addCourseButton.place(x=10, y=10)
        self.calculateButton = Button(self.frame3, text="Calculate", font=("Arial", 14), width=7, command=self.calculateGPA)
        self.calculateButton.place(x=10, y=40)
        
        # to give different value to each new inputs
        self.gradeList = [self.grade]
        self.includeList = [self.include]
        self.courseList = [self.course]
        self.cbList = [self.cb]

        self.newPos = 5 # variable to display new inputs
        self.checkBg = 0 # check background color
        self.courseNum = 1
    def changeBgr(self): # change background red
        self.frame1.config(bg="#d2302c")
        self.frame2.config(bg="#f4a896")
        self.course.config(bg="#f4a896")
        self.cb.config(bg="#f4a896")
        self.courseLabel.config(bg="#d2302c")
        self.gradeLabel.config(bg="#d2302c")
        self.includeLabel.config(bg="#d2302c")
        self.courseLabel2.config(bg="#d2302c")
        self.gradeLabel2.config(bg="#d2302c")
        self.includeLabel2.config(bg="#d2302c")
        
        
        for i in self.courseList:
            i.config(bg="#f4a896")
        for i in self.cbList:
            i.config(bg="#f4a896")
        self.checkBg = 0
        
        
    def changeBgg(self): # change background green
        self.frame1.config(bg="#17553b")
        self.frame2.config(bg="#ced46a")
        self.course.config(bg="#ced46a")
        self.cb.config(bg="#ced46a")
        self.courseLabel.config(bg="#17553b")
        self.gradeLabel.config(bg="#17553b")
        self.includeLabel.config(bg="#17553b")
        self.courseLabel2.config(bg="#17553b")
        self.gradeLabel2.config(bg="#17553b")
        self.includeLabel2.config(bg="#17553b")

        for i in self.courseList:
            i.config(bg="#ced46a")
        for i in self.cbList:
            i.config(bg="#ced46a")
        self.checkBg = 1
    
    def changeBgb(self): # change background blue
        self.frame1.config(bg="#1663b2")
        self.frame2.config(bg="#9cc3d5")
        self.course.config(bg="#9cc3d5")
        self.cb.config(bg="#9cc3d5")
        self.courseLabel.config(bg="#1663b2")
        self.gradeLabel.config(bg="#1663b2")
        self.includeLabel.config(bg="#1663b2")
        self.courseLabel2.config(bg="#1663b2")
        self.gradeLabel2.config(bg="#1663b2")
        self.includeLabel2.config(bg="#1663b2")

        for i in self.courseList:
            i.config(bg="#9cc3d5")
        for i in self.cbList:
            i.config(bg="#9cc3d5")
        self.checkBg = 2
    
    def addCourse(self):
        # to resize frames
        if self.courseNum % 2 == 1:
            self.frame2Height += 25
        self.courseNum += 1
        if self.frame2Height >= self.windowHeight - 50:
            self.windowHeight += 25
            self.frame2.config(height=self.frame2Height - 50)
            self.mainWindow.geometry(f"700x{self.windowHeight + 25}+720+50")
            
            
        if self.courseNum == 51:
            showerror("ERROR", "TOO MANY COURSES")
        else:
            self.newCourse = Entry(self.frame2, width=10, fg="black")
            self.courseList.append(self.newCourse)
            self.newGrade = ttk.Combobox(self.frame2, values=self.gradeValue, width=3)
            self.newGrade.set(self.gradeValue[0])
            self.gradeList.append(self.newGrade)
            self.newInclude=IntVar()
            self.newInclude.set(1)
            self.includeList.append(self.newInclude)
            self.newCb = Checkbutton(self.frame2, width=3, variable=self.newInclude, font=14)
            self.cbList.append(self.newCb)
        
            if self.courseNum % 2 == 1:
                self.newCourse.place(x=10, y=self.newPos)
                self.newGrade.place(x=113, y=self.newPos)
                self.newCb.place(x=195, y=self.newPos)
            else:
                self.newCourse.place(x=280, y=self.newPos)
                self.newGrade.place(x=383, y=self.newPos)
                self.newCb.place(x=470, y=self.newPos)
        
       
        
        
        if self.checkBg == 0:
            for i in self.courseList:
                i.config(bg="#f4a896")
            for i in self.cbList:
                i.config(bg="#f4a896")

        elif self.checkBg == 1:
            for i in self.courseList:
                i.config(bg="#ced46a")
            for i in self.cbList:
                i.config(bg="#ced46a")
         
        elif self.checkBg == 2:
            for i in self.courseList:
                i.config(bg="#9cc3d5")
            for i in self.cbList:
                i.config(bg="#9cc3d5")
        
        if self.courseNum % 2 == 0:
            self.newPos += 25
        
            


    def calculateGPA(self):
        i = 0
        j = 0
        total = 0 # sum of all (grade * 3)
        checkCheckedBox = 0 # variable to check whether checkbox checked
        self.convertList = [] # list converted letter to number

        for grades in self.gradeList:
            grades = self.gradeList[i].get() 
            self.error = False 
            if grades == "A+":
                self.convertList.append(4.33 * 3)
            elif grades == "A":
                self.convertList.append(4.0 * 3)
            elif grades == "A-":
                self.convertList.append(3.67 * 3)
            elif grades == "B+":
                self.convertList.append(3.33 * 3)
            elif grades == "B":
                self.convertList.append(3.0 * 3)
            elif grades == "B-":
                self.convertList.append(2.67 * 3)
            elif grades == "C+":
                self.convertList.append(2.33 * 3)
            elif grades == "C":
                self.convertList.append(2.0 * 3)
            elif grades == "C-":
                self.convertList.append(1.67 * 3)
            elif grades == "D":
                self.convertList.append(1.0 * 3)
            elif grades == "F":
                self.convertList.append(0)
            else:
                showerror("ERROR", "Wrong Input")
                self.error = True
                break
 

            i += 1
        for includes in self.convertList:
            if self.includeList[j].get():
                total += self.convertList[j]
                checkCheckedBox += 1 
            j += 1
        finalTotal = format((total / (checkCheckedBox * 3)), ',.2f') # round up 2 decimal points
        if self.error == False: # if error, shouldn't be displayed
            showinfo("Result", "GPA : " + finalTotal)
            

my_gui = MyGUI()