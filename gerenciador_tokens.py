# gerenciador_tokens.py

class GerenciadorTokens:
    def __init__(self, limite_maximo=1000):
        self.tokens_gastos = 0
        self.limite_maximo = limite_maximo

    def calcular_tokens(self, texto):
        """Simula o cálculo de tokens baseado no número de palavras (1 palavra aprox. 1.3 tokens)."""
        palavras = len(texto.split())
        return int(palavras * 1.3)

    def registrar_consumo(self, texto):
        tokens_texto = self.calcular_tokens(texto)
        self.tokens_gastos += tokens_texto
        return tokens_texto

    def verificar_limite(self):
        """Verifica se o limite de tokens da sessão foi atingido."""
        if self.tokens_gastos >= self.limite_maximo:
            return False
        return True
