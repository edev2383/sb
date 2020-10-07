import re
from .statement_component import StatementComponent
from .focus import Focus


class Comparison(StatementComponent):
    """Breaks the comparison component into manageable pieces

    Args:
        StatementComponent
    """

    re_complex = r"(.*)\s?([*\+\-\/])\s?(.*)"

    def process(self):
        return self.get_matches()

    def get_matches(self):
        found = re.match(self.re_complex, self.component)
        if found:
            comp_focus = found.group(1).strip()
            comp_operator = found.group(2).strip()
            comp_value = found.group(3).strip()
            ret_dict = Focus(comp_focus).process()
            ret_dict["extension"] = {
                "operator": comp_operator,
                "value": comp_value,
            }
            return ret_dict
        else:
            return Focus(self.component).process()
