from __future__ import print_function, unicode_literals
from libraries.linters.usfm_linter import UsfmLinter
from libraries.linters.obs_linter import ObsLinter
from libraries.linters.udb_linter import UdbLinter
from libraries.linters.ulb_linter import UlbLinter
from libraries.linters.ta_linter import TaLinter
from libraries.linters.tn_linter import TnLinter
from libraries.linters.tq_linter import TqLinter
from libraries.linters.tw_linter import TwLinter
from libraries.linters.markdown_linter import MarkdownLinter
from libraries.resource_container.ResourceContainer import BIBLE_RESOURCE_TYPES


class LinterHandler(object):

    @staticmethod
    def get_linter_class(resource_id):
        if resource_id == 'obs':
            return ObsLinter
        elif resource_id == 'ta':
            return TaLinter
        elif resource_id == 'tn':
            return TnLinter
        elif resource_id == 'tq':
            return TqLinter
        elif resource_id == 'tw':
            return TwLinter
        elif resource_id == 'udb':
            return UdbLinter
        elif resource_id == 'ulb':
            return UlbLinter
        elif resource_id in BIBLE_RESOURCE_TYPES:
            return UsfmLinter
        else:
            return MarkdownLinter
