from app import db, venue, venue_address, venue_desc_seeking, venue_genres, venue_sociallinks, artist, artist_address, artist_looking, artist_sociallinks, artists_genres
                
venue1 = venue( name = 'The Dueling Pianos Bar')
venue_genres_classical = venue_genres( genres='Classical')
venue_genres_rnb = venue_genres( genres='R&B')
venue_genres_hiphop = venue_genres( genres='Hip-Hop') 
venue_address1 = venue_address( city='New York', 
                                state='NY', 
                                phone='914-003-1132', 
                                address='335 Delancey Street')

venue_sociallinks1 = venue_sociallinks( image_link='https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
                                        facebook_link='https://www.facebook.com/theduelingpianos', 
                                        website_link='https://www.theduelingpianos.com')

venue_desc_seeking1 = venue_desc_seeking(looking_talent = False,
                                         seeking_description='')

venue2 = venue( name = 'Park Square Live Music & Coffee')
venue_genres_rocknroll = venue_genres( genres='Rock n Roll')
venue_genres_jazz = venue_genres( genres='Jazz')
venue_genres_folk = venue_genres( genres='Folk')
venue_address2 = venue_address( city='San Francisco', 
                                state='CA', 
                                phone='415-000-1234', 
                                address='34 Whiskey Moore Ave')
venue_sociallinks2 = venue_sociallinks( image_link='https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80',
                                        facebook_link='https://www.facebook.com/ParkSquareLiveMusicAndCoffee', 
                                        website_link='https://www.parksquarelivemusicandcoffee.com')

venue_desc_seeking2 = venue_desc_seeking(looking_talent = False,
                                         seeking_description='')


venue3 = venue( name = 'The Musical Hop')
venue_genres_reggae = venue_genres( genres='Reggae')
venue_genres_swing = venue_genres( genres='Swing')
venue_address3 = venue_address( city='San Francisco', 
                                state='CA', 
                                phone='123-123-1234', 
                                address='1015 Folsom Street')
venue_sociallinks3 = venue_sociallinks( image_link='https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60',
                                        facebook_link='https://www.facebook.com/TheMusicalHop', 
                                        website_link='https://www.themusicalhop.com')

venue_desc_seeking3 = venue_desc_seeking(looking_talent = True,
                                         seeking_description='We are on the lookout for a local artist to play every two weeks. Please call us.')

artist1 = artist( name = 'Guns N Petals')
artist_genres_rocknroll = artists_genres( performers_genres='Rock n Roll')
artist_address1 = artist_address( city='San Francisco', 
                                  state='CA', 
                                  phone='326-123-5000')
artist_sociallinks1 = artist_sociallinks( image_link='https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80',
                                          facebook_link='https://www.facebook.com/GunsNPetals', 
                                          website_link='https://www.gunsnpetalsband.com')

artist_desc_seeking1 = artist_looking( looking_venues = True,
                                       seeking_description='We are on the lookout for a local artist to play every two weeks. Please call us.')


artist2 = artist( name = 'Matt Quevedo')
artist_genres_jazz = artists_genres( performers_genres='Jazz')
artist_address2 = artist_address( city='New York', 
                                 state='NY', 
                                 phone='300-400-5000')
artist_sociallinks2 = artist_sociallinks( image_link='https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80',
                                          facebook_link='https://www.facebook.com/mattquevedo923251523', 
                                          website_link='https://www.GunsNPetals.com')

artist_desc_seeking2 = artist_looking(   looking_venues = False,
                                         seeking_description='We are on the lookout for a local artist to play every two weeks. Please call us.')

artist3 = artist( name = 'The Wild Sax Band')
artist_genres_classical = artists_genres( performers_genres= 'Classical')
artist_address3 = artist_address( city='San Francisco', 
                                  state='CA', 
                                  phone='432-325-5432')
artist_sociallinks3 = artist_sociallinks( image_link='https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80',
                                          facebook_link='https://www.facebook.com/GunsNPetals', 
                                          website_link='https://www.GunsNPetals.com')

artist_desc_seeking3 = artist_looking( looking_venues = True,
                                       seeking_description='Looking for shows to perform at in the San Francisco Bay Area!')


venue_genres_classical.venue1= venue1 
venue_genres_rnb.venue1= venue1 
venue_genres_hiphop.venue1= venue1

venue_address1.venue1= venue1
venue_sociallinks1.venue1 = venue1
venue_desc_seeking1.venue1 = venue1

venue_genres_rocknroll.venue2= venue2 
venue_genres_jazz.venue2= venue2 
venue_genres_classical.venue2= venue2 
venue_genres_folk.venue2= venue2 
venue_genres_hiphop.venue2= venue2

venue_address2.venue2= venue2
venue_sociallinks2.venue2 = venue2
venue_desc_seeking2.venue2 = venue2

venue_genres_classical.venue3= venue3
venue_genres_jazz.venue3= venue3
venue_genres_folk.venue3= venue3
venue_genres_reggae.venue3= venue3
venue_genres_swing.venue3= venue3

venue_address3.venue3= venue3
venue_sociallinks3.venue3 = venue3
venue_desc_seeking3.venue3 = venue3


artist_genres_rocknroll.artist1 = artist1
artist_address1.artist1 = artist1
artist_sociallinks1.artiist1 = artist1
artist_desc_seeking1.artist1 = artist1

artist_genres_jazz.artist2 = artist2
artist_address2.artist2 = artist2
artist_sociallinks2.artiist2 = artist2
artist_desc_seeking2.artist2 = artist2

artist_genres_jazz.artist3 = artist3
artist_genres_classical.artist3 = artist3
artist_address3.artist3 = artist3
artist_sociallinks3.artiist3 = artist3
artist_desc_seeking3.artist3 = artist3

db.session.add_all([artist1, artist2, artist3])
db.session.add_all([venue1, venue2, venue3])
db.session.commit()
