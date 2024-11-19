from copy_file import copy_file
from generate_page import generate_pages_recursive

def main():
    copy_file("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()