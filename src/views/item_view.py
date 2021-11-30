from tkinter import ttk, constants

class ItemView:
    def __init__(self, root, handle_view_list, prefill=None):
        self._root = root
        self._prefilled = prefill
        self._frame = None
        self._handle_view_list = handle_view_list

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _save_click(self):
        print("Saving. Exiting to list view.")
        self._handle_view_list()

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
        self.password_entry = ttk.Entry(master=self._frame, show="*")
        save_button = ttk.Button(master=self._frame, text="Add/Save", command=self._save_click) # remember to refetch from db.
        cancel_button = ttk.Button(master=self._frame, text="Cancel", command=self._cancel_click)

        if self._prefilled:
            self.site_entry.insert(0, self._prefilled.website)
            self.email_entry.insert(0, self._prefilled.email)
            self.username_entry.insert(0, self._prefilled.username)
            self.password_entry.insert(0, self._prefilled.password)

        site_label.grid(row=0, sticky=constants.W, padx=5)
        self.site_entry.grid(row=1, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        email_label.grid(row=2, sticky=constants.W, padx=5)
        self.email_entry.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        username_label.grid(row=4, sticky=constants.W, padx=5)
        self.username_entry.grid(row=5, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(row=6, sticky=constants.W, padx=5)
        self.password_entry.grid(row=7, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        save_button.grid(row=8, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=10)
        cancel_button.grid(row=9, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=10)

        self._frame.grid_columnconfigure(1, weight=1, minsize=500)
