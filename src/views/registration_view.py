from tkinter import ttk, constants
import registration

class RegistrationView:
    def __init__(self, root, handle_view_login):
        self._root = root
        self._handle_view_login = handle_view_login
        self._frame = None
        
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _registration_handler(self):
        pw_value = self.password_entry.get()
        pw_verification_value = self.password_verification_entry.get()
        self.password_entry.delete(0, "end")
        self.password_verification_entry.delete(0, "end")
        print(f"Do the passwords match? { 'Yes' if registration.passwords_match(pw_value, pw_verification_value) else 'No' }")
        print(f"Is the password longer than 10 characters? {'Yes' if registration.check_password_length(pw_value) else 'No' }")
        print("----------")
        if registration.passwords_match(pw_value, pw_verification_value) and registration.check_password_length(pw_value):
            self._handle_view_login()
        else:
            foo = ttk.Label(master=self._frame, text="Passwords do not match or password is too short. Please choose retype the password or choose a stronger one.")
            foo.grid(row=6, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=10)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Set master password")
        password_label = ttk.Label(master=self._frame, text="Master password")
        self.password_entry = ttk.Entry(master=self._frame, show="*")
        password_verification_label = ttk.Label(master=self._frame, text="Verify master password")
        self.password_verification_entry = ttk.Entry(master=self._frame, show="*")
        button = ttk.Button(master=self._frame, text="Set", command=self._registration_handler)

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=10)
        password_label.grid(row=1, sticky=constants.W, padx=5)
        self.password_entry.grid(row=2, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_verification_label.grid(row=3, sticky=constants.W, padx=5, pady=5)
        self.password_verification_entry.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(row=5, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=10)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)

