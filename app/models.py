from datetime import datetime

class GithubActionShema():
    def __init__(self, request_id, author, action, from_branch, to_branch):
        self.request_id = request_id
        self.author = author
        self.action = action
        self.from_branch = from_branch
        self.to_branch = to_branch
        
    def to_dict(self):
        return {
            "request_id": self.request_id,
            "author": self.author,
            "action": self.action,
            "from_branch": self.from_branch,
            "to_branch": self.to_branch,
            "timestamp": datetime.now()
        }    
        
        
    