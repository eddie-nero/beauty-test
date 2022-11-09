import re

TEST_TEXT = """{name}, ваша запись изменена:
⌚️ {day_month} в {start_time}
👩 {master}
Услуги:
{services}
управление записью {record_link}"""


class CurlyBracesNotEqualError(Exception):
    pass


class UserRequestChecker:

    keys_regex = r"\{(.*?)\}"

    list_keys = [
        "name",
        "day_month",
        "day_of_week",
        "start_time",
        "end_time",
        "master",
        "services",
        "record_link",
    ]

    @staticmethod
    def _is_braces_equal(text: str):
        equality = text.count("{") == text.count("}")
        if equality:
            return equality
        raise CurlyBracesNotEqualError("Opening and closing braces are not equal.")

    def _is_keys_allowed(self, text: str):
        matches = re.findall(self.keys_regex, text)
        for key in matches:
            if key in self.list_keys:
                continue
            raise ValueError(f"Key <{key}> not allowed")

    def check(self, text: str):
        self._is_braces_equal(text)
        self._is_keys_allowed(text)
        return text


checker = UserRequestChecker()
result = checker.check(TEST_TEXT)
print(result)
