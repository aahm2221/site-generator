def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    return list(filter(lambda line: line , map(lambda line: line.strip(), lines)))

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif block_checker(block, ">"):
        return "quote"
    elif  block_checker(block, "ul"):
        return "unordered_list"
    elif  block_checker(block, "ol"):
        return "ordered_list"
    else:
        return "paragraph"

def block_checker(block, type):
    split_block = block.split("\n")
    line_starter = ">"
    if type == "ol":
        count = 1
        line_starter = str(count) + ". "
    if type == "ul":
        if split_block[0].startswith("*"):
            line_starter = "* "
        else:
            line_starter = "- "
    for line in split_block:
        if not line.startswith(line_starter):
            return False
        if type == "ol":
            count +=1
            line_starter = str(count) + ". "
    return True