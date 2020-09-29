from ..Filter import Filter


class MarketCap(Filter):
    prefix: str = "cap"
    values: dict = {
        "mega": "Mega ($200bln and more)",
        "large": "Large ($10bln to $200bln)",
        "mid": "Mid ($2bln to $10bln)",
        "small": "Small ($300mln to $2bln)",
        "micro": "Micro ($50mln to $300mln)",
        "nano": "Nano (under $50mln)",
        "largeover": "+Large (over $10bln)",
        "midover": "+Mid (over $2bln)",
        "smallover": "+Small (over $300mln)",
        "microover": "+Micro (over $50mln)",
        "largeunder": "-Large (under $200bln)",
        "midunder": "-Mid (under $10bln)",
        "smallunder": "-Small (under $2bln)",
        "microunder": "-Micro (under $300mln)",
    }
