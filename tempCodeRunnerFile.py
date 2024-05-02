from user_manager import UserManager
from book_manager import BookManager
from blog_manager import BlogManager
from community_manager import CommunityManager
from database_connection import Session

def main():
    user_manager = UserManager(Session())
    book_manager = BookManager(Session())
    blog_manager = BlogManager(Session())
    community_manager = CommunityManager(Session())

    while True:
        print("\nWelcome to BookBuddy!")
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            success, message = user_manager.create_user(username, email, password)
            print(message)

        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            success, message = user_manager.authenticate_user(email, password)
            print(message)
            if success:
                while True:
                    print("\nBookBuddy Menu:")
                    print("1. Browse Books")
                    print("2. Write Blog Post")
                    print("3. Start Discussion")
                    print("4. Log Out")

                    user_choice = input("Enter your choice: ")

                    if user_choice == "1":
                        book_manager.display_books()

                    elif user_choice == "2":
                        title = input("Enter blog post title: ")
                        content = input("Enter blog post content: ")
                        blog_manager.add_blog_post(email, title, content)
                        print("Blog post created successfully.")

                    elif user_choice == "3":
                        topic = input("Enter discussion topic: ")
                        content = input("Enter discussion content: ")
                        community_manager.start_discussion(email, topic, content)
                        print("Discussion started successfully.")

                    elif user_choice == "4":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "3":
            print("Exiting BookBuddy...")
            break

        else:
            print("Invalid choice. Please try again.")

    # Close the session when done
    Session.close()

if __name__ == "__main__":
    main()
