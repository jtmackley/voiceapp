import sys
from PyQt4 import QtGui, QtCore
import subprocess


#        for row, category in enumerate(categories):
#            button = QtGui.QPushButton(category.word)
#            self.buttonCategories.append(button)
#            font=QtGui.QFont('Arial',16)
#            button.setFont(font)
#            button.clicked.connect(self.CategoryClicked)            
#            grid.addWidget(button, row,1)

class VoiceApp():
    def GetCategories(self):
        categories=[]
        category = Categories()
        category.word="General"
        category.words=["Yes","No","Please","Thankyou","","","","","","","",""]
        categories.append(category)

        category = Categories()
        category.word="Numbers"
        category.words=["0","1","2","3","4","5","6","7","8","9","10","100"]
        categories.append(category)

        category = Categories()
        category.word="Food"
        category.words=["More","Finished","Hot","Cold","","","","","","","",""]
        categories.append(category)

        category = Categories()
        category.word="Bathroom"
        category.words=["","","","","","","","","","","",""]
        categories.append(category)

        category = Categories()
        category.word="Sleep"
        category.words=["Tired","Upstairs","Downstairs","","","","","","","","",""]
        categories.append(category)

        category = Categories()
        category.word=""
        category.words=["","","","","","","","","","","",""]
        categories.append(category)

        category = Categories()
        category.word=""
        category.words=["","","","","","","","","","","",""]
        categories.append(category)

        return categories

class Categories():
    def __init__(self):
        self.word=""
        self.words=[]

class TalkBoard(QtGui.QWidget):
    
    def __init__(self):
        super(TalkBoard, self).__init__()
        self.voiceapp=VoiceApp()
        self.buttonCategories=[]
        self.buttonWords=[]
        self.buttonPredictive=[]
        self.buttonTextArea=[]
        self.categories=[]
        self.editmode=False
        self.text=QtGui.QTextEdit()
        self.initUI()

    def drawCategoryButtons(self,grid):
        vbox = QtGui.QVBoxLayout()
        for i in range(7):
            button = QtGui.QPushButton("")
            font=QtGui.QFont('Arial',20)
            button.setFont(font)
            button.clicked.connect(self.CategoryClicked)            
            vbox.addWidget(button)
            self.buttonCategories.append(button)
        grid.addLayout(vbox, 0,0,7,1)
        return True
    def PopulateCategories(self):
        x=0
        for button in self.buttonCategories:
            if x<len(self.categories):
                button.setText(self.categories[x].word)
            else:
                button.setText("")
            x+=1

    def drawWordButtons(self,grid):
        for i in range(4):
            for j in range(1,4):
                button = QtGui.QPushButton("Word")
                font=QtGui.QFont('Arial',16)
                button.setFont(font)
                button.clicked.connect(self.WordClicked)            
                grid.addWidget(button, i,j)
                self.buttonWords.append(button)

        return True

    def PopulateWords(self,category):
        # Find the category
        for cat in self.categories:
            if cat.word==category:
                x=0
                for button in self.buttonWords:
                    if x<len(cat.words):
                        button.setText(cat.words[x])
                    else:
                        button.setText("")
                    x+=1

    def drawPredictiveButtons(self,grid):
        # Add Vbox spanning 
        hbox = QtGui.QHBoxLayout()
        for i in range(6):
            button = QtGui.QPushButton("Pred"+str(i))
            font=QtGui.QFont('Arial',12)
            button.setFont(font)
            hbox.addWidget(button)
        grid.addLayout(hbox, 4,1,1,3)
        return True
    def drawTextAreaButtons(self,grid):
        grid.addWidget(self.text, 5,1,1,3)        
        hbox = QtGui.QHBoxLayout()
        button = QtGui.QPushButton("Edit")
        button.clicked.connect(self.ToggleEdit)            
        font=QtGui.QFont('Arial',12)
        button.setFont(font)
        hbox.addWidget(button)
        hbox.addStretch(1)
        button = QtGui.QPushButton("Clear")
        button.clicked.connect(self.ClearText)            
        font=QtGui.QFont('Arial',12)
        button.setFont(font)
        hbox.addWidget(button)
        #button = QtGui.QPushButton("Copy")
        #font=QtGui.QFont('Arial',12)
        #button.setFont(font)
        #hbox.addWidget(button)
        #button = QtGui.QPushButton("Paste")
        #font=QtGui.QFont('Arial',12)
        #button.setFont(font)
        #hbox.addWidget(button)
        hbox.addStretch(1)
        button = QtGui.QPushButton("Say")
        font=QtGui.QFont('Arial',12)
        button.setFont(font)
        button.clicked.connect(self.SayText)            
        hbox.addWidget(button)
        grid.addLayout(hbox, 6,1,1,3)
        return True

    def GetNewText(self):
        text, ok = QtGui.QInputDialog.getText(self, 'New Word', 
            'Enter the new word:')
        if ok:
            return str(text)
        else:
            return False

    def initUI(self):      

        # Load Categories
        self.categories=self.voiceapp.GetCategories()

        grid = QtGui.QGridLayout()
        grid.setSpacing(24)
        self.setLayout(grid)

        self.drawCategoryButtons(grid)
        self.drawWordButtons(grid)
        self.drawPredictiveButtons(grid)        
        self.drawTextAreaButtons(grid)

        self.PopulateCategories()
        self.PopulateWords(self.categories[0].word)
        
        #self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Voice App')
        self.show()
        
    def CategoryClicked(self):
        if self.editmode:
            new=self.GetNewText()
            if new:
                self.sender().setText(new)
        else:
            cat=str(self.sender().text())
            if len(cat):
                self.PopulateWords(cat)
                sp="echo " + cat + " | festival --tts &"
                print sp
                subprocess.call(sp, shell=True)

    def WordClicked(self):
        if self.editmode:
            new=self.GetNewText()
            if new:
                self.sender().setText(new)
        else:
            word=str(self.sender().text())
            if len(word):
                self.text.insertPlainText(" " + word)
                sp="echo " + word + " | festival --tts &"
                print sp
                subprocess.call(sp, shell=True)

    def ToggleEdit(self):
        editmode=str(self.sender().text())
        if editmode=="Edit":
            self.editmode=True
            for button in self.buttonCategories:
                button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
            for button in self.buttonWords:
                button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
            self.sender().setText("Done")
        else:
            self.editmode=False
            for button in self.buttonCategories:
                button.setStyleSheet("")
            for button in self.buttonWords:
                button.setStyleSheet("")
            self.sender().setText("Edit")

    def SayText(self):
        text=str(self.text.toPlainText())
        if len(text):
            sp="echo " + text + " | festival --tts &"
            print sp
            subprocess.call(sp, shell=True)

    def ClearText(self):
        self.text.clear()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = TalkBoard()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
