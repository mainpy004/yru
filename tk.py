import tkinter as tk
import sqlite3

class JokeApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Анекдоты")
        self.button = tk.Button(self, text="Получить анекдот", command=self.get_joke)
        self.button.pack(pady=10)
        self.text_joke = tk.Text(self, width=50, height=10)
        self.text_joke.pack()
        self.conn = sqlite3.connect('jokes.bd')
        self.cursor = self.conn.cursor()
        
    def get_joke(self):
        self.text_joke.delete(0.0, tk.END)
        self.cursor.execute("SELECT joke FROM Jokes ORDER BY RANDOM() LIMIT 1;")
        joke = self.cursor.fetchone()[0]
        self.text_joke.insert(0.0, joke)
        
    def __del__(self):
        self.cursor.close()
        self.conn.close()

app = JokeApp()
app.mainloop()