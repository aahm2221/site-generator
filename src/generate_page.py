import os
from markdown_to_html_node import markdown_to_html_node
from extract_markdown import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    template = ""
    with open(from_path) as file:
        markdown = file.read()
        file.close()
    with open(template_path) as file:
        template = file.read()
        file.close()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)
    os.makedirs(dest_path.rsplit("/",1)[0], exist_ok =True)
    with open(dest_path, "w") as file:
        file.write(template)
        file.close()


    
