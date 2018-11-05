def write_movie_info(string,a_dict):
    filename = open(string, "w")
    keys_list = sorted(a_dict.keys())
    for movie in keys_list:
        for (title,actors) in a_dict.items():
            if movie == title:
                actors.sort()
                new_actors = str(actors)
                new_actors = new_actors.strip("[]")
                new_actors = new_actors.replace("'","")
                filename.write(movie +": " + new_actors + "\n")
    filename.close()
#If your function works correctly, this will originally
#print nothing -- however, it should write the same contents
#as Sample.txt to Test.txt.
movies = [{"Chocolat": ["Juliette Binoche", "Judi Dench", "Johnny Depp", "Alfred Molina"], "Skyfall": ["Judi Dench", "Daniel Craig", "Javier Bardem", "Naomie Harris"]}]
write_movie_info("Test.txt", movies)
