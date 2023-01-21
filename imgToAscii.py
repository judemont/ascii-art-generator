from tkinter import *
from PIL import Image
from array import *

def convert2D(liste):

    list2d =[]

    lines = []

    ii =0

    for i in liste:
   
        if ii >= im.width-1:
            ii=0
            list2d.append(lines)
            lines = []
        else:
            lines.append(i)
            #print(lines)
            ii+=1
    lines.append(i)
    list2d.append(lines)
    return list2d
    


    
        


        




img_filename = input("image path : ")
im = Image.open(img_filename).convert("1")



pixelles = convert2D(list(im.getdata()))
print(len(pixelles))

while len(pixelles) >= 10000:
    print(len(pixelles))
   





print(len(pixelles))
print(len(pixelles[0]))

result=""

test =0

for i in range(0, len(pixelles)):
    result += "\n"
    test=0
    
    for ii in range(0, len(pixelles[i])):
        
        if pixelles[i][ii] == 0:

            result += "ㅤㅤ"
            
        else:
            result += "▄▄"
        test+=1
       
    
    





root = Tk()
root.resizable(True, True)
root.title("ASCII art Generator")


root.geometry("700x350")



root.grid_columnconfigure(0, weight=500)
root.grid_rowconfigure(0, weight=500)


text = Text(root, height=im.height,wrap=NONE)
text.grid(row=0, column=0, sticky=EW)
text.config(font=('Helvetica bold',1))


scrollbarVert = Scrollbar(root, orient='vertical', command=text.yview)
scrollbarVert.grid(row=0, column=1, sticky=NS)


scrollbarHor = Scrollbar(root, orient='horizontal', command=text.xview)
scrollbarHor.grid(row=1, column=0, sticky=EW)

text['yscrollcommand'] = scrollbarVert.set
text['xscrollcommand'] = scrollbarHor.set




text.insert(1.0,result)

root.mainloop()