from pycallgraph import PyCallGraph
from pycallgraph import Config
from pycallgraph import GlobbingFilter
from pycallgraph.output import GraphvizOutput

from test.banana import Banana

config = Config(max_depth=1)
config.trace_filter = GlobbingFilter(exclude=[
    'pycallgraph.*',
    '*.secret_function'
])

graphviz = GraphvizOutput(output_file='filter_max_depth.png')

with PyCallGraph(output=graphviz, config=config):
    banana = Banana()
    banana.eat()
