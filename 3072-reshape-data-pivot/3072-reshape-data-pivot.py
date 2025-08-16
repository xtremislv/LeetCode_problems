import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    aa = weather.pivot(columns= 'city', values ='temperature', index ='month')
    return aa