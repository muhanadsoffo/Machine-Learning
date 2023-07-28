import numpy as np 


one_dimensional_array = np.array([1.2, 2.4, 2.9, 4.7, 6.6, 4.2, 8.3, 8.5])
print(one_dimensional_array)


two_dimensional_array = np.array([[3, 5], [1, 57], [44, 82]])
print(two_dimensional_array)


sequence_of_integers = np.arange(3, 15)
print(sequence_of_integers)

random_integers_between_50_and_100 = np.random.randint(low=23, high=141, size=(8))
print(random_integers_between_50_and_100)


random_floats_between_0_and_1 = np.random.random([4])
print(random_floats_between_0_and_1) 

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 3.0
print(random_floats_between_2_and_3)

random_integers_between_150_and_300 = random_integers_between_50_and_100 * 5
print(random_integers_between_150_and_300)