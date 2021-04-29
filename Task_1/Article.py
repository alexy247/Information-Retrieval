import json

class Article:
    def __init__(self, article_id, title, author_id, author_name, comments, rating, rating_full, date, tags, views, saves, text):
        self.id = article_id
        self.title = title
        self.author_id = author_id
        self.author_name = author_name
        self.comments = comments
        self.rating = rating
        self.rating_full = rating_full
        self.date = date
        self.tags = tags
        self.views = views
        self.saves = saves
        self.text = text 

    def get_json(self):
        return {'id': self.id, 'title': self.title, 'author_id': self.author_id, 'author_name': self.author_name,
             'comments': self.comments, 'rating': self.rating, 'rating_full': self.rating_full, 'date': self.date, 
             'tags': self.tags, 'views': self.views, 'saves': self.saves, 'text': self.text}