
from lib.utils import check_os_variables, get_now, export_to_csv
from lib.school_info_ai_analysis import PromptDataType
from lib.ams_school_info_scraper import fetch_school_data_from_city
from lib.openAI_tools import OpenAIClient
import lib.school_info_ai_analysis as ai_data

import pandas as pd


def produce_school_data(open_ai: OpenAIClient) -> pd.DataFrame:

    print(f"{get_now()} -> Scrapping the AMS city website...")
    schools = fetch_school_data_from_city()

    print(f"{get_now()} -> Will fetch data for: {len(schools)} schools...")
    rows = []
    for school in schools:
        ai_attributes = []
        for a in PromptDataType.get_all_types():
            ai_attributes.append(
                ai_data.get_ai_data(
                    openai_client=open_ai,
                    prompt_type=a,
                    school_name=school.name
                )
            )
        school.update_all_ai_attributes(ai_attributes)
        school.print_all_attributes()
        rows.append(school.turn_into_row())

    print(f"{get_now()} -> Done fetching data for all schools.")
    return pd.DataFrame(rows)

def main():

    print(f"{get_now()} -> Starting app...")

    check_os_variables()
    open_ai = OpenAIClient()

    df = produce_school_data(open_ai)
    export_to_csv(df)

    print(f"{get_now()} -> All done!")

if __name__ == "__main__":
    main()
