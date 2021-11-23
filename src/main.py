from tkinter import Tk, ttk, constants
import registration

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        self.heading_label = ttk.Label(master=self._root, text="Set master password")
        self.password_label = ttk.Label(master=self._root, text="Master password")
        self.password_entry = ttk.Entry(master=self._root, show="*")
        self.password_verification_label = ttk.Label(master=self._root, text="Verify master password")
        self.password_verification_entry = ttk.Entry(master=self._root, show="*")
        self.button = ttk.Button(master=self._root, text="Set", command=self._handle_button_click)
        
        self.heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=10)
        self.password_label.grid(row=1, sticky=constants.W, padx=5)
        self.password_entry.grid(row=2, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self.password_verification_label.grid(row=3, sticky=constants.W, padx=5, pady=5)
        self.password_verification_entry.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        self.button.grid(row=5, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=10)

        self._root.grid_columnconfigure(1, weight=1, minsize=250)

    def _handle_button_click(self):
        pw_value = self.password_entry.get()
        pw_verification_value = self.password_verification_entry.get()
        print(f"Do the passwords match? { 'Yes' if registration.passwords_match(pw_value, pw_verification_value) else 'No' }")
        print(f"Is the password longer than 10 characters? {'Yes' if registration.passwords_match(pw_value, pw_verification_value) >= 10 else 'No' }")

def main():
    window = Tk()
    window.title('Much secrets..')

    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__=="__main__":
    main()