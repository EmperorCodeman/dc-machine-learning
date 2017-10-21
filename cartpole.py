import gym
import time

env = gym.make('CartPole-v0')
LEFT = 0
RIGHT = 1


def choose_direction(observation):
    radians = observation[2]
    if radians < 0:
        return LEFT
    else:
        return RIGHT
    #return env.action_space.sample()


def main():
    for i_episode in range(1):
        observation = env.reset()
        for t in range(500):
            env.render()
            #time.sleep(.5)
            print(observation)
            action = choose_direction(observation)
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break


if __name__ == "__main__":
    main()
