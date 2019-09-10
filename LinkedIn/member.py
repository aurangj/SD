
import datetime
class Member:

    def __init__(self):
        self.memberid
        self.education =None
        self.experience = None
        self.name = None
        self.recommendationiD#maps to recommendationId in recommend table
        self.followerid

    def add_education(self):
        pass

    def add_experience(self):
        pass
    def display_followers(self):

    def display_given_recommendation(self):
        pass

    def display_recieved_recommendation(self):
        pass
    def request_recommendation(self,member):
        r1 = Recommendation(self,member)
        return r1



class Company:

    def __init__(self):
        self.company_id = auto_generated()
        self.name =None
        self.description = None
        self.jobs = []

    def add_jobs(self):
        pass
    def add_description(self):
        pass

class Group:

    def __init__(self,name,description):
        self.group_id = auto_generated()
        self.name = name
        self.description = description

class Post:
    def __init__(self):
        self.post_id
        self.message
        self.no_of_likes
    def edit_post(self,message):
        self.message = message


class Comment:
    def __init__(self):
        self.comment_id
        self.postid
        self.comment_text
        self.recomment_text = None
        self.recomment_id = False

    def add_comment(self,post_id,text):
        self.post_id = post_id
        if self.recomment_id:
            self.recomment_text = text

        else:
            self.comment_text = text
            self.recomment_id = True



class Follow:
    def __init__(self):
        self.follow_id
        self.start_date
        self.end_date

    def un_follow(self):
        self.end_date = today()

class Recommendation:

    def __init__(self):
        self.recommendId
        self.member_giver  #maps to memberID in member table
        self.member_reciever # maps to memberID in member table
        self.recommend_text
    def add_recomendation(self,text):
        self.recommend_text = text


class LinkedinSystem:

    m1 = Member()
    m2 = Member()
    c1 = company()
    g1 = group()
    m2.request_recommendation(m1)
    m1.add_recommendation("text")


