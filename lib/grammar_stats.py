class GrammarStats:
    def __init__(self):
        self.total_checks = 0
        self.passed_checks = 0

    def check(self, text):
        if text[0].isupper() and text[-1] in ['!', '?', '.']:
            self.passed_checks += 1
            self.total_checks += 1
            return True
        self.total_checks += 1
        return False

    def percentage_good(self):
        if self.total_checks == 0:
            return '0%'
        return f'{int((self.passed_checks / self.total_checks) * 100)}%'
