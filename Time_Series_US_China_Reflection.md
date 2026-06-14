Using Claude as a tool, I did my first mini data analysis on real world data. Specifically, I wanted to learn about what kinds of tools are used for analyzing data over time. 
The general steps I learned are:
1. Import data as a dataframe type using Pandas
2. Looking at the row and column names in the dataset, process the data into smaller dataframes depending on trends of interest - I focused on US and China's renewable energy share over time
- my trend of interest is very specific: I initially wanted to look at the makeup of each countrie's renewable energy over time, but decided to keep it simple to learn the basics of data analysis
3. Separately analyze the data by trend, seasonality, and residual

Things I learned about data analysis
- It is crucial to read the raw data beforehand to understand how to extract data and look for missing data
- Remove missing data entries and make the data of equal length before analyzing/comparing
- Plotly library automatically shifts a graph if there is missing data, but you should not rely on this and remove it in the first place
- Before interpreting seasonality analyses, predict whether a trend is expected. It seems that usually there must be more than one data point annually for the seasonality to be meaningful. Some exceptions I can think of are cycles that repeat less than annually. For example, the Olympics, political campaigns, and climate change.
    
