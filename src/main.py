from copy_file import copy_file
from generate_page import generate_page

def main():
    copy_file("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()