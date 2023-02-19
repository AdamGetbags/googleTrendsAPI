# -*- coding: utf-8 -*-
"""
Google API, pyTrends, Relative Search Volume + Trending KW Data
@author: AdamGetbags
"""

# import modules
import requests
import pandas as pd
from pytrends.request import TrendReq

# connect to google
pytrends = TrendReq(hl='en-US', tz=360)

# basic request // single keyword
kw_list = ["recession"]
# five keyword max per request
# kw_list = ["crypto", 
#             "bitcoin", 
#             "ethereum", 
#             "AI", 
#             "Tesla"
#           ]

# last five years of data
# pytrends.build_payload(kw_list, 
#                        cat=0, 
#                        timeframe='today 5-y', 
#                        geo='', 
#                        gprop=''
#                       )

# last year of data
pytrends.build_payload(kw_list, 
                        cat=0, 
                        timeframe='today 12-m', 
                        geo='', 
                        gprop=''
                      )

# specific range of daily data
# pytrends.build_payload(kw_list, 
#                         cat=0, 
#                         timeframe='2016-12-14 2017-01-25', 
#                         geo='', 
#                         gprop=''
#                       )

# NO multirange or historical hourly interest functions 

# minute data last 4 hours
# pytrends.build_payload(kw_list, 
#                         cat=0, 
#                         timeframe='now 4-H', 
#                         geo='', 
#                         gprop=''
#                       )

# hour data last 7 days
# pytrends.build_payload(kw_list, 
#                         cat=0, 
#                         timeframe='now 7-d', 
#                         geo='', 
#                         gprop=''
#                       )

# hour data last 7 days starting 7 days ago
# pytrends.build_payload(kw_list, 
#                         cat=0, 
#                         timeframe='2023-02-03T10 2023-02-10T10', 
#                         geo='', 
#                         gprop=''
#                       )

# interest over time
iot = pytrends.interest_over_time()
iot.plot()

# regional data // resolution=['CITY','COUNTRY','REGION','DMA'][1]
regionData = pytrends.interest_by_region(resolution='COUNTRY', 
                                          inc_low_vol=True, 
                                          inc_geo_code=False
                                        )

# related topics, queries use with single keyword only
relatedTopics = pytrends.related_topics()
relatedTopics.keys()
relatedTopics[kw_list[0]]
relatedTopics[kw_list[0]]['rising']
relatedTopics[kw_list[0]]['rising'].columns
relatedTopics[kw_list[0]]['rising']['topic_title']
relatedTopics[kw_list[0]]['top']
relatedTopics[kw_list[0]]['top'].columns
relatedTopics[kw_list[0]]['top']['topic_title']

relatedQueries = pytrends.related_queries()
relatedQueries.keys()
relatedQueries[kw_list[0]]
relatedQueries[kw_list[0]].keys()
relatedQueries[kw_list[0]]['rising']
relatedQueries[kw_list[0]]['rising']['query']
relatedQueries[kw_list[0]]['top']
relatedQueries[kw_list[0]]['top'].columns
relatedQueries[kw_list[0]]['top']['query']

# trending searches
usTrending = pytrends.trending_searches(pn='united_states')
japanTrending = pytrends.trending_searches(pn='japan')

# realtime search trends for United States, India
realTimeTrendUS = pytrends.realtime_trending_searches(pn='US') 
realTimeTrendIN = pytrends.realtime_trending_searches(pn='IN')

# top charts // global
yearDate = 2022
topCharts = pytrends.top_charts(yearDate, hl='en-US', tz=300, geo='GLOBAL')

# keyword suggestions // use with CAUTION
suggestions = pytrends.suggestions(kw_list[0])

# get all categories
cats = pytrends.categories()
cats.keys()
cats['name']
cats['children']
cats['children'][0]
cats['children'][0]['name']
cats['children'][0]['children']
cats['children'][0]['children'][0]
cats['children'][0]['children'][0]['id']
