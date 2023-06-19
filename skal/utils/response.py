import requests
from requests import ReadTimeout


def envia_request(
    url, metodo, timeout=None, tentativas=5, headers=None, params=None, data=None, verify=None, stream=None
):
    """
    Tenta fazer a request para a url por x tentativas (default=5), para o caso do serviço externo não estar disponível no momento.
    Args:
        url: url do serviço externo
        metodo: get ou post
        timeout: tempo máximo em segundos para a requisição
        tentativas: número máximo de tentativas para a requisição
        headers: headers a serem setados na requisição
        data: dados a serem enviados
        verify: verificação de certificação SSL
        stream: fluxo do conteúdo
    Returns:
        response: resposta da requisição
    """

    last_exception = None
    for _ in range(tentativas):
        try:
            if metodo == 'get':
                return requests.get(url, timeout=timeout, params=params, headers=headers, verify=False, stream=stream)
            elif metodo == 'put':
                return requests.put(url, timeout=timeout, params=params, headers=headers, data=data, verify=False)
            elif metodo == 'delete':
                return requests.delete(url, timeout=timeout, params=params, headers=headers, data=data, verify=False)
            else:
                return requests.post(url, timeout=timeout, params=params, headers=headers, data=data, verify=False)
        except Exception as ex:
            last_exception = ex

    if last_exception and isinstance(last_exception, ReadTimeout):
        raise Exception('TIMEOUT', 'Não foi possível acessar o serviço externo solicitado.')

    raise Exception('SERVICO_INDISPONIVEL', f'URL {url} não disponível.')
