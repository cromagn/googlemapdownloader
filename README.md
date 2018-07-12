# Google map downloader

Using a csv file with a series of GMap queries and / or parameter, produce another csv file with place details. It use  
`https://maps.googleapis.com/maps/api/place/textsearch/xml` to resolve the query to provide the PlaceID and use `https://maps.googleapis.com/maps/api/place/details/xml` to get the maximun details for this PlaceID.
As an example, the comuni.csv contains all the italian towns
