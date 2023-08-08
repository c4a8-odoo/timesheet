from odoo.addons.sale_timesheet.tests.test_reinvoice import TestReInvoice


class TestReInvoiceLineExclude(TestReInvoice):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
