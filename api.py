from fastapi_offline import FastAPIOffline
# from fastapi.staticfiles import StaticFiles
import database

app = FastAPIOffline()

# app.mount(
#     "/images",
#     StaticFiles(directory="src2/images"),
#     name="images")

@app.get('/')
def get_index():
    return{'HELLO':'MOVIES API'}

#######################################################
@app.get('/getmovies/')
def get_all_movies():
    records = database.select_all_records()

    movies = []
    for movie in records:

        movies.append({"id": movie[0],
                "title": movie[1],
                "imdb_rate": movie[2],
                "year": movie[3],
                "country": movie[4],
                "image": movie[5]})

    return {"movies": movies}

    # records = [database.select_all_records()]
    # return {f"Movies: 'id :'  {records[0] } 'title :'  {records[1]}'imdb_rate :' {records[2]}'year : ' {records[3]}'country : ' {records[4]}'image : ' {records[5]} " }

#######################################################
@app.post('/addmovie/')
def add_info_movies(title,imdb_rate:float,year,country,image):
    database.insert_record(title,imdb_rate,year,country,image)
    record = database.select_record_by_title(title)
    return{f'New Movie': {record}}

#######################################################
@app.delete('/deleteid')
def delete_movie_by_id(id:int):
    record = database.select_record_by_id(id)
    if record:
        database.delete_record_by_id(id)

        return {f'movie with id {id} and title {record[1]} removed from Movies'}

    else:
        return {f'{id} Not Found'}

    #Title = database.select_record_by_id(id)

    #record = database.select_all_records()
    # return {f'Id {id} removed from Movies and Movies:{record}'}
##############################################################
@app.put('/updatemovie')
def update_by_id(id:int,title,imdb_rate:float,year,country,image):
    old_record = database.select_record_by_id(id)

    if old_record:
        database.update_record_by_id(id,title,imdb_rate,year,country,image)
        new_record = database.select_record_by_id(id)
        return {f'movie with id {id} and title {old_record[1]} replaced by {new_record[1]}'}
    else:
        return {f'movie with id {id} Not Found'}
         