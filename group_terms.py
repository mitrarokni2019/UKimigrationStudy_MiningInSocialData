#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Define UK-relevant countries and terms
countries = {
    # South Asia
    'India': ['India', 'British India', 'East India'],
    'Pakistan': ['Pakistan', 'West Pakistan', 'East Pakistan'],
    'Bangladesh': ['Bangladesh', 'East Bengal'],
    'Sri Lanka': ['Sri Lanka', 'Ceylon'],
    'Nepal': ['Nepal'],
    'Afghanistan': ['Afghanistan'],

    # Middle East
    'Syria': ['Syria'],
    'Iraq': ['Iraq'],
    'Iran': ['Iran'],
    'Israel': ['Israel'],
    'Palestine': ['Palestine', 'Palestinian'],
    'Jordan': ['Jordan'],
    'Lebanon': ['Lebanon'],

    # Caribbean
    'Jamaica': ['Jamaica', 'West Indies'],
    'Trinidad': ['Trinidad', 'Tobago', 'Trinidad and Tobago'],
    'Barbados': ['Barbados', 'Barbadian'],
    'Cuba': ['Cuba'],

    # Eastern Europe
    'Poland': ['Poland'],
    'Romania': ['Romania', 'Rumania'],
    'Bulgaria': ['Bulgaria'],
    'Hungary': ['Hungary'],
    'Lithuania': ['Lithuania'],
    'Latvia': ['Latvia'],
    'Estonia': ['Estonia'],
    'Croatia': ['Croatia'],

    # Western Europe
    'France': ['France'],
    'Germany': ['Germany'],
    'Italy': ['Italy'],
    'Ireland': ['Ireland'],
    'Greece': ['Greece'],
    'Spain': ['Spain'],
    'Portugal': ['Portugal'],

    # Africa
    'Nigeria': ['Nigeria'],
    'Ghana': ['Ghana'],
    'Somalia': ['Somalia'],
    'Ethiopia': ['Ethiopia'],
    'Kenya': ['Kenya'],
    'Uganda': ['Uganda'],
    'South Africa': ['South Africa'],

    # East Asia
    'China': ['China', 'Hong Kong'],
    'Vietnam': ['Vietnam'],
    'Philippines': ['Philippines', 'Filipino'],
    'Japan': ['Japan'],
    'South Korea': ['South Korea', 'Korea'],

    # Latin America
    'Mexico': ['Mexico'],
    'Brazil': ['Brazil'],
    'Colombia': ['Colombia'],
    'Venezuela': ['Venezuela'],

    # Commonwealth
    'Australia': ['Australia'],
    'Canada': ['Canada'],
    'New Zealand': ['New Zealand'],
    'Malta': ['Malta'],
    'Cyprus': ['Cyprus'],

    # Other Regions
    'Russia': ['Russia', 'USSR', 'Soviet Union'],
    'Ukraine': ['Ukraine'],
    'Belarus': ['Belarus'],
    'Turkey': ['Turkey'],
    'Myanmar': ['Myanmar', 'Burma']
}


# Define nationalities and ethnic terms
nationalities = {
    # South Asia
    'India': ['Indian', 'Indians', 'British Indian', 'Anglo-Indian'],
    'Pakistan': ['Pakistani', 'Pakistanis'],
    'Bangladesh': ['Bangladeshi', 'Bangladeshis'],
    'Sri Lanka': ['Sri Lankan', 'Sri Lankans', 'Ceylonese'],
    'Nepal': ['Nepali', 'Nepalese'],
    'Afghanistan': ['Afghan', 'Afghans'],

    # Middle East
    'Syria': ['Syrian', 'Syrians'],
    'Iraq': ['Iraqi', 'Iraqis'],
    'Iran': ['Iranian', 'Iranians'],
    'Israel': ['Israeli', 'Israelis'],
    'Palestine': ['Palestinian', 'Palestinians'],
    'Jordan': ['Jordanian', 'Jordanians'],
    'Lebanon': ['Lebanese'],

    # Caribbean
    'Jamaica': ['Jamaican', 'Jamaicans'],
    'Trinidad': ['Trinidadian', 'Tobagonian'],
    'Barbados': ['Barbadian', 'Barbadians', 'Bajan'],
    'Cuba': ['Cuban', 'Cubans'],

    # Eastern Europe
    'Poland': ['Polish', 'Poles'],
    'Romania': ['Romanian', 'Romanians'],
    'Bulgaria': ['Bulgarian', 'Bulgarians'],
    'Hungary': ['Hungarian', 'Hungarians'],
    'Lithuania': ['Lithuanian', 'Lithuanians'],
    'Latvia': ['Latvian', 'Latvians'],
    'Estonia': ['Estonian', 'Estonians'],
    'Croatia': ['Croatian', 'Croatians'],

    # Western Europe
    'France': ['French'],
    'Germany': ['German', 'Germans'],
    'Italy': ['Italian', 'Italians'],
    'Ireland': ['Irish', 'Irishman', 'Irishmen'],
    'Greece': ['Greek', 'Greeks'],
    'Spain': ['Spanish', 'Spaniard', 'Spaniards'],
    'Portugal': ['Portuguese'],

    # Africa
    'Nigeria': ['Nigerian', 'Nigerians'],
    'Ghana': ['Ghanaian', 'Ghanaians'],
    'Somalia': ['Somali', 'Somalis'],
    'Ethiopia': ['Ethiopian', 'Ethiopians'],
    'Kenya': ['Kenyan', 'Kenyans'],
    'Uganda': ['Ugandan', 'Ugandans'],

    # East Asia
    'China': ['Chinese'],
    'Vietnam': ['Vietnamese'],
    'Philippines': ['Filipino', 'Filipinos'],
    'Japan': ['Japanese'],
    'South Korea': ['Korean', 'Koreans'],

    # Latin America
    'Mexico': ['Mexican', 'Mexicans'],
    'Brazil': ['Brazilian', 'Brazilians'],
    'Colombia': ['Colombian', 'Colombians'],
    'Venezuela': ['Venezuelan', 'Venezuelans'],

    # Commonwealth
    'Australia': ['Australian', 'Australians'],
    'Canada': ['Canadian', 'Canadians'],
    'New Zealand': ['New Zealander', 'New Zealanders'],
    'Malta': ['Maltese'],
    'Cyprus': ['Cypriot', 'Cypriots'],

    # Other Regions
    'Russia': ['Russian', 'Russians'],
    'Ukraine': ['Ukrainian', 'Ukrainians'],
    'Belarus': ['Belarusian', 'Belarusians'],
    'Turkey': ['Turkish', 'Turks'],
    'Myanmar': ['Burmese']
}

