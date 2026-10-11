from backend.agents.prompts import SOCRATIC_SYSTEM_PROMPT
from backend.core.llm import call_llm

class SocraticAgent:
    def __init__(self):
        self.system_prompt = SOCRATIC_SYSTEM_PROMPT
        self.conversation_history = []

    def ask(self, student_message: str) -> str:
        """
        Reçoit la question ou le message de l'élève
        et retourne une réponse Socratique.
        """
        self.conversation_history.append({
            "role": "user",
            "content": student_message
        })

        messages = [
            {"role": "system", "content": self.system_prompt}
        ] + self.conversation_history

        response = call_llm(messages)

        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })

        return response

    def reset(self):
        """Réinitialise la conversation."""
        self.conversation_history = []
