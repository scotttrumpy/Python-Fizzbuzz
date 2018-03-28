 
 # import unit test
import unittest
# import code to be tested
import counter

class test_fizzbuzz(unittest.TestCase):
 # test the ""fizzbuzz"" response
 	def test_for_the_return_of_fizzbuzz_for_multiples_of_3_and_5(self):
 		self.assertEqual(counter.fizzbuzz(15), 'Fizzbuzz')

 # test the "fizz" response
 	def test_for_the_return_of_fizz_for_multiples_of_3(self):
 		self.assertEqual(counter.fizzbuzz(9), 'Fizz')

 # test the "buzz" response
 	def test_for_the_return_of_buzz_for_multiples_of_5(self):
 		self.assertEqual(counter.fizzbuzz(55), 'Buzz')

 # test integer response for non multiples
 	def test_no_response(self):
		self.assertEqual(counter.fizzbuzz(22), 22)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
 