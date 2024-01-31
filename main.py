import flet as ft
import requests
def main(page: ft.Page):
    page.title = "Прогноз погоды"
    page.theme_mode='dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_data = ft.TextField(label='Введите город', width=400)
    weather_now = ft.Text('')
    weather_feelslike = ft.Text('')
    weather_maxtemp = ft.Text('')
    weather_mintemp = ft.Text('')

    def get_info(event):
        if len(user_data.value) < 2:
            return
        API = 'f84ac7ee3309c7da133cba71e82865fe'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        feels_like = res['main']['feels_like']
        tempmin = res['main']['temp_min']
        tempmax = res['main']['temp_max']
        weather_now.value = 'Сейчас: '+str(temp)
        weather_feelslike.value = 'Ощущается как: '+str(feels_like)
        weather_mintemp.value = 'Минимальная температура: '+str(tempmin)
        weather_maxtemp.value = 'Максимальная температура: '+str(tempmax)
        page.update()
    def change_theme(event):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()
    page.add(
        #иконки слева
        ft.Row([ft.IconButton(ft.icons.HOME)]),
        ft.Row([ft.IconButton(ft.icons.SUNNY, on_click=change_theme)]),
        ft.Row(
            [
                ft.Text('Погодная программа')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_now], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_feelslike], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_maxtemp], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_mintemp], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([ft.ElevatedButton(text='Получить', on_click=get_info)], alignment=ft.MainAxisAlignment.CENTER)

    )
ft.app(target=main, view=ft.WEB_BROWSER)
