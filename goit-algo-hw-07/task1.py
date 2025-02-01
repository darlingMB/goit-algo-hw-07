class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Найбільше значення
def find_max(root):
    current = root
    while current.right:
        current = current.right
    return current.value

# Найменше значення
def find_min(root):
    current = root
    while current.left:
        current = current.left
    return current.value

# Сумма всіх значень
def sum_values(root):
    if not root:
        return 0
    return root.value + sum_values(root.left) + sum_values(root.right)

def main():
    # Бiнарне дерево
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(18)

    print("Максимальное значение:", find_max(root))
    print("Минимальное значение:", find_min(root))
    print("Сумма всех значений:", sum_values(root))


if __name__ == "__main__":
    main()