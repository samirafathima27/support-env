import random

class SupportEnv:

    def __init__(self):
        self.tickets = [
            {
                "text": "Payment failed but money deducted",
                "category": "billing",
                "priority": "high"
            },
            {
                "text": "App crashes when I open profile",
                "category": "technical",
                "priority": "high"
            },
            {
                "text": "How to change my password?",
                "category": "general",
                "priority": "low"
            },
            {
                "text": "Order not delivered even after 5 days",
                "category": "billing",
                "priority": "high"
            }
        ]
        self.reset()

    def reset(self):
        self.current = random.choice(self.tickets)

        self.ticket = {
            "text": self.current["text"],
            "category": None,
            "priority": None,
            "resolved": False
        }

        return self.state()

    def state(self):
        return self.ticket

    def step(self, action):
        reward = 0
        done = False

        correct_category = self.current["category"]
        correct_priority = self.current["priority"]

        # CATEGORY ACTIONS
        if action == 0:
            self.ticket["category"] = "billing"
            reward += 2 if correct_category == "billing" else -2

        elif action == 1:
            self.ticket["category"] = "technical"
            reward += 2 if correct_category == "technical" else -2

        elif action == 2:
            self.ticket["category"] = "general"
            reward += 2 if correct_category == "general" else -2

        # PRIORITY ACTIONS
        elif action == 3:
            self.ticket["priority"] = "high"
            reward += 2 if correct_priority == "high" else -1

        elif action == 4:
            self.ticket["priority"] = "low"
            reward += 2 if correct_priority == "low" else -1

        # RESOLVE
        elif action == 5:
            if (self.ticket["category"] == correct_category and
                self.ticket["priority"] == correct_priority):
                reward += 5
                self.ticket["resolved"] = True
                done = True
            else:
                reward -= 5

        return self.state(), reward, done
