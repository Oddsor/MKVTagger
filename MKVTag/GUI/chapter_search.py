__author__ = 'Odd'
from OddTools.GUI import tkSimpleDialog


class _SearchDialog(tkSimpleDialog.Dialog):
    def __init__(self, parent, title="Chapter search", return_data=False):
        self.return_data = return_data
        tkSimpleDialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        pass

    def apply(self):
        pass

    def validate(self):
        pass