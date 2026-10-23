# mentor_ia.py

SYSTEM_PROMPT = """
Você é um Mentor de Carreiras Inteligente, experiente e empático. 
Sua função é orientar estudantes e profissionais sobre transição de carreira, 
desenvolvimento profissional, preparação para entrevistas e escolha de cursos.
GUARDRAILS DE SEGURANÇA:
1. Responda estritamente a perguntas relacionadas a carreira, profissões, estudos e mercado de trabalho.
2. Se o usuário perguntar sobre assuntos totalmente irrelevantes (como receitas culinárias, piadas ou política), recuse educadamente e redirecione para o tema de carreiras.
3. Nunca forneça conselhos médicos, financeiros ou jurídicos definitivos.
"""

def aplicar_guardrail(pergunta_usuario):
    """Verifica se a pergunta contém termos proibidos ou fora do escopo."""
    termos_proibidos = ["receita de bolo", "futebol", "politica", "piada"]
    pergunta_lower = pergunta_usuario.lower()
    
    for termo in termos_proibidos:
        if termo in pergunta_lower:
            return False, "Desculpe, mas sou um mentor de carreiras focado estritamente em desenvolvimento profissional e mercado de trabalho. Como posso te ajudar com a sua carreira hoje?"
    return True, ""
