from user_interface import UserInterface
from company_finder import CompanyFinder

company_finder = CompanyFinder()

# app = UserInterface()

company_list = ["AAPL"]

# TODO: DECIDE HOW TO DO THE API STUFF OOP STYLE

for company in company_list:
    company_data = company_finder.get_company_data(company)
    print(company_data.market_cap)
