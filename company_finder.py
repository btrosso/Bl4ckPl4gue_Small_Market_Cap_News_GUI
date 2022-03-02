import os
import requests
from company_data import Company
from dotenv import load_dotenv
load_dotenv()

ALPHAV_ENDPOINT = "https://www.alphavantage.co/query"


class CompanyFinder:
    def __init__(self):
        pass

    def get_company_data(self, company):
        query_params = {
            "function": "OVERVIEW",
            "symbol": company,
            "apikey": os.environ["ALPHAV_API_KEY"],
        }
        overview = requests.get(url=f"{ALPHAV_ENDPOINT}", params=query_params).json()
        company_data = Company(overview)
        return company_data
