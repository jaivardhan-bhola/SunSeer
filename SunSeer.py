import requests
from tkinter import *
import os
import requests
import time

script_dir = os.path.dirname(__file__)

api_key = '80a9a0fd35af99ab35f9979a6dd2d2ce'

def get_weather(city):
    global temp, sunrise, sunset, humidity, wind_speed, icon, max_temp, min_temp
    weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
    temp = round((weather_data.json()['main']['temp'] - 32) * 5/9)
    city = weather_data.json()['name']
    sunrise = weather_data.json()['sys']['sunrise']
    sunset = weather_data.json()['sys']['sunset']
    humidity = str(weather_data.json()['main']['humidity'])
    wind_speed = str(round(weather_data.json()['wind']['speed'] * 1.60934)) + ' km/h'
    sunrise = time.strftime('%I:%M %p', time.localtime(sunrise))
    sunset = time.strftime('%I:%M %p', time.localtime(sunset))
    temp = round(temp)
    icon = weather_data.json()['weather'][0]['icon']
    max_temp = round((weather_data.json()['main']['temp_max'] - 32) * 5/9)
    min_temp = round((weather_data.json()['main']['temp_min'] - 32) * 5/9)

def main():
    def search():
        global city
        city = entry_1.get()
        try:
            get_weather(city)
            window.destroy()
            mainscreen()
        except KeyError:
            canvas.itemconfig(a, text="City not found")
    window = Tk()
    window.geometry("600x400")
    window.configure(bg = "#000000")
    window.title("SunSeer")
    logo = PhotoImage(file=script_dir+"/Assets/Logo.png")
    window.iconphoto(False, logo)
    canvas = Canvas(
        window,
        bg = "#000000",
        height = 400,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=script_dir+"/Assets/Start/image_1.png")
    
    image_1 = canvas.create_image(
        300.0,
        200.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=script_dir+"/Assets/Start/image_2.png")
    image_2 = canvas.create_image(
        302.0,
        237.0,
        image=image_image_2
    )

    button_image_1 = PhotoImage(
        file=script_dir+"/Assets/Start/button_1.png")
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=search,
        relief="flat"
    )
    button_1.place(
        x=252.0,
        y=223.0,
        width=100.0,
        height=28.0
    )
    a= canvas.create_text(
        191.0,
        147.0,
        anchor="nw",
        text="Enter your City ",
        fill="#00FF28",
        font=("DMSans", 30 * -1, "bold")
    )

    entry_image_1 = PhotoImage(
        file=script_dir+"/Assets/Start/entry_1.png")
    entry_bg_1 = canvas.create_image(
        299.5,
        197.0,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#2C424A",
        fg="#f0f0f0",
        highlightthickness=0,
        font=("DMSans", 20 * -1),
        justify="center"
    )
    entry_1.place(
        x=169.0,
        y=186.0,
        width=261.0,
        height=20.0
    )
    entry_1.focus()
    image_image_3 = PhotoImage(
        file=script_dir+"/Assets/Start/image_3.png")
    image_3 = canvas.create_image(
        300.3333435058594,
        58.33331298828125,
        image=image_image_3
    )
    window.resizable(False, False)
    window.mainloop()

def mainscreen():
    window = Tk()
    window.geometry("600x400")
    window.configure(bg = "#000000")
    window.title("SunSeer")
    logo = PhotoImage(file=script_dir+"/Assets/Logo.png")
    window.iconphoto(False, logo)
    canvas = Canvas(
        window,
        bg = "#000000",
        height = 400,
        width = 600,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=script_dir+"/Assets/MainScreen/image_1.png")
    image_1 = canvas.create_image(
        300.0,
        200.0,
        image=image_image_1
    )

    canvas.create_text(
        240.0,
        260.0,
        anchor="nw",
        text="{}°C/{}°C".format(min_temp, max_temp),
        fill="#FFFFFF",
        font=("Grandstander", 25 * -1)
    )

    image_image_2 = PhotoImage(
        file=script_dir+"/Assets/MainScreen/image_2.png")
    image_2 = canvas.create_image(
        300.0,
        40.0,
        image=image_image_2
    )

    canvas.create_text(
        269.0,
        220.0,
        anchor="nw",
        text="{}°C".format(temp),
        fill="#FFFFFF",
        font=("FugazOne", 30 * -1)
    )

    canvas.create_text(
        439.0,
        28.0,
        anchor="nw",
        text=city.title(),
        fill="#FFFFFF",
        font=("Grand Hotel", 35 * -1)
    )

    image_image_3 = PhotoImage(
        file=script_dir+"/Assets/MainScreen/image_3.png")
    image_3 = canvas.create_image(
        258.0,
        335.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=script_dir+"/Assets/MainScreen/image_4.png")
    image_4 = canvas.create_image(
        175.0,
        335.0,
        image=image_image_4
    )

    image_image_5 = PhotoImage(
        file=script_dir+"/Assets/MainScreen/image_5.png")
    image_5 = canvas.create_image(
        341.0,
        335.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=script_dir+"/Assets/MainScreen/image_6.png")
    image_6 = canvas.create_image(
        424.0,
        335.0,
        image=image_image_6
    )

    canvas.create_text(
        152.0,
        360.0,
        anchor="nw",
        text=sunrise,
        fill="#FFFFFF",
        font=("Inter", 10 * -1)
    )

    canvas.create_text(
        235.0,
        360.0,
        anchor="nw",
        text=sunset,
        fill="#FFFFFF",
        font=("Inter", 10 * -1)
    )

    canvas.create_text(
        331.0,
        360.0,
        anchor="nw",
        text=humidity + "%",
        fill="#FFFFFF",
        font=("Inter", 10 * -1)
    )

    canvas.create_text(
        406.0,
        359.0,
        anchor="nw",
        text=wind_speed,
        fill="#FFFFFF",
        font=("Inter", 10 * -1)
    )
    if icon == "01d":
        image_image_7 = PhotoImage(
            file=script_dir+"/Assets/MainScreen/image_7.png")
        image_7 = canvas.create_image(
            300.0,
            160.0,
            image=image_image_7
        )
    elif icon == "01n":
        image_image_8 = PhotoImage(
            file=script_dir+"/Assets/MainScreen/image_8.png")
        image_8 = canvas.create_image(
            300.0,
            160.0,
            image=image_image_8
        )
    elif icon in ["02d", "02n", "03d", "03n", "04d", "04n"]:
        image_image_9 = PhotoImage(
            file=script_dir+"/Assets/MainScreen/image_9.png")
        image_9 = canvas.create_image(
            300.0,
            160.0,
            image=image_image_9
        )
    elif icon in ["09d", "09n", "10d", "10n", "11d","11n"]:
        image_image_10 = PhotoImage(
            file=script_dir+"/Assets/MainScreen/image_10.png")
        image_10 = canvas.create_image(
            300.0,
            159.0,
            image=image_image_10
        )
    elif icon in ["13d", "13n"]:
        image_image_11 = PhotoImage(
            file=script_dir+"/Assets/MainScreen/image_11.png")
        image_11 = canvas.create_image(
            300.0,
            159.0,
            image=image_image_11
        )
    elif icon in ["50d", "50n"]:
        image_image_12 = PhotoImage(
            file=script_dir+"/Assets/MainScreen/image_12.png")
        image_12 = canvas.create_image(
            300.0,
            160.0,
            image=image_image_12
        )
    window.resizable(False, False)
    window.mainloop()

main()