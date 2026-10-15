from dispositivo import DispositivoRede
from conectividade import testar_ping

def executar_sistema():
    print("=== SISTEMA NETMONITOR PRO ===")
    lista = [DispositivoRede("Switch-01", "10.0.0.1", "switch")]
    for d in lista:
        d.status = "Online" if testar_ping(d.ip) else "Offline"
        print(d)

if __name__ == "__main__":
    executar_sistema()
