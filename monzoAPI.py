from monzo.monzo import Monzo # Import Monzo class
from pprint import pprint
import json
import hashlib
import numpy as np

client = Monzo('eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJlYiI6InpZS2pBb3lWV0RjNmNkMkd0TkFmIiwianRpIjoiYWNjdG9rXzAwMDA5ZDZtMDZNVnZyZW91bkVnSFIiLCJ0eXAiOiJhdCIsInYiOiI1In0.SllGxvyF4RO4f093tPg3mgIZCc-Z-tsIxKG7dkX8HspMyKDGF5FQIc-fRf9CHzcE3GQOvI9oqos_jE1xKJBfYw') # Replace access token with a valid token found at: https://developers.monzo.com/
# account_id = client.get_first_account()['id'] # Get the ID of the first account linked to the access token
account_id = "acc_00009VIJcdBdP5vmFVETYn"
balance = client.get_balance(account_id) # Get your balance object
#print("My balance is ", balance['balance']) # 100000000000
#print(balance['currency']) # GBP
#print(balance['spend_today']) # 2000



transactions = client.get_transactions(account_id)
# loaded_json = json.loads(transactions)
#for x in transactions:
	#print("{}: {}".format(x, transactions[x]))

# pprint(transactions['transactions'][-1])
trans = transactions['transactions']
import numpy as np

def weightingFunction(number):
    return abs(number) #* 250

def main():
    # for every single transaction, update it with the weighting function abs(transaction) * 250
    newList = []
    for c, t in enumerate(trans):
        if (t['amount']) < 0:
            tempAmount = t['amount']
            tempAmount = weightingFunction(tempAmount)
            transactions['transactions'][c]['amount'] = tempAmount
            newList.append(tempAmount)

    transactions['transactions'][-1]['isHighRiskCountry'] = 0
    

    ##transactions['transactions']['isHighRiskCountry'] = 1
    #transactions = transactions['transactions'][0]['isHighRiskCountry'] = 1
    #pprint(['transactions'][0])
    ##pprint(transactions['transactions'][0])
    
def getFraud():
    transactionAmount = transactions['transactions'][-1]['amount']
    isDeclined = 0
    if transactions['transactions'][-1]['merchant']['address']['formatted'] == "United Kingdom":
        isForeignTransaction = 0
    else:
        isForeignTransaction = 1
    isHighRiskCountry = transactions['transactions'][-1]['isHighRiskCountry']

    s = transactions['transactions'][-1]['merchant']['id']
    merchantId = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10**8

    toSum = 0
    counter = 0
    for t in transactions['transactions']:
        toSum = toSum + transactions['transactions'][counter]['amount']
        counter = counter + 1
    average = toSum / counter

    # Merchant_id 	Average Amount/transaction/day 	Transaction_amount 	Is declined 	isForeignTransaction 	isHighRiskCountry
    #return [[merchantId, average, transactionAmount, isDeclined, isForeignTransaction, isHighRiskCountry]]
    return [[average, 500000, 0, 1, 1]]
    

def getLatestData():
    """
    Transaction_amount
    Is declined 	
    isForeignTransaction
    isHighRiskCountry"""

    transactionAmount = transactions['transactions'][-1]['amount']
    isDeclined = 0
    if transactions['transactions'][-1]['merchant']['address']['formatted'] == "United Kingdom":
        isForeignTransaction = 0
    else:
        isForeignTransaction = 1
    isHighRiskCountry = transactions['transactions'][-1]['isHighRiskCountry']

    s = transactions['transactions'][-1]['merchant']['id']
    merchantId = int(hashlib.sha256(s.encode('utf-8')).hexdigest(), 16) % 10**8

    toSum = 0
    counter = 0
    for t in transactions['transactions']:
        toSum = toSum + transactions['transactions'][counter]['amount']
        counter = counter + 1
    average = toSum / counter

    # Merchant_id 	Average Amount/transaction/day 	Transaction_amount 	Is declined 	isForeignTransaction 	isHighRiskCountry
    #return [[merchantId, average, transactionAmount, isDeclined, isForeignTransaction, isHighRiskCountry]]
    return [[average, transactionAmount, isDeclined, isForeignTransaction, isHighRiskCountry]]



main()

def do():
    import machineLearning
    x = np.reshape(getLatestData(), (1, 5))
    #machineLearning.predict(x, "Monzo")
    machineLearning.predictKNN(x, "Monzo", "Non Fraudulent Data")


    x = np.reshape(getFraud(), (1, 5))
    machineLearning.predictKNN(x, "Monzo", "Fraudulent Data")

    x = np.reshape(getFraud(), (1, 5))
    machineLearning.predict(x, "Monzo", "Fraudulent Data")

do()