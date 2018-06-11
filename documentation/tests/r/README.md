# R Tests README

## Directories

#### data/

Data required for running scripts

#### results/

Results from the scripts

    1_first_visualisations/       # initial visualisations           
    2_filtering_by_condition      # filter data by the four conditions
    r_workbook_pdfs/              # R Workbooks in PDF format
    r_workbooks/                  # R Workbooks in Rmd and HTML

#### src/

Scripts used to create plots.

    functions/                    # functions for reused code.          


#### shiny_

Shiny applications.

## Viewing plots

Plots in 'results/' are PNG.

R Workbooks are in HTML, Rmd or PDF.

Shiny apps require a bit more set-up. Follow the set-up instructions below.

### Installation

#### Requirements

    - R
    - R Studio
    - Git Bash

    NOTE: All commands that use "git" are done in Git Bash. It lets you use MinGW/Linux tools with Git at the command line.

1. Clone this repo -

 `git clone https://github.com/UoMResearchIT/bbc_data_flask_app.git`

2. Open the bbc_data.Rproj file in RStudio. (documentation\tests\r\bbc_data.Rproj)

3. Install the following packages via the Terminal in RStudio.

  ```
  install.packages("tidyverse")
  install.packages("shiny")
  install.packages("forcats")
  install.packages("tidyverse")
  ```

4. Choose which shiny app to run and open `app.R` click 'Run App' in top right corner.

        shiny_bbc_data_interactive/                   # Shows various types of clicks
        shiny_bbc_data_interactive_facet_wrap/        # All conditions on one plot
        shiny_bbc_data_interactive_items/             # in Linear conditions shows when tabs were switched between recipes
        shiny_bbc_interaction_web/                    # web version of shiny_bbc_data_interactive
