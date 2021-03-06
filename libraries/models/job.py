from __future__ import unicode_literals, print_function
from libraries.models.model import Model
from libraries.app.app import App


class TxJob(Model):
    db_keys = [
        'job_id'
    ]

    db_fields = [
        'job_id',
        'user',
        'identifier',
        'convert_module',
        'created_at',
        'expires_at',
        'started_at',
        'ended_at',
        'eta',
        'resource_type',
        'input_format',
        'source',
        'output_format',
        'output',
        'cdn_bucket',
        'cdn_file',
        'callback',
        'links',
        'status',
        'success',
        'message',
        'log',
        'warnings',
        'errors',
    ]

    default_values = {
        'links': [],
        'log': [],
        'warnings': [],
        'errors': [],
    }

    def __init__(self, *args, **kwargs):
        # Init attributes
        self.job_id = None
        self.user = None
        self.identifier = None
        self.convert_module = None
        self.created_at = None
        self.expires_at = None
        self.started_at = None
        self.ended_at = None
        self.eta = None
        self.resource_type = None
        self.input_format = None
        self.source = None
        self.output_format = None
        self.output = None
        self.cdn_bucket = None
        self.cdn_file = None
        self.callback = None
        self.links = []
        self.status = None
        self.success = None
        self.message = None
        self.api_base_url = None
        self.cdn_base_url = None
        self.log = []
        self.warnings = []
        self.errors = []
        if 'db_handler' not in kwargs or not kwargs['db_handler']:
            kwargs['db_handler'] = App.job_db_handler()
        super(TxJob, self).__init__(*args, **kwargs)

    def log_message(self, message):
        self.log.append(message)

    def error_message(self, message):
        self.errors.append(message)

    def warning_message(self, message):
        self.warnings.append(message)
