from resistor import Resistor


class Node:
    def __init__(self, data: Resistor):
        self.left = None
        self.right = None
        self.data = data

    def insert_by_value(self, data: Resistor):
        if self.data:
            if data.value < self.data.value:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_by_value(data)
            elif data.value > self.data.value:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_by_value(data)
        else:
            self.data = data

    def insert_by_model(self, data: Resistor):
        if self.data:
            if data.model < self.data.model:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert_by_model(data)
            elif data.model > self.data.model:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert_by_model(data)
            else:
                self.data = data

    def find_by_value(self, value):
        if value < self.data.value:
            if self.left is None:
                return "not found"
            return self.left.find_by_value(value)
        elif value > self.data.value:
            if self.right is None:
                return "not found"
            return self.right.find_by_value(value)
        else:
            print(self.data)
            if self.left is not None:
                self.left.find_by_value(value)
            if self.right is not None:
                self.right.find_by_value(value)

    def delete_by_accuracy(self, value):
        if value < self.data.accuracy:
            if self.left is None:
                return " not found"
            self.left.delete_by_accuracy(value)
        elif value > self.data.accuracy:
            if self.right is None:
                return "not found"
            self.right.delete_by_accuracy(value)
        else:
            self.data = self.right
            if self.left is not None:
                self.left.delete_by_accuracy(value)
            if self.right is not None:
                self.right.delete_by_accuracy(value)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def __str__(self):
        return " "

    def traverse_preorder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.traverse_preorder()
        if self.right:
            self.right.traverse_preorder()
