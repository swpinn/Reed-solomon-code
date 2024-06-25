# Ensure you have the reedsolo library installed
# You can install it using: pip install reedsolo

import reedsolo

def rs_encode(data, nsym):
    """
    Encodes data using Reed-Solomon code.
    
    :param data: The data to encode (bytes)
    :param nsym: The number of error correction symbols to add
    :return: Encoded data with error correction symbols appended
    """
    rs = reedsolo.RSCodec(nsym)
    encoded_data = rs.encode(data)
    return encoded_data

def rs_decode(encoded_data, nsym):
    """
    Decodes Reed-Solomon encoded data.
    
    :param encoded_data: The encoded data with errors (bytes)
    :param nsym: The number of error correction symbols used during encoding
    :return: Decoded data with errors corrected
    """
    rs = reedsolo.RSCodec(nsym)
    decoded_data = rs.decode(encoded_data)
    return decoded_data

def simulate_noise(encoded_data, error_count):
    """
    Simulates a noisy channel by introducing errors into the encoded data.
    
    :param encoded_data: The encoded data (bytes)
    :param error_count: The number of errors to introduce
    :return: Encoded data with errors
    """
    import random
    noisy_data = bytearray(encoded_data)
    for _ in range(error_count):
        pos = random.randint(0, len(noisy_data) - 1)
        noisy_data[pos] ^= random.randint(1, 255)  # Introduce a random error
    return noisy_data

if __name__ == "__main__":
    # Example usage
    message = b"Hello, this is a test message"
    nsym = 10  # Number of error correction symbols

    print("Original message:", message)

    # Encode the message
    encoded_message = rs_encode(message, nsym)
    print("Encoded message:", encoded_message)

    # Simulate a noisy channel
    noisy_message = simulate_noise(encoded_message, error_count=5)
    print("Noisy message:", noisy_message)

    # Decode the noisy message
    try:
        decoded_message = rs_decode(noisy_message, nsym)
        print("Decoded message:", decoded_message)
    except reedsolo.ReedSolomonError as e:
        print("Decoding failed:", e)
