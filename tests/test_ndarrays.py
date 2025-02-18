# Tests of support for Numpy ndarrays. See
# https://github.com/sgillies/shapely/issues/26 for discussion.

from functools import reduce

import numpy as np

from . import unittest, shapely20_deprecated
from shapely import geometry


class TransposeTestCase(unittest.TestCase):

    def test_multipoint(self):
        arr = np.array([[1.0, 1.0, 2.0, 2.0, 1.0], [3.0, 4.0, 4.0, 3.0, 3.0]])
        tarr = arr.T
        shape = geometry.MultiPoint(tarr)
        coords = reduce(lambda x, y: x + y, [list(g.coords) for g in shape.geoms])
        self.assertEqual(
            coords,
            [(1.0, 3.0), (1.0, 4.0), (2.0, 4.0), (2.0, 3.0), (1.0, 3.0)]
        )

    def test_linestring(self):
        a = np.array([[1.0, 1.0, 2.0, 2.0, 1.0], [3.0, 4.0, 4.0, 3.0, 3.0]])
        t = a.T
        s = geometry.LineString(t)
        self.assertEqual(
            list(s.coords),
            [(1.0, 3.0), (1.0, 4.0), (2.0, 4.0), (2.0, 3.0), (1.0, 3.0)]
        )

    def test_polygon(self):
        a = np.array([[1.0, 1.0, 2.0, 2.0, 1.0], [3.0, 4.0, 4.0, 3.0, 3.0]])
        t = a.T
        s = geometry.Polygon(t)
        self.assertEqual(
            list(s.exterior.coords),
            [(1.0, 3.0), (1.0, 4.0), (2.0, 4.0), (2.0, 3.0), (1.0, 3.0)]
        )
