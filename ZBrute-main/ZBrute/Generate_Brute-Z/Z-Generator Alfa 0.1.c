#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <dirent.h>
#include <sys/stat.h>
#include <unistd.h>

#define BUFFER_SIZE 1024*1024*1024*10 // 10 GB buffer size
#define FOLDER_NAME "wordlists"

void password_generator(int min_length, int max_length, char *base_file_name) {
    DIR *dir;
    struct dirent *ent;
    struct stat statbuf;
    char file_name[256];
    int file_number = 0;
    FILE *file;

    // Cria o diretório se não existir
    if ((dir = opendir(FOLDER_NAME)) == NULL) {
        mkdir(FOLDER_NAME, 0777);
    }

    // Encontra o próximo arquivo disponível
    while (1) {
        sprintf(file_name, "%s/%s_%d.txt", FOLDER_NAME, base_file_name, file_number);
        if (access(file_name, F_OK) == -1 || stat(file_name, &statbuf) == -1 || statbuf.st_size < BUFFER_SIZE) {
            break;
        }
        file_number++;
    }

    file = fopen(file_name, "w");

    for (int length = min_length; length <= max_length; length++) {
        char password[length + 1];
        for (int i = 0; i < length; i++) {
            for (char c = 'a'; c <= 'z'; c++) {
                password[i] = c;
                for (int j = i + 1; j < length; j++) {
                    for (char d = 'a'; d <= 'z'; d++) {
                        password[j] = d;
                        for (int k = j + 1; k < length; k++) {
                            for (char e = 'a'; e <= 'z'; e++) {
                                password[k] = e;
                                // Gera todas as combinações de letras, números e símbolos
                                for (int l = 0; l < 62; l++) {
                                    char symbol;
                                    if (l < 26) {
                                        symbol = 'a' + l;
                                    } else if (l < 52) {
                                        symbol = 'A' + l - 26;
                                    } else {
                                        symbol = '0' + l - 52;
                                    }
                                    password[length - 1] = symbol;
                                    fprintf(file, "%s\n", password);
                                    if (ftell(file) >= BUFFER_SIZE) {
                                        fclose(file);
                                        file_number++;
                                        sprintf(file_name, "%s/%s_%d.txt", FOLDER_NAME, base_file_name, file_number);
                                        file = fopen(file_name, "w");
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    fclose(file);
    printf("Wordlist gerada: %s\n", file_name);
}

int main() {
    char base_file_name[] = "passwords";
    password_generator(8, 10, base_file_name);
    return 0;
}
