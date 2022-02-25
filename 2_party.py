class Party:
    def __init__(self):
        self.names_of_people = []


party = Party()
while True:
    command = input()
    if command == "End":
        break
    else:
        party.names_of_people.append(command)
print(f"Going: {', '.join(party.names_of_people)}")
print(f"Total: {len(party.names_of_people)}")
