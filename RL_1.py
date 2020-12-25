# import gym
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

import gym
from gym import spaces

def random_cart_pole_1():
    env = gym.make('CartPole-v0')
    env.reset()
    for _ in range(1000):
        env.render()
        obs, reward, done, info = env.step(env.action_space.sample()) # take a random action
    env.close()

def random_ms_pacman_1():
    env = gym.make('MsPacman-v0')
    env.reset()
    for _ in range(1000):
        env.render()
        obs, reward, done, info = env.step(env.action_space.sample()) # take a random action
    env.close()


def random_cart_pole_2():
    env = gym.make('CartPole-v0')
    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break
    env.close()


def _print_spaces(environ):
    env = gym.make(environ)
    print(f'Action Space: {env.action_space}')
    # > Discrete(2)
    print(f'Observation Space: {env.observation_space}')


def test_spaces():
    space = spaces.Discrete(8)  # Set with 8 elements {0, 1, 2, ..., 7}
    x = space.sample()
    print(x)
    print(space.contains(x))
    print(space.n == 8)


def random_ant_1():
    env = gym.make('Ant-v2')
    env.reset()
    for _ in range(1000):
        env.render()
        obs, reward, done, info = env.step(env.action_space.sample()) # take a random action
    env.close()


def main():
    # random_cart_pole_1()
    # random_ms_pacman_1()
    # random_cart_pole_2()
    # _print_spaces('CartPole-v0')
    # test_spaces()
    random_ant_1()


if __name__ == "__main__":
    main()