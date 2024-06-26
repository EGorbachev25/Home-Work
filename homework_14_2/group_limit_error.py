class GroupLimitError(Exception):

    def __init__(self, message="The maximum number of students in a group has been exceeded"):
        self.message = message
        super().__init__(self.message)
