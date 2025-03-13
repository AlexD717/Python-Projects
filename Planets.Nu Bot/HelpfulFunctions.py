def AskQuestion(question, viableAnsers):
    answer = input(question + " ").lower()
    if (answer in viableAnsers):
        return answer
    else:
        print("\nThat isn't a valid answer, please try again")
        return AskQuestion(question, viableAnsers)

confirmativeReplies = ["y", "yes", "sure"]
def GetConformation(question="Are you sure you want to do this?"):
    answer = input(question + " ").lower()
    if (answer in confirmativeReplies):
        return True
    else:
        return False