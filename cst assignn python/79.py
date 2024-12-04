##79.	Develop a content management system using object-oriented principles and file handling.1


# Simple CMS with file handling

def add_article():
    """Add a new article."""
    title = input("Enter article title: ")
    content = input("Enter article content: ")
    with open("articles.txt", "a") as file:
        file.write(f"{title}:::{content}\n")
    print("Article added!")

def view_articles():
    """View all articles."""
    try:
        with open("articles.txt", "r") as file:
            articles = file.readlines()
            if articles:
                for article in articles:
                    title, content = article.strip().split(":::")
                    print(f"\nTitle: {title}\nContent: {content}\n")
            else:
                print("No articles found.")
    except FileNotFoundError:
        print("No articles found.")

# Menu
while True:
    print("\n1. Add Article\n2. View Articles\n3.Exit")
    choice = input("Choose an option:")
    if choice == "1":
        add_article()
    elif choice == "2":
        view_articles()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
