# Importing necessary libraries
from tkinter import *
import requests
import json
import datetime
from PIL import ImageTk, Image

# Create GUI Window
root = Tk()
root.title("Weather App")
root.geometry("450x700")
root['background'] = "white"

# Load Image
new = ImageTk.PhotoImage(Image.open('logo.png'))
panel = Label(root, image=new)
panel.place(x=0, y=520)

# Dates
dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15))
date.place(x=5, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

# Time
hour = Label(root, text=dt.strftime('%I : %M %p'), bg='white', font=("bold", 15))
hour.place(x=10, y=160)

# Theme based on time of day
hour_now = int(dt.strftime('%H'))
if 8 <= hour_now <= 17:
    weather_img = ImageTk.PhotoImage(Image.open('sun.png'))
else:
    weather_img = ImageTk.PhotoImage(Image.open('moon.png'))

theme_panel = Label(root, image=weather_img)
theme_panel.place(x=210, y=200)

# City Search
city_name_var = StringVar()
city_entry = Entry(root, textvariable=city_name_var, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)

# Function to fetch weather details
def get_weather():
    api_key = "weatherapp1"  # Replace with your OpenWeatherMap API key
    city = city_entry.get()

    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    # API Call
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={1de8e87a0851924f361e2e09ea84951e}"
    
    try:
        response = requests.get(url)
        api = response.json()

        if api["cod"] != 200:
            messagebox.showerror("Error", "City not found!")
            return

        # Extract Data
        current_temperature = api["main"]["temp"]
        humidity = api["main"]["humidity"]
        temp_min = api["main"]["temp_min"]
        temp_max = api["main"]["temp_max"]
        longitude = api["coord"]["lon"]
        latitude = api["coord"]["lat"]
        country = api["sys"]["country"]
        city_name = api["name"]

        # Update GUI Labels
        label_temp.config(text=f"{current_temperature}°C")
        label_humidity.config(text=f"{humidity}%")
        max_temp.config(text=f"{temp_max}°C")
        min_temp.config(text=f"{temp_min}°C")
        label_lon.config(text=f"{longitude}")
        label_lat.config(text=f"{latitude}")
        label_country.config(text=f"{country}")
        label_city.config(text=f"{city_name}")

    except Exception as e:
        messagebox.showerror("Error", "Failed to fetch data!")

# Search Button
search_button = Button(root, text="Search", command=get_weather)
search_button.grid(row=1, column=1, padx=5, stick=W+E+N+S)

# Labels for Weather Details
label_city = Label(root, text="...", bg='white', font=("bold", 15))
label_city.place(x=10, y=63)

label_country = Label(root, text="...", bg='white', font=("bold", 15))
label_country.place(x=135, y=63)

label_lon = Label(root, text="...", bg='white', font=("Helvetica", 15))
label_lon.place(x=25, y=95)

label_lat = Label(root, text="...", bg='white', font=("Helvetica", 15))
label_lat.place(x=95, y=95)

# Temperature Display
label_temp = Label(root, text="...", bg='white', font=("Helvetica", 110), fg='black')
label_temp.place(x=18, y=220)

# Additional Weather Details
Label(root, text="Humidity:", bg='white', font=("bold", 15)).place(x=3, y=400)
label_humidity = Label(root, text="...", bg='white', font=("bold", 15))
label_humidity.place(x=107, y=400)

Label(root, text="Max Temp:", bg='white', font=("bold", 15)).place(x=3, y=430)
max_temp = Label(root, text="...", bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)

Label(root, text="Min Temp:", bg='white', font=("bold", 15)).place(x=3, y=460)
min_temp = Label(root, text="...", bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)

# Note Label
note = Label(root, text="All temperatures in degree Celsius", bg='white', font=("italic", 10))
note.place(x=95, y=495)

# Run GUI
root.mainloop()
