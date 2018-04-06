
import math

class TileSystem:
    def __init__(EarthRadius, MinLatitude, MaxLatitude, MinLongitude, MaxLongitude):
        self.EarthRadius = 6378137
        self.MinLatitude = -85.05112878;
        self.MaxLatitude = 85.05112878;
        self.MinLongitude = -180;
        self.MaxLongitude = 180;

    def Clip(n, minValue, maxValue):
        return math.min(math.max(n, minValue), maxValue)

    def MapSize(levelOfDetail):
        #ranges from 1 to 23
        return levelOfDetail


    def GroundResolution(latitude, levelOfDetail):
        latitude = Clip(latitude, MinLatitude, MinLongitude)
        return math.cos(latitude * math.pi/180) * 2 * math.pi * EarthRadius / MapSize(levelOfDetail)


    def MapScale(latitude, levelOfDetail, screenDpi):
        return GroundResolution(latitude, levelOfDetail) * screenDpi / 0.0254


    def LatLongToPixelXY(latitude, longitude, levelOfDetail, pixelX, pixelY):
        
            latitude = Clip(latitude, MinLatitude, MaxLatitude);
            longitude = Clip(longitude, MinLongitude, MaxLongitude);

            x = (longitude + 180) / 360; 
            sinLatitude = math.sin(latitude * Math.PI / 180);
            y = 0.5 - math.log((1 + sinLatitude) / (1 - sinLatitude)) / (4 * Math.PI);

            mapSize = MapSize(levelOfDetail);
            pixelX = int(Clip(x * mapSize + 0.5, 0, mapSize - 1));
            pixelY = int(Clip(y * mapSize + 0.5, 0, mapSize - 1));
        

    def PixelXYToLatLong(pixelX, pixelY, levelOfDetail, latitude, longitude):
        mapSize = MapSize(levelOfDetail)
        x = Clip(pixelX,0,mapSize-1)/mapSize
        y = 0.5 - Clip(pixelY, 0, mapSize - 1) / mapSize

        latitude = 90 - 360 * math.atan(math.pow(-y * 2 * math.pi)) / math.pi;
        longitude = 360 * x;


    def PixelXYToTileXY(pixelX, pixelY):
        tileX = pixelX / 256;
        tileY = pixelY / 256;
        return tileX, tileY



    def TileXYToPixelXY(tileX, tileY, pixelX, pixelY):
        pixelX = tileX * 256
        pixelY = tileY * 256


    def tileXYToQuadKey2(tileX, tileY, levelOfDetail):
        quadKey = ""
    #digit = 0
    #while (levelOfDetail > 0):
        for i in range(levelOfDetail,0,-1):
            digit = 0
            mask = 1 << (i-1)
            print(mask)
            if((tileX!=0) and (mask != 0)):
                digit +=1
                pass
            if((tileY!=0) and (mask != 0)):
                digit += 2
                #break
                #digit += 1
                #digit+= 1
            #continue
            quadKey += str(digit)
            #levelOfDetail -= 1
            
        return quadKey
