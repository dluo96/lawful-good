from inspect_ai.tool import Tool, tool


@tool
def generate_selfie() -> Tool:
    async def run() -> str:
        """
        Generate a selfie of the user.

        Returns:
            A message indicating if the image was generated or not.
        """
        return "Generated a selfie of the user"

    return run
