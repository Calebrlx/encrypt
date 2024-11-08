# -------------------------------------------------------

import secrets
import statistics
from typing import Dict, List, Tuple


# -------------------------------------------------------

def add_round_key(data, round_key):
    # Adjusted to handle keys shorter than data by cycling the key
    return bytes([b ^ round_key[i % len(round_key)] for i, b in enumerate(data)])

def sub_bytes(data):
    return bytes([(b + 1) % 256 for b in data])

def inv_sub_bytes(data):
    return bytes([(b - 1) % 256 for b in data])

def shift_rows(data):
    return data[1:] + data[:1]

def inv_shift_rows(data):
    return data[-1:] + data[:-1]

def encrypt(data, key):
    data = add_round_key(data, key)
    data = sub_bytes(data)
    data = shift_rows(data)
    data = add_round_key(data, key)
    return data

def decrypt(data, key):
    data = add_round_key(data, key)
    data = inv_shift_rows(data)
    data = inv_sub_bytes(data)
    data = add_round_key(data, key)
    return data


# -------------------------------------------------------

class Cry():
    def __init__(self, data, x=1) -> None:
        self.data = data.encode()  # Keep as bytes for simplicity
        self.key = secrets.token_bytes(x)  # Key as bytes
        self.key_hex = self.key.hex()  # Hex representation for display/storage
        self.enc = False

    def tog(self):
        '''
        Toggle encryption
        '''
        if self.enc:
            print('Decrypting...')
            self.data = decrypt(self.data, self.key)
        else:
            print('Encrypting...')
            self.data = encrypt(self.data, self.key)
        self.enc = not self.enc
        return self.data
    
    def __del__(self) -> None:
        pass

# -------------------------------------------------------


def brute_force_decrypt(encrypted_hex_data: str) -> List[Tuple[int, bytes, List[Tuple[str, int]]]]:
    encrypted_data = bytes.fromhex(encrypted_hex_data)
    possible_keys = range(256)
    results = {}
    def tokenize(text: str) -> List[str]:
        # Implement your tokenization logic here
        # This is just a placeholder implementation
        tokens = text.split()
        return tokens

    def brute_force_decrypt(encrypted_hex_data: str) -> List[str]:
        encrypted_data = bytes.fromhex(encrypted_hex_data)
        possible_keys = range(256)
        results = {}

        for key in possible_keys:
            decrypted_data = decrypt(data=encrypted_data, key=bytes([key]))
            try:
                plaintext = decrypted_data.decode('utf-8')
                tokens = tokenize(plaintext)
                token_length = len(tokens)
                if key not in results:
                    results[key] = []
                results[key].append((plaintext, token_length))
            except UnicodeDecodeError:
                pass

        # Filter based on token length cutoff
        lengths = [value[0][1] for value in results.values()]
        cutoff = statistics.quantiles(lengths, n=4)[-1]
        filtered_results = [(key, results[key]) for key, values in results.items() for _, length in values if length <= cutoff]

        # Return top quarter of results based on some criterion (e.g., shortest token length)
        srtd = sorted(filtered_results, key=lambda x: x[1][0][1])[:len(filtered_results)//4]
        txt = []
        for item in srtd:
            found = False
            for st in txt:
                if item[1][0][0] == st:
                    found = True
                    break
            if not found:
                txt.append(item[1][0][0])
        return txt

    for key in possible_keys:
        decrypted_data = decrypt(data=encrypted_data, key=bytes([key]))
        try:
            plaintext = decrypted_data.decode('utf-8')
            token_length = len(enc.encode(plaintext))
            if key not in results:
                results[key] = []
            results[key].append((plaintext, token_length))
        except UnicodeDecodeError:
            pass

    # Filter based on token length cutoff
    lengths = [value[0][1] for value in results.values()]
    cutoff = statistics.quantiles(lengths, n=4)[-1]
    filtered_results = [(key, results[key]) for key, values in results.items() for _, length in values if length <= cutoff]

    # Return top quarter of results based on some criterion (e.g., shortest token length)
    srtd = sorted(filtered_results, key=lambda x: x[1][0][1])[:len(filtered_results)//4]
    txt = []
    for item in srtd:
        # print(item[1][0][0])
        found = False
        for st in txt:
            if item[1][0][0] == st:
                found = True
                break
        if not found:
            txt.append(item[1][0][0])
    return txt

#? this should never return an empty array, since the encryption is specificly set for this code. this is also the only time ive seen this while running this function
# Encrypting...
# Encrypted data:  9a6d6d6c21746c736d6549

# []
#?


# --------------------- Random fn's ---------------------

def hex_str():
    hex_str = "48656c6c6f20776f726c64"

    # Split hex string into pairs of hex digits
    hex_pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]

    # Convert each pair to an integer and create a bytes object
    bytes_obj = bytes([int(pair, 16) for pair in hex_pairs])

    return bytes_obj  # Output: b'Hello world'

def simple_key_expansion(key, rounds=10):
    # Placeholder for a simple key expansion
    # This example just repeats the key to match the number of rounds needed
    expanded_keys = [key[i % len(key): i % len(key) + 16] for i in range(rounds)]
    return expanded_keys


# -------------------------------------------------------

def cry(data):
    cry_instance = Cry(data, x=16)
    encrypted_data = cry_instance.tog()
    print("Encrypted:", encrypted_data)
    decrypted_data = cry_instance.tog()
    print("Decrypted:", decrypted_data.decode())

def brute(data):
    cry = Cry(data=data, x=1)
    dta = cry.tog().hex()
    print('Encrypted data: ', dta)
    print('')
    print(brute_force_decrypt(dta))
    


# -------------------------------------------------------

def main(data):
    print(brute(data=data))

if __name__ == "__main__":
    main(data='Hello world')
