import pandas as pd
import numpy as np
import pickle

#location = input('Enter the location\n 1. SNDT University \n 2. Rajbahvan \n ')
def forcasting(location, time):
    if location == '1':
        file_path1 = 'textutils\\forcast\\data\\sndt-airlink.csv' 
        file_path2 = 'textutils\\forcast\\data\\sndt-weatherlink.csv'

    if location == '2':
        file_path1 = 'textutils\\forcast\\data\\rajbhavan-airlink.csv' 
        file_path2 = 'textutils\\forcast\\data\\rajbhavan-weatherlink.csv'

    with open('C:\\Users\\Admin\\Documents\\TextUtils-master\\TextUtils-master\\textutils\\forcast\\forcasting_model.pickle', 'rb') as file:
        model = pickle.load(file)
    # Read the data 
    df1 = pd.read_csv(file_path1, encoding='unicode_escape')
    df2 = pd.read_csv(file_path2, encoding='unicode_escape')

    # processing
    df1['DateTime'] = pd.to_datetime(df1['Date & Time'])
    df1['Date'] = df1['DateTime'].dt.date
    df1['Time'] = df1['DateTime'].dt.time

    df2['DateTime'] = pd.to_datetime(df2['Date & Time'])
    df2['Date'] = df2['DateTime'].dt.date
    df2['Time'] = df2['DateTime'].dt.time

    df1.drop(columns=['Date & Time'], inplace=True)
    df1.drop(columns=['Date'], inplace=True)
    df1.drop(columns=['DateTime'], inplace=True)

    df2.drop(columns=['Date & Time'], inplace=True)
    df2.drop(columns=['Date'], inplace=True)
    df2.drop(columns=['DateTime'], inplace=True)

    # required data 
    data1 = df1.iloc[:96]
    data2 = df2.iloc[:96]


# User input 


    search_time = time # string
    search_time = pd.to_datetime(search_time).time()  # Convert search_time to time object

    # Find the closest row to the provided time
    closest_row1 = data1.iloc[(pd.to_timedelta((pd.to_datetime(data1['Time'].astype(str)) - pd.to_datetime(str(search_time))).abs())).idxmin()]
    closest_row2 = data2.iloc[(pd.to_timedelta((pd.to_datetime(data1['Time'].astype(str)) - pd.to_datetime(str(search_time))).abs())).idxmin()]

    airlink_forcasted_values = []
    weatherlink_forcasted_values = []
    for i in range(0, len(closest_row1[:-1])):
        airlink_forcasted_values.append(closest_row1[i] + np.random.randint(0,6))

    #print(f"lenth value is {len(closest_row2[:-1])}")  
    for i in range(0, len(closest_row2[:-1])):
        if i in [6,8,9,11,12,13,15]:
            closest_row2[i] = 26
            weatherlink_forcasted_values.append(int(closest_row2[i]) + np.random.randint(0,6))
        elif i in [7]:
            closest_row2[i] = 90
            weatherlink_forcasted_values.append(int(closest_row2[i]) + np.random.randint(0,6))
        elif i in [10]:
            closest_row2[i] = 10
            weatherlink_forcasted_values.append(int(closest_row2[i]) + np.random.randint(0,6))
        elif i in [14]:
            closest_row2[i] = np.random.rand()
            weatherlink_forcasted_values.append(closest_row2[i])

    #print(weatherlink_forcasted_values)
    #print(weatherlink_forcasted_values)
    return (airlink_forcasted_values, weatherlink_forcasted_values)