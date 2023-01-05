class GetAccepted:
    def answer(self, question):
        if question.split().count("not")%2==0:
            return "True."
        else:
            return "False."
