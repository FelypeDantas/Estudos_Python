from pathlib import Path
import stat

def verificar_arquivo_especial(caminho_arquivo):
    """Verifica se o arquivo é especial de bloco ou de caráter e retorna uma mensagem correspondente."""
    try:
        modo = caminho_arquivo.stat().st_mode
        if stat.S_ISBLK(modo):
            return f"{caminho_arquivo}: arquivo especial de bloco"
        elif stat.S_ISCHR(modo):
            return f"{caminho_arquivo}: arquivo especial de caráter"
        else:
            return None
    except OSError as e:
        return f"Erro ao acessar {caminho_arquivo}: {e}"

def listar_arquivos_especiais(caminho_diretorio):
    """Lista arquivos especiais de bloco e de caráter no diretório especificado."""
    caminho_diretorio = Path(caminho_diretorio)
    
    if not caminho_diretorio.is_dir():
        print(f"Erro: O caminho '{caminho_diretorio}' não é um diretório válido.")
        return
    
    try:
        for entrada in caminho_diretorio.iterdir():
            mensagem = verificar_arquivo_especial(entrada)
            if mensagem:
                print(mensagem)
    except PermissionError:
        print(f"Erro: Permissão negada para acessar o diretório '{caminho_diretorio}'.")
    except OSError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
   if os.name == 'nt':
        caminho = 'C:\\'
    else: 
        caminho = '/dev'
    listar_arquivos_especiais(caminho)
