from ..Filter import Filter


class Price(Filter):
    prefix: str = "sh_price"
    values: dict = {
        "u1": "Under $1",
        "u2": "Under $2",
        "u3": "Under $3",
        "u4": "Under $4",
        "u5": "Under $5",
        "u7": "Under $7",
        "u10": "Under $10",
        "u15": "Under $15",
        "u20": "Under $20",
        "u30": "Under $30",
        "u40": "Under $40",
        "u50": "Under $50",
        "o1": "Over $1",
        "o2": "Over $2",
        "o3": "Over $3",
        "o4": "Over $4",
        "o5": "Over $5",
        "o7": "Over $7",
        "o10": "Over $10",
        "o15": "Over $15",
        "o20": "Over $20",
        "o30": "Over $30",
        "o40": "Over $40",
        "o50": "Over $50",
        "o60": "Over $60",
        "o70": "Over $70",
        "o80": "Over $80",
        "o90": "Over $90",
        "o100": "Over $100",
        "1to5": "$1 to $5",
        "1to10": "$1 to $10",
        "1to20": "$1 to $20",
        "5to10": "$5 to $10",
        "5to20": "$5 to $20",
        "5to50": "$5 to $50",
        "10to20": "$10 to $20",
        "10to50": "$10 to $50",
        "20to50": "$20 to $50",
        "50to100": "$50 to $100",
    }
