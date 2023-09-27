days_of_the_week = ["Domingo",
                    "Segunda-feira",
                    "Terça-feira",
                    "Quarta-feira",
                    "Quinta-feira",
                    "Sexta-feira",
                    "Sabado",
                    ]

classes_in_the_week = {}

for days in days_of_the_week:
    subjects = input("Digite a matéria que você tem na(o) " + days + ": ")
    classes_in_the_week[days] = subjects

print()

for day, subject in classes_in_the_week.items():
    print(day + ": " + subject)

