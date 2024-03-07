# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render
from .weektemp import get_val



# 
from django.shortcuts import render
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from .forcast import model


def plot_uv_index(request):
    # Sample DataFrame with dummy data
    df2_data = {
        'Time': pd.date_range(start='2023-06-30', periods=288, freq='H'),
        'UV Index': np.random.randint(1, 11, size=288)
    }
    df2 = pd.DataFrame(df2_data)

    # Your plotting code
    x = np.arange(0, 288)
    y = df2['UV Index'][0:288]

    plt.figure(figsize=(22, 10))
    plt.plot(x, y, linestyle='-', marker='o', color='blue', label='1993')

    coefficients = np.polyfit(x, y, 1)
    trendline = np.poly1d(coefficients)
    plt.plot(x, trendline(x), color='red', label='Trend Line')

    plt.xticks(np.arange(0, 288, 12))
    plt.xlabel('Time')
    plt.ylabel('UV Index')
    plt.title('Trend line for UV Index on 2023-06-30')
    plt.legend()

    # Convert plot to PNG image and embed it in HTML
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'plot_uv_index.html', {'graphic': graphic})




def home(request):
    values = model.forcasting('1', '10:20')
    #print(values)
    AQI,Temp,Hum,HI= get_val()
    print(AQI,Temp,Hum,HI)

    return render(request, 'home.html', context={'dict':values,'AQI':AQI,'Temp':Temp,'Hum':Hum,'HI':HI})

def graph(request):
    return render(request, 'graph.html')

 
def contact(request):
    return render(request, 'contact.html')

def rajbhavan(request):
    values2 = model.forcasting('1', '10:20')

    #print(values)
    AQI2,Temp2,Hum2,HI2= get_val()
    
    return render(request, 'rajbhavan.html', context={'dict':values2,'AQI':AQI2,'Temp':Temp2,'Hum':Hum2,'HI':HI2})