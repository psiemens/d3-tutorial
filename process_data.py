import csv

with open('stores.csv', 'U') as csvfile:
    storereader = csv.reader(csvfile)
    storereader.next() # skip header row
    stores = [store[0] for store in storereader]

sales_data = {}
features_data = {}

with open('train.csv', 'U') as csvfile:
    trainreader = csv.reader(csvfile)
    trainreader.next() # skip header row

    for row in trainreader:
        store = row[0]
        week = row[2]
        sales = float(row[3])

        if store not in sales_data:
            sales_data[store] = {}

        if week not in sales_data[store]:
            sales_data[store][week] = 0.0

        sales_data[store][week] += sales

with open('features.csv', 'U') as csvfile:
    featuresreader = csv.reader(csvfile)
    featuresreader.next() # skip header row

    for row in featuresreader:
        store = row[0]
        week = row[1]
        temperature = float(row[2])
        fuel_price = float(row[3])

        if store not in features_data:
            features_data[store] = {}

        features_data[store][week] = {
            'temperature': temperature,
            'fuel_price': fuel_price
        }

for store in stores:
    sales = sales_data[store]
    features = features_data[store]

    with open('stores/%s.csv' % store, 'wb') as csvfile:
        fieldnames = ['week', 'sales', 'fuel_price', 'temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for week in sales:

            data = features[week].copy()
            data['week'] = week
            data['sales'] = sales[week]

            writer.writerow(data)
