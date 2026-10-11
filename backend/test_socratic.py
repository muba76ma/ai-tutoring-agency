from agents.socratic_agent import SocraticAgent

agent = SocraticAgent()

print("Agent Socratique prêt. Tape 'quit' pour quitter.\n")

while True:
    student = input("Élève : ")
    if student.lower() in ["quit", "exit", "q"]:
        break

    reply = agent.ask(student)
    print(f"\nTuteur : {reply}\n")
