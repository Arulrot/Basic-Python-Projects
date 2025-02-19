import tkinter as tk

def NumberOfStrings():
    entered_text = textEntry.get('1.0','end-1c')
    count = 0
    for i in entered_text.strip():
        if i != ' ':
            count += 1
        else: continue
    outputLabel.configure(text='The number of string is: {}'.format(count))


def NumberOfWords():
    entered_text = textEntry.get('1.0','end-1c')
    count = 0
    for i in list(entered_text.strip().split(' ')):
        count +=1
    outputLabel.configure(text='The number of words are: {}'.format(count))
    

root = tk.Tk()
root.title('Number of string counter, excluding punctuations'.upper())
label1 = tk.Label(text='Enter the sentence in the text area below:', font=('Verdana', 16))
label1.pack()
textEntry = tk.Text(root)
textEntry.pack()
outputLabel = tk.Label(text='', font=('Verdana', 16))
outputLabel.pack()
countStringBtn = tk.Button(text='Count strings', font=('Verdana', 16), command=NumberOfStrings)
countStringBtn.pack()
countWordBtn = tk.Button(text='Count words', font=('Verdana', 16), command=NumberOfWords)
countWordBtn.pack()

root.mainloop()