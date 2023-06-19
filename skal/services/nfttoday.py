import requests

from skal.utils.response import envia_request

JWT_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ3YWxsZXQiOiIweDJENDBmZjkzZjA3NThlRjc4QTE3M2NjNzU1MTE4YTY3MWVhOGQwOTQiLCJpYXQiOjE2ODcxOTk1ODEsImV4cCI6MTY4NzI0Mjc4MX0.HHSTgJNIkJwHqCsRua76db_yzzcqwbTzWi9QmYjNdkw'

class MintNftPolygonService:
    def __init__(self) -> None:
        self.url_mint_nft = f'https://ticketing.0xmint.io/api/ticket'
        self.url_0xmint = f'https://api.0xmint.io'
        self.headers_refresh = {
            "x-api-key": "3fd89e0e-8ce0-434e-8b91-34b18cdb1735",
            "x-refresh-token": "1d259010924c30f8f0c070d5669e71890906402940e3a8d6009d8d096de5a489"
        }
        self.headers = {
            "x-api-key": "3fd89e0e-8ce0-434e-8b91-34b18cdb1735",
            "x-auth-token": JWT_TOKEN
        }
        self.wallet = "0x2D40ff93f0758eF78A173cc755118a671ea8d094"

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
status = MintNftPolygonService().get_bath_collections()