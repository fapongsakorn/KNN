from tkinter import *
import KNN

root = Tk()
root.title('KNN Pongsakorn , Virust & Nopparat')
root.resizable(width=False, height=False)
frame = Frame(root)
frame.pack()

canvas = Canvas(frame, 
                bg="white", 
                width=800, 
                height=380)

canvas.pack()
def getKNN():
    K = k.get()
    HEIGHT = height.get()
    BRANCH = branch.get()
    TREE = tree.get()
    AGE = age.get()
    result  =KNN.knn (K,HEIGHT, BRANCH, TREE, AGE)

    txt.set(result)
    return result

txt = StringVar()
txt_label = Label(root,text="Quality =").place(x=15,y=320)
txt_disp =Entry(root,textvariable=txt,state=DISABLED).place(x=150, y=320)


name = Label(root,text="Growth of tree ").place(x=115,y=30)

table = PhotoImage(file="table.png")
canvas.create_image(550,150, image=table)

treeimg = PhotoImage(file="tree.png")
canvas.create_image(550,280, image=treeimg)

k = IntVar()
k_label = Label(root,text="K = ").place(x=15,y=70)
k_input = Entry(root, textvariable=k).place(x=150, y=70)
k.set('')

height = IntVar()
height_label = Label(root,text="HEIGHT = ").place(x=15,y=120)
height_input = Entry(root, textvariable=height).place(x=150, y=120)
height.set('')

branch = IntVar()
branch_label = Label(root,text="BRANCH DISTANCE = ").place(x=15,y=170)
branch_input = Entry(root, textvariable=branch).place(x=150, y=170)
branch.set('')

tree = IntVar()
tree_label = Label(root,text="TREE DIAMETER = ").place(x=15,y=220)
tree_input = Entry(root, textvariable=tree).place(x=150, y=220)
tree.set('')

age = IntVar()
age_label = Label(root,text="AGE = ").place(x=15,y=270)
age_input = Entry(root, textvariable=age).place(x=150, y=270)
age.set('')

btn = Button(root, text = 'Click Here !', bd = '10', command = getKNN)
btn.pack(side = 'bottom') 

root.mainloop()

