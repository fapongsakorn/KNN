from tkinter import *
from PIL import Image, ImageTk
import KNN

root = Tk()
root.title('KNN Pongsakorn , Virust & Nopparat')
root.resizable(width=False, height=False)
frame = Frame(root)
frame.pack()

canvas = Canvas(frame, 
                bg="white", 
                width=300, 
                height=300)
canvas.pack()
def getKNN():
    K = k.get()
    HEIGHT = height.get()
    BRANCH = branch.get()
    TREE = tree.get()
    AGE = age.get()
    testset = [[HEIGHT, BRANCH, TREE, AGE]]
    test = pd.DataFrame(Testset)
    result,neigh = knn(data, test, K)
    res.set(result)
    neig.set(neigh)

K = IntVar()
K_label = Label(root,text="K = ").place(x=15,y=20)
K_input = Entry(root, textvariable=K).place(x=50, y=20)
K.set('')

HEIGHT = IntVar()
HEIGHT_label = Label(root,text="HEIGHT = ").place(x=15,y=70)
HEIGHT_input = Entry(root, textvariable=HEIGHT).place(x=100, y=70)
HEIGHT.set('')

BRANCH = IntVar()
BRANCH_label = Label(root,text="BRANCH = ").place(x=15,y=120)
BRANCH_input = Entry(root, textvariable=BRANCH).place(x=100, y=120)
BRANCH.set('')

TREE = IntVar()
TREE_label = Label(root,text="TREE = ").place(x=15,y=170)
TREE_input = Entry(root, textvariable=TREE).place(x=100, y=170)
TREE.set('')

AGE = IntVar()
AGE_label = Label(root,text="AGE = ").place(x=15,y=220)
AGE_input = Entry(root, textvariable=AGE).place(x=100, y=220)
AGE.set('')

btn = Button(root, text = 'Click Here !', bd = '10',
                          command = root.destroy)
btn.pack(side = 'left') 


root.mainloop()
