import re
import datetime

class Validator:
    @staticmethod
    def is_date(value: str) -> bool:
        try:
            pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$"
            return bool(re.match(pattern, value))
        except TypeError:
            return False
