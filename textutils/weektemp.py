import pandas as pd
import random

# Load the Excel file
excel_file = "textutils/air.csv"  # Replace "your_excel_file.xlsx" with the path to your Excel file

# Read the specific columns from the Excel file
df = pd.read_csv(excel_file)
array1 = df["AQI"].tolist() 
array2 = df["Temp"].tolist()
array3 = df["Humidity"].tolist()
array4 = df["HeatIndex"].tolist()

def get_val():
    # Generate a random number between 0 and the length of the arrays
    random_number = random.randint(10, 90)
    AQI = []
    Temp = []
    Hum = []
    HI = []


    
    # Return the values at that index from the three arrays
    #print(random_number)
    for i in range(0,7):
        AQI.append(int(array1[random_number + i]))
        Temp.append(int(array2[random_number + i]))
        Hum.append( int(array3[random_number + i]))
        HI.append(int(array4[random_number + i]))
    
    return AQI,Temp,Hum,HI


