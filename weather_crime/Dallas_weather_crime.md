Dallas Weather and Crime
================
Micaela Chan
5/16/2019

Weather data: [NOAA Storm data](https://www.ncdc.noaa.gov/stormevents/choosedates.jsp?statefips=48%2CTEXAS#) Crime data: [Dallas Open Data](https://www.dallasopendata.com/resource/ttvp-9tm3)

### NOAA Data

List all available data categories
----------------------------------

``` r
source <- "https://www.ncdc.noaa.gov/cdo-web/api/v2/datacategories?&limit=100"

response <- GET(source, add_headers(token = req_token)) %>%
  content( as="text") %>%
  fromJSON()

df <- response$results %>%
  as.data.frame(stringsAsFactors = FALSE)
kable(df)
```

| name                       | id            |
|:---------------------------|:--------------|
| Annual Agricultural        | ANNAGR        |
| Annual Degree Days         | ANNDD         |
| Annual Precipitation       | ANNPRCP       |
| Annual Temperature         | ANNTEMP       |
| Autumn Agricultural        | AUAGR         |
| Autumn Degree Days         | AUDD          |
| Autumn Precipitation       | AUPRCP        |
| Autumn Temperature         | AUTEMP        |
| Computed                   | COMP          |
| Computed Agricultural      | COMPAGR       |
| Degree Days                | DD            |
| Dual-Pol Moments           | DUALPOLMOMENT |
| Echo Tops                  | ECHOTOP       |
| Evaporation                | EVAP          |
| Hydrometeor Type           | HYDROMETEOR   |
| Land                       | LAND          |
| Miscellany                 | MISC          |
| Other                      | OTHER         |
| Overlay                    | OVERLAY       |
| Precipitation              | PRCP          |
| Pressure                   | PRES          |
| Reflectivity               | REFLECTIVITY  |
| Sky cover & clouds         | SKY           |
| Spring Agricultural        | SPAGR         |
| Spring Degree Days         | SPDD          |
| Spring Precipitation       | SPPRCP        |
| Spring Temperature         | SPTEMP        |
| Summer Agricultural        | SUAGR         |
| Summer Degree Days         | SUDD          |
| Sunshine                   | SUN           |
| Summer Precipitation       | SUPRCP        |
| Summer Temperature         | SUTEMP        |
| Air Temperature            | TEMP          |
| Velocity                   | VELOCITY      |
| Vertical Integrated Liquid | VERTINTLIQUID |
| Water                      | WATER         |
| Winter Agricultural        | WIAGR         |
| Winter Degree Days         | WIDD          |
| Wind                       | WIND          |
| Winter Precipitation       | WIPRCP        |
| Winter Temperature         | WITEMP        |
| Weather Type               | WXTYPE        |

List all available location categories
--------------------------------------

``` r
source <- "https://www.ncdc.noaa.gov/cdo-web/api/v2/locationcategories?&limit=100"

response <- GET(source, add_headers(token = req_token)) %>%
  content( as="text") %>%
  fromJSON()

df <- response$results %>%
  as.data.frame(stringsAsFactors = FALSE)
kable(df)
```

| name                       | id        |
|:---------------------------|:----------|
| City                       | CITY      |
| Climate Division           | CLIM\_DIV |
| Climate Region             | CLIM\_REG |
| Country                    | CNTRY     |
| County                     | CNTY      |
| Hydrologic Accounting Unit | HYD\_ACC  |
| Hydrologic Cataloging Unit | HYD\_CAT  |
| Hydrologic Region          | HYD\_REG  |
| Hydrologic Subregion       | HYD\_SUB  |
| State                      | ST        |
| US Territory               | US\_TERR  |
| Zip Code                   | ZIP       |
