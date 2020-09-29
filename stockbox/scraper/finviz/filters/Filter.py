from ..reader.Reader import Reader


class Filter:
    read_prefix: str = "fs_"
    prefix: str = "no_filter"
    xpath: str = ""
    values: dict = {}
    test: int
    key: str

    # TODO - Check if the key exists in the Filter child and exit if not
    def __init__(self, key=""):
        self.key = key

    # Outputs the complete filter string, with the supplied key value
    def get_filter_string(self):
        return f"{self.prefix}_{self.key}"

    # Output the values dict in the CLI. Future refactoring will
    # output this as JSON to be asynced to Rails front end
    def read(self):
        for key in self.values.keys():
            print(f"{key}: {self.values[key]}")

    # Method for building required xpath to grab values from the url
    # destination, once acquired, should be stable, unless target url
    # changes their filter keys and/or we decide to acquire more
    # of their filters
    # Could automate this and store the values in a JSON file, so
    # we don't have to hard code the dicts
    def build_xpath(self):
        #  "//a[@class='screener-link-primary']/text()"
        return f"{self.read_prefix}{self.prefix}"

    # Deprecated. Since the initial trial run of child Filters is
    # complete, the request() method in class Reader has been changed.
    def acquire(self, xpath):
        # return Reader(xpath).request()
        print("This Reader().request method has been deprecated.")
        print("There is currently no replacement.")


# read() - output definition of all values and their key
# build(value) - output the string value
