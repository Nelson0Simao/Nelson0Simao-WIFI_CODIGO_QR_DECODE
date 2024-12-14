# qr_decoder/utils.py

import os

def is_valid_file_path(path):
    """
    Verifica se o caminho do arquivo é válido e se o arquivo existe.
    """
    return os.path.isfile(path)

