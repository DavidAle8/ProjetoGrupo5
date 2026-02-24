import pytest
from env.Environment0 import LabirintoEnvironment
from aima.agents import Agent

def test_execute_action_move_valido():
    grid = [
        [0, 0],
        [0, 0]
    ]

    env = LabirintoEnvironment(grid)

    class DummyAgent:
        def __init__(self):
            self.location = (0, 0)
            self.performance = 0
            self.program = type("obj", (), {"goal": (1, 1)})

    agent = DummyAgent()
    env.add_thing(agent)

    env.execute_action(agent, 'BAIXO')

    assert agent.location == (1, 0)
    assert (1, 0) in env.path_history


def test_execute_action_desconta_custo():
    grid = [
        [0, 5],
        [0, 0]
    ]

    env = LabirintoEnvironment(grid)

    class DummyAgent:
        def __init__(self):
            self.location = (0, 0)
            self.performance = 0
            self.program = type("obj", (), {"goal": (1, 1)})

    agent = DummyAgent()
    env.add_thing(agent)

    env.execute_action(agent, 'DIR')

    assert agent.location == (0, 1)
    assert agent.performance == -5
    

def test_info_terreno():
    grid = [
        [0, 3],
        [5, 7]
    ]

    env = LabirintoEnvironment(grid)

    nome, custo = env.info_terreno(0, 1)

    assert nome == "pedra"
    assert custo == 3


def test_environment_nao_atravessa_parede():
    grid = [
        [0, 1],
        [0, 0]
    ]

    env = LabirintoEnvironment(grid)

    class DummyAgent:
        def __init__(self):
            self.location = (0, 0)
            self.performance = 0
            self.program = type("obj", (), {"goal": (1, 1)})

    agent = DummyAgent()
    env.add_thing(agent)

    env.execute_action(agent, 'DIR')  # parede

    assert agent.location == (0, 0)


def test_environment_nao_sai_matriz():
    grid = [
        [0, 0],
        [0, 0]
    ]

    env = LabirintoEnvironment(grid)

    class DummyAgent:
        def __init__(self):
            self.location = (0, 0)
            self.performance = 0
            self.program = type("obj", (), {"goal": (1, 1)})

    agent = DummyAgent()
    env.add_thing(agent)

    env.execute_action(agent, 'CIMA')  # fora da matriz

    assert agent.location == (0, 0)


def test_is_done():
    grid = [
        [0, 0],
        [0, 0]
    ]

    env = LabirintoEnvironment(grid)

    class DummyProgram:
        def __init__(self):
            self.goal = (1, 1)

        def __call__(self, percept):
            return None

    class DummyAgent(Agent):
        def __init__(self):
            super().__init__(program=DummyProgram())
            self.performance = 0

    agent = DummyAgent()

    # O ambiente define a posição
    env.add_thing(agent, location=(1, 1))

    assert env.is_done() is True