import tkinter as tk
from tkinter import ttk  # for themed widgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Hypothetical function to retrieve weather data (replace with your implementation)


def get_weather_data(city):
    # Implement logic to fetch 3-day humidity data for the given city
    # This example returns dummy data
    return {
        "city": city,
        "days": ["Mon", "Tue", "Wed"],
        "humidity": [60, 70, 80]
    }


class WeatherGUI:
    def __init__(self, master):
        self.master = master
        master.title("Weather Forecast")

        # Create frame for city input and button
        self.input_frame = tk.Frame(master)
        self.input_frame.pack(fill=tk.X)

        # City entry label
        self.city_label = ttk.Label(self.input_frame, text="Enter City:")
        self.city_label.pack(side=tk.LEFT)

        # City entry field
        self.city_entry = ttk.Entry(self.input_frame)
        self.city_entry.pack(side=tk.LEFT)

        # Get weather button
        self.get_weather_button = ttk.Button(
            self.input_frame, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(side=tk.RIGHT)

        # Create frame for displaying the plot
        self.plot_frame = tk.Frame(master)
        self.plot_frame.pack(fill=tk.BOTH, expand=True)

        # Initialize plot figure
        self.fig, self.ax = plt.subplots()

        # Create a canvas to embed the plot in the Tkinter window
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Initially hide the plot frame
        self.plot_frame.pack_forget()

    def get_weather(self):
        city = self.city_entry.get()
        if not city:
            # Handle empty city name
            return

        # Fetch weather data (replace with your actual function call)
        weather_data = get_weather_data(city)

        # Update plot with retrieved data
        self.update_plot(weather_data)

        # Show the plot frame
        self.plot_frame.pack(fill=tk.BOTH, expand=True)

    def update_plot(self, weather_data):
        self.ax.clear()  # Clear previous plot
        # Use bar chart
        self.ax.bar(weather_data["days"],
                    weather_data["humidity"], color='skyblue')
        self.ax.set_xlabel("Day")
        self.ax.set_ylabel("Humidity (%)")
        self.ax.set_title(f"Humidity Forecast for {weather_data['city']}")
        self.canvas.draw()  # Update the canvas to display the plot


# Create the main window and run the GUI
root = tk.Tk()
gui = WeatherGUI(root)
root.mainloop()
