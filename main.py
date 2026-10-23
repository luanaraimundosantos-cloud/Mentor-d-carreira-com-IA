# main.py
from mentor_ia import SYSTEM_PROMPT, aplicar_guardrail
from gerenciador_tokens import GerenciadorTokens

def main():
    print("==================================================")
    print("🤖 MENTOR DE CARREIRAS INTELIGENTE (IA)")
    print("==================================================")
    print("Olá! Sou o seu mentor virtual de carreiras.")
    print("Digite 'sair' para encerrar a conversa a qualquer momento.\n")

    # Inicializa o gestor de tokens com limite de 500 tokens para a sessão
    gerenciador = GerenciadorTokens(limite_maximo=500)

    # Simulação do histórico de prompt do sistema
    print(f"[Sistema configurado com System Prompt e GuardRails ativos]\n")

    while True:
        if not gerenciador.verificar_limite():
            print("\n⚠️ [AVISO] Limite de tokens da sessão atingido. Encerrando por segurança.")
            break

        pergunta = input("Você: ").strip()
        
        if pergunta.lower() == 'sair':
            print("\nMentor: Foi um prazer ajudar no seu desenvolvimento profissional. Até logo!")
            break
        
        if not pergunta:
            continue

        # Aplica o GuardRail de segurança
valido, mensagem_bloqueio = aplicar_guardrail(pergunta)
        if not valido:
            print(f"\nMentor: {mensagem_bloqueio}\n")
            continue

        # Simulação da resposta do Mentor baseada no tema
        resposta_mentor = f"Com base na minha análise de mercado para a sua pergunta ('{pergunta}'), recomendo focar em soft skills, atualizar o seu currículo e buscar certificações na área desejada."
        
        # Regista o consumo de tokens
        tokens_pergunta = gerenciador.registrar_consumo(pergunta)
        tokens_resposta = gerenciador.registrar_consumo(resposta_mentor)
        total_interacao = tokens_pergunta + tokens_resposta

        print(f"\nMentor: {resposta_mentor}")
        print(f"📊 [Tokens usados nesta mensagem: {total_interacao} | Total gasto: {gerenciador.tokens_gastos}/{gerenciador.limite_maximo}]\n")

if __name__ == "__main__":
    main()
