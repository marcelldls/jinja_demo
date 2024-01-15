from copy import copy
from typing import List, Dict
from jinja2 import Environment, FileSystemLoader

max_score = 100
test_name = "Python Challenge"
students: List[Dict[str, str | int]] = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "Sirius", "score": 75},
]

# Bubble sorting list by grade
sorted = False
while not sorted:
    broken = False
    for num_student in range(len(students)-1):
        if students[num_student]["score"] < students[num_student+1]["score"]:
            store = students[num_student]
            students[num_student] = students[num_student+1]
            students[num_student+1] = store
            broken = True
        else:
            continue
    if broken is False:  # Full pass no swap
        sorted = True

environment = Environment(
    loader=FileSystemLoader("templates/"),
    )  # contains important shared variables

# Create text messages
template = environment.get_template("message.txt")

for student in students:
    assert isinstance(student['name'], str)  # type narrowing
    lower_name = student['name'].lower()
    filename = f"message_{lower_name}.txt"
    content = template.render(
        student,
        max_score=max_score,
        test_name=test_name
    )
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")

# Create web page
results_filename = "students_results.html"
web_template = environment.get_template("results.html")
context = {
    "students": students,
    "test_name": test_name,
    "max_score": max_score,
}
with open(results_filename, mode="w", encoding="utf-8") as results:
    results.write(web_template.render(context))
    print(f"... wrote {results_filename}")
