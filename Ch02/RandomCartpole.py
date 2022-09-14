import gym
from typing import TypeVar
import random

if __name__ == '__main__':
    e = gym.make('CartPole-v1')
    obs = e.reset()
    total_reward = 0
    total_steps = 0
    done = False
    while not done:
        action = e.action_space.sample()
        obs, reward, done, _, _ = e.step(action)
        total_reward += reward
        total_steps += 1
        if done:
            break
        
    print("Episode completed in {0} steps, total reward: {1}".format(total_steps, "%.2f"%total_reward))