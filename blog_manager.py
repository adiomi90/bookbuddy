from models import BlogPost

class BlogManager:
    def __init__(self, session):
        self.session = session

    def add_blog_post(self, user_id, title, content):
        # Create a new BlogPost object with the provided information
        new_post = BlogPost(user_id=user_id, title=title, content=content)

        # Add the new_post object to the session
        self.session.add(new_post)
        
        # Commit the transaction to save the changes to the database
        self.session.commit()

    def display_blog_posts(self):
        # Query all blog posts from the database
        posts = self.session.query(BlogPost).all()

        if not posts:
            print("No blog posts found.")
            return

        # Print information for each blog post
        for post in posts:
            print(f"Title: {post.title}, Content: {post.content}")
