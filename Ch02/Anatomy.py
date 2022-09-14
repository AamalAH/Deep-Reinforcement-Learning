from typing import List
import numpy as np
import random


class Environment():
    def __init__(self) -> None:
        self.remaining_steps = 10
        
    def get_observation(self) -> List[float]:
        return [0.0, 0.0, 0.0]
    
    def get_actions(self) -> List[int]:
        return [0, 1]
    
    def is_done(self) -> bool:
        return self.remaining_steps == 0
    
    def action(self, action: int) -> float:
        if self.is_done():
            raise Exception("Game is over")
        self.remaining_steps -= 1
        return random.random()
    
class Agent:
    def __init__(self) -> None:
        self.total_reward = 0.0
        
    def step(self, env: Environment) -> None:
        current_obs = env.get_observation()
        current_act = random.choice(env.get_actions())
        reward = env.action(current_act)
        self.total_reward += reward
        

if __name__ == '__main__':
    env = Environment()
    agent = Agent()
    while not env.is_done():
        agent.step(env)
    
    print("Total Reward: ", "%.3f"%agent.total_reward)