import requests
from pprint import pprint

class Dfuse:

    DFUSE_SERVERKEY = "server_42be8d5f944cb5747f3d65ba81468bf2"

    def updateBearerToken(self):
        endpoint = "https://auth.dfuse.io/v1/auth/issue"
        data = '{"api_key":"'+self.DFUSE_SERVERKEY+'"}'
        headers = {"Content-Type": "application/json"}
        response = requests.post(endpoint, data=data, headers=headers).json()
        return(response['token'])

    def getEosTxn(self, txnHash, bt):
        endpoint = f"https://jungle.eos.dfuse.io/v0/transactions/{txnHash}"
        data = {"json": True}
        # print(bt)
        headers = {"Authorization": f"Bearer {bt}"}
        txnDat = requests.post(endpoint, data=data, headers=headers).json()

        return txnDat
