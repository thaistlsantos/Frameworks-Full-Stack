import json
import requests
import time
from unittest import TestCase, main

class Blog:
	def __init__(self, nome):
		self.nome = nome

	def posts(self):
		endereco = "https://jsonplaceholder.typicode.com/posts"
		response = requests.get(endereco)
		return response.json()

	def __repr__(self):
		return 'texto: {}>'.format(self.nome)



class Testes(TestCase):

    def teste_dowload(self):
        start = time.time()

        blog = Blog("Teste")
        result =blog.posts()
        with open('person.json', 'w') as json_file:
            json.dump(result, json_file)

        end = time.time()
        execution_time = end - start
        self.assertIsNotNone(result)
        self.assertIsInstance(result[0], dict)

        print(" %0.3f ms    " % (execution_time * 1000.))

    def teste_toobject(self):
        with open("person.json", "r") as read_file:
            data = json.load(read_file)
            print(type(data))
            for x in range(len(data)):
                print (data[x])
        self.assertIsNotNone(data)

    def teste_toobject2(self):
        with open("person.json", "r") as read_file:
            data = json.load(read_file)
            print(type(data))
            for x in range(len(data)):
                print(data[x])
        self.assertIsNotNone(data)


if __name__ == '__main__':
    main()

