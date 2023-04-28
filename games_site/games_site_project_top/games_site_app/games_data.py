import requests
import psycopg2

url = "https://free-to-play-games-database.p.rapidapi.com/api/filter"

querystring = {"tag":"3d"}

querystring_2d = {"tag":"2d"}

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "7870182cecmsh6726ede8ada5833p18a4f9jsne9d3e5695d84",
	"X-RapidAPI-Host": "free-to-play-games-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response_2d = requests.get(url, headers=headers, params=querystring_2d)


extracted_data = response.json()
extracted_data_2d = response_2d.json()


complete_extracted_data = []

for item in extracted_data:
    complete_extracted_data.append(item)

for item in extracted_data_2d:
    complete_extracted_data.append(item)


# preparing the data-----------------------------------------------------------------

def extract(instance: dict):

    try:
        title = instance['title']
        thumbnail = instance['thumbnail']
        description = instance['short_description']
        game_url = instance['game_url']
        genre = instance['genre']
        platform = instance['platform']
        publisher = instance['publisher']
        developer = instance['developer']
        release_date = instance['release_date']
        storepage_url = instance['freetogame_profile_url']

        return title, thumbnail, description, game_url, genre, platform, publisher ,developer, release_date, storepage_url
    except KeyError:
        return None


def preprocess(instances: list[dict]): 

    preprocessed = []
    for instance in instances:
        preprocessed_inst = extract(instance)
        if preprocessed_inst is None:
            continue
        preprocessed.append(preprocessed_inst)
    return preprocessed


test = extract(complete_extracted_data[12])
test2 = preprocess(complete_extracted_data)

def clean_data(data: tuple):
    new_data = list(data)
    for i, item in enumerate(new_data):
        if isinstance(item, str) and "'" in item:
            new_data[i] = item.replace("'", "")
    return tuple(new_data)

cleaned_data_list = []


for item in test2:
    new_data = clean_data(item)
    cleaned_data_list.append(new_data)


# pushing to database------------------------------------------------------------------------------

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Ns9517530809'
DATABASE = 'games_site_db'


connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)


def insert_query(columns_names: list[str], data: tuple, table_name:str) -> str:
    columns = ", ".join(columns_names)
    title, thumbnail, description, game_url, genre, platform, publisher, developer, release_date, storepage_url = data
    query = f"""insert into {table_name} ({columns}) values (N'{title}', N'{thumbnail}', N'{description}', N'{game_url}', N'{genre}', N'{platform}', N'{publisher}', N'{developer}', '{release_date}', N'{storepage_url}');"""

    return query

columns = ['title', 'thumbnail', 'description', 'game_url', 'genre', 'platform','publisher','developer','release_date','storepage_url']

def run_change_query(query: str): 
    try:
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.commit()
            print("SUCCESS")
    except SyntaxError:
        pass


for clean_inst in cleaned_data_list:
    q = insert_query(columns_names = columns, data = clean_inst, table_name = 'games_site_app_games_data')
    run_change_query(q)