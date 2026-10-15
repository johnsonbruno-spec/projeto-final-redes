import subprocess

def testar_ping(ip: str) -> bool:
    """Executa um comando de ping simples para verificar alcance."""
    try:
        resultado = subprocess.run(["ping", "-n", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return resultado.returncode == 0
    except Exception:
        return False
