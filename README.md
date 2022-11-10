# election_analysys

## Project Overview
The Colorado Board of Elections is aduting an election for the US Congressional precinct of Colorda. Given [election_results.csv](https://github.com/ahualoh/election_analysis/blob/main/resources/election_results.csv), it displayed a ballot ID, the county where the ballot counted, and the candidate voted for. We need to generate a report that answered following points: 

- How many votes were cast in this congressional election? 
- A breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Which county had the largest number of votes?
- A breakdown of the number of votes and the percentage of the total votes each candidate received.
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

The analysis of the election shows the following results (see "[election_analysis.txt](https://github.com/ahualoh/election_analysis/blob/main/analysis/election_analysis.txt)":

``` 
Election Results
-------------------------
Total Votes: 369,711
-------------------------
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
-------------------------
Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%
-------------------------
```

## Resources

- Data Source: [election_results.csv](https://github.com/ahualoh/election_analysis/blob/main/resources/election_results.csv)
- Software: Python 3.9.12

## Summary

This script can be used for any future elections and modified to include more information.
A simple change is that for an info related to "county", may want to be renamed for "state" if a bigger election for example. 

One may be interested also in the distribution of candidate outcomes for each county. So either a list of each county showing voting distribution for each candidate, or a list of candidates with a distrubtion for how many votes they got from each county. 

Unfortunately, I was unable to come up with direct examples for working code, but those are at least two way one might try to expand on this script. 

