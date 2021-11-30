from tkinter import ttk, constants

data = [
    {
        "id": 1,
        "website": "https://www.111.com",
        "username": "Foobar",
        "email": "foobar@foobar.com",
        "password": "111?"
    },
    {
        "id": 2,
        "website": "https://www.222.com",
        "username": "Foobar",
        "email": "foobar@foobar.com",
        "password": "222?"
    },
    {
        "id": 3,
        "website": "https://www.333.io",
        "username": "Foob329ar",
        "email": "foobar@foobar.com",
        "password": "33333?"
    },
    {
        "id": 4,
        "website": "4444",
        "username": "Fooba999r",
        "email": "foobar@foobar.com",
        "password": "444?"
    },
    {
        "id": 5,
        "website": "https://www.lorem.com",
        "username": "Foobar223",
        "email": "foobar@foobar.com",
        "password": "555?55"
    }
]

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
            print("Load data from db here, and prefill", prefill)
            self._handle_view_item(prefill)
        else:
            self._handle_view_item()

    def _logout_handler(self):
        self._handle_logout()

    def _initialize(self):
        global data
        self._frame = ttk.Frame(master=self._root)
        add_button = ttk.Button(master=self._frame, text="Add new", command=self._item_handler)
        logout_button = ttk.Button(master=self._frame, text="Logout", command=self._logout_handler)
        add_button.grid(row=0, column=0, columnspan=3, sticky=(constants.E, constants.W), padx=5, pady=10)
        logout_button.grid(row=1, column=0, columnspan=3, sticky=(constants.E, constants.W), padx=5, pady=10)

        # Canvas for scrolling?

        for i, entry in enumerate(data):
            entity = ttk.Label(master=self._frame, text=entry["website"])
            entity.grid(row=i+2, column=0, sticky=(constants.W), padx=5, pady=5)
            entity_link = ttk.Button(master=self._frame, text="View", command=lambda i=data[i]: self._item_handler(i))
            entity_link.grid(row=i+2, column=1, padx=5, pady=5)
            copy_link = ttk.Button(master=self._frame, text="Copy", command=lambda i=data[i]: print(f"Copy password {i['id']} to clipboard.")) # Subprocess maybe?
            copy_link.grid(row=i+2, column=2, sticky=(constants.E), padx=5, pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=250)
