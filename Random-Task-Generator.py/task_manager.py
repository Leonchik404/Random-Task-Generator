import json
import random
from collections import deque
from task_models import TaskFactory

class TaskManager:
    def __init__(self, history_file="history.json", max_history=10):
        self.history_file = history_file
        self.history = deque(maxlen=max_history)
        self.task_pool = [
            ("WorkTask", "Finish project report", 4),
            ("SportTask", "Morning 5km run", 3),
            ("StudyTask", "Learn Design Patterns", 5),
            ("WorkTask", "Email clients", 1),
            ("StudyTask", "Read 20 pages", 2)
        ]
        self.load_history()

    def generate_random_task(self):
        t_type, desc, diff = random.choice(self.task_pool)
        task = TaskFactory.create_task(t_type, desc, diff)
        self.history.append(task)
        self.save_history()
        return task

    def save_history(self):
        with open(self.history_file, "w", encoding="utf-8") as f:
            data = [t.to_dict() for t in self.history]
            json.dump(data, f, indent=4)

    def load_history(self):
        try:
            with open(self.history_file, "r") as f:
                items = json.load(f)
                for i in items:
                    self.history.append(TaskFactory.create_task(i['type'], i['description'], i['difficulty']))
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def filter_history(self, criteria: str):
        # Фильтрация по типу или сложности
        return [t for t in self.history if criteria.lower() in t.task_type.lower() or criteria == str(t.difficulty)]
