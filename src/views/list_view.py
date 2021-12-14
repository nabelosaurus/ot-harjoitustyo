from tkinter import ttk, constants, Canvas
from services.logins_service import LoginService
from services.hashing_service import hashing_service


class ListView:
    def __init__(self, root, handle_view_item, handle_logout):
        self._root = root
        self._handle_view_item = handle_view_item
        self._frame = None
        self._handle_logout = handle_logout
        self._login_service = LoginService()

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
        self._second_frame.destroy()
        self._scroll_frame.destroy()

    def _item_handler(self, prefill=None):
        if prefill:
            self._handle_view_item(prefill)
        else:
            self._handle_view_item()

    def _logout_handler(self):
        self._handle_logout()

    def _copy_handler(self, item):
        self._root.clipboard_clear()
        self._root.clipboard_append(hashing_service.decrypt_login_password(item.password, item.salt))

    def _initialize(self):
        data = self._login_service.get_all_logins()

        self._frame = ttk.Frame(master=self._root)
        add_button = ttk.Button(
            master=self._frame, text="Add new", command=self._item_handler)
        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._logout_handler)
        add_button.grid(
            row=0, column=0, columnspan=3, sticky=(constants.E, constants.W), padx=5, pady=10
        )
        logout_button.grid(
            row=1, column=0, columnspan=3, sticky=(constants.E, constants.W), padx=5, pady=10
        )

        self._second_frame = ttk.Frame(master=self._root)
        self._second_frame.pack(fill="both", expand="yes")
        self._canvas = Canvas(self._second_frame)
        self._canvas.pack(side="left", fill="both", expand="yes")
        self._scrollbar = ttk.Scrollbar(
            self._second_frame, orient="vertical", command=self._canvas.yview)
        self._scrollbar.pack(side="right", fill="y")
        self._canvas.configure(yscrollcommand=self._scrollbar.set)
        self._canvas.bind('<Configure>', lambda e: self._canvas.configure(
            scrollregion=self._canvas.bbox("all")))
        self._scroll_frame = ttk.Frame(self._canvas)
        self._canvas.create_window(
            (0, 0), window=self._scroll_frame, anchor="nw")

        for i, entry in enumerate(data):
            entity = ttk.Label(master=self._scroll_frame,
                               text=f"{entry.website if len(entry.website) < 30 else (entry.website[:30]+'...')}")
            entity.grid(row=i+2, column=0,
                        sticky=(constants.W), padx=5, pady=5)
            entity_link = ttk.Button(
                master=self._scroll_frame, text="View",
                command=lambda entry=entry: self._item_handler(entry)
            )
            entity_link.grid(row=i+2, column=1, padx=5, pady=5)
            copy_link = ttk.Button(
                master=self._scroll_frame, text="Copy",
                command=lambda entry=entry: self._copy_handler(entry)
            )
            copy_link.grid(row=i+2, column=2,
                           sticky=(constants.E), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=425)
