from tkinter import ttk, constants
from services.logins_service import LoginService


class ItemView:
    def __init__(self, root, handle_view_list, prefill=None):
        self._root = root
        self._prefilled = prefill
        self._frame = None
        self._handle_view_list = handle_view_list
        self._login_service = LoginService()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _save_click(self):
        site_entry = self.site_entry.get()
        email_entry = self.email_entry.get(
        ) if self.email_entry.get() != "" else None
        username_entry = self.username_entry.get(
        ) if self.username_entry.get() != "" else None
        password_entry = self.password_entry.get()

        if self._login_service.process_save(
            website=site_entry,
            username=username_entry,
            email=email_entry,
            password=password_entry
        ):
            self._handle_view_list()
        else:
            msg = "Validation failed. "
            msg += "Website and password are required. "
            msg += "Either a username or email is also required.\n"
            msg += "Minimun character lengths are: website: 4, username: 2, email: 8, password: 1."
            error_msg = ttk.Label(master=self._frame, text=msg)
            error_msg.grid(
                row=10, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=10)

    def _cancel_click(self):
        self.site_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self._handle_view_list()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        site_label = ttk.Label(master=self._frame, text="Website:")
        self.site_entry = ttk.Entry(master=self._frame)
        email_label = ttk.Label(master=self._frame, text="Email:")
        self.email_entry = ttk.Entry(master=self._frame)
        username_label = ttk.Label(master=self._frame, text="Username:")
        self.username_entry = ttk.Entry(master=self._frame)
        password_label = ttk.Label(master=self._frame, text="Password:")
        self.password_entry = ttk.Entry(master=self._frame)
        save_button = ttk.Button(
            master=self._frame, text="Add", command=self._save_click)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._cancel_click)

        if self._prefilled:
            self.site_entry.insert(0, self._prefilled.website)
            self.email_entry.insert(0, self._prefilled.email)
            self.username_entry.insert(0, self._prefilled.username)
            self.password_entry.insert(0, self._prefilled.password)

        site_label.grid(row=0, sticky=constants.W, padx=5)
        self.site_entry.grid(row=1, column=0, columnspan=2,
                             sticky=(constants.E, constants.W), padx=5, pady=5)
        email_label.grid(row=2, sticky=constants.W, padx=5)
        self.email_entry.grid(row=3, column=0, columnspan=2,
                              sticky=(constants.E, constants.W), padx=5, pady=5)
        username_label.grid(row=4, sticky=constants.W, padx=5)
        self.username_entry.grid(row=5, column=0, columnspan=2,
                                 sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=6, sticky=constants.W, padx=5)
        self.password_entry.grid(row=7, column=0, columnspan=2,
                                 sticky=(constants.E, constants.W), padx=5, pady=5)
        save_button.grid(row=8, column=0, columnspan=2,
                         sticky=(constants.E, constants.W), padx=5, pady=10)
        cancel_button.grid(row=9, column=0, columnspan=2,
                           sticky=(constants.E, constants.W), padx=5, pady=10)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)
