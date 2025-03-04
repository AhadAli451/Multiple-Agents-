from crewai.flow.flow import Flow, start, listen
from litellm import completion

API_KEY = 'AIzaSyBsJlhwQXvqc-k3hIycOjiSa_pG1655eJM'
class CityFunFact(Flow):

    @start()
    def generate_random_city(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[
                {
                    "role": "user",
                    "content": "Return any random city name form pakistan some like and in greet way .",
                },
            ],
        )


        result = response["choices"][0]["message"]["content"]
    #     # Store the city in our state
        self.state["city"] = result
        print(f"Random City: {result}")

        return result

    @listen(generate_random_city)
    def generate_fun_fact(self, city_name):
        response = completion(
        model="gemini/gemini-1.5-flash",
        api_key=API_KEY,
            messages=[
                {
                    "role": "user",
                    "content": f"write a fun fact about {city_name}",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        # Store the fun fact in our state
        self.state["fun_fact"] = fun_fact
        return fun_fact
    

    @listen(generate_fun_fact)
    def save_fun_fact(self,):
        with open("fun_fact.md","w") as file:
            file.write(self.state['fun_fact'])
            return self.state['fun_fact']

def kickoff():
    obj = CityFunFact()
    result = obj.kickoff()
    print(result)

def plot():
    obj = CityFunFact()
    result = obj.plot()
    print(result)
    