import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=7261c193ca150806a303b6d18fa43d96"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15) #converet to Celcius
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S GMT", time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%H:%M:%S GMT", time.gmtime(json_data['sys']['sunset']))
    
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max: " + str(max_temp) + "°C\n" + "Min: " + str(min_temp) + "°C\n" + "Pressure: " + str(pressure) + "hPa\n" + "Humidity: " + str(humidity) + "%\n" + "Wind Speed: " + str(wind) + "m/s\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

def clear_textfield(event):
    if textfield.get() == "Type city name":
        textfield.delete(0, tk.END)
    
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Sung's Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)
textfield.insert(0, "Type city name")
textfield.bind("<Key>", clear_textfield)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()