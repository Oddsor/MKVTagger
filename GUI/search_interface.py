__author__ = 'Odd'

import tkinter as tk
from OddTools.GUI import Listbox
from OddTools.GUI import tkSimpleDialog
import Scrapers.themoviedb

class SearchGUI(tk.Toplevel):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.config()
        self.pack()
        label = tk.Label(self, text="Enter title: ")
        label.grid(row=0, column=0)
        search_entry = tk.Entry(self)
        search_entry.insert(0, "Showname")
        search_entry.grid(row=0, column=1)
        variable = tk.StringVar(self)
        variable.set("TheMovieDB")
        search_dropdown = tk.OptionMenu(self, variable, "TheMovieDB", "TheMovieDB tv", "TheTVDB")
        search_dropdown.grid(row=0, column=2)

        listbox = Listbox()

        def start_search():
            if variable.get() == "TheMovieDB":
                import scrapers.themoviedb
                result = scrapers.themoviedb.search(search_entry.get())

        search_button = tk.Button(self, text="Search", command=start_search)
        search_button.grid(row=0, column=3)


class Search_dialog(tkSimpleDialog.Dialog):
    def __init__(self, parent, title="Scraper search", module=None):
        self.scraper = module
        tkSimpleDialog.Dialog.__init__(self, parent, title)

    def body(self, master):
        search_frame = tk.Frame(self)
        entry = self.search_text = tk.Entry(search_frame)
        entry.pack(side=tk.LEFT)
        search_button = tk.Button(search_frame, text="Search", command=self.start_search)
        search_button.pack(side=tk.RIGHT)
        if self.scraper is None:
            #TODO make list of scrapers and add to an optionsmenu
            None
        search_frame.pack()
        results_frame = self.results_frame = tk.Frame()

    def start_search(self):
        result = self.scraper.search(self.search_text.get())

    def apply(self):
        self.result = "Test"
        return "Test"


if __name__ == "__main__":
    root = tk.Tk()
    app = Search_dialog(root, module=Scrapers.themoviedb)
    print(app) #Boo
    print(app.result) #Yay