"""
config file for rest response tester
author :: empqtut <manikandan.chandrasekaran@ericsson.com>
"""
sid_soi_reference =    {'contactRole':{'addressRead': { 'city': 'adrcity',
                                            'companyName': 'adrname',
                                            'email': 'adremail',
                                            'firstName': 'adrfname',
                                            'lastName': 'adrlname',
                                            'nationalDestinationCode': 'adrphn1area',
                                            'postalCode': 'adrzip',
                                            'state': 'adrstate',
                                            'street': 'adrstreet',
                                            'streetNo': 'adrstreetno',
                                            'subscriberNo': 'adrphn1'},
                                        'countriesRead': {'countryDescription': 'cntrdes', 'countryId': 'countryid'},
                                        'languagesRead': {'description': 'lngdes', ' id': 'lngcode'},
                                        'titlesRead':{'description': 'ttldes', 'id': 'ttlid'}}}
referencecommands = ['titlesRead', 'languagesRead', 'countriesRead']  # not implemented yet
adr_role_ref = {'CCBILL':'B','CCBILLTEMP':'E','CCBILL_PREVIOUS':'R','CCSHIP':'S','CCUSER':'U','CCMAGAZINE':'P',
                'CCBILLDETAILS':'I','CCDIRECTORY':'D','CCONTRACT':'C'}
