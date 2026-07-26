# Practice project for python dictionaries ---------------

"""
Student Grade Manager
A single project to practice Python dictionaries and their common methods:
.get(), .keys(), .values(), .items(), .clear(), .pop(), .update(),
iteration, enumerate(), and dict comprehensions.
"""


students = {}

# 1. Adding data -----------------------
def add_student(name):
    if name not in students:
        students[name] = []
        print(f"Added student: {name}")
    else:
        print(f"{name} already exists")

def add_score(name, score):
    if name in students:
        students[name].append(score)
    else:
        print(f"{name} not found. Add them first.")


# 2. .get() ------------------------------------
def get_average(name):
    scores = students.get(name) # returns None if missing, no KeyError
    if scores is None:
        return f"{name} not found"
    if not scores:
        return f"{name} has no scores yet."
    return sum(scores) / len(scores)



# 3. .keys() ------------------------------
def list_students():
    print("Students:", list(students.keys()))



# 4. .values() ---------------------------
def all_scores_flat():
    flat = []
    for score_list in students.values():
        flat.extend(score_list)
    return flat 


# 5. .items() + iteration + enumerate()---------------------------
def print_report():
    for i, (name, scores) in enumerate(students.items(), start = 1):
        avg = sum(scores) / len(scores) if scores else 0
        print(f"{i}. {name} - avg: {avg:.1f}")



# 6. .update() -----------------------------------
def merge_students(other_dict):
    students.update(other_dict)
    print(f"Merged {len(other_dict)} student(s) in.")



# 8. .pop() -------------------------------------
def remove_student(name):
    removed = students.pop(name, None)
    if removed is None:
        print(f"{name} not found, nothing removed.")
    else:
        print(f"Removed {name}, had scores: {removed}")
    return removed 


# 9. .clear() ----------------------------------
def reset_all():
    students.clear()
    print("Gradebook wiped clean.")


# 10. Bonus: dict comprehension ========================
def top_students(threshold):
    return {
        name: sum(scores) / len(scores)
        for name, scores in students.items()
        if scores and sum(scores) / len(scores) > threshold 
    }

# Demo run - shows every method in action ============================
if __name__ == "__main__":
    add_student("Fuad")
    add_student("Rafi")
    add_student("Nadia")
 
    add_score("Fuad", 85)
    add_score("Fuad", 90)
    add_score("Rafi", 70)
    add_score("Rafi", 60)
    add_score("Nadia", 95)
    add_score("Nadia", 88)
 
    print("\n-- get_average --")
    print("Fuad's average:", get_average("Fuad"))
    print("Unknown student:", get_average("Shakib"))  # tests .get() safety
 
    print("\n-- list_students (.keys) --")
    list_students()
 
    print("\n-- all_scores_flat (.values) --")
    print(all_scores_flat())
 
    print("\n-- print_report (.items) --")
    print_report()

 
    print("\n-- merge_students (.update) --")
    new_class = {"Tanvir": [78, 82], "Mim": [91, 94]}
    merge_students(new_class)
    list_students()
 
    print("\n-- remove_student (.pop) --")
    remove_student("Rafi")
    remove_student("GhostStudent")  # tests safe pop
 
    print("\n-- top_students (dict comprehension) --")
    print(top_students(80))
 
    print("\n-- reset_all (.clear) --")
    reset_all()
    list_students()















