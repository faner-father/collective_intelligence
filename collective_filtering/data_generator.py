# coding: utf-8
import random
rand_float = lambda :round(random.uniform(0, 5.0), 1)
rand_mark = lambda movies:dict([(movie, rand_float()) for movie in movies])

data_gen = lambda movies, audiences:dict([(aud, rand_mark(movies)) for aud in audiences])
