# Base R with RMarkdown support
FROM rocker/verse
LABEL maintainer="aboghoss@broadinstitute.org"

ARG BUILD_DATE

LABEL org.label.schema.name="bargraph"
LABEL org.label-schema.build-date=$BUILD_DATE
LABEL org.label-schema.url="https://a-few-beers-later.surge.sh"
LABEL org.label-schema.vcs-url="https://github.com/alexdanilowicz/BarGraph"
LABEL org.label-schema.schema-version="0.0.1"

# Updadte some basic packages for R compatibility

# Set working directory
WORKDIR /

# Copy scripts into image
COPY ./install_packages.R /install_packages.R
COPY ./index.Rmd /index.Rmd
COPY ./report.sh /bargraph/bin/report.sh

# Install R packages
RUN Rscript /install_packages.R

# Make report,sh executable
ENV PATH /bargraph/bin:$PATH
RUN ["chmod","-R", "+x", "/bargraph/bin"]

# Entrypoint to run container
ENTRYPOINT ["report.sh"]
