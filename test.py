import sys
from PyQt4 import QtGui, QtCore

def GetCategories():
    categories=[]
    category = Categories()
    category.word="General"
    category.words.append("Yes")
    category.words.append("No")
    category.words.append("Please")
    category.words.append("Thankyou")
    categories.append(category)

    category = Categories()
    category.word="Food"
    category.words.append("More")
    category.words.append("Finished")
    category.words.append("Hot")
    category.words.append("Cold")
    categories.append(category)

    category = Categories()
    category.word="Bathroom"
    category.words.append("Option1")
    category.words.append("Option2")
    categories.append(category)

    category = Categories()
    category.word="Sleep"
    category.words.append("Tired")
    category.words.append("Upstairs")
    category.words.append("Downstairs")
    categories.append(category)

    return categories

class Categories():
    def __init__(self):
        self.word=""
        self.words=[]

class TalkBoard(QtGui.QWidget):
    
    def __init__(self):
        super(TalkBoard, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        # Load Categories
        categories=GetCategories()

        grid = QtGui.QGridLayout()
        self.setLayout(grid)

        for row, category in enumerate(categories):
            button = QtGui.QPushButton(category.word)
            button.clicked.connect(self.buttonClicked)            
            grid.addWidget(button, row,1)
            

        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()
        
    def buttonClicked(self):
      
        sender = self.sender()
        print sender.text() + ' was pressed'
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = TalkBoard()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()