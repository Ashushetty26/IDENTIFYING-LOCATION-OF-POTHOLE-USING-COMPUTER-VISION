# import gmplot package
import gmplot
def process():
    latitude_list = [ 13.0325168, 13.0335168, 13.0355168 ]
    longitude_list = [ 77.5909889, 77.591000, 77.591100]
    gmap5 = gmplot.GoogleMapPlotter(13.0325168,77.5909889, 18)
    gmap5.scatter( latitude_list, longitude_list, '# FF0000',size = 40, marker = False)
    # polygon method Draw a polygon with
    # the help of coordinates
    gmap5.polygon(latitude_list, longitude_list,color = 'cornflowerblue')
    gmap5.draw( "map15.html" )
    
