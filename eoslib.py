import eospy.cleos
import os
import pytz
import eospy.keys
from pprint import pprint
import json
import datetime as dt

OWNER_ACCOUNT = "anuditnagar2"

OWNER_ACCOUNT_KEY = "5JDvKERkzz5rVX9DwkMpcG4rS34Dwcdo2CwJ5jH4nyDewswYDeS"
ENDPOINT = "https://api.jungle.alohaeos.com:443"

OWNER_ACCOUNT_KEY = eospy.keys.EOSKey(OWNER_ACCOUNT_KEY)
ce = eospy.cleos.Cleos(url=ENDPOINT)

def transfer(acct = "antestacc111", amt="0.0000 ANT"):

    arguments = {
                "from": OWNER_ACCOUNT,  # sender
                "to": acct,  # receiver
                "quantity": amt,
                "memo": "tbnb16uq5gcvg25psr2gqt5y0svn4j53n39lzxkuvl7",
            }
    payload = {
            "account": OWNER_ACCOUNT,
            "name": "transfer",
            "authorization": [{
                "actor": OWNER_ACCOUNT,
                "permission": "active",
            }],
        }

    #Converting payload to binary
    data=ce.abi_json_to_bin(payload['account'],payload['name'],arguments)
    payload['data']=data['binargs']
    trx = {"actions": [payload]}
    trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))

    resp = ce.push_transaction(trx, OWNER_ACCOUNT_KEY, broadcast=True)
    return(resp)

def issue(acct = "antestacc111", amt="0.0000 ANT"):

    arguments = {
                "to": acct,  # receiver
                "quantity": amt,
                "memo": "Multichain Swap Issue",
            }
    payload = {
            "account": OWNER_ACCOUNT,
            "name": "issue",
            "authorization": [{
                "actor": OWNER_ACCOUNT,
                "permission": "active",
            }],
        }

    #Converting payload to binary
    data=ce.abi_json_to_bin(payload['account'],payload['name'],arguments)
    payload['data']=data['binargs']
    trx = {"actions": [payload]}
    trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))

    resp = ce.push_transaction(trx, OWNER_ACCOUNT_KEY, broadcast=True)
    return(resp)

def retire(amt="0.0000 ANT"):

    arguments = {
                "quantity": amt,
                "memo": "Multichain Swap Retire",
            }
    payload = {
            "account": OWNER_ACCOUNT,
            "name": "retire",
            "authorization": [{
                "actor": OWNER_ACCOUNT,
                "permission": "active",
            }],
        }

    #Converting payload to binary
    data=ce.abi_json_to_bin(payload['account'],payload['name'],arguments)
    payload['data']=data['binargs']
    trx = {"actions": [payload]}
    trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))

    resp = ce.push_transaction(trx, OWNER_ACCOUNT_KEY, broadcast=True)
    pprint(resp)
    return(response['transaction_id'])

def getBalance(acct = "antestacc111"):
    resp = ce.get_table(OWNER_ACCOUNT, acct, "accounts")
    balance = resp['rows'][0]['balance']
    print(balance)
    return(balance)

# def getTxnStatus(acct = "antestacc111"):

# pprint(ce.get_transaction("a56d744250e3744bb20f311a56cb7a6a1129a8202751d2245b677763924f5bab"))

# getBalance("antestacc111")
transfer("antestacc111", "100.0000 ANT")
# issue("antestacc111", "100.0000 ANT")
# retire( "100.0000 ANT" )
