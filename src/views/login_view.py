from tkinter import ttk, constants
from services.user_service import UserService


class LoginView:
    def __init__(self, root, handle_login):
        self._root = root
        self._handle_login = handle_login
        self._frame = None
        self.user_login = UserService()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        if self.user_login.login_succesfull(self.password_entry.get()):
            self._handle_login()
        else:
            error_msg = ttk.Label(master=self._frame,
                                  text="Wrong password. Please try again..")
            error_msg.grid(
                row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=10)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Login")
        password_label = ttk.Label(master=self._frame, text="Password")
        self.password_entry = ttk.Entry(master=self._frame, show="*")
        button = ttk.Button(master=self._frame, text="Login",
                            command=self._login_handler)

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=10)
        password_label.grid(row=1, sticky=constants.W, padx=5)
        self.password_entry.grid(
            row=2, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(
            row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=10)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
