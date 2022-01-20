import base64


def encoding(message):
    sample_string_bytes = message.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def decoding(message):
    base64_bytes = message.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    decoded_msg = sample_string_bytes.decode("ascii")

    return decoded_msg
