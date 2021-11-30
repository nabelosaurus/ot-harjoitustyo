from tkinter import ttk, constants
from database_connection import get_database_connection
from repositories.login_repository import LoginRepository


class ListView:
    def __init__(self, root, handle_view_item, handle_logout):
        self._root = root
        self._handle_view_item = handle_view_item
        self._frame = None
        self._handle_logout = handle_logout

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _item_handler(self, prefill=None):
        if prefill:
            self._handle_view_item(prefill)
        else:
            self._handle_view_item()

    def _logout_handler(self):
        self._handle_logout()

    def _copy_handler(self, item):
        self._root.clipboard_clear()
        self._root.clipboard_append(item.password)

    def _initialize(self):
        login_repository = LoginRepository(get_database_connection())
        data = login_repository.find_all()

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

        # Canvas for scrolling?

        for i, entry in enumerate(data):
            entity = ttk.Label(master=self._frame, text=entry.website)
            entity.grid(row=i+2, column=0,
                        sticky=(constants.W), padx=5, pady=5)
            entity_link = ttk.Button(
                master=self._frame, text="View",
                command=lambda entry=entry: self._item_handler(entry)
            )
            entity_link.grid(row=i+2, column=1, padx=5, pady=5)
            copy_link = ttk.Button(
                master=self._frame, text="Copy",
                command=lambda entry=entry: self._copy_handler(entry)
            )
            copy_link.grid(row=i+2, column=2,
                           sticky=(constants.E), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
