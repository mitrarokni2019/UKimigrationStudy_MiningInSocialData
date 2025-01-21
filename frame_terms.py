#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Frame Words for 14 Frames
frame_words = {
    'Contributions': [
        'ability', 'attract', 'build', 'contribute', 'contribution', 'desirable',
        'enlist', 'enrich', 'friendly', 'gain', 'genuine', 'hardworking', 'hero',
        'highskilled', 'industrious', 'lawabide', 'loyal', 'patent', 'qualified',
        'selfsufficiency', 'sturdy', 'veteran', 'worthy', 'energetic', 'enterprising',
        'entrepreneurial', 'intelligent', 'motivate', 'patriotic', 'productive',
        'resourceful', 'selfreliant', 'talented', 'thrifty', 'welleducated'
    ],
    'Crime': [
        'absconder', 'apprehend', 'arrest', 'bootlegger', 'capture', 'convict', 'criminal',
        'criminalize', 'detain', 'detainee', 'felon', 'fugitive', 'gang', 'illegal',
        'imprison', 'imprisonment', 'incarcerate', 'incarceration', 'inmate', 'jail',
        'noncriminal', 'offense', 'parole', 'prosecute', 'prosecution', 'smuggle',
        'smuggler', 'smuggling', 'steal', 'terrorist', 'unlawful', 'violent',
        'adultery', 'apprehending', 'felonious', 'felony', 'habitual', 'indictable',
        'informer', 'kidnap', 'larceny', 'manslaughter', 'murder', 'offender',
        'perjury', 'perpetrator', 'rapist', 'trumpedup'
    ],
    'Culture': [
        'americanization', 'assimilate', 'assimilation', 'background', 'christian',
        'citizenship', 'culture', 'diverse', 'diversity', 'ethnic', 'flag', 'foreigner',
        'heritage', 'integrate', 'integration', 'language', 'nation', 'race', 'society',
        'tradition', 'amalgamation', 'anglosaxon', 'caste', 'caucasian', 'civilization',
        'cultural', 'folklore', 'individuality', 'lineage', 'linguistic', 'mosaic',
        'multicultural', 'multiethnic', 'nationhood', 'pluralism', 'richness', 'tapestry'
    ],
    'Deficient': [
        'aidsinfected', 'cheap', 'diseased', 'drunk', 'ignorant', 'illiteracy',
        'illiterate', 'insane', 'objectionable', 'slacker', 'undesirable', 'unfit',
        'unskilled', 'addicted', 'degraded', 'depraved', 'idiot', 'illegitimate', 'immoral',
        'infected', 'institutionalized', 'lazy', 'lunatic', 'obese', 'overweight', 'pauper',
        'pauperism', 'unclean', 'uneducated', 'unemployable', 'unwanted'
    ],
    'Economic': [
        'agricultural', 'allocation', 'bank', 'budget', 'buy', 'cash', 'cent', 'coin',
        'compete', 'competition', 'corporation', 'cost', 'economic', 'finance', 'fund',
        'funding', 'investor', 'owner', 'ownership', 'pay', 'property', 'purchase',
        'reimbursement', 'sale', 'specie', 'tax', 'taxpayer', 'workforce',
        'capitalization', 'depreciation', 'financing', 'investment', 'loan', 'loans',
        'mortgage', 'payments', 'premium', 'savings', 'subsidy', 'taxfree'
    ],
    'Exclusion': [
        'admissibility', 'allow', 'ban', 'bar', 'cap', 'ceiling', 'criterion', 'debar',
        'deny', 'deport', 'deportable', 'deportation', 'detain', 'deter', 'eligibility',
        'excludable', 'exclude', 'expel', 'expulsion', 'forbid', 'inadmissible', 'inspect',
        'interdict', 'interdiction', 'limit', 'prevent', 'prohibit', 'prohibition',
        'quota', 'reject', 'removal', 'restrict', 'restriction', 'screen', 'shut', 'stop',
        'unauthorized', 'vet', 'vetting', 'apply', 'banning', 'circumvent', 'discourage',
        'disqualify', 'inhibit', 'nullify', 'penalize', 'permit', 'preclude', 'proscribe',
        'revoke', 'waive'
    ],
    'Family': [
        'ancestor', 'boy', 'child', 'daughter', 'descendant', 'family', 'familybased',
        'familysponsored', 'generation', 'girl', 'grandchild', 'granddaughter',
        'grandparent', 'grandson', 'household', 'husband', 'kid', 'marriage', 'marry',
        'neighbor', 'neighborhood', 'orphan', 'parent', 'relative', 'son', 'spouse', 'wife',
        'aunt', 'bride', 'brother', 'cousin', 'father', 'grandfather', 'grandmother',
        'mother', 'nephew', 'niece', 'sibling', 'stepfather', 'stepmother'
    ],
    'Flood/Tide': [
        'absorb', 'absorption', 'drain', 'fill', 'flood', 'flow', 'inflow', 'influx',
        'outflow', 'pour', 'spill', 'stream', 'surge', 'tide', 'trickle', 'wave',
        'avalanche', 'deluge', 'drift', 'flooding', 'hemorrhage', 'infusion', 'inundate',
        'inundation', 'melt', 'overflow', 'seepage', 'swarm', 'tidal', 'torrent'
    ],
    'Labor': [
        'agricultural', 'compete', 'competition', 'crewman', 'employ', 'employee',
        'employer', 'employment', 'farmworker', 'hire', 'hiring', 'laborer', 'miner',
        'nurse', 'tailor', 'unskilled', 'worker', 'workforce', 'apprentice', 'artisan',
        'bricklayer', 'electrician', 'helper', 'journeyman', 'labor', 'lowwage',
        'mechanic', 'parttime', 'seasonal', 'skilled', 'wages', 'workman', 'workmen'
    ],
    'Legality': [
        'adjudication', 'amnesty', 'applicant', 'application', 'authorization',
        'authorize', 'citizenship', 'eligibility', 'eligible', 'exemption',
        'familysponsored', 'hearing', 'identification', 'illegal', 'inadmissible',
        'ineligible', 'law', 'lawful', 'legal', 'legalization', 'legalize', 'legitimacy',
        'naturalization', 'naturalize', 'overstay', 'permanent', 'prosecute', 'qualify',
        'registration', 'status', 'unauthorized', 'undocumented', 'verification', 'visa'
    ],
    'Quantity': [
        'additional', 'boatload', 'bulk', 'bunch', 'cap', 'count', 'crowd', 'estimate',
        'estimated', 'flock', 'fraction', 'horde', 'increase', 'majority', 'many', 'mass',
        'million', 'more', 'most', 'much', 'number', 'percentage', 'proportion', 'statistic',
        'sum', 'thousand', 'total'
    ],
    'Threats': [
        'aidsinfected', 'anarchist', 'apprehension', 'attack', 'belligerent', 'blame',
        'combatant', 'danger', 'enemy', 'gang', 'horde', 'infect', 'invasion', 'menace',
        'problem', 'terrorist', 'threaten', 'violent'
    ],
    'Victims': [
        'acceptance', 'afflict', 'aid', 'amnesty', 'asylum', 'assist', 'battered',
        'compassion', 'desperate', 'escape', 'exploit', 'feed', 'flee', 'help', 'helpless',
        'hope', 'humanitarian', 'impoverished', 'languish', 'orphan', 'penniless',
        'persecute', 'persecution', 'plight', 'prejudice', 'refuge', 'refugee', 'relief',
        'rescue', 'reward', 'sanctuary', 'shelter', 'struggle', 'suffering', 'survivor',
        'tragedy', 'unfortunate', 'victim', 'welcome'
    ],
    'Migration': [
        'arrival', 'arrive', 'boatload', 'convoy', 'cross', 'departure', 'destination',
        'displacement', 'emigrate', 'enter', 'entry', 'exodus', 'flight', 'immigrate',
        'incoming', 'land', 'landing', 'migrate', 'migration', 'move', 'passage', 'port',
        'relocate', 'relocation', 'resettle', 'resettlement', 'return', 'route', 'settle',
        'settlement', 'ship', 'transport', 'travel', 'voyage'
    ]
}












    # Frame Queries
frame_queries = [
    ('self sufficiency', 'selfsufficiency'),
    ('law abide', 'lawabide'),
    ('high skilled', 'highskilled'),
    ('family based', 'familybased'),
    ('family sponsored', 'familysponsored'),
    ('aids infected', 'aidsinfected'),
    ('employment based', 'employmentbased'),
    ('farm worker', 'farmworker'),
    ('two third', 'twothird')
]



# Frame Replacements
frame_replacements = [
    ('self (n) sufficiency (n)', 'selfsufficiency'),
    ('law (n) abide (v)', 'lawabide'),
    ('high (a) skilled (a)', 'highskilled'),
    ('family (n) based (n)', 'familybased'),
    ('family (n) sponsored (n)', 'familysponsored'),
    ('aids (n) infected (a)', 'aidsinfected'),
    ('employment (n) based (n)', 'employmentbased'),
    ('farm (n) worker (n)', 'farmworker'),
    ('farm (v) worker (n)', 'farmworker'),
    ('two (c) third (n)', 'twothird')
]




# Helper Functions
def get_frame_terms():
    return frame_words

def get_frame_queries():
    return frame_queries

def get_frame_replacements():
    return frame_replacements


# In[ ]:




