

class Error(object):

    def __set_error(self, error):

        self.__error = {
            "errors": error
        }

    @classmethod
    def errors(cls, error):

        Error.__set_error(cls, error)

        return Error.__error
