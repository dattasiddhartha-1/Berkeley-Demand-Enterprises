#probably called by collect data to process data on the go (when being downloaded)

import json
import pickle



class ProcessData:
    def __init__(self):
        data_path = "../../data/"
        #constructor

        #hardcoded
        # self.latTop = 37.890390
        # self.latLow = 37.844567
        # self.longTop = -122.220956
        # self.longBot = -122.302470   
        self.latTop = 41.981271
        self.latLow = 32.640031
        self.longTop = -113.691906
        self.longBot = -125.603718
         
        self.in_california = []
        self.cali_businesses = set()
        self.cali_business_time = {}
        self.categories = set()
        self.process_business_data(data_path + 'orig/yelp_academic_dataset_business.json')
        self.process_checkin_data(data_path + 'orig/yelp_academic_dataset_checkin.json')

        self.output(self.categories, data_path + "processed/categories.pkl")
        self.output(self.in_california, data_path + "processed/california_businesses.pkl")
        self.output(self.cali_business_time, data_path + "processed/business_times.pkl")

        print(len(self.categories))

    def in_bounds(self, lat, longt):
        # print(lat, longt)
        if lat < self.latLow or lat > self.latTop:
            return False
        if longt < self.longBot or longt > self.longTop:
            return False
        return True

    def process_business_data(self, location):
        count = 0
        with open(location, 'r', encoding='utf-8') as f:
            # print(type(f))

            for line in f:
                curr_business = json.loads(line)
                lat = curr_business['latitude']
                longt = curr_business['longitude']

                if lat is None or longt is None:
                    print('passing!')
                    continue
                if self.in_bounds(lat, longt) and curr_business["categories"] is not None: #
                    # print(curr_business["categories"], type(curr_business["categories"]))
                    business_categories = set()

                    for cat in curr_business["categories"].split(","):
                        business_categories.add(cat.strip().lower())
                        self.categories.add(cat.strip().lower())
                    curr_business["categories"] = business_categories
                    self.in_california.append(curr_business)
                    self.cali_businesses.add(curr_business["business_id"])
                    # return

                    # if curr_business['hours'] is not None:
                    # print(curr_business)
                    # return

                count += 1
                if count % 1e4 == 0:
                    print(count)
                # print(curr_business)
                # print(curr_business['categories'])
                # print(lat, longt)
            # self.data = json.load(f, encoding='utf-8')
            # print(type(self.data))
        print(self.in_california[1])
        # print(self.categories)
        print(len(self.in_california))
        print(count)

    def process_checkin_data(self, location):
        count = 0
        with open(location, 'r', encoding='utf-8') as f:
            for line in f:
                checkins = json.loads(line)
                if checkins['business_id'] in self.cali_businesses:
                    self.cali_business_time[checkins['business_id']] = checkins['time']
        print(len(self.cali_business_time))

    def output(self, obj, path, use_pickle = True):
        if use_pickle:
            out_file = open(path,"wb")
            pickle.dump(obj, out_file)
            out_file.close()
            return

        out_file = open(path, "w", encoding='utf-8')
        out_file.write( repr(obj) )
        out_file.close()

if __name__ == '__main__':
    p = ProcessData()
