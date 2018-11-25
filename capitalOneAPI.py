import requests
from pprint import pprint
import numpy as np



headers = {
  'Version': '1.0',
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

accounts = requests.get('https://sandbox.capitalone.co.uk/open-banking-example/accounts', params={

}, headers = headers, verify=False)

transactions=requests.get('https://sandbox.capitalone.co.uk/open-banking-example/transactions', params={

}, headers = headers, verify=False)
# This returns all transactions for all accounts
trans = transactions.json()
# Assigns transaction data to a variable
# Since it is just a list we can use the index to access one particular transaction

max = 0
x = []
for transacts in trans:
    x.append(float(transacts['amount']['amount']))
for item in x:
    if item>max:
        max=item


i = 0
totalAmount=0
while i<len(trans):
    myRecord=trans[i]
    var=myRecord['amount']['amount']
    totalAmount=totalAmount+float(var)
    i=i+1



# Finding the average 
total=len(trans)
averageTransaction=totalAmount/total



record=trans[-1]
del record['addressLine']
del record['bookingDateTime']
del record['creditDebitIndicator']
del record['status']
del record['amount']['currency']
del record['merchantDetails']
del record['accountId']

record.update({'isForeignTransaction': 0})
record.update({'isHighRiskCountry': 0})
record.update({'Is declined': 0})
record.update({'Average Amount/transaction/day': averageTransaction})


num=record['amount']['amount']
record.update({'Transaction_amount': float(num)})

del record['amount']
# Merchant_id 	Average Amount/transaction/day 	Transaction_amount 	Is declined 	isForeignTransaction 	isHighRiskCountry



def do():
  x = [[record['Average Amount/transaction/day'], record['Transaction_amount'], record['Is declined'], record['isForeignTransaction'], record['isHighRiskCountry']]]

  import machineLearning
  x = np.reshape(x, (1, 5))
  # Average amount of transactions per day, transaction amount, was the transaction declined? Is the transaction performed in a foreign country? Is that country a 'high risk' country according to the Foreign Office?
  machineLearning.predictKNN(x, "Capital One","Non Fraudulent Data")
  # machineLearning.predict(x, "Capital One", "Non Fraudulent Data")

  x = [[record['Average Amount/transaction/day'], 500000, 0, 1, 1]]
  x = np.reshape(x, (1, 5))
  machineLearning.predictKNN(x, "Capital One","Fraudulent Data")
  # machineLearning.predict(x, "Capital One", "Fraudulent Data")
