import unittest

from vehicle_info_after import VehicleInfo


class TestVehicleInfoMethods(unittest.TestCase):

    # pass

    def test_compute_tax_non_electric(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(), 500)

    def test_compute_tax_electric(self):
        v = VehicleInfo("BMW", True, 10000)
        self.assertEqual(v.compute_tax(), 200)

    def test_compute_tax_exemption(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(5000), 250)

    def test_compute_tax_exemption_negative(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertRaises(
            ValueError, v.compute_tax, -5000
        )  # fn call raises error - type of error is valueerror.-5000 -> parameter to fn

    # tax exemption higher than tax - return 0
    def test_compute_tax_exemption_high(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.compute_tax(20000), 0)

    # you can only lease this car if the catalogue price is not more than 70% of
    # your year income
    def test_can_lease_false(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.can_lease(5000), False)

    def test_can_lease_true(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertEqual(v.can_lease(15000), True)

    # year_income should be >= 0
    def test_can_lease_negative_income(self):
        v = VehicleInfo("BMW", False, 10000)
        self.assertRaises(ValueError, v.can_lease, -5000)


# run the actual unittests
unittest.main()
