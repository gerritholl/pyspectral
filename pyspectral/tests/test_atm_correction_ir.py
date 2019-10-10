#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2017 - 2019 Pytroll

# Author(s):

#   Adam.Dybbroe <adam.dybbroe@smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Unit tests of the atmospherical correction in the ir spectral range."""


import numpy as np
from pyspectral.atm_correction_ir import AtmosphericalCorrection
import sys
if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

SATZ = np.ma.array([[48.03,  48.03002,  48.03004,  48.03006,  48.03008,  48.0301,
                     48.03012,  48.03014,  48.03016,  48.03018],
                    [48.09,  48.09002,  48.09004,  48.09006,  48.09008,  48.0901,
                     48.09012,  48.09014,  48.09016,  48.09018],
                    [48.15,  48.15002,  48.15004,  48.15006,  48.15008,  48.1501,
                     48.15012,  48.15014,  48.15016,  48.15018],
                    [48.21,  48.21002,  48.21004,  48.21006,  48.21008,  48.2101,
                     48.21012,  48.21014,  48.21016,  48.21018],
                    [48.27,  48.27002,  48.27004,  48.27006,  48.27008,  48.2701,
                     48.27012,  48.27014,  48.27016,  48.27018],
                    [48.33,  48.33002,  48.33004,  48.33006,  48.33008,  48.3301,
                     48.33012,  48.33014,  48.33016,  48.33018],
                    [48.39,  48.39002,  48.39004,  48.39006,  48.39008,  48.3901,
                     48.39012,  48.39014,  48.39016,  48.39018],
                    [48.45,  48.45002,  48.45004,  48.45006,  48.45008,  48.4501,
                     48.45012,  48.45014,  48.45016,  48.45018],
                    [48.51,  48.51002,  48.51004,  48.51006,  48.51008,  48.5101,
                     48.51012,  48.51014,  48.51016,  48.51018],
                    [48.57,  48.57002,  48.57004,  48.57006,  48.57008,  48.5701,
                     48.57012,  48.57014,  48.57016,  48.57018]], mask=False)

TBS = np.ma.array([[284.04,  284.04002667,  284.04005333,  284.04008,
                    284.04010667,  284.04013333,  284.04016,  284.04018667,
                    284.04021333,  284.04024],
                   [284.12,  284.12002667,  284.12005333,  284.12008,
                    284.12010667,  284.12013333,  284.12016,  284.12018667,
                    284.12021333,  284.12024],
                   [284.2,  284.20002667,  284.20005333,  284.20008,
                    284.20010667,  284.20013333,  284.20016,  284.20018667,
                    284.20021333,  284.20024],
                   [284.28,  284.28002667,  284.28005333,  284.28008,
                    284.28010667,  284.28013333,  284.28016,  284.28018667,
                    284.28021333,  284.28024],
                   [284.36,  284.36002667,  284.36005333,  284.36008,
                    284.36010667,  284.36013333,  284.36016,  284.36018667,
                    284.36021333,  284.36024],
                   [284.44,  284.44002667,  284.44005333,  284.44008,
                    284.44010667,  284.44013333,  284.44016,  284.44018667,
                    284.44021333,  284.44024],
                   [284.52,  284.52002667,  284.52005333,  284.52008,
                    284.52010667,  284.52013333,  284.52016,  284.52018667,
                    284.52021333,  284.52024],
                   [284.6,  284.60002667,  284.60005333,  284.60008,
                    284.60010667,  284.60013333,  284.60016,  284.60018667,
                    284.60021333,  284.60024],
                   [284.68,  284.68002667,  284.68005333,  284.68008,
                    284.68010667,  284.68013333,  284.68016,  284.68018667,
                    284.68021333,  284.68024],
                   [284.76,  284.76002667,  284.76005333,  284.76008,
                    284.76010667,  284.76013333,  284.76016,  284.76018667,
                    284.76021333,  284.76024]], mask=False)

RES = np.ma.array([[286.03159412,  286.03162417,  286.03165421,  286.03168426,
                    286.0317143,  286.03174434,  286.03177439,  286.03180443,
                    286.03183447,  286.03186452],
                   [286.12174723,  286.12177729,  286.12180735,  286.12183741,
                    286.12186747,  286.12189752,  286.12192758,  286.12195764,
                    286.1219877,  286.12201776],
                   [286.21194545,  286.21197552,  286.2120056,  286.21203567,
                    286.21206574,  286.21209582,  286.21212589,  286.21215597,
                    286.21218604,  286.21221611],
                   [286.30218896,  286.30221905,  286.30224913,  286.30227922,
                    286.30230931,  286.3023394,  286.30236949,  286.30239958,
                    286.30242967,  286.30245976],
                   [286.39247793,  286.39250803,  286.39253814,  286.39256824,
                    286.39259834,  286.39262845,  286.39265855,  286.39268866,
                    286.39271876,  286.39274886],
                   [286.48281254,  286.48284266,  286.48287278,  286.4829029,
                    286.48293302,  286.48296314,  286.48299325,  286.48302337,
                    286.48305349,  286.48308361],
                   [286.57319297,  286.5732231,  286.57325324,  286.57328337,
                    286.57331351,  286.57334364,  286.57337378,  286.57340391,
                    286.57343405,  286.57346418],
                   [286.6636194,  286.66364955,  286.6636797,  286.66370985,
                    286.66374,  286.66377015,  286.6638003,  286.66383045,
                    286.6638606,  286.66389075],
                   [286.754092,  286.75412216,  286.75415233,  286.75418249,
                    286.75421266,  286.75424283,  286.75427299,  286.75430316,
                    286.75433332,  286.75436349],
                   [286.84461096,  286.84464114,  286.84467132,  286.8447015,
                    286.84473168,  286.84476186,  286.84479204,  286.84482222,
                    286.8448524,  286.84488258]], mask=False)


class TestAtmCorrection(unittest.TestCase):
    """Class for testing pyspectral.atm_correction_ir."""

    def test_get_correction(self):
        """Test getting the atm correction."""
        this = AtmosphericalCorrection('EOS-Terra', 'modis')
        atm_corr = this.get_correction(SATZ, None, TBS)
        np.testing.assert_almost_equal(RES, atm_corr)


def suite():
    """Create the test suite for test_atm_correction_ir."""
    loader = unittest.TestLoader()
    mysuite = unittest.TestSuite()
    mysuite.addTest(loader.loadTestsFromTestCase(TestAtmCorrection))

    return mysuite
