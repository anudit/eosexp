import eospy.cleos
import os
import pytz
import eospy.keys

antestacc111_key = eospy.keys.EOSKey('5JvpRugDVrZvX8yCq9sgszDgcYTqRvNRLMGnXYrAJbu5ScyYjoi')
ce = eospy.cleos.Cleos(url='http://jungle2.cryptolions.io:80')

arguments = {
            "from": "anuditnagar2",  # sender
            "to": "antestacc111",  # receiver
            "quantity": '100000000000.0000 ANT',
            "memo": "Transfer Test",
        }
payload = {
        "account": "antestacc111",
        "name": "transfer",
        "authorization": [{
            "actor": "anuditnagar2",
            "permission": "active",
        }],
    }

#Converting payload to binary
data=ce.abi_json_to_bin(payload['account'],payload['name'],arguments)
payload['data']=data['binargs']
trx = {"actions": [payload]}


import datetime as dt
trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))

resp = ce.push_transaction(trx, antestacc111_key, broadcast=True)
print('------------------------------------------------')
print(resp)
print('------------------------------------------------')

