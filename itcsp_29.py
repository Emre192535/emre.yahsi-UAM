'''
Exercise 29
A dictionary is given.
students = {
    'Ana Bel': {'Department': 'LMT', 'Age': 25, 'Average Grade': 4.5},
    'Jessica Jones': {'Department': 'LMT', 'Age': 24, 'Average Grade': 4.8},
    'Supergirl': {'Department': 'Super Heroes', 'Age': 26, 'Average Grade': 5.0}
}
Change an average grade for a student Supergirl belonging to Department 'Super Heroes' to 6.0. Later print it to the console

'''
students = {
    'Ana Bel': {'Department': 'LMT', 'Age': 25, 'Average Grade': 4.5},
    'Jessica Jones': {'Department': 'LMT', 'Age': 24, 'Average Grade': 4.8},
    'Supergirl': {'Department': 'Super Heroes', 'Age': 26, 'Average Grade': 5.0}
}
students["Supergirl"]["Average Grade"] = 6
print(students["Supergirl"]["Average Grade"])