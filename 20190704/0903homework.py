import csv

movie_list = [["Star wars", "Terminator", "AI"],
                ["Space", "Matrix", "Vampire"],
                ["Men in black", "I am a robot", "Evolution"]]

with open("0903file.csv","w", newline = "") as f:
    w = csv.writer(f, delimiter=";")
    for movies in movie_list:
        w.writerow(movies)