class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        s = ''
        queue = [(0, 0, root)]
        while len(queue) > 0:
            depth, x, node = queue.pop(0)
            s += '{}/{}/{},'.format(depth, x, node.val)
            if node.left is not None:
                queue.append((depth + 1, x * 2, node.left))
            if node.right is not None:
                queue.append((depth + 1, x * 2 + 1, node.right))

        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        elements = data[1:-1].split(',')
        root = TreeNode(elements[0].split('/')[2])
        nodes = {(0, 0): root}
        for element in elements[1:]:
            depth, x, val = map(int, element.split('/'))
            node = TreeNode(int(val))
            if x % 2 == 0:
                nodes[(depth - 1, x // 2)].left = node
            else:
                nodes[(depth - 1, x // 2)].right = node
            nodes[(depth, x)] = node
        return root


if __name__ == '__main__':
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(codec.serialize(root))
    print(codec.deserialize(codec.serialize(root)).val)

    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(3)
    root.right.left.right = TreeNode(1)
    print(codec.serialize(root))
    print(codec.deserialize(codec.serialize(root)).val)

    root = TreeNode(-1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    print(codec.serialize(root))
    print(codec.deserialize(codec.serialize(root)).val)
