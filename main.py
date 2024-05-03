import algorithm

import tkinter as tk
from tkinter import messagebox

def linear_search_click():
    data_str = data_entry.get()
    target_str = target_entry.get()

    try:
        data = [int(x) for x in data_str.split(',')]
        target = int(target_str)
        result = algorithm.linear_search(data, target)

        if result != -1:
            messagebox.showinfo("Result", f"Target found at index {result}")
        else:
            messagebox.showinfo("Result", "Target not found")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter comma-separated numbers.")


def selection_sort_click():
    data_str = data_entry.get()

    try:
        data = [int(x) for x in data_str.split(',')]
        result = algorithm.selection_sort(data)

        messagebox.showinfo("Result", f"Sorted data: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter comma-separated numbers.")

def binary_search_click():
    data_str = data_entry.get()
    target_str = target_entry.get()

    try:
        data = [int(x) for x in data_str.split(',')]
        target = int(target_str)
        result = algorithm.binary_search(data, target)

        if result != -1:
            messagebox.showinfo("Result", f"Target found at index {result}")
        else:
            messagebox.showinfo("Result", "Target not found")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter comma-separated numbers.")

def bubble_sort_click():
    data_str = data_entry.get()

    try:
        data = [int(x) for x in data_str.split(',')]
        result = algorithm.bubble_sort(data)

        messagebox.showinfo("Result", f"Sorted data: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter comma-separated numbers.")


# Main Window setup
window = tk.Tk()
window.title("Search and Sort Algorithms")

# Input Area
data_label = tk.Label(window, text="Enter data (comma-separated):")
data_label.pack()
data_entry = tk.Entry(window)
data_entry.pack()

target_label = tk.Label(window, text="Enter target to search:")
target_label.pack()
target_entry = tk.Entry(window)
target_entry.pack()

# Buttons
linear_button = tk.Button(window, text="Linear Search", command=linear_search_click)
linear_button.pack()

selection_button = tk.Button(window, text="Selection Sort", command=selection_sort_click)
selection_button.pack()

binary_button = tk.Button(window, text="Binary Search", command=binary_search_click)
binary_button.pack()

bubble_button = tk.Button(window, text="Bubble Sort", command=bubble_sort_click)
bubble_button.pack()

window.mainloop()
