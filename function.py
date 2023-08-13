# Fungsi untuk mengganti nama kota menjadi tier
def map_to_tier(city):
    if city in ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune']:
        return 'Tier 1'
    elif city in ['Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Anand', 'Asansol', 'Aurangabad', 'Bareilly', 'Belagavi',
          'Brahmapur', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur','Bokaro',
          'Burdwan' , 'Chandigarh', 'Coimbatore', 'Cuttack', 'Dahod', 'Dehradun', 'Dombivli', 'Dhanbad', 'Bhilai',
          'Durgapur', 'Erode', 'Faridabad', 'Ghaziabad', 'Gorakhpur', 'Guntur', 'Gurgaon', 'Guwahati', 'Gwalior', 'Hamirpur',
          'Hubballi-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jalgaon', 'Jammu','Jamshedpur', 'Jhansi', 'Jodhpur',
          'Kalaburagi', 'Kakinada', 'Kannur', 'Kanpur', 'Karnal', 'Kochi', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana',
          'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Mangaluru', 'Meerut', 'Moradabad', 'Mysuru', 'Nagpur', 'Nanded', 'Nadiad',
          'Nashik', 'Nellore', 'Noida', 'Patna', 'Puducherry', 'Purulia', 'Prayagraj', 'Raipur', 'Rajkot', 'Rajamahendravaram',
          'Ranchi', 'Rourkela', 'Ratlam', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Surat', 'Thanjavur',
          'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tirunelveli', 'Tiruvannamalai', 'Ujjain', 'Vijayapura',
          'Vadodara', 'Varanasi', 'Vasai-Virar', 'Vijayawada', 'Visakhapatnam', 'Vellore','Warangal']:
        return 'Tier 2'
    else:
        return 'Tier 3'


# Fungsi untuk menggolongkan negara bagian berdasarkan wilayah
def classify_region(state):
    if state in ['Haryana', 'Himachal_Pradesh', 'Jharkhand', 'Punjab', 'Uttar_Pradesh','Uttar_Pradesh[5]', 'Uttarakhand','Jammu_and_Kashmir','Delhi','Chandigarh']:
        return 'North'
    elif state in ['Andhra_Pradesh', 'Karnataka', 'Kerala', 'Tamil_Nadu', 'Telangana']:
        return 'South'
    elif state in ['Goa', 'Gujarat', 'Maharashtra', 'Rajasthan','Madhya_Pradesh']:
        return 'West'
    elif state in ['Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Sikkim', 'Tripura', 'West_Bengal','Puducherry']:
        return 'East'
    else:
        return 'East'