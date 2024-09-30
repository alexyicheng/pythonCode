# 28.09.2024
# es gibt 20 Vorlesungen
# Professor: 1 x Namensabfrage
# Schüler: 1 x nicht da
# zusätzlich Prof weiße nur nicht, dass seine Schüler mehr als 1xmal nicht da sein kann
# aber Schüler können mehr Mals nicht da sein

import random


class Professor:
    def __init__(self, num_lectures=20):
        self.num_lectures = num_lectures
        self.attendance_check = random.randint(1, num_lectures)  # Der Professor überprüft zufällig eine Vorlesung

    def check_attendance(self, students):
        for student in students:
            if student.absences[self.attendance_check - 1]:  # Wenn der Schüler in der überprüften Vorlesung schwänzt
                print(f"Student {student.name} wurde beim Schwänzen erwischt!")
                student.caught = True
            else:
                print(f"Student {student.name} war anwesend.")


class Student:
    def __init__(self, name, num_lectures=20):
        self.name = name
        self.num_lectures = num_lectures
        self.absences = [False] * num_lectures  # False bedeutet anwesend, True bedeutet abwesend
        self.caught = False  # Gibt an, ob der Schüler erwischt wurde

    def skip_lectures(self, num_skips):
        skipped_lectures = random.sample(range(self.num_lectures),
                                         num_skips)  # Zufällig ausgewählte Vorlesungen, die der Schüler schwänzt
        for lecture in skipped_lectures:
            self.absences[lecture] = True


# Initialisierung
num_lectures = 20
students = [Student(f"Student {i + 1}", num_lectures) for i in range(5)]  # Erstelle 5 Schüler

# Jeder Schüler entscheidet, wie viele Vorlesungen er schwänzen will (z.B. zufällig zwischen 1 und 5)
for student in students:
    num_skips = random.randint(1, 5)  # Jeder Schüler schwänzt zufällig 1 bis 5 Vorlesungen
    student.skip_lectures(num_skips)
    print(f"{student.name} hat {num_skips} Vorlesungen geschwänzt.")

# Der Professor führt eine zufällige Anwesenheitsprüfung durch
professor = Professor(num_lectures)
print(f"\nDer Professor überprüft die Anwesenheit in Vorlesung {professor.attendance_check}.\n")
professor.check_attendance(students)
