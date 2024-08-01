<?php

const BUFFER_SIZE = 1024*1024*1024*10; // 10 GB buffer size
const FOLDER_NAME = "wordlists";

function password_generator($min_length, $max_length, $base_file_name) {
    $file_number = 0;
    $file_name = "$FOLDER_NAME/$base_file_name_$file_number.txt";

    // Cria o diretório se não existir
    if (!is_dir(FOLDER_NAME)) {
        mkdir(FOLDER_NAME, 0777);
    }

    // Encontra o próximo arquivo disponível
    while (file_exists($file_name) && filesize($file_name) >= BUFFER_SIZE) {
        $file_number++;
        $file_name = "$FOLDER_NAME/$base_file_name_$file_number.txt";
    }

    $file = fopen($file_name, "w");

    for ($length = $min_length; $length <= $max_length; $length++) {
        $password = "";
        for ($i = 0; $i < $length; $i++) {
            $password.= chr(rand(33, 126)); // Gera um caractere aleatório
        }
        fwrite($file, "$password\n");
        if (ftell($file) >= BUFFER_SIZE) {
            fclose($file);
            $file_number++;
            $file_name = "$FOLDER_NAME/$base_file_name_$file_number.txt";
            $file = fopen($file_name, "w");
        }
    }

    fclose($file);
    echo "Wordlist gerada: $file_name\n";
}

if (__FILE__ == $_SERVER["SCRIPT_FILENAME"]) {
    $base_file_name = "passwords";
    password_generator(8, 10, $base_file_name);
}
