from resistor import Resistor
from binary_tree import Node


def main():
    resistor_one = Resistor("Resistor1", 45, 340, 78)
    resistor_two = Resistor("Resistor2", 67, 200, 80)
    resistor_three = Resistor("Resistor3", 90, 400, 80)
    resistor_four = Resistor("Resistor4", 56, 50, 80)
    resistor_five = Resistor("Resistor5", 89, 8, 80)
    root = Node(resistor_one)
    root.insert_by_value(resistor_two)
    root.insert_by_value(resistor_three)
    root.insert_by_value(resistor_four)
    root.insert_by_value(resistor_five)
    root.insert_by_value(resistor_five)
    root.print_tree()
    print("\n\n")
    root.find_by_value(45)
    root.delete_by_accuracy(78)
    print("\n\n")
    root.print_tree()


if __name__ == '__main__':
    main()
