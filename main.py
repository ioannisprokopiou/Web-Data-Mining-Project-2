import gather_keys_oauth2 as Oauth2
import fitbit
import pandas as pd 
import datetime

CLIENT_ID='23QSLM'
CLIENT_SECRET='8ed82541d286c938f9b8bc3f4e46da82'

server=Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET)
server.browser_authorize()
ACCESS_TOKEN=str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN=str(server.fitbit.client.session.token['refresh_token'])
auth2_client=fitbit.Fitbit(CLIENT_ID,CLIENT_SECRET,oauth2=True,access_token=ACCESS_TOKEN,refresh_token=REFRESH_TOKEN)


oneDate = pd.to_datetime('2023-04-10',format='%Y-%m-%d')
print(oneDate)

oneDayData = auth2_client.intraday_time_series('activities/heart',base_date=oneDate,detail_level='1sec')

df = pd.DataFrame(oneDayData['activities-heart-intraday']['dataset'])

filename = oneDayData['activities-heart'][0]['dateTime'] +'_intradata'

#hello 
#hello2