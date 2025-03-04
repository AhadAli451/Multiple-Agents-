from crewai import Agent, Task, Crew, Process, LLM
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
import os

# Get the GEMINI API key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Ensure the file path is correct
file_path = "text.txt"


# Create a knowledge source
text_source = TextFileKnowledgeSource(
    file_paths=file_path,
)

# Create an LLM with a temperature of 0 to ensure deterministic outputs
gemini_llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=GEMINI_API_KEY,
    temperature=0,
)

# Create an agent with the knowledge store
agent = Agent(
    role="About Text",
    goal="You know everything about the text file.",
    backstory="""You are a master at understanding text files and their contents.""",
    verbose=True,
    allow_delegation=False,
    llm=gemini_llm,
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

# Define the task
task = Task(
    description="Answer the following questions about the text file: {question}",
    expected_output="A clear and accurate response based on the file content.",
    agent=agent,
)

# Create the Crew with the task and agent
crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge_sources=[text_source],
    embedder={
        "provider": "google",
        "config": {
            "model": "models/text-embedding-004",
            "api_key": GEMINI_API_KEY,
        }
    }
)

# Function to execute the CrewAI workflow
def your_knowledge():
    result = crew.kickoff(inputs={"question": "What is written in the text file?"})
    print(result)

# Run the function
your_knowledge()
