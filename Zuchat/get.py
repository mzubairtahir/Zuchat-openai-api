import openai
import customtkinter
import threading

class Getclass:
    def __init__(self,prompt,donefunc):

        self.prompt=prompt
        self.donefunction=donefunc

    def start_threading(self):
        self.thread=threading.Thread(target=self.main_geting)

        self.thread.start()
        

    def token_count(self,prompt):
        length_of_prompt=len(prompt)
        if length_of_prompt <=5:
            self.request_tokens=20

        else:
            self.request_tokens=1500

        return self.request_tokens


    
    def main_geting(self):
        try:
            openai.api_key = "" #your api key will be here

            


            response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.prompt,
            max_tokens=self.token_count(prompt=self.prompt),
            n=3,
            stop=None,
            temperature=0.7,
            )

            self.generatedtext=  response.choices[0].text
            self.donefunction(text=self.generatedtext,generated_sucss=True)
        except Exception as p:
            self.donefunction()
