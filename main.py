class Node:
    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

def huffman_encoding(alphabet, weights):
    nodes = [Node(char, f) for char, f in zip(alphabet, weights)]

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        node1 = nodes.pop(0)
        node2 = nodes.pop(0)
        new_node = Node(None, node1.freq + node2.freq)
        new_node.left = node1
        new_node.right = node2
        nodes.append(new_node)

    encoding_table = {}
    def traverse_tree(node, code=''):
        if node.value is not None:
            encoding_table[node.value] = code
        else:
            traverse_tree(node.left, code + '0')
            traverse_tree(node.right, code + '1')
    traverse_tree(nodes[0])

    encoded_data = ''.join(encoding_table[char] for char in alphabet)
    return encoded_data, encoding_table

alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 't', 'g', 'h', 'i', 'j'}
weights = [8, 6, 2, 3, 4, 7, 11, 9, 8, 1, 3]
encoded_data, encoding_table = huffman_encoding(alphabet, weights)

print("Alphabet:", alphabet)
print("Weights:", weights)
print("Encoded data:", encoded_data)
print("Encoding table:", encoding_table)
