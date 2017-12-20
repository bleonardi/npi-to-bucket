import pandas as pd
import requests

num = input("Enter the physician's NPI: ")

resp = requests.get("https://npiregistry.cms.hhs.gov/api/?number="+num+"&enumeration_type=&taxonomy_description=&first_name=&last_name=&organization_name=&address_purpose=&city=&state=&postal_code=&country_code=&limit=&skip")
type(resp.json())
resp.json()['results']

data = pd.io.json.json_normalize(resp.json()['results'], 'taxonomies')

anesth = ["207L00000X","207LA0401X","207LC0200X","207LH0002X","207LP2900X","207LP3000X"]
radiol = ["2085B0100X","2085D0003X","2085H0002X","2085N0700X","2085N0904X","2085P0229X","2085R0001X","2085R0202X","2085R0203X","2085R0204X","2085R0205X","2085U0001X"]
genprac = ["208D00000X"]

code = data['code'].to_string(index = False)
if code in anesth:
    print("Anesthesiologist")
elif code in radiol:
    print("Radiologist")
elif code in genprac:
    print("General practitioner")
else:
    print("Not bucketed")