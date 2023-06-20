# Packages

from prettytable import PrettyTable

table = PrettyTable()

col1 = table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

col2 = table.add_column("Type", ["Electric", "Water", "Fire"])


table.align = "l"
print(table)
