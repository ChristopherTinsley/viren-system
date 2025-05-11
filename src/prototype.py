# prototype.py - A basic simulation setup for the Viren System
class Agent:
    def __init__(self, name):
        self.name = name
        self.trust_score = 1.0

    def respond(self, message):
        return f"{self.name} responding to: {message}"

class SystemC:
    def __init__(self, agents):
        self.agents = agents

    def choose_agent(self, message):
        best = max(self.agents, key=lambda a: a.trust_score)
        return best.respond(message)

a = Agent("System A - Logic")
b = Agent("System B - Emotion")
c = SystemC([a, b])

print(c.choose_agent("How should we proceed with the next version?"))
