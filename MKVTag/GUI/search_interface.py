__author__ = 'Odd'

import tkinter as tk
from OddTools.GUI import Listbox
from OddTools.GUI import tkSimpleDialog
import Scrapers.themoviedb
import requests
from PIL import ImageTk
from PIL import Image
import io

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
        self.results_frame = self.results_frame = tk.Frame(self)
        self.results_frame.pack()

    def start_search(self):
        result = self.resultlist = self.scraper.search(self.search_text.get())
        items = list()
        image_list = list()
        for item in result:
            #TODO just in time download of image and caching
            items.append(item['title'])
            if "http" in item['thumbnail']:
                request = requests.get(item['thumbnail'])
                pilimg = Image.open(io.BytesIO(request.content))
                image_list.append(ImageTk.PhotoImage(pilimg))
            else:
                image_list.append(None)

        listbox = self.listbox = Listbox.Listbox(items, self.results_frame, orderable=False)
        listbox.add_data(items)
        listbox.grid(row=0, column=0, sticky=tk.N)
        imagebox = tk.Frame(self.results_frame)
        imagebox.grid(row=0,column=1)

        def show_image(event):
            if len(imagebox.winfo_children()) > 0:
                imagebox.winfo_children()[0].destroy()
            if image_list[listbox.get_selected()[0]] is not None:
                label = tk.Label(imagebox, image=image_list[listbox.get_selected()[0]])
                label.pack()
            else:
                label = tk.Label(imagebox, text="No image")
                label.pack()

        self.listbox.add_onclick(show_image)

    def apply(self):
        selected = self.listbox.get_selected()
        for item in self.resultlist:
            if item['title'] == self.listbox.get_items()[selected[0]]:
                self.result = item['id']

    def validate(self):
        if self.listbox is not None and len(self.listbox.get_selected()) > 0:
            return 1
        else:
            return 0


def search_title(module=Scrapers.themoviedb, parent=None):
    if parent is None:
        parent = tk.Tk()
    app = Search_dialog(parent, module)
    return app.result

if __name__ == "__main__":
    print(search_title())