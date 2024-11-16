def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    return list(filter(lambda line: line , map(lambda line: line.strip(), lines)))