from abc import ABC, abstractmethod

class Task(ABC):
    def __init__(self, description: str, difficulty: int):
        self._description = description
        self._difficulty = difficulty
        self._type = self.__class__.__name__

    @property
    def description(self): return self._description

    @property
    def difficulty(self): return self._difficulty

    @property
    def task_type(self): return self._type

    @abstractmethod
    def get_details(self) -> str:
        pass

    def to_dict(self):
        return {
            "description": self._description,
            "type": self._type,
            "difficulty": self._difficulty
        }

class WorkTask(Task):
    def get_details(self):
        return f"[WORK] Diff: {self._difficulty} | {self._description}"

class SportTask(Task):
    def get_details(self):
        return f"[SPORT] Diff: {self._difficulty} | {self._description}"

class StudyTask(Task):
    def get_details(self):
        return f"[STUDY] Diff: {self._difficulty} | {self._description}"

class TaskFactory:
    @staticmethod
    def create_task(task_type: str, description: str, difficulty: int) -> Task:
        types = {
            "worktask": WorkTask,
            "sporttask": SportTask,
            "studytask": StudyTask
        }
        target_class = types.get(task_type.lower().strip())
        if not target_class:
            raise ValueError(f"Unknown task type: {task_type}")
        return target_class(description, difficulty)
