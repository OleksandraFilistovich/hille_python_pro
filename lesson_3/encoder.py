def encoder(origin_file, origin_encoding, encoded_file, encoded_encoding):
    """Function encoded file and writes it to the new one."""
    with open(origin_file, "r", encoding=origin_encoding) as file:
        lines = file.readlines()
    with open(encoded_file, "w", encoding=encoded_encoding) as file:
        file.writelines(lines)


source_encoding = "latin1"
source_file = "./source/rockyou.txt"

target_encoding = "utf-8"
target_file = "./source/rockyou_encoded.txt"

encoder(source_file, source_encoding, target_file, target_encoding)
