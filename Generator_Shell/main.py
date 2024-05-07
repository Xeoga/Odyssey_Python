import customtkinter as cutk

cutk.set_appearance_mode("dark")
cutk.set_default_color_theme("blue")

app = cutk.CTk()
app.geometry("1100x1100")
app.title("Shell Generate V1")


def generate_listener_on(event):
    user_port_input = port_entry.get()
    print(f"nc -lvnp {user_port_input}")
    return f'nc -lvnp {user_port_input}'


# Create a frame 
main_frame = cutk.CTkFrame(master=app) 
main_frame.pack(pady=20,padx=40, fill='both',expand=True)
# Set the label inside the frame
main_label = cutk.CTkLabel(master=main_frame, text='Shell Generator', font=("Roboto", 32))
main_label.pack(pady=12,padx=10)
# Crează un frame interior în cadrul frame-ului exterior
ip_port_frame = cutk.CTkFrame(master=main_frame, corner_radius=10, width=400, height=400)
ip_port_frame.pack(side='left', pady=10,padx=10, anchor='ne', fill="x", expand=False)

ip_port_label = cutk.CTkLabel(master=ip_port_frame, text="IP & Port")
ip_port_label.pack()

ip_entry = cutk.CTkEntry(master=ip_port_frame, placeholder_text="Enter IP", width=200)
ip_entry.pack(side="right", padx=(10, 20), pady=10)
ip_entry.bind("<Return>")

port_entry = cutk.CTkEntry(master=ip_port_frame, placeholder_text="Port", width=200)
port_entry.pack(side="left", padx=(2, 10), pady=10)
port_entry.bind("<Return>", generate_listener_on)

listent_frame = cutk.CTkFrame(master=main_frame, corner_radius=10, width=400, height=40)
listent_frame.pack(side='top', padx=20, pady=20, fill="both", expand=False)

listent_label = cutk.CTkLabel(master=listent_frame, text="Listener")
listent_label.pack(pady=12, padx=10)

listent_entry = cutk.CTkEntry(master=listent_frame, placeholder_text=generate_listener_on, width=220)
listent_entry.pack()
# shell_frame = cutk.CTkFrame(master=main_frame, corner_radius=10)
# shell_frame.pack(padx=20, pady=20, fill="both", expand=True)

app.mainloop()
