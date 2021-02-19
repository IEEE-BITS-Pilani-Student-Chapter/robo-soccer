""" 
    observation- np.concatenate((self.player.position,
            self.player.velocity,
            [self.player.orientation],
            self.goalie.position,
            self.goalie.velocity,
            [self.goalie.orientation],
            self.ball.position,
            self.ball.velocity))
"""

import gym
import gym_goal


import gym
import gym_goal

env = gym.make('Goal-v0')

env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()


# import gym
# import gym_goal

# import gym
# env = gym.make('Goal-v0')
# def basic_Policy(observation):
#     return env.action_space.sample()
# for i in range(20):
#     for t in range(1000):
#         observation = env.reset()
#         env.render()
#         action = basic_Policy(observation)
#         observation, reward, done, info = env.step(action)
#         print(observation)
#         if done:
#             print ("Episode finished after {} timestamps".format(t+1))
#             break
# env.close()