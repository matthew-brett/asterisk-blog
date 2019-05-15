from copy import deepcopy

from nbconvert.preprocessors import Preprocessor


class HideInputs(Preprocessor):
    """ Preprocessor removes souce code from cells with 'hide_input' tag
    """

    def preprocess(self, nb, resources):
        nbc = deepcopy(nb)
        cells = []
        for c in nbc.cells:
            if c['metadata'].get('hide_input'):
                c['transient'] = {'remove_source': True}
            cells.append(c)
        nbc.cells = cells
        return nbc, resources
