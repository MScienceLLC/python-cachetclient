#!/usr/bin/env python
import mscience_cachetclient.cachet as cachet
import json
import os

ENDPOINT = os.environ['QA_CACHET_ENDPOINT']
TOKEN = os.environ['QA_CACHET_TOKEN']

factory = cachet.Factory(api_token=TOKEN, endpoint=ENDPOINT)
ping = factory.get("Ping")
print(ping.get())

components = factory.get('Components')
print(components.get(id=2))

# groups = factory.get('Groups')
# print(groups.get(id=1))

runs = factory.get('Runs')
# print( runs.get(id=23))

# new_run = json.loads(runs.post(name='Test nile component run',
#                               component_id=2,
#                               description='API Client Inserted',
#                               airflow='https://airflow.com'
#                               )
#                     )
                               
# print(runs.get(id=new_run['data']['id']))

updated_run = json.loads(runs.put(
                                    id=37,
                                    status=-1
                                 )
                        )

run = runs.get(id=37)
print(run)

updated_run = json.loads(runs.put(
                                    id=37,
                                    status=1
                                 )
                        )

run = runs.get(id=37)
print(run)

# testing = factory.get('NotHere')
