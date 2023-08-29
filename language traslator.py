import tkinter as tk
from tkinter import ttk
from googletrans import Translator

def translate_text():
    input_text = input_textbox.get("1.0", "end-1c")
    target_language = target_language_combobox.get()

    translator = Translator()
    translated_text = translator.translate(input_text, dest=target_language).text

    translated_textbox.delete("1.0", "end")
    translated_textbox.insert("1.0", translated_text)

root = tk.Tk()
root.title("Language Translator")


input_label = ttk.Label(root, text="Enter text to translate:")
input_label.pack(pady=5)

input_textbox = tk.Text(root, height=5, width=40)
input_textbox.pack()

target_language_label = ttk.Label(root, text="Select target language:")
target_language_label.pack(pady=5)

target_language_combobox = ttk.Combobox(root, values=["es", "fr", "de", "ja", "ko"])
target_language_combobox.pack()

translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

translated_textbox = tk.Text(root, height=10, width=40)
translated_textbox.pack()

root.mainloop()


