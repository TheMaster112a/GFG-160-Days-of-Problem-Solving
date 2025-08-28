import os
import re

topics = {
    "Arrays": 13,
    "Strings": 7,
    "Sorting": 7,
    "Searching": 8,
    "Matrix": 6,
    "Hashing": 9,
    "Two Pointer Technique": 10,
    "Prefix Sum": 4,
    "Linked List": 10,
    "Recursion & Backtracking": 5,
    "Tree": 15,
    "Heap": 4,
    "Stack": 9,
    "Queue & Deque": 2,
    "Dynamic Programming": 23,
    "Greedy": 5,
    "Graph": 17,
    "Tries": 2,
    "Bit Manipulation": 4,
}

def count_solutions(topic):
    folder = os.path.join(os.getcwd(), topic.replace(" ", "_"))
    if os.path.exists(folder):
        return len([f for f in os.listdir(folder) if f.endswith(".py")])
    return 0

progress_lines = []
total_solved = 0
total_problems = sum(topics.values())

for topic, total in topics.items():
    solved = count_solutions(topic)
    total_solved += solved
    status = "✅ Completed" if solved == total else "🚀 In Progress" if solved > 0 else "⏳ Coming Soon"
    progress_lines.append(f"| {topic} | {solved} / {total} | {status} |")

table = (
    "## 📊 Progress Tracker\n\n"
    "| Topic                    | Problems Solved | Status |\n"
    "|-------------------------|-----------------|--------|\n"
    + "\n".join(progress_lines)
    + f"\n\n**Total: {total_solved} / {total_problems}**\n\n"
    "*(I’ll keep updating this table as I move forward)*\n"
)

with open("README.md", "r+", encoding="utf-8") as f:
    content = f.read()
    new_content = re.sub(r"## 📊 Progress Tracker[\s\S]*", table, content)
    f.seek(0)
    f.write(new_content)
    f.truncate()
