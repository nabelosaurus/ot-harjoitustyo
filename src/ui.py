from views.item_view import ItemView
from views.list_view import ListView
from views.login_view import LoginView
from views.registration_view import RegistrationView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_registration_view()
        # self._show_list_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    # View switchers
    def _show_registration_view(self):
        self._hide_current_view()
        self._current_view = RegistrationView(self._root, self._handle_view_login)
        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()
        self._current_view = LoginView(self._root, self._handle_login)
        self._current_view.pack()

    def _show_list_view(self):
        self._hide_current_view()
        self._current_view = ListView(self._root, self._handle_view_item, self._handle_view_login)
        self._current_view.pack()

    def _show_item_view(self, prefill=None):
        self._hide_current_view()
        if prefill:
            self._current_view = ItemView(self._root, self._handle_view_list, prefill)
        else:
            self._current_view = ItemView(self._root, self._handle_view_list)
        self._current_view.pack()

    def _handle_view_login(self):
        self._show_login_view()

    def _handle_login(self):
        self._show_list_view()

    def _handle_view_item(self, prefill=None):
        if prefill:
            self._show_item_view(prefill)
        else:
            self._show_item_view()

    def _handle_view_list(self):
        self._show_list_view()
