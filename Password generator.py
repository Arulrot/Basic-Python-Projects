
import tkinter as tk
import rando
import string

def generate_password(length):

    if length.isdigit():
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(int(length)))
        return password
    else:
        return 'Invalid length'

def validate_length(text):

    if text == '':
        return True
    elif text.isdigit():
        return int(text) > 0
    else:
        return False

def invalid_length():
  
    label.config(text='Invalid length', fg='red')


window = tk.Tk()
window.title('Password Generator')
window.geometry('400x400')
window.configure(bg='#1a1a1a', padx=20, pady=20)


entry_label = tk.Label(window, text='Enter password length:', font=('Arial', 20), bg='#1a1a1a', fg='#f0f0f0')
entry_label.pack(side=tk.TOP, pady=10)


pass_entry = tk.Entry(window, width=20, font=('Arial', 20), bg='#1a1a1a', fg='#f0f0f0', textvariable="")
pass_entry.pack(side=tk.TOP, pady=10)


pass_entry.config(validate='focusout', validatecommand=(window.register(validate_length), '%P'), invalidcommand=invalid_length)


label = tk.Label(window, text='Password', font=('Arial', 20), bg='#1a1a1a', fg='#f0f0f0')
label.pack(side=tk.TOP, pady=10)


button = tk.Button(window, text='Generate Password', font=('Arial', 20), bg='#1a1a1a', fg='#f0f0f0', command=lambda: label.config(text=generate_password(pass_entry.get()), fg='#f0f0f0'))
button.pack(side=tk.TOP, pady=10)


window.mainloop()
