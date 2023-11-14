import sys

input = sys.stdin.readline


class Agent :
    def __init__(self,code_name,grade) :
        self.n = code_name
        self.g = grade


agents = []

for _ in range(5) :
    code_name , grade = tuple(map(str, input().split()))
    grade = int(grade)
    agents.append(Agent(code_name, grade))


mini = agents[0].g
name = agents[0].n
for agent in agents :
    # print(agent.n, agent.g)
    if agent.g < mini :
        mini = agent.g
        name = agent.n
print(name, mini)