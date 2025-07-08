import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:

    weather = weather.sort_values('recordDate').reset_index(drop=True)
    rising_ids = []
    for i in range(1, len(weather)):
        if weather.loc[i, 'temperature'] > weather.loc[i - 1, 'temperature']:
            if (weather.loc[i,"recordDate"] - weather.loc[i-1,"recordDate"]).days == 1:

                rising_ids.append(weather.loc[i, 'id'])

    return pd.DataFrame({'id': rising_ids})
