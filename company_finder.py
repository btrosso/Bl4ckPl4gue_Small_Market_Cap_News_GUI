import os
import requests
from company_data import Company
from dotenv import load_dotenv
load_dotenv()

ALPHAV_ENDPOINT = "https://www.alphavantage.co/query"
FMP_ENDPOINT = "https://financialmodelingprep.com/api/v3"


class CompanyFinder:
    def __init__(self):
        pass

    def stock_screener(self):
        ticker_list = []
        screening_criteria = {
            "marketCapMoreThan": 1000000000,
            "marketCapLowerThan": 3000000000,
            "volumeMoreThan": 1000000,
            "exchange": "nyse,nasdaq",
            "apikey": os.environ["FMP_API_KEY"]
        }
        tickers_json = requests.get(
            url=f"{FMP_ENDPOINT}/stock-screener",
            params=screening_criteria
        ).json()
        for ticker in tickers_json:
            ticker_list.append(ticker["symbol"])
        return ticker_list

    def get_company_data(self, ticker):
        query_params = {
            "function": "OVERVIEW",
            "symbol": ticker,
            "apikey": os.environ["ALPHAV_API_KEY"],
        }
        overview = requests.get(url=f"{ALPHAV_ENDPOINT}", params=query_params).json()
        company_data = Company(overview)
        return company_data
