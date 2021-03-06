from ..Filter import Filter


class HighLowYear(Filter):
    prefix: str = "ta_highlow52w"
    values: dict = {
        "nh": "New High",
        "nl": "New Low",
        "b5h": "5% or more below High",
        "b10h": "10% or more below High",
        "b15h": "15% or more below High",
        "b20h": "20% or more below High",
        "b30h": "30% or more below High",
        "b40h": "40% or more below High",
        "b50h": "50% or more below High",
        "b60h": "60% or more below High",
        "b70h": "70% or more below High",
        "b80h": "80% or more below High",
        "b90h": "90% or more below High",
        "b0to3h": "0-3% below High",
        "b0to5h": "0-5% below High",
        "b0to10h": "0-10% below High",
        "a5h": "5% or more above Low",
        "a10h": "10% or more above Low",
        "a15h": "15% or more above Low",
        "a20h": "20% or more above Low",
        "a30h": "30% or more above Low",
        "a40h": "40% or more above Low",
        "a50h": "50% or more above Low",
        "a60h": "60% or more above Low",
        "a70h": "70% or more above Low",
        "a80h": "80% or more above Low",
        "a90h": "90% or more above Low",
        "a100h": "100% or more above Low",
        "a120h": "120% or more above Low",
        "a150h": "150% or more above Low",
        "a200h": "200% or more above Low",
        "a300h": "300% or more above Low",
        "a500h": "500% or more above Low",
        "a0to3h": "0-3% above Low",
        "a0to5h": "0-5% above Low",
        "a0to10h": "0-10% above Low",
    }
