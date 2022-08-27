
class Success(object):

    def __set_response(self, *args):

        if args:

            self.__response = {
                "action": args[0],
                "method": args[1],
                "message": args[2],
                "code": args[3],
            }

        else:
            self.__response = {
                "action": "",
                "method": "",
                "message": "",
                "code": "",
            }

    @classmethod
    def response(cls, *args):

        Success.__set_response(cls, *args)

        return Success.__response