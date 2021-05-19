# Point to CRAN for package repos
options(repos=structure(c(CRAN="http://cran.r-project.org")))

# CRAN packages
install.packages(c(
  "tidyverse",
  "RColorBrewer",
  "ggthemes",
  "cowplot",
  "GGally",
  "DT",
  "randomNames",
  "devtools",
  "caret",
  "ranger"
))

devtools::install_github("hadley/emo")
