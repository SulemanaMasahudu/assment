#----------------------------------covid 19 estimator------------------------------------------
def estimator(data):
  
  output ={
        'data': {},  # the input data you got
        'impact': {}, # your best case estimation
        'severeImpact': {}  # your severe case estimation hello
  }
  #compute currentlyInfected
  impact_currentlyInfected = int(data['reportedCases'] * 10)
  severeimpact_currentlyInfected = int(data['reportedCases'] * 50)
  
  #Estimating infectionsByRequestedTime,
  impact_infectionsByRequestedTime = int(impact_currentlyInfected * 512)
  severeimpact_infectionsByRequestedTime = int(severeimpact_currentlyInfected * 512)
  
  #This is the estimated number of severe positive cases that will require hospitalization to recover.
  impact_severeCasesByRequestedTime = int(0.15 * impact_infectionsByRequestedTime)
  severeimpact_severeCasesByRequestedTime = int(0.15 * severeimpact_infectionsByRequestedTime)
  
  
  available_beds = int(0.35 * data['totalHospitalBeds'])
  impact_hospitalBedsByRequestedTime = int(available_beds - impact_severeCasesByRequestedTime )
  severeimpact_hospitalBedsByRequestedTime = int(available_beds -  severeimpact_severeCasesByRequestedTime)
  
  #This is the estimated number of severe positive cases that will require ICU care.
  impact_casesForICUByRequestedTime = int(0.05 * impact_infectionsByRequestedTime)
  severeimpact_casesForICUByRequestedTime = int(0.05 * severeimpact_infectionsByRequestedTime)
  
  #This is the estimated number of severe positive cases that will require ventilators.
  impact_casesForVentilatorsByRequestedTime = int(0.02 * impact_infectionsByRequestedTime)
  severeimpact_casesForVentilatorsByRequestedTime = int(0.02 * severeimpact_infectionsByRequestedTime)
  
  #Estimated Income loss!!! estimate how much money the economy is likely to lose over the said period.
  impact_dollarsInFlight= int((impact_infectionsByRequestedTime * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / 30)
  severeimpact_dollarsInFlight= int((severeimpact_infectionsByRequestedTime * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / 30)
  
  #updating output to have current data hello there 
  output['data'].update(data)
  output['impact'].update({'currentlyInfected': impact_currentlyInfected,
                           'infectionsByRequestedTime': impact_infectionsByRequestedTime,
                           'hospitalBedsByRequestedTime': impact_hospitalBedsByRequestedTime,
                           'casesForICUByRequestedTime': impact_casesForICUByRequestedTime,
                           'casesForVentilatorsByRequestedTime': impact_casesForVentilatorsByRequestedTime,
                           'dollarsInFlight': impact_dollarsInFlight})
  
  output['severeImpact'].update({'currentlyInfected': severeimpact_currentlyInfected,
                           'infectionsByRequestedTime': severeimpact_infectionsByRequestedTime,
                           'hospitalBedsByRequestedTime': severeimpact_hospitalBedsByRequestedTime,
                           'casesForICUByRequestedTime': severeimpact_casesForICUByRequestedTime,
                           'casesForVentilatorsByRequestedTime': severeimpact_casesForVentilatorsByRequestedTime,
                           'dollarsInFlight': severeimpact_dollarsInFlight})
  return output

