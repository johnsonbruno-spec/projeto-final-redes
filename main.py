from dispositivo import DispositivoRede
from conectividade import testar_ping

def iniciar_monitoramento():
    print("=== NetMonitor v1.0 ===")
    dev = DispositivoRede("Roteador-Core", "192.168.1.1", "roteador")
    status = testar_ping(dev.ip)
    dev.status = "Ativo" if status else "Inativo"
    print(dev)

if __name__ == "__main__":
    iniciar_monitoramento()
