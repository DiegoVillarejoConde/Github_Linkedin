import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        
        # Pantalla de resultados
        self.display = tk.Entry(master, width=30, justify='right', font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+'
        ]
        
        # Crear botones en la cuadrícula
        fila = 1
        columna = 0
        for boton in botones:
            cmd = lambda x=boton: self.click(x)
            tk.Button(master, text=boton, command=cmd, width=7, height=2).grid(row=fila, column=columna, padx=3, pady=3)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1
        
        # Botón de igual
        tk.Button(master, text='=', command=self.calcular, width=7, height=2).grid(row=fila, column=columna, padx=3, pady=3)
    
    def click(self, key):
        if key == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)
    
    def calcular(self):
        try:
            resultado = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, resultado)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

def main():
    root = tk.Tk()
    root.geometry("300x400")
    calculadora = Calculadora(root)
    root.mainloop()

if __name__ == "__main__":
    main()