from crewai.flow.flow import Flow, start, listen
from litellm import completion

API_KEY = 'AIzaSyACFw5PV4dquQ3JO253thpsYvj5ho4dMuI'
class CityFunFact(Flow):

    @start()
    def generate_rondom_city(slef):
        result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"content":"Return any random city name.",
                       "role":"user"}]
        )
        randon_city = result['choices'][0]['message']['content']
        self.state['city'] = randon_city
        print(randon_city["randon_city"])
        return randon_city
    
    @listen(generate_rondom_city)
    def generate_fun_fact(self, randon_city):

         result = completion(
            model="gemini/gemini-1.5-flash",
            api_key=API_KEY,
            messages=[{"content":f"write some fun fact about{randon_city}.",
                       "role":"user"}]
        )
         
        fun_fact = result['choices'][0]['message']['content']
        print(city_name)
        self.state['fun_fact'] = fun_fact
    

    @listen(generate_fun_fact)
    def save_fun_fact(self):
        with open("fun_fac.md","w") as file:
            file.write(self.state['fun_fact'])
            return self.state['fun_fact']
def kickoff():
    obj = CityFunFact()
    result = obj.kickoff()
    print(result)