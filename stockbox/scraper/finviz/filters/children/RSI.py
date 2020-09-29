from ..Filter import Filter


class RSI(Filter):
    prefix: str = "ta_rsi"
    values: dict = {
        "ob90": "Overbought (90)",
        "ob80": "Overbought (80)",
        "ob70": "Overbought (70)",
        "ob60": "Overbought (60)",
        "os40": "Oversold (40)",
        "os30": "Oversold (30)",
        "os20": "Oversold (20)",
        "os10": "Oversold (10)",
        "nob60": "Not Overbought (<60)",
        "nob50": "Not Overbought (<50)",
        "nos50": "Not Oversold (>50)",
        "nos40": "Not Oversold (>40)",
    }
