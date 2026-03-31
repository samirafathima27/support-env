from env import SupportEnv

env = SupportEnv()

state = env.reset()
print("Start:", state)

# Try actions
state, reward, done = env.step(0)  # classify billing
print("After action 0:", state, reward, done)

state, reward, done = env.step(3)  # set high priority
print("After action 3:", state, reward, done)

state, reward, done = env.step(5)  # resolve
print("After action 5:", state, reward, done)
