import requests
import os
from skal.utils.response import envia_request


class MintNftPolygonService:
    def __init__(self) -> None:
        self.url_mint_nft = f'https://ticketing.0xmint.io/api/ticket'
        self.url_0xmint = f'https://api.0xmint.io'
        self.headers_refresh = {
            "x-api-key": os.environ.get('X_API_KEY'),
            "x-refresh-token": os.environ.get('X_REFRESH_TOKEN')
        }
        self.headers = {
            "x-api-key": os.environ.get('X_API_KEY'),
            "x-auth-token": os.environ.get('JWT_TOKEN')
        }
        self.wallet = os.environ.get('WALLET')

    def fazer_upload_assets(self):
        try:
            data = {
                "wallet": self.wallet,
                "sessionName": "",
                "csv": "",
                "assets": "",
                "preview": ""
            }
            url = f'{self.url_0xmint}/v2/batch/uploadAssets'
            response = envia_request(url=url, metodo='post', headers=self.headers, data=data)
            # Retorna a SessionID
            return response.text
        except Exception as e:
            e
    
    def fazer_deploy_ou_update_contrato(self):
        try:
            url = f'{self.url_0xmint}/v2/batch/updateCollectionData'
            data = {'sessionId': '','wallet': self.wallet}
            response = envia_request(url=url, metodo='post', headers=self.headers, data=data)
            return response.text
        except Exception as e:
            ...

    def pegar_status(self, sessionID):
        try:
            url = f'{self.url_0xmint}/v2/batch/checkStatus/${sessionID}'
            response = envia_request(url=url, metodo='get', headers=self.headers)
            return response.text
        except Exception as e:
            ...

    def depositar_gas(self, sessionID):
        try:
            url = f'{self.url_0xmint}/v2/batch/getEstimatedGas/${sessionID}'
            response = envia_request(url=url, metodo='get', headers=self.headers)
            return response.text
        except Exception as e:
            ...
    
    def mintar_NFT(self):
        ...

    def pegar_detalhes_do_mint(self):
        ...

    def refresh_jwt_0xmint(self):
        payload = {
            "wallet": self.wallet,
        }
        url = f'{self.url_0xmint}/v2/refreshJWT'
        response = requests.post(url, headers=self.headers_refresh, data=payload)
        return response

# response = MintNftPolygonService().mint()
status = MintNftPolygonService().fazer_deploy_ou_update_contrato()