from htmlnode import HtmlNode
class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("error: no tag")
        if not self.children:
            raise ValueError("error: no children")
        return f"<{self.tag}{self.props_to_html()}>{"".join(list(map(lambda child: child.to_html(), self.children)))}</{self.tag}>\n"