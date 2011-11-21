# -*- coding: utf-8 -*-
# study.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('study/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'study/index': 'study.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='study.views.index'),
  )
]

