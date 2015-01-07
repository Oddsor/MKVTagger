__author__ = 'Odd'

import tkinter as tk



class SearchGUI(tk.Frame):
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

        listbox = OddTools.GUI.Listbox()

        def start_search():
            if variable.get() == "TheMovieDB":
                import scrapers.themoviedb
                result = scrapers.themoviedb.search(search_entry.get())


        search_button = tk.Button(self, text="Search", command=start_search)
        search_button.grid(row=0, column=3)



if __name__ == "__main__":
    root = tk.Tk()
    app = SearchGUI(root)
    app.mainloop()