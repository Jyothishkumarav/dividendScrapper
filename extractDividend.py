import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from nselists import stock_details
from telgramMsgPublisher import send_message


def print_data(obj):
    for record in obj:
        for v in record.values():
            print("{:<30} {:<12} {:<8}".format(v, end=' '))
        print()


def print_data_dup(obj):
    for record in obj:
        c, e, a = record.values()
        print("{:<50} {:<12} {:<8}".format(c, str(e), a), end=' ')
        stock_details(c)
        print()
def send_stock_date(obj):
    for record in obj:
        c, e, a = record.values()
        text_sample = "{:<50} {:<12} {:<8}".format(c, str(e), a)
        print(text_sample)
        stock_detail = stock_details(c)
        text_sample_telegram_Msg  = text_sample + ' ---- ' +stock_detail
        send_message(text_sample_telegram_Msg)

        print()


def filter_stocks(obj, amount):
    filter_dic = [ele for ele in obj if ele['amount'] > amount]
    return filter_dic


def filter_stocks_wit_date(obj, amount, still_date):
    till_date = datetime.datetime.strptime(still_date, '%d %b %Y')
    filter_dic = [ele for ele in obj if
                  ele['amount'] > amount and datetime.datetime.strptime(str(ele['exdate']), '%d %b %Y') < till_date]
    return filter_dic


options = Options()
options.headless = True
chrome_path = 'chromedriver.exe'
driver = webdriver.Chrome(chrome_path, options=options)
driver.get('https://www.bseindia.com/corporates/corporates_act.html')
results = driver.find_elements_by_css_selector(
    "div[class =\"container-fluid marketstartarea\"] table[class=\"mGrid ng-scope\"] tr[class='TTRow ng-scope']")
div_list = list()

for result in results:
    records = result.find_elements_by_tag_name('td')
    div_record = dict()
    div_bonus = str(records[3].text)
    ex_str_date = str(records[2].text)
    today = datetime.datetime.today()
    ex_date = datetime.datetime.strptime(ex_str_date, '%d %b %Y')
    if "dividend" in div_bonus.lower() and ex_date > today:
        div_record['company'] = records[1].text
        div_record['exdate'] = ex_str_date
        amount = div_bonus.split("-")[-1]
        try:
            div_record['amount'] = float(amount)
        except:
            div_record['amount'] = float("0.0")
        div_list.append(div_record)

driver.quit()
#filter_dict = filter_stocks(div_list, 10.0)
filter_amount_date = filter_stocks_wit_date(div_list, 10.0, '22 Aug 2021')
send_stock_date(filter_amount_date)
