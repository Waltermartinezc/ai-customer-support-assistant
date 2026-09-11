import json

def generate_ai_response(customer_intent):
    """
    Simula la respuesta de una IA basada en la intención del cliente.
    """
    
    # Prompt del sistema con reglas estrictas de calidad
    system_prompt = """
    Eres un asistente virtual de soporte. 
    Regla crítica: No debemos indicar plazos de resolución ni Acuerdos de Nivel de Servicio (SLA) en los mensajes. 
    Mantén un tono empático pero enfocado en la solución inmediata.
    """
    
    # Lógica de enrutamiento
    if customer_intent == "refund":
        return "Su solicitud de reembolso ha sido procesada y escalada al equipo de finanzas. Nos pondremos en contacto pronto."
    elif customer_intent == "order_status":
        return "Puede rastrear el estado exacto de su pedido desde la sección 'Mis Compras' en la aplicación."
    else:
        return "Para brindarle una mejor ayuda, lo transferiré con uno de nuestros especialistas."

# Prueba del sistema
if __name__ == "__main__":
    test_intent = "refund"
    print(f"Respuesta generada: {generate_ai_response(test_intent)}")
