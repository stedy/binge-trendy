# binge-trendy
A python program to help you binge watch smarter by only listing the best episodes of TV shows

I use the website [GraphTV](http://graphtv.kevinformatics.com/)
frequently to get a quick insight if a TV show is getting better or
worse over the course of a season. GraphTV plots the IMDb user ratings for every episode and then performs a
[linear regression](https://en.wikipedia.org/wiki/Linear_regression) of
the episode rating on the episode number to make a trend line. I have personally found that
watching only the shows above the trend line means I just watch the good
episodes and skip the bad ones (i.e. the ones below the trend line). I
also wanted a good reason to use [OMDb API](http://www.omdbapi.com/)

Of course this will only work for TV shows where you can just watch a few
episodes here and there and not for shows like the [greatest show ever](http://www.imdb.com/title/tt0306414/)

## Examples
Show the best episodes of [Golden Girls](http://www.imdb.com/title/tt0088526/) Season 4:

```$python binge_trendy.py -url http://www.imdb.com/title/tt0088526/ -key your_omdb_file.txt -s 4```

|   Season| Episode |                                Name| Residual
| -------- | :-----: | ----------------------------------:|  :--------:|
|       4 |     1 |               Yes, We Have No Havanas|   0.215385|
|       4 |     6 |              Sophia's Wedding: Part 1|   0.127692|
|       4 |     9 |                       Scared Straight|   0.695077|
|      4  |   11  |                          The Auction|    0.340000|
|      4  |   14  |                       Love Me Tender|    0.307385|
|      4  |   15  |                      Valentine's Day|    0.829846|
|      4  |   19  |              Till Death Do We Volley|    0.519692|
|      4  |   20  |                         High Anxiety|    0.442154|
|      4  |   22  |                      Sophia's Choice|    0.187077|
|      4  |   23  |                      Rites of Spring|    0.709538|
|      4  |   24  |                     Foreign Exchange|    0.532000|


Show the highest-rated episode ever of [MacGuyver](http://www.imdb.com/title/tt0088559/):

```$python binge_trendy.py -url http://www.imdb.com/title/tt0088559/ -key your_omdb_file.txt -b```

|Season| Episode |       Name | Residual|
| -------- | :-----: | :--------: | ----------:|
|    7      | 3    | Obsessed  | 1.060922

Show the top ten best episodes of [The Simpsons](https://www.imdb.com/title/tt0096697/):

```$python binge_trendy.py -url https://www.imdb.com/title/tt0096697/ -key your_omdb_file.txt -tt```

| Season| Episode|                                 Name|  Residual|
| ----- | :-----: | -----------------------------------: | -------:|
|   27  |     9  |                               Barthood|  1.671316|
|   23  |     9  |              Holidays of Future Passed|  1.349520|
|   12  |    18  |                       Trilogy of Error|  1.318788|
|   30  |    10  |                   'Tis the 30th Season|  1.262113|
|   19  |     9  |  Eternal Moonshine of the Simpson Mind|  1.196692|
|   26  |     6  |                             Simpsorama|  1.195991|
|   31  |     5  |                   Gorillas on the Mast|  1.183386|
|    8  |    23  |                          Homer's Enemy|  1.168615|
|   18  |    21  |                             24 Minutes|  1.036194|
|    4  |    17  |               Last Exit to Springfield|  0.898918|
