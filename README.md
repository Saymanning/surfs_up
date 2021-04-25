## Surfs Up

### Overview of the analysis:
 
The purpose of this analysis was to gather more data and information about temperature trends before opening a surf and ice cream shop in Hawaii on the island of Oahu. Specifically, temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.


**- The first step was to determine the Summary Statistics for June**

  Using Python, Pandas functions and methods, and SQLAlchemy, the date column of the Measurements table in the hawaii.sqlite database was filtered to retrieve all the 
  temperatures for the month of June. Then those temperatures were converted to a list, a DataFrame was created from the list, and the summary statistics were generated.
 
 
 <img width="515" alt="June Temps Query" src="https://user-images.githubusercontent.com/78699465/116007581-69209d80-a5de-11eb-84cf-1c9815bcdd32.png">
 
 <img width="534" alt="June list and dataframe" src="https://user-images.githubusercontent.com/78699465/116007586-750c5f80-a5de-11eb-9821-71308d048513.png">

<img width="143" alt="June temps" src="https://user-images.githubusercontent.com/78699465/116007594-7b024080-a5de-11eb-8068-1a23c50492c1.png">


  

**- The second step was to determine the Summary Statistics for December**

  Again, using Python, Pandas functions and methods, and SQLAlchemy, the date column of the Measurements table in the hawaii.sqlite database was filtered to retrieve all the     temperatures for the month of December. Then those temperatures were converted to a list, a DataFrame was created from the list, and the summary statistics was generated.

<img width="518" alt="December Temps Query" src="https://user-images.githubusercontent.com/78699465/116007802-8013bf80-a5df-11eb-9f16-0d45f5bcc7ed.png">

<img width="656" alt="December List_Dataframe_Sumary" src="https://user-images.githubusercontent.com/78699465/116007808-843fdd00-a5df-11eb-9280-0b760fc7b4d7.png">

<img width="148" alt="December temps" src="https://user-images.githubusercontent.com/78699465/116007811-873acd80-a5df-11eb-8e53-96785834bde4.png">






### Results: 
 
 - The average temperatures for June and Decembers are very close. The average temperature for December is 71 degrees and the average for the month of June is 75 degrees. 
 - The maximum temperatures for December and June are even closer with the max temperature for the month of December at 83 degrees and just 2 degrees higher at 85 for June.
 - The minimum temperature for December is 56 degrees and the minimum temperature for June is 64 degrees.


### Summary: 
The data gathered for temperature trends during the months of December and June shows that the temperature on Oahu is very stable year-round with average temperatures in the low to mid-seventies. These are very pleasant temperatures for enjoying surfing and ice cream (just maybe don't try to eat your ice cream while you are surfing). The maximum temperatures of 83 degrees for December and 85 degrees for June are ideal for water activities such as surfing and enjoying some cold ice cream. Although the minimum temperature for December is 56 degrees and the minimum temperature for June is 64 degrees. These temps may be a bit chilly for ice cream and/or surfing for a few folks. It worth considering having wetsuits available for rent or purchase surfers for these occasional cooler days and possibly options of coffee and tea drinks.

It is recommended that two additional queries should be performed to gather more weather data to consider before opening the surf and ice cream shop. One to gather more information regarding precipitation trends in the months June through November, the months with the highest probability of hurricanes. As well as a query to gather more information on wind, specifically the trade winds that are present in Hawaii from May to October.
