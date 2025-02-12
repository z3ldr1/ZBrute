import os
import itertools
import string

def password_generator(length_range, base_file_name, buffer_size=1024*1024*1024*10): # 10 GB buffer size
    folder_name = "wordlists"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    file_number = 0
    file_name = os.path.join(folder_name, f"{base_file_name}_{file_number}.txt")

    while os.path.exists(file_name) and os.path.getsize(file_name) > buffer_size:  # 10 GB threshold
        file_number += 1
        file_name = os.path.join(folder_name, f"{base_file_name}_{file_number}.txt")

    file = open(file_name, 'w')

    for length in range(*length_range):
        password_iter = itertools.product(string.ascii_letters + string.digits + string.punctuation, repeat=length)
        for password_chars in password_iter:
            password = ''.join(password_chars)
            password_line = f"{password}\n"
            file.write(password_line)

            if file_number % (buffer_size // len(password_line)) == 0:
                file.flush()
                os.fsync(file.fileno())
                file.close()
                file_number += 1
                file_name = os.path.join(folder_name, f"{base_file_name}_{file_number}.txt")
                file = open(file_name, 'w')

    file.close()
    return file_name

if __name__ == "__main__":
    base_file_name = "passwords"
    wordlist = password_generator(range(8, 10), base_file_name)  # Set the number of threads to 10
    print(f"Wordlist generated: {wordlist}")


