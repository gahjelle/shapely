from . import unittest
from shapely.geometry import LineString, LinearRing
from shapely.testing import assert_geometries_equal
from shapely.wkt import loads

class OperationsTestCase(unittest.TestCase):

    def test_parallel_offset_linestring(self):
        line1 = LineString([(0, 0), (10, 0)])
        left = line1.parallel_offset(5, 'left')
        assert_geometries_equal(left, LineString([(0, 5), (10, 5)]))
        right = line1.parallel_offset(5, 'right')
        assert_geometries_equal(right, LineString([(10, -5), (0, -5)]), normalize=True)
        right = line1.parallel_offset(-5, 'left')
        assert_geometries_equal(right, LineString([(10, -5), (0, -5)]), normalize=True)
        left = line1.parallel_offset(-5, 'right')
        assert_geometries_equal(left, LineString([(0, 5), (10, 5)]))

        # by default, parallel_offset is right-handed
        assert_geometries_equal(line1.parallel_offset(5), right)

        line2 = LineString([(0, 0), (5, 0), (5, -5)])
        assert_geometries_equal(line2.parallel_offset(2, 'left', resolution=1),
                                LineString([(0, 2), (5, 2), (7, 0), (7, -5)]))
        assert_geometries_equal(line2.parallel_offset(2, 'left', join_style=2,
                                                      resolution=1),
                                LineString([(0, 2), (7, 2), (7, -5)]))
        # offset_curve alias
        assert_geometries_equal(
            line1.offset_curve(2, 'left', resolution=1),
            line1.parallel_offset(2, 'left', resolution=1)
        )

    def test_parallel_offset_linear_ring(self):
        lr1 = LinearRing([(0, 0), (5, 0), (5, 5), (0, 5), (0, 0)])
        assert_geometries_equal(lr1.parallel_offset(2, 'left', resolution=1),
                                LineString([(2, 2), (3, 2), (3, 3), (2, 3), (2, 2)]))
        # offset_curve alias
        assert_geometries_equal(
            lr1.offset_curve(2, 'left', resolution=1),
            lr1.parallel_offset(2, 'left', resolution=1)
        )
