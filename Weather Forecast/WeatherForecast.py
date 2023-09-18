from tkinter import *
import requests
from tkinter import messagebox

window = Tk()
window.title("// WEATHER FORECAST //")
window.geometry("410x400+600+300")
Icon = PhotoImage(file="Icon.png")
window.iconphoto(True, Icon)

def get_weather(city):
    api_key = "bd5e378503939ddaee76f12ad7a97608"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params = params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def display_weather():
    city = city_entry.get()
    weather_data = get_weather(city)

    if weather_data is not None:
        humidity_label.config(text= f"Humidity: {weather_data['main']['humidity']}%")
        temp_label.config(text= f"Temperature: {weather_data['main']['temp']}°C")
        description_label.config(text= f"Description: {weather_data['weather'][0]['description']}")
    else:
        messagebox.showerror("Error", "City not found")



label1 = Label(window, text= "WEATHER FORECAST", font = ("Times New Roman", 20, "italic bold"))
label1.pack(pady=10)

label = Label(window, text="Enter the City", font= ("Arial", 12, "bold"),fg="#413430")
label.pack(pady=15)

city_entry = Entry(window, font= ("Arial",12, "bold"))
city_entry.pack()

generate_button = Button(window,text="Show weather forecast", font= ("Arial", 12, "bold"),fg="#413430",command= display_weather)
generate_button.pack(pady=15)

temp_label = Label(window, text="", width=30, font=("Arial", 12, "bold"),bg="#000000",fg="White")
temp_label.pack()

humidity_label = Label(window,text="",width=30,font= ("Arial", 12, "bold"), bg="#000000", fg="White")
humidity_label.pack()

description_label = Label(window, text="",width=30,font= ("Arial", 12, "bold"), bg="#000000", fg="White")
description_label.pack()

window.mainloop()
