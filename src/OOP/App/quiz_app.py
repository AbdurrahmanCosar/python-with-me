# Quiz App

# Question sınıfı
#   Instance Attributes
#       - text, choices, answer
#   Instance Methods
#       - q1.checkAnswer('python') => True ya da False

# q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
# q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
# q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

# sorular = [q1,q2,q3]

# Quiz sınıfı
#   Instance Attributes
#       - questions, questionIndex, score
#   Instance Methods
#       - getQuestion()         => questionIndex' e göre question nesnesi getirir.
#       - displayQuestion()     => getQuestion() ile alınan nesneyi gösterir.
#       - loadQuestion()        => Testi başlatır.
#       - displayScore()        => Score bilgisini gösterir.
#       - displayProgress()     => Testdeki ilerlemeyi gösterir. (5 sorunun 2.sorusundasınız.)

#quiz = Quiz(sorular)


from random import sample

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer


    def checkAnswer(self, answer):
        if answer not in self.choices:
            raise ValueError("Hatalı Bilgi")
        return self.answer == answer
    
q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")


sorular = [q1,q2,q3]

class Quiz:
    def __init__(self, questions):
        self.questions = sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]


    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Skor: {self.score}")
        print(f"{self.questionIndex + 1}. Soru) {question.text}")
              
        for q in question.choices:
            print(f"- {q}".title())

        answer = input("Cevap: ")

        question = self.getQuestion()

        if (question.checkAnswer(answer)):
            self.score += 1

        self.questionIndex += 1
        self.loadQuestion()
        

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()
    
    def displayScore(self):
        print(f"Skor: {self.score}")
    
    def displayProgress(self):
        print(f"{len(self.questions)} sorunun {self.questionIndex + 1}. sorusundasınız.".center(100, "*"))
    
    
    


quiz = Quiz(sorular)
quiz.loadQuestion()

