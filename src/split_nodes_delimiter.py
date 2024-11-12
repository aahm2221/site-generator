from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if delimiter in node.text:
                split_node = node.text.split(delimiter)
                if len(split_node) % 2 == 0:
                    raise Exception("Invalid markdown: Number of delimiters is not even")
                for i in range(0, len(split_node)-1, 2):
                    if split_node[i]:
                        new_nodes.append(TextNode(split_node[i], TextType.TEXT))
                    if not split_node[i+1]:
                        raise Exception("Invalid markdown: no text within delimiters")
                    if split_node[i+1][0].isspace() or split_node[i+1][-1].isspace():
                        raise Exception("Invalid markdown: Spacing between delimiter and text")
                    new_nodes.append(TextNode(split_node[i+1].strip(), text_type))
                if split_node[-1]:
                        new_nodes.append(TextNode(split_node[-1], TextType.TEXT))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)

    return new_nodes
