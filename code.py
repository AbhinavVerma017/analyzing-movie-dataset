# --------------
from csv import reader


def explore_data(dataset,start,end,rows_and_columns=False):

    dataset_slice=dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')

    if rows_and_columns:
        print('Number of rows:',len(dataset))
        print('Number of columns:',len(dataset[0]))

def duplicate_and_unique_movies(dataset,index_):

    duplicate=[]
    unique=[]

    for movie in dataset:
        name=movie[index_]
        if name in unique:
            duplicate.append(name)
        else:
            unique.append(name)

        print('Number of duplicate Movies:',len(duplicate))  
        print('\n')
        print('Examles of duplicate Movies:',duplicate[:15])


def movies_lang(dataset,index_,lang_):
    movies_=[]

    for movie in movies:
        lang=movie[index_]
        if lang==lang_:
            movies_.append(movie)

    print("Examle of Movies in English Language:")
    explore_data(movies_,0,3,True)
    return movies_



def rate_bucket(dataset,rate_low,rate_high):

    rated_movies=[]

    for movie in dataset:
        vote_avg=float(movie[-4])
        if ((vote_avg>=rate_low)&(vote_avg<=rate_high)):
            rated_movies.append(movie)

    print("Examples of Movies in required rating bucket:")
    explore_data(rated_movies,0,3,True)
    return rated_movies


opend_file=open(path,encoding="utf8")
read_file=reader(opend_file)
movies=list(read_file)

movies_header=movies[0]
print("Movies Header:\n",movies_header)

movies=movies[1:]


print("Entry at index 4553:")
explore_data(movies,4533,4554)
del movies[4553]

print("Firts 5 Entries:")
explore_data(movies,0,5,True)


duplicate_and_unique_movies(movies,13)


reviews_max={}

for movie in movies:
    name=movie[13]
    n_reviews=float(movie[12])

    if name in reviews_max and reviews_max[name]<n_reviews:
        reviews_max[name]=n_reviews

    elif name not in reviews_max:
        reviews_max[name]=n_reviews
len(reviews_max)


movies_clean=[]
already_added=[]

for movie in movies:
    name=movie[13]
    n_reviews=float(movie[12])



    if (reviews_max[name]==n_reviews)and(name not in already_added):
        movies_clean.append(movie)
        already_added.append(name)

len(movies_clean)


movies_en=movies_lang(movies_clean,3,'en')

high_rated_movies=rate_bucket(movies_en,8,10)                


