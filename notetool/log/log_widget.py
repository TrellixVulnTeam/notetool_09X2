import logging

import ipywidgets as widgets
from IPython.display import display

DEFAULT_FORMAT = '%(asctime)s  - [%(levelname)s] %(message)s'


class OutputWidgetHandler(logging.Handler):
    """ Custom logging handler sending logs to an output widget """

    def __init__(self, *args, **kwargs):
        super(OutputWidgetHandler, self).__init__(*args, **kwargs)
        layout = {
            'width': '100%',
            'height': '160px',
            'border': '1px solid black'
        }
        self.out = widgets.Output(layout=layout)

    def emit(self, record):
        """ Overload of logging.Handler method """
        formatted_record = self.format(record)
        new_output = {
            'name': 'stdout',
            'output_type': 'stream',
            'text': formatted_record + '\n'
        }
        self.out.outputs = (new_output,) + self.out.outputs

    def show_logs(self):
        """ Show the logs """
        display(self.out)

    def clear_logs(self):
        """ Clear the current logs """
        self.out.clear_output()


def load_log_widget(name=None, formatter=None, *args, **kwargs):
    name = name or __name__
    formatter = formatter or DEFAULT_FORMAT
    logger = logging.getLogger(name)
    handler = OutputWidgetHandler(*args, **kwargs)
    handler.setFormatter(logging.Formatter(formatter))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    return logger, handler

    # handler.show_logs()
    # handler.clear_logs()
    # logger.info('Starting program')
