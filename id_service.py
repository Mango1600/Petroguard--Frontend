class IDService:

    def __init__(self):
        self.company = "ABC"
        self.station = "IBD"

    def generate(self, prefix, number, digits=6):
        return f"{prefix}-{number:0{digits}d}"

    def company(self, number):
        return self.generate("CMP", number)

    def station(self, number):
        return f"STN-{self.company_code}-{number:03d}"

    def staff(self, number):
        return f"PG-{self.company}-{self.station}-{number:06d}"

    def pump(self, number):
        return f"PMP-{self.company}-{self.station}-{number:03d}"

    def tank(self, number):
        return f"TNK-{self.company}-{self.station}-{number:03d}"


if __name__ == "__main__":
    ids = IDService()

    print(ids.staff(1))
    print(ids.pump(1))
    print(ids.tank(1))
