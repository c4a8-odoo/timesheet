from odoo.addons.sale_timesheet.tests.test_project_profitability import (
    TestSaleTimesheetProjectProfitability,
)


class TestSaleTimesheetProjectProfitabilityLineExclude(
    TestSaleTimesheetProjectProfitability
):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
