class ResultWriter(object):
    def output_for(self, account_number):
        return account_number.as_string() + '\t' + self.status_for(account_number)

    def status_for(self, account_number):
        if not account_number.is_legible(): return "ILL"
        if not account_number.is_valid(): return "ERR"
        return ""