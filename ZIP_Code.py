import requests

ask = str(input("Search using (i)ZIP Code or (ii)Post Office Name: "))
if ask.lower() == "zip code":
    input = str(input("Enter ZIP Code: "))
    pincode = "https://api.postalpincode.in/pincode/"
    Pin_URL = pincode + input.upper()
    r = requests.get(Pin_URL)
    data = r.json()
elif ask.lower() == "post office" or ask.lower() == "post office name":
    input = str(input("Enter Post Office Name: "))
    postoffice = "https://api.postalpincode.in/postoffice/"
    Post_URL = postoffice + input.upper()
    r = requests.get(Post_URL)
    data = r.json()

for i in data:
    if 'PostOffice' in i and i['PostOffice']:
        for post_office in i['PostOffice']:
            details = [
                "Post Office Information for " + input.upper() + ":",
                "Name: " + post_office.get('Name', 'N/A'),
                "Branch Type: " + post_office.get('BranchType', 'N/A'),
                "Delivery Status: " + post_office.get('DeliveryStatus', 'N/A'),
                "Circle: " + post_office.get('Circle', 'N/A'),
                "District: " + post_office.get('District', 'N/A'),
                "Division: " + post_office.get('Division', 'N/A'),
                "Region: " + post_office.get('Region', 'N/A'),
                "State: " + post_office.get('State', 'N/A'),
                "Country: " + post_office.get('Country', 'N/A'),
                "Pincode: " + post_office.get('Pincode', 'N/A')
            ]
            
            for item in details:
                print(item)
                print(" ")
