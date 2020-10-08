import re
from .statement_component import StatementComponent
from .focus import Focus


class Comparison(StatementComponent):
    """Breaks the comparison component into manageable pieces

    Args:
        StatementComponent
    """

    re_complex = r"(.*)\s?([*\+\-\/])\s?(.*)"
    re_numeric = r"[-+]?\d*\.\d+|\d+"

    def process(self):
        return self.get_matches()

    def get_matches(self):
        found = re.match(self.re_complex, self.component)
        if found:
            return self.format_comparison(found)
        else:
            numeric = re.match(self.re_numeric, self.component)
            if numeric:
                return self.format_numeric_comparison(numeric)
        return Focus(self.component).process()

    def format_comparison(self, match):
        comp_focus = match.group(1).strip()
        comp_operator = match.group(2).strip()
        comp_value = match.group(3).strip()
        ret_dict = Focus(comp_focus).process()
        ret_dict["extension"] = {
            "operator": comp_operator,
            "value": comp_value,
        }
        return ret_dict

    def format_numeric_comparison(self, match):
        return {"value": match.group().strip()}
