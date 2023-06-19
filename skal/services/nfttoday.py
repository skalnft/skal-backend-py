import requests

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

    
    def create_event(self):
        data = {
            "wallet": self.wallet,
            "eventId": "08a6e226-4fa2-4fe5-aa3d-fc39c17a2720",
            "personalDetails": "My Event Teste",
        }
        url = requests.post(f'{self.url_mint_nft}/user/create', headers=self.headers, data=data)
        return url
    
    def get_user_status(self):
        url = requests.get(f'{self.url_mint_nft}/user/scan/0x2D40ff93f0758eF78A173cc755118a671ea8d094/08a6e226-4fa2-4fe5-aa3d-fc39c17a2720', headers=self.headers, data={})
        return url
    
    def refresh_jwt_0xmint(self):
        payload = {
            "wallet": self.wallet,
        }
        url = f'{self.url_0xmint}/v2/refreshJWT'
        response = requests.post(url, headers=self.headers_refresh, data=payload)
        return response
    
    def mint_batch_nft(self):
        url = f'{self.url_0xmint}/v2/batch/uploadAssets'
        response = requests.post(url, headers=self.headers, data={})
        return response
    
    def get_bath_collections(self):
        url = f'{self.url_0xmint}/v2/batch/collection/${self.wallet}'
        response = requests.get(url, headers=self.headers)
        return response
    

# response = MintNftPolygonService().mint()
status = MintNftPolygonService().get_bath_collections()