# No user input; data for individual provided.
MIN_YEARS_EXPERIENCE_OVERSEAS = 6
MIN_YEARS_EXPERIENCE_IN_US = 2

years_oconus = int(input('Enter years of overseas work: '))
years_garrison = int(input('Enter of years of service in the US: '))

if years_oconus >= MIN_YEARS_EXPERIENCE_OVERSEAS and years_garrison > MIN_YEARS_EXPERIENCE_IN_US:
    print('Congradualtions! You are eligible for a selecting a new assingment.')
else:
# Multi-line with f-string
    print(f'''
Sorry, you do not meet the requirements for the Sales Manager Position.
          
          You need at least:
          - {MIN_YEARS_EXPERIENCE_OVERSEAS} years of overseas experience
          - {MIN_YEARS_EXPERIENCE_IN_US} years of in country experience 
          ''')
    
    