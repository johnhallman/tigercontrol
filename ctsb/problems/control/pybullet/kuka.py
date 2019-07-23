"""
PyBullet Pendulum enviornment
"""

import gym
import pybullet_envs
from ctsb.problems.control.pybullet.pybullet_problem import PyBulletProblem


class Kuka(PyBulletProblem):
    """
    Description: Simulates a kuka arm picking up diverse objects
    """
    def __init__(self):
        self.initialized = False

    def initialize(self):
        self.initialized = True
        self._env = gym.make("KukaBulletEnv-v0")
        self.observation_space = self._env.observation_space.shape
        self.action_space = self._env.action_space.shape
        self.state = {}
        initial_obs = self.reset()
        return initial_obs





