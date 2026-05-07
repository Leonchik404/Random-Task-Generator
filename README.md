# Random Task Generator

**Author:** [Lysenko Vladislav]
**Description:** A console application that generates random tasks using OOP principles and the Factory Design Pattern. 

### Features
- **Factory Pattern:** Dynamically creates Work, Sport, and Study tasks.
- **History Queue:** Stores the last 10 generated tasks using `collections.deque`.
- **JSON Storage:** Automatically saves and loads history.
- **Filtering:** Search history by task type or difficulty level.

### How to Run
1. Ensure you have Python 3.x installed.
2. Clone the repository.
3. Run `python main.py`.

### Example Usage
- Press `1` to get a task like `[SPORT] Diff: 3 | Morning 5km run`.
- Press `3` and type `WorkTask` to see only job-related history.
