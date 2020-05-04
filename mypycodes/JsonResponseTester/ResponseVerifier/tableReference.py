''' table reference holds all the SOI commands and corresponding table names with column names
author :: empqtut <manikandan.chandrasekaran@ericsson.com>
'''
import _utils
tableReference = {
  "addressRead":
      {"ccontact_all":{
        "adrcity":"CCCITY",
        "adrzip":"CCZIP",
        "adrstreetno":"CCSTREETNO",
        "adrstreet":"CCSTREET",
        "adrstate":"CCSTATE",
        "adremail":"CCEMAIL",
        "adrphn1_area":"CCTN_AREA",
        "adrphn1":"CCTN",
        "lngcode":"CCLANGUAGE",
        "adrfname":"CCFNAME",
        "adrlname":"CCLNAME",
        "adrname":"CCNAME",
        "ttlid":"CCTITLE",
        "countryid":"COUNTRY"
      }},
  "titlesRead" : {"title":{"ttlid":"TTL_ID","ttldescription":"TTL_DES"}},
  "countriesRead":{"country":{'cntrdes': 'NAME', 'countryid': 'COUNTRY_ID'}},
  "languagesRead":{"language":{'lngdes': 'LNG_DES', 'lngcode': 'LNG_ID'}}}
