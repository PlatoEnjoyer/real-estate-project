import cianparser

data = cianparser.parse(
    deal_type="sale",
    accommodation_type="flat",
    location="Москва",
    start_page=1,
    end_page=1,
    is_express_mode=True,
)

for d in data:
    print(d)
