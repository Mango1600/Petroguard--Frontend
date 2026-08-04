from datetime import datetime

class EnterpriseIDGenerator:

    def __init__(self):
        self.company = "ABC"
        self.station = "IBD"

    def staff_id(self, number):
        return f"PG-{self.company}-{self.station}-{number:06d}"

    def station_id(self, number):
        return f"STN-{self.company}-{number:03d}"

    def company_id(self, number):
        return f"CMP-{number:06d}"

    def sale_id(self, number):
        return f"SAL-{datetime.now():%Y%m%d}-{number:06d}"

    def delivery_id(self, number):
        return f"DLV-{datetime.now():%Y%m%d}-{number:04d}"

    def business_day_id(self, number):
        return f"BD-{datetime.now():%Y%m%d}-{number:03d}"


if __name__ == "__main__":
    gen = EnterpriseIDGenerator()

    print("Company :", gen.company_id(1))
    print("Station :", gen.station_id(1))
    print("Staff   :", gen.staff_id(1))
    print("Sale    :", gen.sale_id(1))
    print("Delivery:", gen.delivery_id(1))
    print("Business:", gen.business_day_id(1))
