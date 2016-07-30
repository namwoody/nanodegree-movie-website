import fresh_tomatoes
import media

# create a new object movie
sardaarji = media.Movie('Sardaar ji', 'Actor in this movie diljit',
                        'http://static.blugaa.com/thumbs/100_100/'
                        'mivvi.png',
                        'https://www.youtube.com/watch?v=Y93uXRGGEN8')

# create a new object movie
sultan = media.Movie('sultan', 'Salman Khan movie',
                     'http://s1.dmcdn.net/VvYWv.jpg',
                     'https://www.youtube.com/watch?v=wPxqcq6Byq0')

# create a new object movie
grandmasti = media.Movie('grand masti', 'Vivek oberio movie',
                         'https://upload.wikimedia.org/wikipedia/'
                         'en/f/fa/Grand_Masti.jpg',
                         'https://www.youtube.com/watch?v=ZojV0FC-KdI')

# create a new object movie
udtapunjab = media.Movie('udta punjab', 'shahid kapoor',
                         'https://1.bp.blogspot.com/-ZsFINk'
                         '-jOss/VrcXKqAyrdI/AAAAAAAAPDI/NkfKXRBqq5s/'
                         's1600/udta-punjab-movies-story-and-script-'
                         'are-the-real-heroes.JPG',
                         'https://www.youtube.com/watch?v=EJylz_9KYf8')

# create a new object movie
lovepunjab = media.Movie('love punjab', 'amrinder',
                         'http://t1.gstatic.com/images?'
                         'q=tbn:ANd9GcSaR-Zp1mbXvzizHotmUg'
                         'gUDRuKxwVpdE6VhTiAxjqIQfpkdzK0',
                         'https://www.youtube.com/watch?v=1lTWvdYxUMk')
# create a new object movie
dishoom = media.Movie('Dishoom', 'John Ambrahim',
                      'https://i.ytimg.com/vi/DU6IdS2gVog/maxresdefault.jpg',
                      'https://www.youtube.com/watch?v=DU6IdS2gVog')


# All movie in movies array variable
movies = [sardaarji, sultan, grandmasti, udtapunjab, lovepunjab, dishoom]
fresh_tomatoes.open_movies_page(movies)
