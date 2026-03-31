import sys
sys.path.append("..")

from env import SupportEnv

def run_medium():
    env = SupportEnv()
    state = env.reset()

    correct = 0
    total = 2

    # classify
    state, reward, done = env.step(0)
    if reward > 0:
        correct += 1

    # set priority
    state, reward, done = env.step(3)
    if reward > 0:
        correct += 1

    score = correct / total
    return score


if __name__ == "__main__":
    print("Medium Score:", run_medium())
