import os
import datetime as dt

import pandas as pd

def check_os_variables():
    try:
        assert os.environ.get('BASE_POSTAL_CODE', None) is not None
        assert os.environ.get('OPENAI_API_KEY', None) is not None
    except Exception as e:
        raise EnvironmentError(f"""
    Missing keys: BASE_POSTAL_CODE and OPENAI_API_KEY in your environment variables: {e}. 
    Make sure you add a house postal code (or address) as well as a valid OpenAI API token to your
    zshrc, bashrc or any other enviroment file this app will be accessing. 
            """)

def get_now() -> str:
    return dt.datetime.now().strftime('%Y-%m-%d %H_%M_%S')

def export_to_csv(df: pd.DataFrame):
    date_time = get_now()
    df.to_csv(f'ams_school_analysis_{date_time}.csv', index=False)
