import sys
sys.path.append(".")

from task.easy import run_easy
from task.medium import run_medium
from task.hard import run_hard


def run_all():
    print("Running All Tasks...\n")

    easy_score = run_easy()
    print("Easy Task Score:", easy_score)

    medium_score = run_medium()
    print("Medium Task Score:", medium_score)

    hard_score = run_hard()
    print("Hard Task Score:", hard_score)

    final_score = (easy_score + medium_score + hard_score) / 3
    print("\nFinal Score:", final_score)


if __name__ == "__main__":
    run_all()
