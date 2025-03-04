from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class DevCrew:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"


    @agent
    def front_end_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["front_end_developer"],
        )
    
    @agent
    def review_feedback(self) -> Agent:
        return Agent(
            config=self.agents_config["review_feedback"],
        )


    @task
    def write_code(self) -> Task:
        return Task(
            config=self.tasks_config["write_code"],
        )
    
    @task
    def give_feedback(self) -> Task:
        return Task(
            config=self.tasks_config["give_feedback"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
