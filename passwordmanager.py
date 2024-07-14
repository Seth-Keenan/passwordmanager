import tkinter as tk

def login_window():
    admin_window = tk.Tk()
    admin_window.geometry("400x200")
    admin_window.configure(bg="#333333")
    admin_window.rowconfigure((0,5), weight=1)
    admin_window.columnconfigure((0,2), weight=1)

    userlabel = tk.Label(admin_window, text="Username:", font=("Helvetica", 22, "bold"), bg="#333333", fg="white")
    userlabel.grid(row=1, column=1, pady=5, padx=5, sticky="NESW")

    userEntry = tk.Entry(admin_window)
    userEntry.grid(row=2, column=1, pady=5, padx=5, sticky="NESW")

    passlabel = tk.Label(admin_window, text="Password:", font=("Helvetica", 22, "bold"), bg="#333333", fg="white")
    passlabel.grid(row=3, column=1, pady=5, padx=5, sticky="NESW")

    passEntry = tk.Entry(admin_window)
    passEntry.grid(row=4, column=1, pady=5, padx=5, sticky="NESW")

    admin_window.mainloop()

def main():
    login_window()

if __name__ == "__main__":
    main()