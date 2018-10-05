users = [
{
"id": 1,
"name": "Kevin",
"email": "kevin@email.com",
"password": "kevinrules"
},
{
"id": 2,
"name": "Jemo",
"email": "jemo@email.com",
"password": "jemo2020"
},
{
"id": 3,
"name": "Nzioka",
"email": "nzioka@email.com",
"password": "nzioka2010"
}
]
questions = [
	{
		"id": 1,
		"authorid": 1,
		"header": "Python",
		"subject": "What is python"
	},
	{
		"id": 2,
		"authorid": 2,
		"header": "Material",
		"subject": "What is material css"
	},
	{
		"id": 3,
		"authorid": 3,
		"header": "Java",
		"subject": "What is java"
	},
	{
		"id": 4,
		"authorid": 2,
		"header": "Ruby",
		"subject": "What is ruby"
	}
	
]
answers = [
	{
		"id": 1,
		"questionid": 1,
		"authorid": 3,
		"subject": "This is a boolean",
        "accepted": False
	},
	{
		"id": 1,
		"questionid": 1,
		"authorid": 3,
		"subject": "Python is awesome and usses classes",
        "accepted": False
	},
	{
		"id": 1,
		"questionid": 1,
		"authorid": 3,
		"subject": "Booleans are important",
        "accepted": False
	},
	{
		"id": 1,
		"questionid": 1,
		"authorid": 3,
		"subject": "javascript is irreplacebale",
        "accepted": False
	}
]
class User(object):
	def __init__(self, name, email, password):
		self.name = name
		self.email = email
		self.password = password
		
	def create_user(self):
		user = {}
		user["id"] = users[-1]["id"] + 1
		user["name"] = self.name
		user["email"] = self.email
		user["password"] = self.password

		users.append(user)
		return users

	def login_user(self, email, password):
		self.email = email
		self.password = password

		for user in users:
			if user["email"] == self.email  and user["password"] == self.password:
				return "granted", user
		return "You have entered the wrong details"


class Admin(User):
	def __init__(self, name, email, password):		
		User.__init__(self, name, email, password)


	def delete_user(self, email):
		self.email = email
		for user in users:
			if user["email"] == self.email:
				users.remove(user)
				return users
		return "user email does not exist"

class Reply(object):
	def __init__(self, authorid, subject):
		self.authorid = authorid
		self.subject = subject

	def post_question(self):
		pass
	
	def fetch_one_question(self):
		pass

class Question(Reply):
	def __init__(self, authorid, header, subject):
		self.header = header
		Reply.__init__(self, authorid, subject)
    # def delete_question(self, questionid, authorid):
    #     for question in questions:
    #         if question["id"] = questionid and question["authorid"] == authorid:
    #             questions.remove(question)
    #             return questions
    

	def get_all_questions(self):
		return questions


	def post_question(self):
		new_question = {}

		new_question["id"] = questions[-1]["id"] + 1
		new_question["authorid"] = self.authorid
		new_question["header"] = self.header
		new_question["subject"] = self.subject

		questions.append(new_question)
		return questions

	def fetch_one_question(self, questionid):
		for question in questions:
			if question["id"] == questionid:
				return "success", question
		return "You have entered a wrong question ID"
class Answer(Reply):
    def __init__(self, questionid, authorid, subject, accepted):
        self.accepted = accepted
        self.questionid = questionid
        Reply.__init__(self, authorid, subject)

    def post_answer(self):
        new_answer = {}

        new_answer["id"] = answers[-1]["id"] + 1
        new_answer["questionid"] = self.questionid
        new_answer["authorid"] = self.authorid
        new_answer["subject"] = self.subject

        answers.append(new_answer)
        return answers

    def update_answer(self, id,questionid):
        self.id = id
        for answer in answers:

            if answer["id"] == self.id and answer["questionid"] == self.questionid:
                if answer["authorid"] == self.authorid:
                    new_subject = "I think java is a powerful language"

                    answer["id"] = id
                    answer["questionid"] = self.questionid
                    answer["subject"] = new_subject
                    answer["accepted"] = self.accepted

                    return answers

                else:
                    for question in questions:
                        if self.questionid == question["id"]:
                            if question["authorid"] == self.authorid:
                                answer["accepted"] = True
                                return answers

                return "You have entered the wrong details or no auth"




    
        
# ans = Answer(2, 1, "It think java is such a hard language", False)
# print(ans.post_answer())   
# deleteQ = Question(3, "Java", "What is java")
# print(deleteQ.delete_question(3))
# fetchquiz = Question(5, "Kew", "Material css")
# print(fetchquiz.fetch_one_question(4))
# # newquiz = Question(2, "Javascript", "What is javascript?" )
# print(newquiz.post_question())
# # # userad = Admin("maria", "maria@email.com", "maria")

# # print(userad.delete_user( "kevin@email.com"))
# newuser = User("seth", "seth@email.com", "seth2020")
# usertry = User("jemoku", "jemoh@email.com", "jemo2020")
# # user2 = User("Kevin", "kevin@email.com", "kevinrules")
# print(usertry.login_user("jemo@email.com", "jemo2020"))
# print(newuser.create_user())