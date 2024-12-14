# QuebradoQRCode-WIFI/decoder.py

from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_code(image_path):
    """
    Função para decodificar um código QR de uma imagem.
    """
    try:
        img = Image.open(image_path)
        qr_codes = decode(img)
        
        if not qr_codes:
            print("Nenhum QR Code encontrado na imagem.")
            return None
        
        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')
            qr_type = qr_code.type
            return qr_data, qr_type
    
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo {image_path} não encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao tentar abrir a imagem: {e}")

