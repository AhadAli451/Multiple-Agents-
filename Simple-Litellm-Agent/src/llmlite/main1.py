from crewai.flow import Flow, listen, start
from litellm import completion

class LiteLlmFlow(Flow):

    @start()
    def start_function(self):
        output = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
            {"role": "user",
             "content": "Hello, how are you?"}
        ])
        return output['choices'][0]['message']['content']

def run_litellm_flow():
    obj = LiteLlmFlow()
    result = obj.kickoff()
    print(result)
