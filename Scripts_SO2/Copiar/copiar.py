import os
import sys

BUF_SIZE = 4096
OUTPUT_MODE = 0o640

def main():
    if len(sys.argv) != 3:
        print("Uso: python script.py input_file output_file", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        in_fd = os.open(input_file, os.O_RDONLY)
    except OSError as e:
        print(f"Erro ao abrir o arquivo de entrada: {e}", file=sys.stderr)
        sys.exit(2)

    try:
        out_fd = os.open(output_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, OUTPUT_MODE)
    except OSError as e:
        os.close(in_fd)
        print(f"Erro ao criar o arquivo de saída: {e}", file=sys.stderr)
        sys.exit(3)

    while True:
        try:
            buffer = os.read(in_fd, BUF_SIZE)
            if not buffer:
                break
            os.write(out_fd, buffer)
        except OSError as e:
            os.close(in_fd)
            os.close(out_fd)
            print(f"Erro durante a operação de leitura/escrita: {e}", file=sys.stderr)
            sys.exit(4)

    os.close(in_fd)
    os.close(out_fd)

    if not buffer:
        sys.exit(0)
    else:
        sys.exit(5)

if __name__ == "__main__":
    main()
