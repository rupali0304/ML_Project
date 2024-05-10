import os


FLIGHT_FARE_MODEL_FILE = os.path.join('My_project_ML','lr_model.pkl')


airline = {"air_india" : 0,
        "goair" : 0,
        "indigo" : 0,
        "multiple_carriers" : 0,
        "multiple_carriers_premium_economy" : 0,
        "spicejet" : 0,
        "trujet": 0,
        "vistara": 0,
        "vistara_premium_economy":0}

source = {"s_chennai" : 0,
"s_delhi" :  0,
"s_kolkata" : 0,
"s_mumbai" :0}

destination ={"d_cochin" : 0,
"d_delhi" : 0,
"d_hyderabad" : 0,
"d_kolkata" : 0,
"d_new_delhi":0}

booking_company = {"IRCTC": 0, "Goibibo": 1, "Makemytrip": 2}

membership_discount = {"gold":10,"platinum":15,"silver":5}