import config
import pickle
from flask import Flask,request, jsonify

app = Flask(__name__)


@app.route('/predict-flight-fare',methods=['POST'])
def predict_flight_fare():
    flight_data = request.json
    fare = flight_fare_model(data =flight_data)
    print(fare)

    return jsonify(fare)

def flight_fare_model(data):
    from datetime import datetime
    Total_stops = data['Number_Of_Stops']
    journey_date = data['Journey_Date']
    Journey_day = int(datetime.strptime(journey_date,"%d-%b-%Y").date().day)
    Journey_month = int(datetime.strptime(journey_date,"%d-%b-%Y").date().month)
    departure_time = data['Dept_Time']
    Dep_hour = int(departure_time.split(':')[0])
    print(Dep_hour)
    Dep_min = int(departure_time.split(':')[1])
    arrival_time = data['Arrival_Time']
    Arrival_hour = int(arrival_time.split(':')[0])
    Arrival_min = int(arrival_time.split(':')[1])
    dur_min = int((datetime.strptime(arrival_time, '%H:%M') - datetime.strptime(departure_time, '%H:%M')).total_seconds()/60)
    print(dur_min)
    airline = data['Airline_Name']
    config.airline[airline.lower()] = 1
    Air_India = config.airline['Air_India'.lower()]
    GoAir = config.airline['GoAir'.lower()]
    IndiGo = config.airline['IndiGo'.lower()]
    Multiple_carriers = config.airline['Multiple_carriers'.lower()]
    Multiple_carriers_Premium_economy = config.airline['Multiple_carriers_Premium_economy'.lower()]
    SpiceJet = config.airline['SpiceJet'.lower()]
    Trujet = config.airline['Trujet'.lower()]
    Vistara = config.airline['Vistara'.lower()]
    Vistara_Premium_economy = config.airline['Vistara_Premium_economy'.lower()]
    print(Air_India)
    print(IndiGo)
    print(GoAir)
    print(SpiceJet)
    print(Vistara)
    print(Vistara_Premium_economy)
    source = data['Source']
    config.source['s_'+ source.lower()] = 1
    s_Chennai = config.source['s_Chennai'.lower()]
    s_Delhi = config.source['s_Delhi'.lower()]
    s_Kolkata = config.source['s_Kolkata'.lower()]
    s_Mumbai = config.source['s_Mumbai'.lower()]
    print(s_Chennai)
    print(s_Delhi)
    print(s_Kolkata)
    print(s_Mumbai)
    destination = data['Destination']
    config.destination['d_'+destination.lower()] = 1

    d_Cochin = config.destination['d_Cochin'.lower()]
    d_Delhi = config.destination['d_Delhi'.lower()]
    d_Hyderabad = config.destination['d_Hyderabad'.lower()]
    d_Kolkata = config.destination['d_Kolkata'.lower()]
    d_New_Delhi = config.destination['d_New_Delhi'.lower()]
    print(d_Cochin)
    print(d_Delhi)
    print(d_Hyderabad)
    print(d_Kolkata)
    print(d_New_Delhi)

    with open(config.FLIGHT_FARE_MODEL_FILE,'rb') as pkl:
        flight_fare_model = pickle.load(pkl)
    new_fare = {}
    for i,j in config.booking_company.items():
        print(i)
        print(j)
        predicted_fare = flight_fare_model.predict(([
            [
                dur_min,
                Total_stops,
                j,
                Dep_hour,
                Dep_min,
                Arrival_hour,
                Arrival_min,
                Journey_day,
                Journey_month,
                Air_India,GoAir,
                IndiGo,
                Multiple_carriers,
                Multiple_carriers_Premium_economy,
                SpiceJet,
                Trujet,
                Vistara,
                Vistara_Premium_economy,
                s_Chennai,
                s_Delhi,
                s_Kolkata,
                s_Mumbai,
                d_Cochin,
                d_Delhi,
                d_Hyderabad,
                d_Kolkata,
                d_New_Delhi
            ]]))
        print(predicted_fare)
        new_fare[i] = round(predicted_fare[0])
    print(new_fare)
    discount = config.membership_discount[data['Membership_status'].lower()]
    new_fare['Best_offered_price'] = round(min(new_fare.values()) - min(new_fare.values())*(discount/100))
    
    return new_fare

if __name__== '__main__' :
    app.run(host="0.0.0.0",port=8080)