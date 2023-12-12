import json
from datetime import datetime, timedelta

class Merchant:
    def __init__(self, merchant_data):
        self.id = merchant_data['id']
        self.name = merchant_data['name']
        self.distance = merchant_data['distance']

    def __str__(self):
        return f"Merchant {self.id}: {self.name}, Distance: {self.distance}"

class Offer:
    def __init__(self, offer_data):
        self.id = offer_data['id']
        self.title = offer_data['title']
        self.description = offer_data['description']
        self.category = offer_data['category']
        self.valid_to = offer_data['valid_to']
        self.merchants = [Merchant(merchant_data).__dict__ for merchant_data in offer_data['merchants']]

    def __str__(self):
        return f"Offer {self.id}: {self.title}, Category: {self.category}, Valid until: {self.valid_to} "

    def is_valid(self, checkin_date):
        return datetime.strptime(self.valid_to, "%Y-%m-%d") > checkin_date + timedelta(days=5)

class OfferFilter:
    def __init__(self, checkin_date):
        self.checkin_date = datetime.strptime(checkin_date, "%Y-%m-%d")

    def load_data(self, input_file):
        with open(input_file, "r") as file:
            data = json.load(file)
            self.offers = [Offer(offer_data) for offer_data in data['offers']]
    
    # Returns list of offers that have valid check-in date and category
    def filter_offers(self):
        filtered_offers = []
        for offer in self.offers:
            #check valid chẹck-in date anh category
            if offer.is_valid(self.checkin_date) and offer.category in {1, 2, 4}:
                filtered_offers.append(offer)
        return filtered_offers

    #Param is list of offer that valid category and check-in date
    #Returns list of offers that have only 1 merchant closest and sort list offers by the distance of the merchant
    def select_closest_merchant(self, offers):
        closest_merchant_offers = []
        #get list of offers that have only 1 merchant closest
        for offer in offers:
            closest_merchant =  offer.merchants[0]
            for merchant in  offer.merchants:
                if closest_merchant["distance"] > merchant["distance"]:
                    closest_merchant = merchant
            offer.merchants = [closest_merchant]
            closest_merchant_offers.append(offer)
        #sort list offers by the distance of the merchant
        closest_merchant_offers.sort(key=lambda x: x.merchants[0]["distance"])
        return closest_merchant_offers
    
    #Param is list of sorted offer by distance
    #Returns 2 final offers that have different catgory and have closest distance
    def select_final_offers(self,offers):
        #Get first final offer
        final_offer=[offers[0]]
        for offer in offers:
            #check if offer.category is final_offer.category and skip
            if offer.category == final_offer[0].category:
                continue
            #if not get second final offer and return
            else:
                final_offer.append(offer)
                break
        return final_offer
    #write to output file
    def save_to_file(self, output_file, filtered_offers):
        with open(output_file, "w") as file:
            json.dump({'offers':[offer.__dict__ for offer in filtered_offers]}, file, indent=2)
def main():
    import sys

    if len(sys.argv) != 3:
        print("Usage: python filter_offers.py <checkin_date> <input_file>")
        sys.exit(1)

    checkin_date = sys.argv[1]
    input_file = sys.argv[2]
    output_file = "output.json"

    offer_filter = OfferFilter(checkin_date)
    offer_filter.load_data(input_file)

    try:
        # Get list of offers that have valid check-in date and category
        filtered_offers = offer_filter.filter_offers()
        # Get list of offers that have only 1 merchant closest and sort list offers by the distance of the merchant
        closest_merchant = offer_filter.select_closest_merchant(filtered_offers)
        # Get 2 final offers that have different catgory and have closest distance
        final_offers = offer_filter.select_final_offers(closest_merchant)
        # Write to output file
        offer_filter.save_to_file(output_file, final_offers)
        print(f"Filtered offers saved to {output_file}")
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()
