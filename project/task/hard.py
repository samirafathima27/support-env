import sys
sys.path.append("..")

from env import SupportEnv

def run_hard():
    env = SupportEnv()
    state = env.reset()

    text = state["text"].lower()

    correct = 0
    total = 3

    # ---------------------------
    # 1. SMART CLASSIFICATION
    # ---------------------------
    if "payment" in text or "order" in text or "deducted" in text:
        action = 0  # billing
    elif "crash" in text or "error" in text or "bug" in text:
        action = 1  # technical
    else:
        action = 2  # general

    state, reward, done = env.step(action)
    if reward > 0:
        correct += 1

    # ---------------------------
    # 2. SMART PRIORITY
    # ---------------------------
    if ("failed" in text or 
        "crash" in text or 
        "not delivered" in text or 
        "deducted" in text):
        action = 3  # high priority
    else:
        action = 4  # low priority

    state, reward, done = env.step(action)
    if reward > 0:
        correct += 1

    # ---------------------------
    # 3. RESOLUTION
    # ---------------------------
    state, reward, done = env.step(5)  # resolve

    if reward > 0:
        correct += 1

    # ---------------------------
    # FINAL SCORE
    # ---------------------------
    score = correct / total
    return score


if __name__ == "__main__":
    print("Hard Score:", run_hard())
