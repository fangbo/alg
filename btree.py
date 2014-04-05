

MAX = 8


class Node(object):

    def __init__(self, length):
        self.length = length  # the number of the element
        self.entries = []
        for i in range(MAX):
            self.entries.append(None)


class Entry(object):

    def __init__(self, key, value, next_node):
        self.key = key
        self.value = value
        self.next = next_node  # the reference to the Node


class BTree(object):

    def __init__(self):
        self.size = 0
        self.height = 0
        self.root = Node(0)

    def get(self, key):
        return self.search(key, self.root, self.height)

    def search(self, key, node, height):
        if height == 0:
            # if height is 0 it denotes that we enter the leaf node, we should
            # find the right position of the key.
            for j in range(node.length):
                if key == node.entries[j].key:
                    return node.entries[j].value

        else:
            # the node is nonleaf node, we should recursivly search the subtree
            # from the right position.
            for j in range(node.length):
                if j + 1 == node.length or key < node.entries[j + 1].key:
                    return self.search(key, node.entries[j].next, height - 1)

        return None

    def put(self, key, value):
        new_node = self.insert(self.root, key, value, self.height)

        self.size += 1

        if new_node:
            # it implies that the root node has been splitted, so we create a
            # new root node.
            new_root = Node(2)
            new_root.entries[0] = Entry(self.root.entries[0].key, None, self.root)
            new_root.entries[1] = Entry(new_node.entries[0].key, None, new_node)

            self.root = new_root
            self.height += 1

    def insert(self, node, key, value, height):
        """
        Return a new Node if split occurs.
        """
        entry = Entry(key, value, None)
        j = 0
        if height == 0:
            while j < node.length:
                if key < node.entries[j].key:
                    break
                j += 1

        else:
            while j < node.length:
                if j + 1 == node.length or key < node.entries[j + 1].key:
                    # recursely to call insert in the low level subtree.
                    # If split happens the return value is the new splitted
                    # node or the return value is None.
                    new_node = self.insert(node.entries[j].next, key, value, height - 1)
                    if new_node is None:
                        return None

                    # j is the position where the entry should be insert in the
                    # node.
                    j += 1
                    # entry is the smallest key of the new splitted node.
                    entry.key = new_node.entries[0].key
                    entry.next = new_node
                    break

                j += 1

        # now the j is the position where the entry should be insert in the
        # node whether the node is a leaf node or a nonleaf node.
        i = node.length
        node.entries.append(None)
        while i > j:
            node.entries[i] = node.entries[i - 1]
            i -= 1
        node.entries[j] = entry
        node.length += 1
        if node.length < MAX:
            return None
        else:
            return self.split(node)

    def split(self, node):
        """
        Parameter
            node: Node element.

        Return a new splitted node.

            | 5 | 6 | 8 | 9| -> | 5 | 6 | (old node)
                                | 8 | 9 | (new node)

        It is noticed that the new node should be added into the tree.
        The old node is already in the tree.
        """
        new_node = Node(MAX / 2)
        node.length = MAX / 2
        for i in range(MAX / 2):
            new_node.entries[i] = node.entries[MAX / 2 + i]
        return new_node

    def delete(self, key):
        self.remove(key, self.root, self.height)
        if self.root.length == 1 and self.height > 0:
            self.root = self.root.entries[0].next
            self.height -=1

    def remove(self, key, node, height):
        if height == 0:
            i = 0
            while i < node.length:
                if key == node.entries[i].key:
                    break
                i += 1

            if i < node.length:
                # found the position which should be removed.
                j = i
                while j + 1 < node.length:
                    node.entries[j] = node.entries[j + 1]
                    j += 1
                node.length -= 1

            return node
        else:
            i = 0
            while i < node.length:
                if (i + 1) == node.length or key < node.entries[i + 1].key:
                    new_node = self.remove(key, node.entries[i].next, height - 1)
                    if new_node is None:
                        return None
                    node.entries[i].key = new_node.entries[0].key
                    # we merge the deleted_node with other node when it is
                    # necessary
                    delete = False
                    if i == 0:
                        if self.merge(new_node, node.entries[i + 1].next):
                            new_node = node.entries[i + 1].next
                            delete = True
                        node.entries[i + 1].key = node.entries[i + 1].next.entries[0].key
                    else:
                        if self.merge(new_node, node.entries[i - 1].next):
                            new_node = node.entries[i - 1].next
                            delete = True
                        node.entries[i - 1].key = node.entries[i - 1].next.entries[0].key

                    node.entries[i].key = new_node.entries[0].key

                    # now i is the position needed to be deleted
                    if delete:
                        j = i
                        while j + 1 < node.length:
                            node.entries[j] = node.entries[j + 1]
                            j += 1
                        node.length -= 1
                    return node

                i += 1

        return None

    def merge(self, node, other_node):
        """Return True if the node needed to be deleted."""
        if node.length >= MAX / 2:
            return False

        if node.entries[0].key < other_node.entries[0].key:
            """node is less than other_node like:
                node = | 5 | 6 |
                other_node = | 7 | 8 |
            """
            if other_node.length <= MAX / 2:
                """
                we need to fill other_node using node, before filling:
                    node = | 5 |
                    other_node = | 6 | 7 |

                and after filling:

                    node = | 5 |
                    other_node = | 5 | 6 | 7 |

                and the method return True
                """
                for i in range(other_node.length):
                    try:
                        other_node.entries[other_node.length + node.length - 1 - i] = other_node.entries[other_node.length - 1 - i]
                    except:
                        raise
                for i in range(node.length):
                    other_node.entries[i] = node.entries[i]
                other_node.length += node.length
                node.length = 0
                return True
            else:
                """
                we need to borrow some entries from other_node, before borrowing:
                    node = | 5 |
                    other_node = | 6 | 7 | 8 |

                after borrowing:

                    node = | 5 | 6 |
                    other_node = | 7 | 8 |
                """
                borrow_num = other_node.length - MAX / 2
                for i in range(borrow_num):
                    node.entries[node.length + i] = other_node.entries[i]
                node.length += borrow_num

                for i in range(other_node.length - borrow_num):
                    other_node.entries[i] = other_node.entries[borrow_num + i]
                other_node.length -= borrow_num

                return False

        else:
            """node = | 7 | 8|
            other_node = | 5 | 6 |
            """
            if other_node.length <= MAX / 2:
                """In this case:
                    node = | 7 |
                    other_node = | 5 | 6 |
                So, we should add all the entries of the node to other_node
                """
                for i in range(node.length):
                    other_node.entries[other_node.length + i] = node.entries[i]
                other_node.length += node.length
                node.length = 0
                return True
            else:
                """ In this case:
                    node = | 7 |
                    other_node = | 4 | 5 | 6 |
                So, we should borror some node from other_node
                """
                borrow_num = other_node.length - MAX / 2
                for i in range(borrow_num):
                    node.entries[node.length + i] = node.entries[i]
                for i in range(borrow_num):
                    node.entries[i] = other_node.entries[other_node.length - borrow_num + i]

                node.length += borrow_num
                other_node.length -= borrow_num
                return False

    def string(self, node, height):
        if height == 0:
            buf = []
            prefix = []
            for i in range(self.height - height):
                prefix.append("\t")
            prefix = "".join(prefix)
            for i in range(node.length):
                buf.append("%s%s\n" % (prefix, str(node.entries[i].value)))

            return "".join(buf)

        else:
            buf = []
            for i in range(node.length):
                for j in range(self.height - height):
                    buf.append("\t")
                buf.append(str(node.entries[i].key))
                buf.append("\n")
                buf.append(self.string(node.entries[i].next, height - 1))
                buf.append("\n")

            return "".join(buf)

    def __str__(self):
        return self.string(self.root, self.height)


if __name__ == "__main__":
    max = 10000
    tree = BTree()
    for i in range(max):
        tree.put(i, i)

    import random
    print tree
    for i in range(10000000):
        k = random.randint(1, 1000000000)
        tree.delete(k)
        v = tree.get(k)
        if v is not None:
            raise Exception("error")
