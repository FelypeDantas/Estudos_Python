import os

def listar_diretorio(caminho):
    """Lista arquivos e diretórios no caminho especificado."""
    try:
        with os.scandir(caminho) as entradas:
            for entrada in entradas:
                if entrada.is_file():
                    print(f"Arquivo: {entrada.path}")
                elif entrada.is_dir():
                    print(f"Diretório: {entrada.path}")
    except FileNotFoundError:
        print(f"Erro: O caminho '{caminho}' não existe.")
    except PermissionError:
        print(f"Erro: Permissão negada para acessar '{caminho}'.")
    except OSError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    caminho = '/'
    listar_diretorio(caminho)

