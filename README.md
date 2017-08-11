# binge-trendy
A python program to help you binge watch better episodes of your favorite TV shows

I use the website [GraphTV](http://graphtv.kevinformatics.com/)
frequently to get a quick insight if a TV show is getting better or
worse over the course of a season. GraphTV plots the IMDb user ratings for every episode and then performs a
[linear regression](https://en.wikipedia.org/wiki/Linear_regression) of
the episode rating on the episode number to make a trend line. I have often found that
watching only the shows above the trend line means I can just watch the best
episodes and skip the bad ones (i.e. the ones below the trend line). I
also wanted a good reason to use [OMDb API](http://www.omdbapi.com/)

For example, lets say I am interested in watching the best episodes of
[Golden Girls](http://www.imdb.com/title/tt0088526/) Season 4:

```$python trendy_binge.py -url http://www.imdb.com/title/tt0088526/ -api your_omdb.txt -s 4```

This command prints to terminal only the finest episodes of the Golden Girls of Season 4 (as decided by IMDb
members) for your viewing pleasure:


|   Season| Episode |                                Name|
| -------- | :-----: | ----------------------------------:|
|       4 |     1 |               Yes, We Have No Havanas|
|       4 |     2 |The Days and Nights of Sophia Petrillo|
|       4 |     6 |              Sophia's Wedding: Part 1|
|       4 |     9 |                       Scared Straight|
|      4  |   11  |                          The Auction|
|      4  |   14  |                       Love Me Tender|
|      4  |   15  |                      Valentine's Day|
|      4  |   19  |              Till Death Do We Volley|
|      4  |   20  |                         High Anxiety|
|      4  |   22  |                      Sophia's Choice|
|      4  |   23  |                      Rites of Spring|
|      4  |   24  |                     Foreign Exchange|

Of course this will only work for TV shows where you can just watch a few
episodes here and there and not for shows like the [greatest show ever](http://www.imdb.com/title/tt0306414/)
