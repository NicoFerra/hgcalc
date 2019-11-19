import math
from tkinter import *
import webbrowser


# function
def calculate():
    population = int(population_box.get())
    items = int(items_box.get())
    sample = int(sample_box.get())
    success = int(successes_box.get())
    c_hgd = float(0)
    exact_output.delete(0.0, END)
    cumul_output.delete(0.0, END)
    try:
        term1 = math.factorial(items) / (math.factorial(success) * math.factorial(items - success))
        term2 = math.factorial(population - items) / (math.factorial(sample - success) * math.factorial((population - items) - (sample - success)))
        term3 = math.factorial(population) / (math.factorial(sample) * math.factorial(population - sample))
        hgd = term1 * term2 / term3
        hgd_output = '%.5f' % (hgd * 100), "%"
        while items >= success and sample >= success:
            term1 = math.factorial(items) / (math.factorial(success) * math.factorial(items - success))
            term2 = math.factorial(population - items) / (
                        math.factorial(sample - success) * math.factorial((population - items) - (sample - success)))
            term3 = math.factorial(population) / (math.factorial(sample) * math.factorial(population - sample))
            hgd = term1 * term2 / term3
            c_hgd = c_hgd + hgd
            success = success + 1
        c_hgd_output = '%.5f' % (c_hgd * 100), "%"
    except:
        hgd_output = "ERROR!"
        c_hgd_output = "ERROR!"
    exact_output.insert(END, hgd_output)
    cumul_output.insert(END, c_hgd_output)


def callback(url):
    webbrowser.open_new(url)


def infos():
    i_window = Tk()
    i_window.title("HGC infos")
    i_window.configure(background="gray10")
    i_label = Label(i_window, text="Software developed by Nicolo' Ferrari\n"
                                   "Compiled in Python 3.6.2\n\n"
                                   "for more infos about the\n"
                                   "Hypergeometric Distribution", bg="gray10", fg="white", font="Ubuntu 12")
    i_label.grid(row=0)
    i_link = Label(i_window, text="click here", bg="gray10", fg="blue", font="Ubuntu 12")
    i_link.grid(row=1)
    i_link.bind("<Button-1>", lambda e: callback("https://en.wikipedia.org/wiki/Hypergeometric_distribution"))
    i_window.mainloop()


# window
root = Tk()
root.title("HyperGeoCalculator")
root.configure(background="gray10", padx=20, pady=10)

# label
icon = PhotoImage(file="icon.png")
theLabel = Label(root, image=icon, bg="gray10")
theLabel.grid(row=0, column=0, sticky=W)
theTitle = Label(root, text="HyperGeo\nCalculator", bg="gray10",
                 fg="white", font="Ubuntu 18 bold")
theTitle.grid(row=0, column=1, sticky=E)
space1 = Label(root, background="gray10")
space1.grid(row=1)

# entry boxes
p_text = Label(root, text="population", background="gray10", fg="white")
p_text.grid(row=2, column=0)
population_box = Entry(root, width=10, bg="grey15", fg="white")
population_box.grid(row=2, column=1)

i_text = Label(root, text="items", background="gray10", fg="white")
i_text.grid(row=3, column=0)
items_box = Entry(root, width=10, bg="gray15", fg="white")
items_box.grid(row=3, column=1)

s_text = Label(root, text="sample", background="gray10", fg="white")
s_text.grid(row=4, column=0)
sample_box = Entry(root, width=10, bg="gray15", fg="white")
sample_box.grid(row=4, column=1)

x_text = Label(root, text="successes", background="gray10", fg="white")
x_text.grid(row=5, column=0)
successes_box = Entry(root, width=10, bg="gray15", fg="white")
successes_box.grid(row=5, column=1)

# click button
space2 = Label(root, background="gray10")
space2.grid(row=6)
cButton = Button(root, text="CALCULATE", width=9, command=calculate)
cButton.grid(row=7, columnspan=2)
space3 = Label(root, background="gray10")
space3.grid(row=8)

# output text box
exact_text = Label(root, text="exact", background="grey10", fg="white")
exact_text.grid(row=9, column=0)
exact_output = Text(root, width=11, height=1, wrap=WORD, background="gray15", fg="white")
exact_output.grid(row=9, column=1)

cumul_text = Label(root, text="cumulative", background="gray10", fg="white")
cumul_text.grid(row=10, column=0)
cumul_output = Text(root, width=11, height=1, wrap=WORD, background="gray15", fg="white")
cumul_output.grid(row=10, column=1)

# info & button
space4 = Label(root, background="gray10")
space4.grid(row=11)
sign = Label(root, text=" by DaFerra", background="gray10", fg="gray20", font="Ubuntu 10 italic", anchor="w")
sign.grid(row=12, column=0, sticky=W)

info = PhotoImage(file="info.png")
info_button = Button(root, image=info, background="gray10", command=infos)
info_button.grid(row=12, column=1, sticky=E)

root.mainloop()
