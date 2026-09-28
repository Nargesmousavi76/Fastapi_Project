import requests

def get_all_movies():
    url = 'http://127.0.0.1:8000/getitems/'
    response = requests.get(url)

    if response.status_code != 200:
        return "ERRORE"
    else:
        return response.json()

if __name__ == "__main__":
    print(get_all_movies())

def add_movie(title,imdb_rate:float,year,country,image):
    url = f'http://127.0.0.1:8000/addmovie/'
    parms = {
        'title' : title,
        'imdb_rate': imdb_rate,
        'year' : year ,
        'country' : country ,
        'image' : image
        }

    response = requests.post(url, params=parms)

    if response.status_code != 200:
        return "ERRORE"
    else:
        return response.json()
    
#if __name__ == "__main__":
    #print(add_movie("Grean book",7.3,"2018","USA","Grean book.jpg"))

def delete(id):
    url = f'http://127.0.0.1:8000/deleteid?id={id}'
    response = requests.delete(url)

    if response.status_code != 200:
        return "ERRORE"
    else:
        return response.json()

# if __name__ == '__main__':
#     print(delete(13))

def update_movie(id,title,imdb_rate,year,country,image):
    url = f'http://127.0.0.1:8000/updatemovie/'
    parms = {
        "id" : id,
        "title" : title ,
        "imdb_rate" : imdb_rate,
        "year" : year,
        "country" : country,
        "image" : image
             }
    response = requests.put(url, params=parms)

    if response.status_code != 200 :
        return "ERRORE"
    else:
        return response.json()

#if __name__ == "__main__":
    #print(update_movie(9, "God Father",8.8,"2009","USA","God Father.jpg"))