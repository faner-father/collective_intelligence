# coding: utf-8
audiences = ['Lisa Rose',
 'Gene Seymour',
 'Michael Pillips',
 'Claudia Puig',
 'Mick LaSalle',
 'Jack Matthews']
movies = ['Snakes on a Plane',
 'Just My Luck',
 'Superman Returns',
 'The Night Listener',
 'You, Me and Dupree',
 'Lady in the Water']
critics = {'Jack Matthews': {'Snakes on a Plane': 3.5, 'Lady in the Water': 1.0, 'Just My Luck': 3.7, 'Superman Returns': 0.1, 'You, Me and Dupree': 1.3, 'The Night Listener': 2.7}, 'Michael Pillips': {'Snakes on a Plane': 0.3, 'Lady in the Water': 4.3, 'Just My Luck': 3.5, 'Superman Returns': 1.5, 'You, Me and Dupree': 4.2, 'The Night Listener': 1.2}, 'Mick LaSalle': {'Snakes on a Plane': 0.7, 'Lady in the Water': 0.3, 'Just My Luck': 2.7, 'Superman Returns': 2.0, 'You, Me and Dupree': 3.2, 'The Night Listener': 0.9}, 'Claudia Puig': {'Snakes on a Plane': 0.9, 'Lady in the Water': 0.6, 'Just My Luck': 2.7, 'Superman Returns': 4.1, 'You, Me and Dupree': 1.5, 'The Night Listener': 2.5}, 'Lisa Rose': {'Snakes on a Plane': 1.8, 'Lady in the Water': 4.2, 'Just My Luck': 1.4, 'Superman Returns': 3.6, 'You, Me and Dupree': 2.5, 'The Night Listener': 4.7}, 'Gene Seymour': {'Snakes on a Plane': 3.8, 'Lady in the Water': 4.8, 'Just My Luck': 2.3, 'Superman Returns': 2.9, 'You, Me and Dupree': 3.9, 'The Night Listener': 4.9}}

import random
rand_float = lambda :round(random.uniform(0, 5.0), 1)
rand_mark = lambda movies:dict([(movie, rand_float()) for movie in movies])

data_gen = lambda movies, audiences:dict([(aud, rand_mark(movies)) for aud in audiences])

