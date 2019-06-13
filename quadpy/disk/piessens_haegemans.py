# -*- coding: utf-8 -*-
#
from .helpers import _pm, _pmx, _pmy

from ..helpers import untangle


class PiessensHaegemans(object):
    """
    Robert Piessens and Ann Haegemans,
    Cubature Formulas of Degree Nine for Symmetric Planar Regions,
    Mathematics of Computation, Volume 29, Number 11, July 1975, Pages 810-815,
    <https://doi.org/10.2307/2005291>.
    """

    def __init__(self):
        self.degree = 9
        self.name = "PiessensHaegemans"

        data = [
            (
                0.12937261598422958670,
                _pm(0.86686876801492291622, 0.28376671812094800827),
            ),
            (
                0.77785540900483355115e-2,
                _pm(0.63925306939199114680, 0.95409639862933054563),
            ),
            (
                0.22713305094453060651,
                _pm(0.48645191470776426796, 0.63982457013387676359),
            ),
            (0.32090673961381781518, _pmx(0.51286789206607718656)),
            (0.16042870730308439624, _pmy(0.88859953503035797854)),
            (0.36089243784037735036, _pmy(0.35335517369353007690)),
        ]

        self.points, self.weights = untangle(data)
        return