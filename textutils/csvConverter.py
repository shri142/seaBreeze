import csv

def select_columns(input_csv, output_csv, columns_to_select):
    try:
        with open(input_csv, 'r', newline='') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames

            selected_columns = [col for col in columns_to_select if col in fieldnames]

            with open(output_csv, 'w', newline='') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=selected_columns)
                writer.writeheader()

                for row in reader:
                    selected_row = {col: row[col] for col in selected_columns}
                    writer.writerow(selected_row)

        print(f"Selected columns {', '.join(selected_columns)} saved to {output_csv}")
    except FileNotFoundError:
        print("File not found. Please provide valid file paths.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
input_file_path = '../static/data1.csv'  # Replace 'input.csv' with your CSV file path
output_file_path = '../static/output1.csv'  # Replace 'output.csv' with the desired output file path
columns_to_keep = ['AQI', 'PM 1 - ug/m³', 'PM 2.5 - ug/m³',
'PM 10 - ug/m³', 'Temp - °C', 'Hum - %', 'Dew Point - °C',
'Wet Bulb - °C', 'Heat Index - °C','Date & Time']  
select_columns(input_file_path, output_file_path, columns_to_keep)