# Define broader regions
# Updated broader regions
regions = {
    'South_Asia': ['India', 'Pakistan', 'Bangladesh', 'Sri Lanka', 'Nepal', 'Afghanistan'],
    'Middle_East': ['Syria', 'Iraq', 'Iran', 'Israel', 'Palestine', 'Jordan', 'Lebanon'],
    'Caribbean': ['Jamaica', 'Trinidad', 'Barbados', 'Cuba', 'West Indies'],
    'Eastern_Europe': ['Poland', 'Romania', 'Bulgaria', 'Hungary', 'Lithuania', 'Latvia', 'Estonia', 'Croatia'],
    'Western_Europe': ['France', 'Germany', 'Italy', 'Ireland', 'Greece', 'Spain', 'Portugal'],
    'East_Africa': ['Uganda', 'Kenya', 'Ethiopia', 'Somalia', 'Nigeria', 'Ghana'],
    'East_Asia': ['China', 'Hong Kong', 'Vietnam', 'Japan', 'South Korea', 'Philippines'],
    'Latin_America': ['Mexico', 'Brazil', 'Colombia', 'Venezuela'],
    'Commonwealth': ['Australia', 'Canada', 'New Zealand', 'South Africa', 'Cyprus', 'Malta'],
    'Other_Regions': ['Russia', 'Ukraine', 'Belarus', 'Turkey', 'Myanmar']
}

# Define regional/ethnic groupings
# Updated regional/ethnic groupings
regionalities = {
    'South_Asia': ['Asian', 'Asians', 'South Asian', 'South Asians', 'British Asian', 'British Asians'],
    'Middle_East': ['Middle Eastern', 'Middle Easterners', 'Arab', 'Arabs', 'Palestinian', 'Syrian', 'Lebanese'],
    'Caribbean': ['Caribbean', 'West Indian', 'West Indians', 'Afro-Caribbean', 'Windrush'],
    'Eastern_Europe': ['Eastern European', 'Eastern Europeans', 'EU migrant', 'EU migrants'],
    'Western_Europe': ['Western European', 'Western Europeans', 'EU national', 'EU nationals'],
    'East_Africa': ['East African Asian', 'East African Asians', 'African Asian', 'African Asians'],
    'East_Asia': ['East Asian', 'East Asians', 'Oriental', 'Orientals'],
    'Latin_America': ['Latin American', 'Hispanic', 'Latino', 'Latina'],
    'Commonwealth': ['Commonwealth', 'Commonwealth citizen', 'Commonwealth national', 'British Commonwealth']
}

# Define regional/ethnic groupings
# Updated additional terms for historical periods
historical_terms = {
    'Windrush': ['Windrush', 'Empire Windrush', 'SS Empire Windrush', 'West Indian', 'Caribbean'],
    'EU_Migration': ['EU', 'European Union', 'EU national', 'EU nationals', 'EU migrant', 'EU migrants',
                     'freedom of movement', 'A8', 'accession', 'EU citizen', 'EU citizens'],
    'Hostile_Environment': ['hostile environment', 'compliant environment', 'right to rent', 'immigration check'],
    'Post_Brexit': ['post-Brexit', 'Brexit', 'points-based system', 'skilled worker visa', 'settled status', 'pre-settled status']
}



# Helper Functions
def get_countries():
    return countries

def get_nationalities():
    return nationalities

def get_regions_and_regionalities():
    return regions, regionalities

def get_historical_terms():
    return historical_terms

# Function to return country and nationality terms
def get_group_terms():
    return countries, nationalities


# In[ ]:




