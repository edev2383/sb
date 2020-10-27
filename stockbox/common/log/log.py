import logging


class Log:
    def __init__(self, module, level):
        self.level = level
        logging.basicConfig(
            filename=f"/var/www/edickdev/cgi-bin/py/{module}/{module}.log",
            format="%(asctime)s %(levelname)-8s %(message)s",
            level=logging.DEBUG,
            datefmt="%Y-%m-%d %H:%M:%S",
        )

    @staticmethod
    def info(msg, module="sb"):
        Log(module, "info").write(msg)

    @staticmethod
    def debug(msg, module="sb"):
        Log(module, "debug").write(msg)

    def write(self, msg):
        switch = {"info": logging.info, "debug": logging.debug}
        func = switch.get(self.level)
        return func(msg)
