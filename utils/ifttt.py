

class IFTTT:
    """A class for representation of 'If This Then That' operation.

    General idea: call <handler>(params) if <trigger>(params) returns True.
    """

    def __init__(self, trigger, handler):
        """Initializes an IFTTT operation object.

        :param trigger: a reference to the trigger function
        :param handler: a reference to the handler function
        """
        self.trigger = trigger
        self.handler = handler

    def perform_operation(self, trigger_params, handler_params=None):
        """Performs an IFTTT operation.

        :param trigger_params: a dictionary of args to pass to the trigger function
        :param handler_params: a dictionary of args to pass to the handler function
        """

        # if handler_params are not specified
        if not handler_params:
            handler_params = trigger_params

        if self.trigger(trigger_params):
            self.handler(handler_params)
