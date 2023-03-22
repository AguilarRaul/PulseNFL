# NFL Pulse project proposal

## Motivation and purpose

##### Our role

> NFL Data Science Team (fictional role).

##### Target audience

> Enthusiasts who want to know more about their favorite NFL team.
> Sports analysts who want to have a glimpse of any team's historical performance.

##### Dashboard motivation

> The National Football League (NFL) is the most important professional sports league in the United States. For NFL fans and analysts, it is important to get information about the historical performance of their teams to have passionate conversations and debates.

> The objective of this dashboard is to put the most important statistics of team performance in one place, allowing anyone to obtain fast and accurate information just a couple of clicks away.

> As sports fans, knowing the statistics of our favorite teams is necessary to analyze a game or competition, as well as to be able to chat and debate with other sports enthusiasts.

## Description of the data

We will visualize a historical dataset containing NFL Team standings from 2000 to 2019.

The dataset is made up of from 638 observations and 15 variables, both categorical and numerical, these variables represent attributes associated with the team performance given a specific season. Below is a summary of the variables of the dataset:

|variable             |class     |description |
|:--------------------|:---------|:-----------|
|team                 |character | Team city |
|team_name            |character | Team name|
|year                 |integer   | season year |
|wins                 |double    | Wins (0 to 16)|
|loss                 |double    | Losses (0 to 16) |
|points_for           |double    | points for (offensive performance) |
|points_against       |double    | points for (defensive performance) |
|points_differential  |double    | Point differential (points_for - points_against) |
|margin_of_victory    |double    | (Points Scored - Points Allowed)/ Games Played |
|strength_of_schedule |double    | Average quality of opponent as measured by SRS (Simple Rating System) |
|simple_rating        |double    |Team quality relative to average (0.0) as measured by SRS (Simple Rating System) SRS = MoV + SoS = OSRS + DSRS |
|offensive_ranking    |double    | Team offense quality relative to average (0.0) as measured by SRS (Simple Rating System)|
|defensive_ranking    |double    | Team defense quality relative to average (0.0) as measured by SRS (Simple Rating System) |
|playoffs             |character | Made playoffs or not |
|sb_winner            |character | Won superbowl or not |

Attribution:

> The data set is public and can be found in [tidytuesday](https://github.com/rfordatascience/tidytuesday). Follow this link  to access to the source dataset [standings.csv](https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-04/standings.csv).

## Research questions

Below are some of the questions that will be answered through interaction with our dashboard:

- How many games did the New England Patriots win in 2006?
- Did the Kansas City Chiefs make it to the playoffs in 2018?
- What was the Packers' defensive rating in 2010?
- Is there a trend in the offensive rating of the Panthers from 2010 to 2019?
- Are the 49ers better at offensive or defensive?
- What was the winning percentage of the Dolphins in 2017?
- Is my favorite team getting better or worst?

## Usage Scenario

Considering our target audience, a fictitious use case for our dashboard is presented below:
> Daniel Amancio is a big fan of the NFL, especially he supports the New England Patriots, he knows that in the 2017 season his favorite team won all the regular season games finishing with a perfect 16-0 record. Daniel would like to know what the Patriots' strengths were during that season and additionally how difficult their schedule was to find out if the quality of the rivals influenced the Patriots to achieve this never-before-seen milestone.
