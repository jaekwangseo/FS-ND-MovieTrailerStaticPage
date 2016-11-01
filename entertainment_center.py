import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "Woody the cowboy is young Andy’s favorite toy. Yet this changes when Andy get the new super toy Buzz Lightyear for his birthday. Now that Woody is no longer number one he plans his revenge on Buzz. Toy Story is a milestone in film history for being the first feature film to use entirely computer animation.",
                        "https://image.tmdb.org/t/p/w1280/uMZqKhT4YA6mqo2yczoznv7IDmv.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "In the 22nd century, a paraplegic Marine is dispatched to the moon Pandora on a unique mission, but becomes torn between following orders and protecting an alien civilization.",
					 "https://image.tmdb.org/t/p/w1280/vUb6JH5WR7xHxpnB8RVITpX0kek.jpg",
					 "https://youtu.be/5PSNL1qE6VY")

transformers = media.Movie("Transformers",
						  "Young teenager Sam Witwicky becomes involved in the ancient struggle between two extraterrestrial factions of transforming robots, the heroic Autobots and the evil Decepticons. Sam holds the clue to unimaginable power and the Decepticons will stop at nothing to retrieve it.",
						  "https://image.tmdb.org/t/p/w1280/bgSHbGEA1OM6qDs3Qba4VlSZsNG.jpg",
						  "https://youtu.be/dxQxgAfNzyE")








movies = [toy_story, avatar, transformers]

fresh_tomatoes.open_movies_page(movies)
