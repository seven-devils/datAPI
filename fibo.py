#!/datAPI/flask/bin/python


class restfib(object):
    def san_number(self, number='null'):

        """
        Sanitize them numbers.

        Sanity check to make sure the number is:
            1: not negative.
            2: not suuuuuuuuuuuuuuuper large.
            3: not empty.
            4: a ... you know... number.
        """

        self.number = number

        if self.number == 'null':
            result = {"Error01": "You must submit only a whole number!"}

        elif self.number < 0:
            result = {"Error02": "Negative numbers not allowed."}

        elif self.number > 999:
            result = {"Error03": "Numbers larger than 999 not allowed."}

        else:
            result = True

        return result

    def make_list(self, number=0):

        """
        Create our actual list.

        Takes the input from the API and creates the list.
        Returns a list to caller.
        """

        number = number
        fiblist = []
        orig_num = 0
        next_num = 1
        for step in xrange(0, number):
            fiblist.append(orig_num)
            orig_num, next_num = next_num, orig_num + next_num
        return fiblist
