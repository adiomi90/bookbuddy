from models import Discussion

class CommunityManager:
    def __init__(self, session):
        self.session = session

    def start_discussion(self, user_id, topic, content):
        # Create a new Discussion object with the provided information
        new_discussion = Discussion(user_id=user_id, topic=topic, content=content)

        # Add the new_discussion object to the session
        self.session.add(new_discussion)
        
        # Commit the transaction to save the changes to the database
        self.session.commit()

    def display_discussions(self):
        # Query all discussions from the database
        discussions = self.session.query(Discussion).all()

        if not discussions:
            print("No discussions found.")
            return

        # Print information for each discussion
        for discussion in discussions:
            print(f"Topic: {discussion.topic}, Content: {discussion.content}")
