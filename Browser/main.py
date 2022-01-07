import tkinter as tk
import json
import requests
from tkinter import messagebox
from tkinter.messagebox import showinfo, showerror

class App:
    def __init__(self, root):
        root.title("Studious Search")
        width = 1000
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        
        self.root = root
        self.reloadbutton = tk.Button(root, text="Reload", command=self.reloadWebsite)
        self.searchbar = tk.Entry(root, font=("Helvetica", 16))
        self.searchButton = tk.Button(root, text="Search", command=self.search)
        self.browser = tk.Canvas(root)
        
        
        self.reloadbutton.place(x=0, y=0, relwidth=0.1, height=35)
        self.searchbar.place(relx=0.1, rely=0, relwidth=0.8, height=35)
        self.searchButton.place(relx=0.9, rely=0, relwidth=0.1, height=35)
        self.browser.place(relx=0, y=35, relwidth=1, relheight=1)
        
        self.url = ""
    
    def search(self):
        url = self.searchbar.get()
        try:
            self.url = url
            website = requests.get(url)
            website = json.loads(website.text)
            self.loadWebsite(website)
        except Exception as e:
            showerror("Error", "Invalid URL \nerror: " + str(e))
    
    def loadWebsite(self, content):
        self.browser.delete("all")
        self.root.title(content["title"])
        for item in content['body']:
            if item['type'] == 'text':
                self.browser.create_text(item['x'], item['y'], text=item['text'], anchor=tk.NW,
                                        font=("Helvetica", int(item['size'])), fill=item['color'])
    def reloadWebsite(self):
        if self.url != "":
            try:
                website = requests.get(self.url)
                website = json.loads(website.text)
                self.loadWebsite(website)
            except Exception as e:
                showerror("Error", "Invalid URL \nerror: " + str(e))
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()