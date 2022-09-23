from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M:%S')
    with open('C:\\Users\\ukeuk\\Desktop\\Учеба\\Знакомство с Python\\Lec 4\\task_2\\log.csv', 'a') as file:
        file.write(f'{time};temperature;{data} \n') 

def preassure_logger(data):
    time = dt.now().strftime('%H:%M:%S')
    with open('C:\\Users\\ukeuk\\Desktop\\Учеба\\Знакомство с Python\\Lec 4\\task_2\\log.csv', 'a') as file:
        file.write(f'{time};preassure;{data} \n')

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M:%S')
    with open('C:\\Users\\ukeuk\\Desktop\\Учеба\\Знакомство с Python\\Lec 4\\task_2\\log.csv', 'a') as file:
        file.write(f'{time};wind_speed;{data} \n')

        