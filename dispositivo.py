class DispositivoRede:
    def __init__(self, hostname: str, ip: str, tipo: str):
        self.hostname = hostname
        self.ip = ip
        self.tipo = tipo  # ex: roteador, switch, servidor
        self.status = "Desconhecido"

    def __str__(self):
        return f"[{self.tipo.upper()}] {self.hostname} ({self.ip}) - Status: {self.status}"
