from datetime import datetime, timedelta
import pandas as pd


def date_arithmetics(start_date, durations, mode = 'addition'):
    parsed_start_date = datetime.strptime(start_date, "%d-%m-%Y")
    
    if mode.lower() == 'subtraction':
        pass
    elif mode.lower() == 'multiplication':
        pass
    elif mode.lower() == 'division':
        pass
    else:
        return (parsed_start_date + timedelta(days = durations)).strftime("%d-%m-%Y")

def get_hotel_geo_id_based_on_location(location):
    hotel_geo_data = pd.read_csv("C:/Projects/Python/DataScience/data/traveloka/traveloka hotel geo data.csv")
    return hotel_geo_data.set_index("location").loc[location]["hotel_geo_id"]