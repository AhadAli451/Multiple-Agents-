from crewai.flow.flow import Flow, start, listen, router
from pydantic import BaseModel
import random

class RouteFlow(Flow):

    @start()
    def greeting(self):
        print("Assalam-o-alikum")

    @router(greeting)
    def selecet_city(self):
        cities =["karachi", "islamabad", "lahore"]
        self.city = random.choice(cities)
        print("selected city is", self.city)
        # self.state['city'] = selecet_city


        if self.state=='karachi':
           return 'karachi'
        if self.state=='islamabad':
           return 'islamabad'
        if self.state=="lahore":
           return 'lahore'
    
    @listen("karachi")
    def karachi1(self):
        print(f"write some fun fact about karachi")

    @listen("islamabad")
    def islamabad1(self):
        print("write some fun fact about islamabad")

    @listen("lahore")
    def lahore1(self):
        print("write some fun fact about lahore")

def kickoff():
    obj = RouteFlow()
    obj.kickoff()

def plot():
    obj = RouteFlow()
    obj.plot()