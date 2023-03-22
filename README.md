# NFL Pulse  🏈

## Welcome, sports enthusiast! 

I am glad you are interested in exploring your favorite team's regular season standings. In this dashboard, you will find the most important statistics of teams' performance in one place, fast and accurate information is just a couple of clicks away!

## Table of contents

- [Explore the app](#explore-the-app)
- [Motivation](#motivation)
- [Description and usage](#description-and-usage)
- [About the data](#about-the-data)
- [Installation](#installation)
- [Contributing](#contributing)

## Explore the app

You can access the deployed app on [Render.com here](https://nflpulse.onrender.com/)!

## Motivation

The National Football League (NFL) is the most important professional sports league in the United States. For NFL fans and analysts, it is important to know information about the historical performance of their teams to have passionate conversations and debates. This is what motivated me to build this dashboard!

You can find more information on the dashboard motivation in the [proposal.md](https://github.com/AguilarRaul/PulseNFL/tree/main/reports/proposal.md).

## Description and usage

![](img/NFL_Pulse.gif)

The dashboard contains two filters, allowing the user to select its favorite team and the season of his preference. The dashboard also consists of two plots:

1. `Team Winning Percetage During Regular Season`: here you can find the number of wins and losses of a team (tooltip), the winning percentage and whether or not the team qualified for the postseason that year.

2. `Team Performance Metrics During Regular Season`: contains the defensive rating (a measure of how good a team's defense was, the higher the better, a value greater than 0 is desirable), the offensive rating (higher than 0 is better), and the schedule difficulty rating (indicates how difficult the team's opponents were, a number greater than 0 indicates that the opponents were difficult).

## About the data

The original dataset is made up of from 638 observations and 15 variables, both categorical and numerical, these variables represent attributes associated with the team performance given a specific season. Below is a summary of the variables of the dataset being used currently, the whole data set description can be found here [proposal.md](https://github.com/AguilarRaul/PulseNFL/tree/main/reports/proposal.md):

|variable             |class     |description |
|:--------------------|:---------|:-----------|
|team_name            |character | Team name|
|year                 |integer   | season year |
|wins                 |double    | Wins (0 to 16)|
|loss                 |double    | Losses (0 to 16) |
|strength_of_schedule |double    | Average quality of opponent as measured by SRS (Simple Rating System) |
|offensive_ranking    |double    | Team offense quality relative to average (0.0) as measured by SRS (Simple Rating System)|
|defensive_ranking    |double    | Team defense quality relative to average (0.0) as measured by SRS (Simple Rating System) |
|playoffs             |character | Made playoffs or not |

> The data set is public and can be found in [tidytuesday](https://github.com/rfordatascience/tidytuesday). Follow this link to access to the source dataset [standings.csv](https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-04/standings.csv).

## Installation

To run `NFL Pulse` locally follow this steps:

1. Clone this repository to your local directory.

2. I have created an environment `nflpulse.yaml`, using which our app can be reproduced locally. To create this environment locally, go to the root of this repository and run:

    ``` bash
    conda env create -f nflpulse.yaml
    ```

3. Activate it by running:

        conda activate nflpulse

4. In the src folder of this repository run the following command:

        python app.py

5. Copy the address and paste it in your browser to load the dashboard.

## Contributing

I need your help, I just scratched the surface! Please check out the [contributing guidelines](https://github.com/AguilarRaul/PulseNFL/blob/main/CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`NFL Pulse` was created by Raul Aguilar. The materials of this project are licensed under the MIT License. If re-using/re-mixing please provide attribution and link to this webpage.

## Contributors

<a href="https://github.com/AguilarRaul/PulseNFL/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=AguilarRaul/PulseNFL" />
</a>

