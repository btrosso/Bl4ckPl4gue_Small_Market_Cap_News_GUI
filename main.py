from user_interface import UserInterface
from company_finder import CompanyFinder

company_finder = CompanyFinder()
app = UserInterface()

# TODO: DECIDE HOW TO DO THE API STUFF OOP STYLE

ticker_list = company_finder.stock_screener()
# for ticker in ticker_list:
#     company_data = company_finder.get_company_data(ticker)
#     print(company_data.market_cap)
