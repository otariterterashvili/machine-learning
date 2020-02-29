import tkinter as tk

class MainDrawer(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = MainPage(container, self)
        self.frames[MainPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()



class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.miligram_wight = ""
        self.kg_wight = ""
        self.gram_wight = ""
        self.tone_wight = ""

        # miligrams inputs
        label = tk.Label(self, text="miligrams")
        label.pack(pady=10, padx=10)
        self.miligram_entry = tk.Entry(self, bd=5)
        self.miligram_entry.pack()

        # grams inputs
        grams_label = tk.Label(self, text="grams")
        grams_label.pack(pady=10, padx=10)
        self.grams_entry = tk.Entry(self, bd=5)
        self.grams_entry.pack()

        # kg inputs
        kg_label = tk.Label(self, text="kilo")
        kg_label.pack(pady=10, padx=10)
        self.kg_entry = tk.Entry(self, bd=5)
        self.kg_entry.pack()

        # tone inputs
        tone_label = tk.Label(self, text="tone")
        tone_label.pack(pady=10, padx=10)
        self.tone_entry = tk.Entry(self, bd=5)
        self.tone_entry.pack()

        click_button = tk.Button(self, text="calculate", bg="blue", command=self.click_me)
        click_button.pack(side="bottom")

        clear_button = tk.Button(self, text="clear", bg="red", command=self.clear_values)
        clear_button.pack(side="bottom")

    def click_me(self):

        self.get_exist_parameter(self.miligram_entry.get(), self.kg_entry.get(), self.grams_entry.get(), self.tone_entry.get())


    def clear_values(self):
        self.miligram_wight = ""
        self.kg_wight = ""
        self.gram_wight = ""
        self.tone_wight = ""
        self.update_values()

    def get_exist_parameter(self, mlg, kg, gram, tone):

        if bool(mlg) == True:
            self.mile_converter(mlg)
        elif bool(kg) == True:
            self.kg_converter(kg)
        elif bool(gram) == True:
            self.gram_converter(gram)
        elif bool(tone) == True:
            self.tone_converter(tone)
        else:
            return "none"
        self.update_values()

    def mile_converter(self, mlg):

        try:
            self.miligram_wight = mlg
            self.gram_wight = str(float(mlg)/1000)
            self.kg_wight = str(float(mlg)/100000)
            self.tone_wight = str(float(self.kg_wight)/1000)
        except Exception as e:
            print(e)

    def gram_converter(self, gram):
        self.miligram_wight = str(float(gram) * 1000)
        self.gram_wight = gram
        self.kg_wight = str(float(gram) / 1000)
        self.tone_wight = str(float(self.kg_wight) / 1000)

    def kg_converter(self, kg):
        self.miligram_wight = str(float(kg) * 100000)
        self.gram_wight = str(float(kg) * 1000)
        self.kg_wight = kg
        self.tone_wight = str(float(self.kg_wight) / 1000)

    def tone_converter(self, tone):
        self.kg_wight = str(float(tone) / 1000)
        self.gram_wight = str(float(self.kg_wight) / 1000)
        self.miligram_wight = str(float(self.gram_wight) / 1000)
        self.tone_wight = tone

    def update_values(self):
        self.miligram_entry.delete(0, tk.END)
        self.miligram_entry.insert(0, self.miligram_wight)

        # update kg value
        self.kg_entry.delete(0, tk.END)
        self.kg_entry.insert(0, self.kg_wight)

        # update gram value
        self.grams_entry.delete(0, tk.END)
        self.grams_entry.insert(0, self.gram_wight)

        # update tone value
        self.tone_entry.delete(0, tk.END)
        self.tone_entry.insert(0, self.tone_wight)

app = MainDrawer()
app.geometry('500x500')
app.mainloop()

