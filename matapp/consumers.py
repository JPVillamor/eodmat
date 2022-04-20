from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

'''
from .models import Sensor
from .models import User
from .models import Record
from .models import UserInfo

from . import counter
#from . import IR
from . import PIR
from . import forcemux
'''

pause = False
#timestamp = float(0)

class WSConsumer(AsyncJsonWebsocketConsumer):
      async def connect(self):
            global timestamp
            self.groupname='dashboard'
            await self.channel_layer.group_add(
                  self.groupname,
                  self.channel_name,
            )
            await self.accept()
            timestamp = float(0)
    
      async def receive(self, text_data):
            global pause
            global timestamp
            datapoint = json.loads(text_data)
            msg_type = datapoint['type']
            val = datapoint['value']

            if msg_type == 'control':
                  if val == 0:
                        pause = True
                        #print(pause)
                  elif val == 1:
                        pause = False
                        #print(pause)

            elif msg_type == 'data':
                  if pause == True:
                        pass
                  elif pause == False:
                        #print(pause)
                        await self.channel_layer.group_send(
                              self.groupname,
                              {
                              'type':'frontend', #function name to run
                              'value':val #value to send function
                              }
                        )
            elif msg_type == 'ir_data':
                  if pause == True:
                        pass
                  elif pause == False:
                        await self.channel_layer.group_send(
                              self.groupname,
                              {
                              'type':'ir_graph', #function name to run
                              'value':val #value to send function
                              }
                        )

            #timestamp = timestamp + 0.4

      async def frontend(self,event):
            val_list=event['value']
            await self.send(text_data=json.dumps(val_list))# send for frontend
                  
      async def ir_graph(self, event):
            graph_data = event['value']
            await self.send(text_data=json.dumps(graph_data))

      async def disconnect(self, close_code):
            await self.channel_layer.group_discard(
                  self.groupname,
                  self.channel_name
            )   
