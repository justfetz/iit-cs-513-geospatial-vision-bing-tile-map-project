# CS-513: Geospatial Vision - Bing Maps Tile System Project  

## Project Description
This project is part of the CS-513 Geospatial Vision course at Illinois Institute of Technology. The project demonstrates the use of the Bing Maps Tile System, a system used to render map tiles for various zoom levels and locations. The project involves visualizing geospatial data using the Bing Maps Tile System, manipulating tile coordinates, and integrating various geospatial data sources.

## Features
- **Map Visualization:** Render maps using the Bing Maps Tile System.
- **Tile Coordinates Manipulation:** Convert between geographic coordinates (latitude, longitude) and tile coordinates (x, y, zoom level).
- **Overlay Geospatial Data:** Overlay additional geospatial data on the map tiles.

## Prerequisites
- Java Development Kit (JDK) 8 or higher
- Integrated Development Environment (IDE) such as IntelliJ IDEA or Eclipse
- Bing Maps API key

## Installation (Incomplete)


2. **Open the project in your IDE:**
    - Open your preferred IDE and import the cloned project.

3. **Configure API Key:**
    - Obtain a Bing Maps API key from the [Bing Maps Portal](https://www.bingmapsportal.com/).
    - Add your API key to the project configuration file.

4. **Build the project:**
    - Use the build tool provided by your IDE (e.g., Maven or Gradle) to build the project.

## Usage

1. **Run the Program:**
    - Execute the main class `BingMapsTileSystem.java` to run the program.

2. **Navigate the Map:**
    - Use the interactive interface to zoom in/out and pan across the map.

3. **Overlay Data:**
    - Overlay additional geospatial data by providing the relevant data files or inputs through the interface.

## Example

### Code Example in Java
```java
public class BingMapsTileSystem {

    private static final int TILE_SIZE = 256;
    private static final int EARTH_RADIUS = 6378137;
    private static final double INITIAL_RESOLUTION = 2 * Math.PI * EARTH_RADIUS / TILE_SIZE;
    private static final double ORIGIN_SHIFT = 2 * Math.PI * EARTH_RADIUS / 2.0;

    public static void main(String[] args) {
        // Example usage
        double lat = 41.881832;
        double lon = -87.623177;
        int zoom = 15;

        Point tile = latLonToTileXY(lat, lon, zoom);
        System.out.println("Tile X: " + tile.x + ", Tile Y: " + tile.y);
    }

    public static Point latLonToTileXY(double lat, double lon, int zoom) {
        Point p = latLonToMeters(lat, lon);
        return metersToTileXY(p.x, p.y, zoom);
    }

    public static Point latLonToMeters(double lat, double lon) {
        double mx = lon * ORIGIN_SHIFT / 180.0;
        double my = Math.log(Math.tan((90 + lat) * Math.PI / 360.0)) / (Math.PI / 180.0);
        my = my * ORIGIN_SHIFT / 180.0;
        return new Point(mx, my);
    }

    public static Point metersToTileXY(double mx, double my, int zoom) {
        double res = INITIAL_RESOLUTION / (1 << zoom);
        int px = (int) ((mx + ORIGIN_SHIFT) / res);
        int py = (int) ((my + ORIGIN_SHIFT) / res);
        return new Point(px / TILE_SIZE, py / TILE_SIZE);
    }
}
```

### Code Example in python

```python
import math

TILE_SIZE = 256
EARTH_RADIUS = 6378137
INITIAL_RESOLUTION = 2 * math.pi * EARTH_RADIUS / TILE_SIZE
ORIGIN_SHIFT = 2 * math.pi * EARTH_RADIUS / 2.0

def lat_lon_to_tile_xy(lat, lon, zoom):
    mx, my = lat_lon_to_meters(lat, lon)
    return meters_to_tile_xy(mx, my, zoom)

def lat_lon_to_meters(lat, lon):
    mx = lon * ORIGIN_SHIFT / 180.0
    my = math.log(math.tan((90 + lat) * math.pi / 360.0)) / (math.pi / 180.0)
    my = my * ORIGIN_SHIFT / 180.0
    return mx, my

def meters_to_tile_xy(mx, my, zoom):
    res = INITIAL_RESOLUTION / (1 << zoom)
    px = int((mx + ORIGIN_SHIFT) / res)
    py = int((my + ORIGIN_SHIFT) / res)
    return px // TILE_SIZE, py // TILE_SIZE

# Example usage
lat = 41.881832
lon = -87.623177
zoom = 15

tile_x, tile_y = lat_lon_to_tile_xy(lat, lon, zoom)
print(f"Tile X: {tile_x}, Tile Y: {tile_y}")
```
