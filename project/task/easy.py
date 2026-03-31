import sys
sys.path.append("..")

from env import SupportEnv

def run_easy():
    env = SupportEnv()
    state = env.reset()

    correct = 0
    total = 1

    # simple logic: always choose billing
    state, reward, done = env.step(0)

    if reward > 0:
        correct += 1

    score = correct / total
    return score


if __name__ == "__main__":
    print("Easy Score:", run_easy())
