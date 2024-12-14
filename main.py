#main.py

import argparse
from decoder import decode_qr_code
from utils import is_valid_file_path

def main():
    # Configura a interface de linha de comando
    parser = argparse.ArgumentParser(
            description="Decodificar QR Code de Wi-Fi de uma imagem.",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        '-f', '--file',
        type=str,
        required=True,
        help="Caminho da imagem contendo o QR Code."
    )

    args = parser.parse_args();

    # Verifica se o arquivo existe
    if not is_valid_file_path(args.file):
        print(f"Arquivo '{args.file}' não encontrado.")
        return

    try:
        # Chama a função de decodificação
        qr_data, qr_type = decode_qr_code(args.file)
        print(f"QR Code Detectado: Tipo = {qr_type}, Dados = {qr_data}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()

