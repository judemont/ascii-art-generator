#!/usr/bin/env python3
from tkinter import *
from PIL import Image
import os
from pathlib import Path
from tqdm import tqdm
import sys

def reduce_resolution(image_path, new_height):
    with Image.open(image_path) as img:
    
        width, height = img.size
        
        reduction_factor = new_height / height

        new_width = int(width * reduction_factor)

        img = img.resize((new_width, new_height), resample=Image.BOX)
       
        return img
    

def print_help():
    print("Usage: ascii-art-generator [image_path] [height] \n --help or -h for help")
    raise SystemExit()

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
    


    
if len(sys.argv) >= 2:
    if(sys.argv[1] == "--help" or sys.argv[1] == "-h"):
        print_help()
    else:
        if len(sys.argv) == 3:
            img_filename = os.path.abspath(sys.argv[1])
            img_height = int(sys.argv[2])

        else:
            print_help()
else:
    print_help()


#try:

im = reduce_resolution(img_filename, img_height).convert("L")



pixelles = convert2D(list(im.getdata()))


CHARS = ['ㅤㅤㅤ',  '+++', '***', '===', '%%%', '###', '@@@', '&&&', '$$$', 'MMM', 'WWW', '888', '▌▌▌', '▬▬▬', '▒▒▒', '███', '▓▓▓']



result=""

test =0

for i in tqdm( range(0, len(pixelles)), desc="Loading..."):
   

    result += "\n"
   

    
    for ii in range(0, len(pixelles[i])):
        result += CHARS[int(pixelles[i][ii]//(256/len(CHARS)))]
     





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
