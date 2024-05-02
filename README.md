# BookBuddy

Welcome to BookBuddy, your ultimate reading platform! BookBuddy is designed to make your reading experience more enjoyable, social, and engaging. Whether you're looking for your next favorite book, eager to share your thoughts on the latest bestseller, or craving to connect with fellow book lovers, BookBuddy has you covered.

## Features

- **Discover**: Explore a vast catalog of books across genres and authors.
- **Read**: Dive into captivating stories directly within the platform.
- **Blog**: Share your reading journey, insights, and reviews through personal blog posts.
- **Connect**: Engage with a vibrant community of book enthusiasts through discussions and book clubs.
- **Share**: Spread the love for books by sharing recommendations, blog posts, and reading updates with friends.

## Get Started

### Installation

1. **Clone the Repository**:
- github.com/adiomi90/bookbuddy.git

2. **Install Dependencies**:
- pip install bcrypt mysql-connector-python


3. **Set up MySQL Database**:
- Create a MySQL database for BookBuddy.
- Update the database connection details in `database.py`.

4. **Run the Application**:
python3 bookbuddy.py


## Usage

1. **Sign Up or Log In**: Create an account or log in to access the platform.
2. **Explore**: Discover new books, read online, and add them to your collection.
3. **Blog**: Write and publish blog posts to share your reading experiences and recommendations.
4. **Connect**: Engage with the community by joining discussions, book clubs, and sharing your thoughts.


## Database Schema

BookBuddy uses MySQL to store user information, book data, blog posts, and community interactions. Here's a simplified overview:

### users
| id | username | email          | password        |
|----|----------|----------------|-----------------|
| 1  | user1    | user1@email.com | hashed_password |
| 2  | user2    | user2@email.com | hashed_password |

### books
| id | title   | author   | genre       | image |
|----|---------|----------|-------------|-------|
| 1  | Book 1  | Author 1 | Fiction     | url   |
| 2  | Book 2  | Author 2 | Non-fiction | url   |

### blog_posts
| id | user_id | title           | content     | created_at         | updated_at |
|----|---------|-----------------|-------------|---------------------|------------|
| 1  | 1       | My Reading Diary| Lorem ipsum | 2022-04-01 12:00:00 | NULL       |
| 2  | 2       | Book Review     | Lorem ipsum | 2022-04-02 09:00:00 | NULL       |

### community
| id | user_id | discussion_topic | created_at         |
|----|---------|------------------|---------------------|
| 1  | 1       | Book Club        | 2022-04-01 12:00:00 |
| 2  | 2       | Literary Circle  | 2022-04-02 09:00:00 |


## Contributing

We welcome contributions from the community! If you have any suggestions, bug reports, or feature requests, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
