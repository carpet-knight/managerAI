import sys
import importlib
from yaml import safe_load, YAMLError
from utils.ifttt import IFTTT


class Manager:

    DEFAULT_MANAGER_CONFIG_NAME = "manager_config.yaml"

    EXCLUDE_FROM_PARAMS = [
        "trigger",
        "handler"
    ]

    def __init__(self, config_path):
        # load configuration info from YAML file
        with open(config_path, 'r') as config_file:
            try:
                self.config_dict = safe_load(config_file.read())
            except YAMLError as e:
                # TODO: Exception handling
                return

    @staticmethod
    def _get_func_by_path(path: str):
        """Returns a reference to a function specified in {path}."""

        try:
            module, cls, method = path.split(".")
            module = importlib.import_module(module)
            cls = getattr(module, cls)
            method = getattr(cls, method)
        except Exception as e:
            # TODO: Exception handling
            return

        return method

    def start(self):
        for task in self.config_dict["tasks"]:
            # IFTTT.trigger function
            trigger = Manager._get_func_by_path(task["trigger"])
            # IFTTT.handler function
            handler = Manager._get_func_by_path(task["handler"])

            # params_dict for trigger and handler
            params = {k: v for k, v in task.items() if k not in Manager.EXCLUDE_FROM_PARAMS}

            ifttt = IFTTT(trigger, handler)
            ifttt.perform_operation(params)


if __name__ == "__main__":
    config = sys.argv[1] if len(sys.argv) > 1 else Manager.DEFAULT_MANAGER_CONFIG_NAME
    manager = Manager(config)
    manager.start()
