# Joshua Simpson, 09/02/14
# This module extracts all charges from a WatCard balance table
# and stores it as a .csv

from BeautifulSoup import BeautifulSoup

id_num = raw_input('Welcome to the WatCard Wizard. What is your student number?')
id_pin = raw_input('And your PIN?')

#open file, get text
data = open('January Account History.txt', 'r')
html = data.read() 
#convert text to BeautifulSoup friendly object
soup = BeautifulSoup(''.join(html))
data.close()

table = soup.find('table')

charges = table.findAll('td', id='oneweb_financial_history_td_amount')

for td in charges:
   print td.find(text=True)

#print text
