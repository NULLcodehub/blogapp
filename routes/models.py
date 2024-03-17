from app import mongo

class News:
    def __init__(self,title,discription):
        self.title=title
        self.discription=discription
    
    def save_to_db(self):
        mongo.db.news_data.insert_one({
            'title':self.title,
            'discription':self.discription
        })