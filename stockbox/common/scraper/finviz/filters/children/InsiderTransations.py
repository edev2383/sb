from ..Filter import Filter


class InsiderTransactions(Filter):
    prefix: str = "sh_insidertrans"
    values: dict = {
        "veryneg": "Very Negative (<20%)",
        "neg": "Negative (<0%)",
        "pos": "Positive (>0%)",
        "verypos": "Very Positive (>20%)",
        "u-90": "Under -90%",
        "u-80": "Under -80%",
        "u-70": "Under -70%",
        "u-60": "Under -60%",
        "u-50": "Under -50%",
        "u-45": "Under -45%",
        "u-40": "Under -40%",
        "u-35": "Under -35%",
        "u-30": "Under -30%",
        "u-25": "Under -25%",
        "u-20": "Under -20%",
        "u-15": "Under -15%",
        "u-10": "Under -10%",
        "u-5": "Under -5%",
        "o5": "Over +5%",
        "o10": "Over +10%",
        "o15": "Over +15%",
        "o20": "Over +20%",
        "o25": "Over +25%",
        "o30": "Over +30%",
        "o35": "Over +35%",
        "o40": "Over +40%",
        "o45": "Over +45%",
        "o50": "Over +50%",
        "o60": "Over +60%",
        "o70": "Over +70%",
        "o80": "Over +80%",
        "o90": "Over +90%",
    }
