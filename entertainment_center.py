import fresh_tomatoes
import media

"""in all different files as created downword, here with help of instances or
   objects we are calling the property of class movie"""


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://goo.gl/nYw7V3",
                        "http://y2u.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "a marine on an alien",
                     "https://goo.gl/Z1KkjV",
                     "http://y2u.be/5PSNL1qE6VY")

avenger = media.Movie("Avenger",
                      "a marvels production",
                      "https://goo.gl/BXiq2c",
                      "http://y2u.be/eOrNdBpGMv8")

Bourne_Identity = media.Movie("Bourne Identity",
                              """A man with a bullet-ridden body is
                              found and looked after by strangers""",
                              "https://goo.gl/7kf26R",
                              "http://y2u.be/FpKaB5dvQ4g")

shawshank_redemption = media.Movie("Shawshank Redemption",
                                   """Andy Dufresne, a successful banker, is arrested
                                   for the murders of his wife and her lover,
                                   and is sentenced to life imprisonment
                                   at the Shawshank prison""",
                                   "https://goo.gl/KuuERn",
                                   "http://y2u.be/6hB3S9bIaco")

hunger_games = media.Movie("Hunger Games",
                           "a vempire movie",
                           "https://goo.gl/VkbrXa",
                           "http://y2u.be/mfmrPu43DF8")

movies = [toy_story, avatar, avenger, Bourne_Identity,
          shawshank_redemption, hunger_games]
"""it is list of instances that i have created """

fresh_tomatoes.open_movies_page(movies)
"""with help of this upper i am connecting both forntend
   and backend i.e- python file and html file """
