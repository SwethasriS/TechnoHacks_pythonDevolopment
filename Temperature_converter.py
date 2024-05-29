import tkinter as tk

class TemperatureConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry("300x150")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Enter temperature:")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        self.unit_var = tk.StringVar(value="Fahrenheit")
        self.unit_menu = tk.OptionMenu(self, self.unit_var, "Fahrenheit", "Celsius")
        self.unit_menu.pack()

        self.convert_button = tk.Button(self, text="Convert", command=self.convert_temperature)
        self.convert_button.pack()

    def convert_temperature(self):
        try:
            temperature = float(self.entry.get())
            from_unit = self.unit_var.get()
            converted_temperature = self.convert(temperature, from_unit)
            self.result_label.config(text=f"Converted temperature: {converted_temperature:.2f} {self.get_to_unit(from_unit)}")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")

    def convert(self, temperature, from_unit):
        if from_unit == "Fahrenheit":
            return (temperature - 32) * 5/9
        else:
            return (temperature * 9/5) + 32

    def get_to_unit(self, from_unit):
        return "Celsius" if from_unit == "Fahrenheit" else "Fahrenheit"

if __name__ == "__main__":
    app = TemperatureConverter()
    app.mainloop()
