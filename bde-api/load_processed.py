#like either webscraping or downloading existing datasets
import pickle

class DataWrapper:
    def __init__(self):
        #constructor
        data_path = "../../data/"
        self.categories = self.load_data(data_path + "processed/categories.pkl")
        self.in_california = self.load_data(data_path + "processed/california_businesses.pkl")
        self.cali_business_time = self.load_data(data_path + "processed/business_times.pkl")

        # print(len(self.categories))
        #now build quad tree
        #on query, look through each location, and if match, add to list, with corresponding checkins. return list.

    #Thu-19
    def query(self, lat_low, lat_high, long_low, long_high, categories, time):
        assert lat_low <= lat_high and long_low <= long_high

        valid_categories = self.validate_categories(categories)
        if len(valid_categories) == 0:
            return "No valid categories!"

        businesses = self.businesses_in_bounds(lat_low, lat_high, long_low, long_high)
        print(len(businesses))
        return_list = []
        for business in businesses:
            # print(business)
            # break
            same_categories = business['categories'].intersection(valid_categories)
            if len(same_categories) == 0:
                continue

            if business['business_id'] in self.cali_business_time and time in self.cali_business_time[business['business_id']]:
                return_list.append(self.smaller_package(business, self.cali_business_time[business['business_id']][time]))
        return return_list

    def smaller_package(self, business_dict, frequency):
        return_dict = {}
        for key in ['name', 'address', 'city', 'state', 'latitude', 'longitude', 'hours', 'business_id']:
            return_dict[key] = business_dict.get(key, "")
        return_dict['categories'] = list(business_dict.get('categories', ''))
        return_dict['frequency'] = frequency    
        return return_dict

    def businesses_in_bounds(self, lat_low, lat_high, long_low, long_high):
        return [business for business in self.in_california if self.in_bounds(business['latitude'], business['longitude'], lat_low, lat_high, long_low, long_high)]

    def in_bounds(self, lat, longt, lat_low, lat_high, long_low, long_high):
        # print(lat, longt, lat_low, lat_high, long_low, long_high)
        #naive: loop through all and filter. fix!
        # print(lat, longt)
        if lat < lat_low or lat > lat_high:
            # print("lat bad")
            return False
        if longt < long_low or longt > long_high:
            # print("long bad")
            return False
        return True

    def validate_categories(self, categories):
        return set([category for category in categories if category in self.categories])

    def load_data(self, path, use_pickle = True):
        if use_pickle:
            return pickle.load( open( path, "rb" ) )
        #load data
        data = open(path, 'r', encoding='utf-8').read()
        return eval(data)

    def test_print(self, number):
        for i in range(number):
            business = self.in_california[i]
            print(business['latitude'], ",", business['longitude'])

if __name__ == '__main__':
    l = DataWrapper()
    # l.test_print(len(l.in_california))
    # 36.411223, -115.491963
    # 35.928757, -114.832228
    q = l.query(35.928757, 36.411223, -115.491963, -114.832228, ['bubble tea'], "Fri-13")
    # print(len(q))
    # print(q)