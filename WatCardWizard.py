# Joshua Simpson, 09/02/14
# This module calculates how much you've spent on your WatCard for a 
# given time period.

from BeautifulSoup import BeautifulSoup
import urllib

id_num = int(raw_input('Welcome to the WatCard Wizard. What is your student number? '))
id_pin = int(raw_input('And your PIN? '))
start_date = raw_input('Please enter the start date for records, in MM/DD/YYYY form: ')
end_date = raw_input('End date (MM/DD/YYYY): ')

usr = urllib.urlencode({
   'acnt_1': id_num,
   'acnt_2': id_pin,
   'DBDATE': start_date,
   'DEDATE': end_date,
   'PASS' : 'PASS',
   'STATUS' : 'HIST',
   })
    
url = 'https://account.watcard.uwaterloo.ca/watgopher661.asp'
resp = urllib.urlopen(url, usr)
resp = resp.read()
    
soup = BeautifulSoup(''.join(resp))
table = soup.find('table', id='oneweb_financial_history_table')

charges_html = table.findAll('td', id='oneweb_financial_history_td_amount')
charges = []

for td in charges_html:
    charges.append(float(td.find(text=True)))
    
def remove_credits(x):
   if x >= 0:
      return 0
   else: return x 
   
print 'You\'ve spent ${0} in the given period!'.format(abs(sum(map(remove_credits, charges))))
