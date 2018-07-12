# Google map downloader

Using a csv file with a series of GMap queries, produce another csv file with details. It use  
`https://maps.googleapis.com/maps/api/place/textsearch/xml` to resolve the query to privide the PlaceID and use `https://maps.googleapis.com/maps/api/place/details/xml` to get the maximun details for this PlaceID
