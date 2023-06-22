from typing import Dict, Any, Union


class RestClient:
    def __init__(self) -> None:
        self.estabelecimento_index_name = ""

    def get_estabelecimento(cnes: str) -> Dict[str, Union[str, None, Any]]:
        pass


cnes_rest_client = RestClient()
