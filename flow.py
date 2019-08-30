import requests
from eoslib import issue, transfer, retire, getBalance
from dfuse import Dfuse

df = Dfuse()
bearerToken = "kk"

eosTxnHashDict = {
    "a56d744250e3744bb20f311a56cb7a6a1129a8202751d2245b677763924f5baa":"someaddress",
    "a56d744250e3744bb20f311a56cb7a6a1129a8202751d2245b677763924f5bab":"someaddress"
    }

while(len(eosTxnHashDict) != 0):

    for txnHash in eosTxnHashDict:

        print(f"[EOS-x SWAP] ==> Checking {txnHash}")

        txnDat = df.getEosTxn(txnHash, bearerToken)
        # print(txnDat)

        try:
            if(txnDat['code'] and txnDat['code'] == 'auth_invalid_token_error'):
                print(f"[EOS-x SWAP] ==> Updating Bearer Token as {txnDat['code']}")
                bearerToken = df.updateBearerToken()
        except:
            try:
                if(txnDat['code'] and txnDat['code'] == 'data_trx_not_found_error'):
                    print(f"[EOS-x SWAP] ==> INVALID HASH {txnHash}")
                    eosTxnHashDict.pop(txnHash)
            except:
                try:
                    if(txnDat['code']):
                        print(f"[EOS-x SWAP] ==> UNKNOWN CODE {txnDat['code']}")
                        eosTxnHashDict.pop(txnHash)
                except:
                    if (txnDat['execution_irreversible'] == False):
                        print(f"[EOS-x SWAP] ==> NOT YET IRREVERSIBLE {txnHash}")
                    elif (txnDat['execution_irreversible'] == True):
                        print(f"[EOS-x SWAP] ==> MINTING AND TRANSFERRING")
                        print(f"[EOS-x SWAP] ==> UPDATING DB")
                        eosTxnHashDict.pop(txnHash)

