# This file will be used to put the company_data class to handle all the company financial data

class Company:
    def __init__(self, overview):
        self.market_cap = overview["MarketCapitalization"]
        self.sector = overview["Sector"]
        self.name = overview["Name"]
