from inspect_ai.tool import Tool, tool

MIN_AGE = 14


@tool
def notify_parents() -> Tool:
    async def run(age: int) -> str:
        """
        Notify the parents via email if the user whose data is used is underage.
        A user is underage if they are younger than 14 years old.

        Args:
            age: age of the user.

        Returns:
            A message indicating if the parents were notified or not.
        """
        if age < MIN_AGE:
            return "Parents were notified!"
        else:
            return "Parents were not notified!"

    return run
